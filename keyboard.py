from telebot import types

main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)

key1 = types.KeyboardButton('Перевести валюту 😳')
key2 = types.KeyboardButton('Поточні курси 💰')
main_keyboard.add(key1, key2)



userCurrency = types.InlineKeyboardMarkup(row_width = 1)
key1 = types.InlineKeyboardButton(text="Доллари $", callback_data='userUSD')
key2 = types.InlineKeyboardButton(text="Євро €", callback_data='userEUR')
key3 = types.InlineKeyboardButton(text="Рубль ₽ 🤮", callback_data='userRUB')
key4 = types.InlineKeyboardButton(text="Гривня ₴", callback_data='userUAH')
userCurrency.add(key1, key2, key3, key4)


calcCurrency = types.InlineKeyboardMarkup(row_width = 1)
key1 = types.InlineKeyboardButton(text="Доллари $", callback_data='getUSD')
key2 = types.InlineKeyboardButton(text="Євро €", callback_data='getEUR')
key3 = types.InlineKeyboardButton(text="Рубль ₽ 🤮", callback_data='getRUB')
key4 = types.InlineKeyboardButton(text="Гривня ₴", callback_data='getUAH')
calcCurrency.add(key1, key2, key3, key4)


rate_menu = types.InlineKeyboardMarkup(row_width = 1)
key1 = types.InlineKeyboardButton(text="Курс доллара", callback_data='USD_rate')
key2 = types.InlineKeyboardButton(text="Курс євро", callback_data='EUR_rate')
key3 = types.InlineKeyboardButton(text="Курс рубля 🤮", callback_data='RUB_rate')
key4 = types.InlineKeyboardButton(text="Курс гривні", callback_data='UAH_rate')
rate_menu.add(key1, key2, key3, key4)
