from telebot import TeleBot
from telebot.types import Message

TOKEN = "7373419973:AAEYMy7UbcQF0fMi_WBjdNypLUIye3iZD9A"

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Hello {message.from_user.first_name}!")

@bot.message_handler(commands=['help'])
def help(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Help is working!")


if __name__ == '__main__':
    bot.infinity_polling()