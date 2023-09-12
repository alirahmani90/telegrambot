import telebot
import cryptocompare
token = "6362416184:AAEIpNWpl-4Md6kkkoU1UFi2c6nTS1U8AO4"

text_meno = "قیمت بیتکوین /btc \n /eth قیمت اتریوم \n /shib قیمت شیبا"

bot = telebot.TeleBot(token)
print("bot is run")

# @bot.message_handler(content_types=['text'])
# def main(user):
#     username = user.from_user.username
#     text = user.text
#     id = user.chat.id
#     print(f"{username} type : {text}")

@bot.message_handler(commands=['start'])
def start(user):
    username = user.from_user.username
    text = user.text
    id = user.chat.id
    bot.send_message(id,text_meno)
    
@bot.message_handler(commands=['btc'])
def btc_price(user):
    username = user.from_user.username
    text = user.text
    id = user.chat.id
    btc_price = cryptocompare.get_price("BTC",currency='USD')["BTC"]['USD']
    bot.send_message(id,f"قیمت بیتکوین {btc_price} دلار")

@bot.message_handler(commands=['eth'])
def eth_price(user):
    username = user.from_user.username
    text = user.text
    id = user.chat.id
    eth_price = cryptocompare.get_price("ETH",currency='USD')["ETH"]['USD']
    bot.send_message(id,f"قیمت اتریوم {eth_price} دلار")

@bot.message_handler(commands=['shib'])
def shib_price(user):
    username = user.from_user.username
    text = user.text
    id = user.chat.id
    shib_price = cryptocompare.get_price("SHIB",currency='USD')["SHIB"]['USD']
    bot.send_message(id,f"قیمت شیبا {shib_price} دلار")

    



bot.polling(True)
