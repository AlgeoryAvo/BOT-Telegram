import telebot
import datetime
from telebot import types
import mysql.connector
import responses
import logging

mydb = mysql.connector.connect(
host= 'localhost',
user= 'root',
passwd= '',
database= 'bot')



#set LOG
# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')



#database akses dengan cara RUN
#print(mydb)

sql = mydb.cursor()
#API BOT ADA DIBAWAH INI :
#shiu=6065176168:AAH6VscAnFdnU_a9jjekELSSQzvbtGGlzN8
#tsel=AAGJfxfMnV3fC_taSYnhOV68s8IZiGUQzW0
api = '6299982967:AAGJfxfMnV3fC_taSYnhOV68s8IZiGUQzW0'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['penjualan'])
def penjualan(message):
  #split message
  texts = message.text.split(' ')
  print(texts)
  tanggal = texts[1]
  sql.execute("select konter, pulsa, voucher, kartu_perdana, total from  bot_penjualan where tanggal='{}'".format(tanggal))
  hasil_sql = sql.fetchall()
  # print(hasil_sql)

  # pesan yang dikirim oleh bot
  pesan_balasan = ''
  for x in hasil_sql:
    pesan_balasan = pesan_balasan + str(x) + '\n'
  #memperbagus balasan bot
  #menghilangkan tanda petik
  #pesan_balasan = pesan_balasan.replace("'","")
  #menghilangkan tanda kurung
  pesan_balasan = pesan_balasan.replace("(","")
  pesan_balasan = pesan_balasan.replace(")","")
  #menghilangkan tanda koma
  pesan_balasan = pesan_balasan.replace(",","")

  bot.reply_to(message, pesan_balasan)
#FITUR INPUT BELUM MAU MASUK INPUTAN
  @bot.message_handler(commands=['input'])
  def input(message):
      texts = message.text.split(' ')
      konter = texts[1]
      tanggal = texts[2]
      pulsa = texts[3]
      voucher = texts[4]
      kartu_perdana = texts[5]
      total = texts[6]

      insert = 'insert into bot_penjualan (konter, tanggal, pulsa, voucher, kartu_perdana,total) values (%s,%s,%s)'
      val = (konter, tanggal, pulsa, voucher, kartu_perdana, total)
      sql.execute(insert, val)
      mydb.commit()
      bot.reply_to(message, 'data berhasil diinput')
def log(message,perintah):
  tanggal = datetime.datetime.now()
  tanggal = tanggal.strftime('%d-%B-%Y')
  nama_awal = message.chat.first_name
  nama_akhir = message.chat.last_name
  id_user = message.chat.id
  text_log = '{}, {}, {} {}, {} \n'.format(tanggal, id_user, nama_awal, nama_akhir, perintah)
  log_bot = open('log_bot.txt','a')
  log_bot.write(text_log)
  log_bot.close()

@bot.message_handler(commands=['start'])
def action_start(message):
	user = open('user.txt','r')
	user = user.read()
	id_message = message.chat.id
	if str(id_message) in user:		
		log(message,'Start')
		first_name = message.chat.first_name
		last_name = message.chat.last_name
		bot.reply_to(message, ' Hi, selamat datang..  {} {}?'.format(first_name,last_name))
	else:
		bot.reply_to(message, 'Silahkan Cek ID Anda terlebih dahulu "/id" s')

@bot.message_handler(commands=['info'])
def action_learn(message):
	user = open('user.txt','r')
	user = user.read()
	id_message = message.chat.id
	if str(id_message) in user:	
		log(message, 'Info')
		first_name = message.chat.first_name
		last_name = message.chat.last_name
		bot.reply_to(message, '''
Hi {} {},Chatbot ini dibangun untuk mempermudah sales dan pihak konter saling terhubung.

		'''.format(first_name,last_name))
	else:
		bot.reply_to(message, 'Authorized user only')



@bot.message_handler(commands=['menu'])
def action_menu(message) :
    #Function pilihan 
    log(message, 'Menu')
    markup = types.ReplyKeyboardMarkup() 
    itema = types.KeyboardButton('/start')
    itemb = types.KeyboardButton('/info')
    itemc = types.KeyboardButton('/promo')
    itemd = types.KeyboardButton('/menu')
    iteme= types.KeyboardButton('/konter')
    itemf = types.KeyboardButton('/id')
    itemg = types.KeyboardButton('/help')

#Mengatur Tombol pilihan pada BOT Tele
    markup.row(itema,itemb,itemc)
    markup.row(itemd,itemf,itemg)

    first_name = message.chat.first_name
    last_name = message.chat.last_name
    bot.reply_to(message, 'Hi, berikut menu yang ada, Silahkan dipilih ??, {} {}'.format(first_name,last_name))
    bot.send_message(message.chat.id, 'Silahkan Pilih Menu yang kalian cari!', reply_markup=markup)


