#!/usr/bin/python3
import telebot
import mysql.connector

mydb = mysql.connector.connect(
host= 'localhost',
user= 'root',
passwd= '',
database= 'bot')



#cek database sudah bisa diakses apa belum
#print(mydb)

sql = mydb.cursor()

api = '6065176168:AAH6VscAnFdnU_a9jjekELSSQzvbtGGlzN8'
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
  pesan_balasan = pesan_balasan.replace("'","")
  #menghilangkan tanda kurung
  pesan_balasan = pesan_balasan.replace("(","")
  pesan_balasan = pesan_balasan.replace(")","")
  #menghilangkan tanda koma
  pesan_balasan = pesan_balasan.replace(",","")

  bot.reply_to(message, pesan_balasan)

print('bot start running')
bot.polling()