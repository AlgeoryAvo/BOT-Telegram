#!/usr/bin/python3
import telebot
import datetime

api = '6065176168:AAH6VscAnFdnU_a9jjekELSSQzvbtGGlzN8'
bot = telebot.TeleBot(api)

def log(message,perintah):
	tanggal = datetime.datetime.now()
	tanggal = tanggal.strftime('%d-%B-%Y')
	nama_awal = message.chat.first_name
	nama_akhir = message.chat.last_name
	id_user = message.chat.id
	text_log = '{}, {}, {} {}, {} \n'.format(tanggal, id_user, nama_awal, nama_akhir, perintah)
	print(text_log)
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
		bot.reply_to(message, 'Hi, apa kabar {} {}?'.format(first_name,last_name))
	else:
		bot.reply_to(message, 'Authorized user only')

@bot.message_handler(commands=['id'])
def action_id(message):
	user = open('user.txt','r')
	user = user.read()
	id_message = message.chat.id
	if str(id_message) in user:	
		log(message,'Cek ID')
		first_name = message.chat.first_name
		last_name = message.chat.last_name
		id_telegram = message.chat.id
		bot.reply_to(message, '''
Hi, ini ID Telegram kamu
Nama = {} {}
ID = {}
		'''.format(first_name,last_name, id_telegram))
	else:
		bot.reply_to(message, 'Authorized user only')

@bot.message_handler(commands=['learn_python'])
def action_learn(message):
	user = open('user.txt','r')
	user = user.read()
	id_message = message.chat.id
	if str(id_message) in user:	
		log(message, 'Open tutorial')
		first_name = message.chat.first_name
		last_name = message.chat.last_name
		bot.reply_to(message, '''
Hi {} {} berikut list 

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
/start -> Sapa Bot dulu Gan
/id -> Cek id Kamu
/help -> List Command Bot
/learn_python -> open tutorial youtube
'''.format(first_name,last_name))
	else:
		bot.reply_to(message, 'Authorized user only')

print('bot start running')
bot.polling()