@bot.message_handler(commands=['promo'])
def action_konter(message):
	user = open('user.txt','r')
	user = user.read()
	id_message = message.chat.id
	if str(id_message) in user:
		log(message,'melihat promo')
		first_name = message.chat.first_name
		last_name = message.chat.last_name
		bot.reply_to(message, '''
Hi {} {} Berikut Promo Bulan Ini :
1GB Kuota Internet Hanya 20RB
Ketik "/promo1" untuk info selengkapnya...

3GB Kuota Internet Hanya 40RB
Ketik "/promo2" untuk info selengkapnya...

10GB Kuota Internet Hanya 90RB
Ketik "/promo3" untuk info selengkapnya...

500MB Kuota Internet Hanya 10RB
Ketik "/promo4" untuk info selengkapnya...

Unlimited Kuota Internet Hanya 220RB
Ketik "/promo5" untuk info selengkapnya...


'''.format(first_name,last_name))
	else:
		bot.reply_to(message, 'Authorized user only')



#Transfer video,foto,pdf
#CODING FOTO
@bot.message_handler(commands=['promo1'])
def text(message) :
    chat_id = message.chat.id
    bot.send_photo(chat_id, open('Dir/promo1.png', 'rb'))

@bot.message_handler(commands=['promo2'])
def text(message) :
    chat_id = message.chat.id
    bot.send_photo(chat_id, open('Dir/promo2.png', 'rb'))

@bot.message_handler(commands=['promo3'])
def text(message) :
    chat_id = message.chat.id
    bot.send_photo(chat_id, open('Dir/promo3.png', 'rb'))

@bot.message_handler(commands=['promo4'])
def text(message) :
    chat_id = message.chat.id
    bot.send_photo(chat_id, open('Dir/promo4.png', 'rb'))

@bot.message_handler(commands=['promo5'])
def text(message) :
    chat_id = message.chat.id
    bot.send_photo(chat_id, open('Dir/promo5.png', 'rb'))


#Transfer video,foto,pdf
#CODING VIDEO
@bot.message_handler(commands=['video1'])
def text(message) :
    chat_id = message.chat.id
    bot.send_video(chat_id, open('Dir/video1.mp4', 'rb'))

@bot.message_handler(commands=['id'])
def action_id(message):
  log(message,'Cek ID')
  first_name = message.chat.first_name
  last_name = message.chat.last_name
  id_telegram = message.chat.id
  bot.reply_to(message, '''
Hi, ini ID Telegram kamu
Nama = {} {}
ID = {}
'''.format(first_name,last_name, id_telegram))



@bot.message_handler(commands=['konter'])
def action_konter(message):
	user = open('user.txt','r')
	user = user.read()
	id_message = message.chat.id
	if str(id_message) in user:	
		log(message,'melihat konter')
		first_name = message.chat.first_name
		last_name = message.chat.last_name
		bot.reply_to(message, '''
Hi {} {} berikut list Konter Telkomsel Yang Berada DiSurabaya
KONTER Hp Surabaya 1
Dengan ID (11111111)
LOKASI : https://goo.gl/maps/UCSZv5ekQL9GJzim9

KONTER Hp Surabaya 2
Dengan ID (22222222)
LOKASI : https://goo.gl/maps/JyTjCHfRvVxp5vXd6

KONTER Hp Surabaya 3
Dengan ID (33333333)
LOKASI :https://goo.gl/maps/JyTjCHfRvVxp5vXd6

KONTER Hp Surabaya 4
Dengan ID (44444444)
LOKASI :https://goo.gl/maps/JyTjCHfRvVxp5vXd6

KONTER Hp Surabaya 5
Dengan ID (55555555)
LOKASI :https://goo.gl/maps/JyTjCHfRvVxp5vXd6
'''.format(first_name,last_name))
	else:
		bot.reply_to(message, 'Authorized user only')


@bot.message_handler(commands=['website'])
def action_website(message):
	user = open('user.txt','r')
	user = user.read()
	id_message = message.chat.id
	if str(id_message) in user:
		log(message,'melihat website')
		first_name = message.chat.first_name
		last_name = message.chat.last_name
		bot.reply_to(message, '''
		
Hi {} {} berikut list Website Kami:
Website Telkomsel :
('http://www.telkomsel.com' )

Tukar Poin Telkomsel :
('https://www.telkomsel.com/en/telkomsel-poin' )

Promo Telkomsel :
('https://www.telkomsel.com/en/promo')

Download Aplikasi MyTelkomsel Di:
('PlayStore/AppStore')

'''.format(first_name,last_name))
	else:
		bot.reply_to(message, 'Authorized user only')


@bot.message_handler(commands=['help'])
def action_help(message):
	user = open('user.txt','r')
	user = user.read()
	id_message = message.chat.id
	if str(id_message) in user:	
		log(message,'Help')
		first_name = message.chat.first_name
		last_name = message.chat.last_name
		bot.reply_to(message, '''
Hi {} {}, ini list command yaa
/start -> awalan untuk mengobrol dengan bot
/id    -> cek id kamu
/help  -> list comand untuk bot
/promo -> untuk melihat promo apa saja yang tersedia
/menu  -> membuka menu pilihan
/konter-> melihat id konter di surabaya
'''.format(first_name,last_name))
	else:
		bot.reply_to(message, 'Authorized user only')


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    # Bot response
    response = responses.get_response(text)
    update.message.reply_text(response)


def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')


print('bot start running')
bot.polling()