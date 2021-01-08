import telebot
from keyboard import *
from config import TOKEN
from ExchangesData import currencyList

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(
        chat_id=message.chat.id,
        text='Привіт, ' + message.chat.first_name + "  😳",
        reply_markup=main_keyboard
    )


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(
        chat_id=message.chat.id,
        text='😳 Розробив 😳 Судак 😳 Павло 😳'
    )


@bot.callback_query_handler(func=lambda call:
                            call.data == 'USD_rate' or
                            call.data == 'EUR_rate' or
                            call.data == 'RUB_rate' or
                            call.data == 'UAH_rate')
def send_rates(call):
    currency_id = call.data
    currency_id = currency_id[:3]
    text_to_send = ""
    for curr in currencyList:
        if currency_id != curr:
            text_to_send = text_to_send +\
                           f"1 {currency_id} = {currencyList[currency_id].exchangeRate(currencyList[curr])} {curr}\n"

    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text=text_to_send)


userValue = 0
user_value_id = ""


@bot.message_handler(content_types=['text'])
def text_reader(message):
    global userValue
    if message.text.isnumeric():
        userValue = float(message.text)
        bot.send_message(chat_id=message.chat.id,
                         text="Оберіть вашу валюту",
                         reply_markup=userCurrency)
    else:
        text = message.text.lower()
        if text == 'поточні курси 💰':
            bot.send_message(chat_id=message.chat.id,
                             text='Оберіть валюту',
                             reply_markup=rate_menu
                             )

        elif text == 'перевести валюту 😳':
            bot.send_message(chat_id=message.chat.id,
                             text="Введіть ціну")
        elif userValue == -1:
            bot.send_message(chat_id=message.chat.id,
                             text="Спочатку введіть ціну!")
            return
        else:
            bot.send_message(
                chat_id=message.chat.id,
                text='Не можу розпізнати команду!'
            )


@bot.callback_query_handler(func=lambda call:
                            call.data == 'userUSD' or
                            call.data == 'userEUR' or
                            call.data == 'userRUB' or
                            call.data == 'userUAH')
def get_user_value_id(call):
    global user_value_id
    user_value_id = call.data
    user_value_id = user_value_id[-3:]
    calc_currency_kb = init_calc_kb(call.data)
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text="Введіть валюту яку ви хочете отримать",
                          reply_markup=calc_currency_kb)


@bot.callback_query_handler(func=lambda call:
                            call.data == 'getUSD' or
                            call.data == 'getEUR' or
                            call.data == 'getRUB' or
                            call.data == 'getUAH')
def print_new_value(call):
    wanted_currency_id = call.data
    wanted_currency_id = wanted_currency_id[-3:]
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text=f"{userValue} {user_value_id} = "
                               f"{currencyList[user_value_id].buyCurrency(currencyList[wanted_currency_id], userValue)}"
                               f" {wanted_currency_id}")
