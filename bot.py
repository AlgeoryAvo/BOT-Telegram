import telebot
from telebot import types

#API
bot = telebot.TeleBot('6065176168:AAH6VscAnFdnU_a9jjekELSSQzvbtGGlzN8')


#ACCOUNT


@bot.message_handler(commands=['start'])
def start(message) :
    bot.reply_to(message, 'Halo... Selamat Datang')
   
@bot.message_handler(commands=['info'])
def start(message) :
    bot.reply_to(message, 'Info opo su')

@bot.message_handler(commands=['menu'])
def send_welcome(message) :
    #Function pilihan 
    markup = types.ReplyKeyboardMarkup() 
    itema = types.KeyboardButton('/start')
    itemb = types.KeyboardButton('/info')
    itemc = types.KeyboardButton('/promo1')
    itemd = types.KeyboardButton('/promo2')

    markup.row(itema,itemb)
    markup.row(itemc,itemd)
    bot.send_message(message.chat.id, 'menu??', reply_markup=markup)

@bot.message_handler(commands=['template'])
def send_welcome(message) :
    #Function pilihan 
    row = types.ForceReply()
    table = types.ForceReply('Kode Transaksi')
    itemb = types.ForceReply('Nominal Transaksi')
    itemc = types.ForceReply('Tanggal Transaksi')
    itemd = types.ForceReply('Konter')

#Transfer video,foto,pdf
#CODING FOTO
@bot.message_handler(commands=['promo1'])
def text(message) :
    chat_id = message.chat.id
    bot.send_photo(chat_id, open('Dir/img.png', 'rb'))

@bot.message_handler(commands=['promo2'])
def text(message) :
    chat_id = message.chat.id
    bot.send_photo(chat_id, open('Dir/img1.jpg', 'rb'))

@bot.message_handler(commands=['promo3'])
def text(message) :
    chat_id = message.chat.id
    bot.send_photo(chat_id, open('Dir/img2.jpg', 'rb'))

#Transfer video,foto,pdf
#CODING VIDEO
@bot.message_handler(commands=['video1'])
def text(message) :
    chat_id = message.chat.id
    bot.send_video(chat_id, open('Dir/video1.mp4', 'rb'))


@bot.message_handler(commands=['video2'])
def text(message) :
    chat_id = message.chat.id
    bot.send_video(chat_id, open('Dir/video2.mp4', 'rb'))

print('Bot is Running')
bot.polling()