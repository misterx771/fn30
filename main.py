import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import FilmBaza
from buttons import asosiy_tugmalar, kategoriya_tugmalari, film_tugmalari, orqaga_tugmasi

bot = telebot.TeleBot("7373419973:AAEYMy7UbcQF0fMi_WBjdNypLUIye3iZD9A")
baza = FilmBaza()


@bot.message_handler(commands=['start'])
def start_xabari(message):
    bot.send_message(
        message.chat.id,
        "🎥 Film botiga xush kelibsiz!\n"
        "Quyidagi menyudan tanlang:",
        reply_markup=asosiy_tugmalar()
    )


@bot.callback_query_handler(func=lambda call: call.data == "filmlar")
def kategoriyalar_royxati(call):
    try:
        kat_list = baza.kategoriyalarni_ol()
        if not kat_list:
            bot.answer_callback_query(call.id, "Kategoriyalar topilmadi!")
            return

        bot.edit_message_text(
            "Kategoriyani tanlang:",
            call.message.chat.id,
            call.message.message_id,
            reply_markup=kategoriya_tugmalari(kat_list))
    except Exception as e:
        print(f"Xato: {e}")
        bot.answer_callback_query(call.id, "Xatolik yuz berdi!")


@bot.callback_query_handler(func=lambda call: call.data.startswith("kat_"))
def filmlar_royxati(call):
    kat_id = int(call.data.split("_")[1])
    film_list = baza.filmlarni_ol(kat_id)

    if not film_list:
        bot.answer_callback_query(call.id, "Bu kategoriyada filmlar yoʻq!")
        return

    bot.edit_message_text(
        "Filmlar roʻyxati:",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=film_tugmalari(film_list))


@bot.callback_query_handler(func=lambda call: call.data.startswith("film_"))
def film_malumoti(call):
    film_id = int(call.data.split("_")[1])
    film = baza.film_malumot(film_id)

    if not film:
        bot.answer_callback_query(call.id, "Film topilmadi!")
        return

    text = f"🎬 <b>{film[0]}</b> ({film[2]})\n\n{film[1]}"

    if film[3]:
        bot.send_video(
            call.message.chat.id,
            film[3],
            caption=text,
            parse_mode="HTML",
            reply_markup=orqaga_tugmasi())
        bot.delete_message(call.message.chat.id, call.message.message_id)
    else:
        bot.edit_message_text(
            text,
            call.message.chat.id,
            call.message.message_id,
            parse_mode="HTML",
            reply_markup=orqaga_tugmasi())


@bot.callback_query_handler(func=lambda call: call.data == "orqaga")
def orqaga_qaytish(call):
    bot.edit_message_text(
        "Bosh menyu:",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=asosiy_tugmalar())


@bot.callback_query_handler(func=lambda call: call.data == "yordam")
def yordam(call):
    bot.answer_callback_query(call.id, "Yordam uchun @mister_x771 bilan bogʻlaning")


if __name__ == "__main__":
    bot.infinity_polling()