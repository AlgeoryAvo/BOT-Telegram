@bot.message_handler(commands=['video1'])
def text(message) :
    chatid = message.chat.id
    bot.send_video(chat_id, open('Dir/video1.mp4', 'rb'))


@bot.message_handler(commands=['video2'])
def text(message) :
    chatid = message.chat.id
    bot.send_video(chat_id, open('Dir/video2.mp4', 'rb'))



@bot.message_handler(commands=['promo1'])
def text(message) :
    chatid = message.chat.id
    bot.send_photo(chat_id, open('img.png', 'rb'))


@bot.message_handler(commands=['promo2'])
def text(message) :
    chatid = message.chat.id
    bot.send_image(chat_id, open('Dir/img1.jpg', 'rb'))


