import telebot

token = "TOKEN"

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def main(user):
    username = user.from_user.username
    text = user.text
    print(f"{username} type : {text}")


bot.polling(True)
