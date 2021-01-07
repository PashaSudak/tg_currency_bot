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


@bot.callback_query_handler(func=lambda call: call.data == 'USD_rate' or
                                              call.data == 'EUR_rate' or
                                              call.data == 'RUB_rate' or
                                              call.data == 'UAH_rate')
def send_rates(call):
    currencyID = call.data
    currencyID = currencyID[:3]
    textToSend = ""
    for curr in currencyList:
        if currencyID != curr:
            textToSend = textToSend + f"1 {currencyID} = {currencyList[currencyID].exchangeRate(currencyList[curr])} {curr}\n"

    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text=textToSend)


userValue = 0
userValueID = ""

@bot.message_handler(content_types=['text'])
def textReader(message):
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


@bot.callback_query_handler(func=lambda call: call.data == 'userUSD' or
                                              call.data == 'userEUR' or
                                              call.data == 'userRUB' or
                                              call.data == 'userUAH')
def getUserValueID(call):
    global userValueID
    userValueID = call.data
    userValueID = userValueID[-3:]
    calcCurrencyKB = initCalcKB(call.data)
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text="Введіть валюту яку ви хочете отримать",
                          reply_markup=calcCurrencyKB)


@bot.callback_query_handler(func=lambda call: call.data == 'getUSD' or
                                              call.data == 'getEUR' or
                                              call.data == 'getRUB' or
                                              call.data == 'getUAH')
def printNewValue(call):
    wantedCurrencyID = call.data
    wantedCurrencyID = wantedCurrencyID[-3:]
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text=f"{userValue} {userValueID} = {currencyList[userValueID].buyCurrency(currencyList[wantedCurrencyID], userValue)} {wantedCurrencyID}")
