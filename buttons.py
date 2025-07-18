from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = KeyboardButton("Fantazy")
    btn2 = KeyboardButton("Comedy")
    btn3 = KeyboardButton("Dramma")
    btn4 = KeyboardButton("Triller")
    markup.add(btn1, btn2, btn3, btn4)
    return markup
