import telebot
from keyboard import *
from config import TOKEN
from ExchangesData import currencyList, exchanges

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def hello(message):
    msg = bot.send_message(
        chat_id=message.chat.id,
        text='Привіт, ' + message.chat.first_name + "  😳",
        reply_markup=main_keyboard
    )

@bot.message_handler(commands=['help'])
def help(message):
    msg = bot.send_message(
        chat_id=message.chat.id,
        text='😳 Розробив 😳 Судак 😳 Павло 😳'
    )

userValue = -1
userValueSymbol = ""
userValueInUAH = -1


@bot.callback_query_handler(func=lambda call: call.data == 'USD_rate')
def get_usd_rate(call):
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text= "1$ = " + str(currencyList['USD'].exchange(currencyList['EUR'])) +
                                "€\n1$ = " + str(currencyList['USD'].exchange(currencyList['RUB'])) +
                                "₽\n1$ = " + str(currencyList['USD'].sell) + "₴")


@bot.callback_query_handler(func=lambda call: call.data == 'EUR_rate')
def get_usd_rate(call):
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text="1€ = " + str(currencyList['EUR'].exchange(currencyList['USD'])) +
                                "$\n1€ = " + str(currencyList['EUR'].exchange(currencyList['RUB'])) +
                                "₽\n1€ = " + str(currencyList['EUR'].sell) + "₴")


@bot.callback_query_handler(func=lambda call: call.data == 'RUB_rate')
def get_usd_rate(call):
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text="1₽ = " + str(currencyList['RUB'].exchange(currencyList['USD'])) +
                               "$\n1₽ = " + str(currencyList['RUB'].exchange(currencyList['EUR'])) +
                               "€\n1₽ = " + str(currencyList['RUB'].sell) + "₴")


@bot.callback_query_handler(func=lambda call: call.data == 'UAH_rate')
def get_usd_rate(call):
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text="1₴ = " + str(currencyList['UAH'].exchange(currencyList['USD'])) +
                               "$\n1₴ = " + str(currencyList['UAH'].exchange(currencyList['EUR'])) +
                               "€\n1₴ = " + str(currencyList['UAH'].exchange(currencyList['RUB'])) + "₽")


@bot.message_handler(content_types=['text'])
def step1(message):
    global userValue
    if (message.text.isnumeric()):
        userValue = float(message.text)
        msg = bot.send_message(chat_id=message.chat.id,
                               text="Оберіть вашу валюту",
                               reply_markup=userCurrency
                               )
    else:
        text = message.text.lower()
        if text == 'поточні курси 💰':
            bot.send_message(chat_id=message.chat.id,
                             text='Оберіть валюту',
                             reply_markup=rate_menu
                             )

        elif text == 'перевести валюту 😳':
            msg = bot.send_message(chat_id=message.chat.id,
                                   text="Введіть ціну",
                                   )
        elif (userValue == -1):
            msg = bot.send_message(chat_id=message.chat.id,
                                   text="Спочатку введіть ціну!")
            return
        else:
            msg = bot.send_message(
                chat_id=message.chat.id,
                text='Не можу розпізнати команду!'
            )


@bot.callback_query_handler(func=lambda call: call.data == 'userUSD')
def get_usd_rate(call):
    global userValueInUAH
    global userValueSymbol
    userValueInUAH = float(userValue) * float(exchanges[0]["rateSell"])
    userValueSymbol = "$"
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text="Введіть валюту яку ви хочете отримать",
                          reply_markup=calcCurrency)


@bot.callback_query_handler(func=lambda call: call.data == 'userEUR')
def get_usd_rate(call):
    global userValueInUAH
    global userValueSymbol
    userValueInUAH = float(userValue) * float(exchanges[1]["rateSell"])
    userValueSymbol = "€"
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text="Введіть валюту яку ви хочете отримать",
                          reply_markup=calcCurrency)


@bot.callback_query_handler(func=lambda call: call.data == 'userRUB')
def get_usd_rate(call):
    global userValueInUAH
    global userValueSymbol
    userValueInUAH = float(userValue) * float(exchanges[2]["rateSell"])
    userValueSymbol = "₽"
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text="Введіть валюту яку ви хочете отримать",
                          reply_markup=calcCurrency)


@bot.callback_query_handler(func=lambda call: call.data == 'userUAH')
def get_usd_rate(call):
    global userValueInUAH
    global userValueSymbol
    userValueInUAH = float(userValue)
    userValueSymbol = "₴"
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text="Введіть валюту яку ви хочете отримать",
                          reply_markup=calcCurrency)


@bot.callback_query_handler(func=lambda call: call.data == 'getUSD')
def get_usd_rate(call):
    inUsd = float(userValueInUAH) / float(exchanges[0]["rateBuy"])
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text=str(userValue) + userValueSymbol + "  = " + str(inUsd) + "$")


@bot.callback_query_handler(func=lambda call: call.data == 'getEUR')
def get_usd_rate(call):
    inEur = float(userValueInUAH) / float(exchanges[1]["rateBuy"])
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text=str(userValue) + userValueSymbol + "  = " + str(inEur) + "€")


@bot.callback_query_handler(func=lambda call: call.data == 'getRUB')
def get_usd_rate(call):
    inRub = float(userValueInUAH) / float(exchanges[2]["rateBuy"])
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text=f"{str(userValue)} {userValueSymbol}  = {str(inRub)} ₽")


@bot.callback_query_handler(func=lambda call: call.data == 'getUAH')
def get_usd_rate(call):
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text=f"{str(userValue)} {userValueSymbol} = {str(userValueInUAH)} ₴")
