import telebot
import webbrowser
from telebot import types


bot = telebot.TeleBot('7322942271:AAEeZm-KqN9EAyviMlMh23MxVm61vyi3a6w')
markup = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton('Загугли, дурачок', url='https://google.com')
btn2 = types.InlineKeyboardButton('Гав-гав', callback_data='gav')
btn3 = types.InlineKeyboardButton('Мяу-мяу', callback_data='miy')
btn4 = types.InlineKeyboardButton('Удалиться', callback_data='delete')
btn5 = types.InlineKeyboardButton('Нажми сюда и увидишь кое-что крутое 😏', callback_data='edit')
markup.row(btn1)
markup.row(btn2, btn3)
markup.row(btn4, btn5)

markup_for_start = types.ReplyKeyboardMarkup()
btn_start_1 = types.KeyboardButton('Царь')
btn_start_2 = types.KeyboardButton('Князи')
btn_start_3 = types.KeyboardButton('Знать')
btn_start_4 = types.KeyboardButton('Холопы')
btn_start_5 = types.KeyboardButton('Крепостные')
btn_start_6 = types.KeyboardButton('Граждане')
markup_for_start.row(btn_start_1)
markup_for_start.row(btn_start_2, btn_start_3)
markup_for_start.row(btn_start_4, btn_start_5, btn_start_6)


@bot.message_handler(content_types=['photo', 'audio', 'video'])
def get_content(message):
    bot.reply_to(message, 'So cool photo!', reply_markup=markup)


@bot.message_handler(commands=['site', 'website'])
def to_site(message):
    webbrowser.open('google.com')


@bot.message_handler(commands=['start', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!', reply_markup=markup_for_start)

    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'Царь':
        bot.send_message(message.chat.id, 'Царь - глава государства')
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Князи':
        bot.send_message(message.chat.id, 'Князи - главы уездов')
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Знать':
        bot.send_message(message.chat.id, 'Знать - бояре и тп')
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Холопы':
        bot.send_message(message.chat.id, 'Холопы - ну считай рабы')
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Крепостные':
        bot.send_message(message.chat.id, 'Крепостные - ну это чуть получше холопов, почти рабы')
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Граждане':
        bot.send_message(message.chat.id, 'Граждане - ну простые люди, в городах живут')
        bot.register_next_step_handler(message, on_click)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'gav':
        bot.send_message(callback.message.chat.id, 'ГАВ-ГАВ, Я ПЕС ОБЛЕЗЛЫЙ')
        return
    elif callback.data == 'miy':
        bot.send_message(callback.message.chat.id, 'МЯУ-МЯУ, Я КОШАК ДРАНЫЙ')
        return
    elif callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
        return
    elif callback.data == 'edit':
        bot.edit_message_text('Ты лох', callback.message.chat.id, callback.message.message_id)
        return


@bot.message_handler()
def info(message):
    if message.text.lower() == 'my info':
        bot.send_message(message.chat.id, message)


bot.polling(none_stop=True)
