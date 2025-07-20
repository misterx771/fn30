from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def asosiy_tugmalar():
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("🎬 Filmlar", callback_data="filmlar"),
        InlineKeyboardButton("📝 Yordam", callback_data="yordam")
    )
    return markup

def kategoriya_tugmalari(kategoriyalar):
    markup = InlineKeyboardMarkup()
    for kat in kategoriyalar:
        markup.add(InlineKeyboardButton(kat[1], callback_data=f"kat_{kat[0]}"))
    markup.add(InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga"))
    return markup

def film_tugmalari(filmlar):
    markup = InlineKeyboardMarkup()
    for film in filmlar:
        markup.add(InlineKeyboardButton(film[1], callback_data=f"film_{film[0]}"))
    markup.add(InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga"))
    return markup

def orqaga_tugmasi():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga"))
    return markup