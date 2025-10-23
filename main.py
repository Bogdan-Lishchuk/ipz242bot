import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


bot = telebot.TeleBot(TOKEN)

def create_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Розклад"), KeyboardButton("Кабінет"), KeyboardButton("Learn"))
    return keyboard


@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(
        message.chat.id,
        "Вітаю! Оберіть одну з опцій нижче:",
        reply_markup=create_keyboard()
    )


@bot.message_handler(func=lambda message: True)
def message_handler(message):
    if message.text == "Розклад":
        bot.send_message(message.chat.id, "Ось посилання на розклад: https://rozklad.ztu.edu.ua/schedule/group/%D0%86%D0%9F%D0%97-24-2?new")
    elif message.text == "Кабінет":
        bot.send_message(message.chat.id, "Ось посилання на кабінет: https://cabinet.ztu.edu.ua/")
    elif message.text == "Learn":
        bot.send_message(message.chat.id, "Ось посилання на навчання: https://learn.ztu.edu.ua/")
    else:
        bot.send_message(message.chat.id, "Виберіть один із варіантів на клавіатурі!")



bot.polling(none_stop=True)
