import telebot
from keyboard import *
from config import TOKEN
from ExchangesData import currencyList

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
userValueID = ""


@bot.callback_query_handler(func=lambda call: call.data == 'USD_rate')
def get_usd_rate(call):
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text= "1USD = " + str(currencyList['USD'].exchangeRate(currencyList['EUR'])) +
                                "EUR\n1USD = " + str(currencyList['USD'].exchangeRate(currencyList['RUB'])) +
                                "RUB\n1USD = " + str(currencyList['USD'].sell) + "UAH")


@bot.callback_query_handler(func=lambda call: call.data == 'EUR_rate')
def get_usd_rate(call):
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text="1EUR = " + str(currencyList['EUR'].exchangeRate(currencyList['USD'])) +
                                "USD\n1EUR = " + str(currencyList['EUR'].exchangeRate(currencyList['RUB'])) +
                                "RUB\n1EUR = " + str(currencyList['EUR'].sell) + "UAH")


@bot.callback_query_handler(func=lambda call: call.data == 'RUB_rate')
def get_usd_rate(call):
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text="1RUB = " + str(currencyList['RUB'].exchangeRate(currencyList['USD'])) +
                               "USD\n1RUB = " + str(currencyList['RUB'].exchangeRate(currencyList['EUR'])) +
                               "EUR\n1RUB = " + str(currencyList['RUB'].sell) + "UAH")


@bot.callback_query_handler(func=lambda call: call.data == 'UAH_rate')
def get_usd_rate(call):
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text="1UAH = " + str(currencyList['UAH'].exchangeRate(currencyList['USD'])) +
                               "USD\n1UAH = " + str(currencyList['UAH'].exchangeRate(currencyList['EUR'])) +
                               "EUR\n1UAH = " + str(currencyList['UAH'].exchangeRate(currencyList['RUB'])) + "RUB")


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
    global userValueID
    userValueID = "USD"
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text="Введіть валюту яку ви хочете отримать",
                          reply_markup=calcCurrency)


@bot.callback_query_handler(func=lambda call: call.data == 'userEUR')
def get_usd_rate(call):
    global userValueID
    userValueID = "EUR"
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text="Введіть валюту яку ви хочете отримать",
                          reply_markup=calcCurrency)


@bot.callback_query_handler(func=lambda call: call.data == 'userRUB')
def get_usd_rate(call):
    global userValueID
    userValueID = "RUB"
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text="Введіть валюту яку ви хочете отримать",
                          reply_markup=calcCurrency)


@bot.callback_query_handler(func=lambda call: call.data == 'userUAH')
def get_usd_rate(call):
    global userValueID
    userValueID = "UAH"
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text="Введіть валюту яку ви хочете отримать",
                          reply_markup=calcCurrency)


@bot.callback_query_handler(func=lambda call: call.data == 'getUSD'  or 'getEUR' or 'getRUB' or 'getUAH')
def get_usd_rate(call):
    wantedCurrencyID = call.data
    wantedCurrencyID = wantedCurrencyID[3:]
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text=f"{userValue} {userValueID} = {currencyList[userValueID].buyCurrency(currencyList[wantedCurrencyID],userValue)} {wantedCurrencyID}")
