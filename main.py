import telebot
import webbrowser


bot = telebot.TeleBot('7322942271:AAEeZm-KqN9EAyviMlMh23MxVm61vyi3a6w')


@bot.message_handler(commands=['site', 'website'])
def to_site(message):
    webbrowser.open('google.com')


@bot.message_handler(commands=['start', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')
    bot.send_message(message.chat.id, message)


@bot.message_handler()
def info(message):
    if message.text.lower() == 'my info':
        bot.send_message(message.chat.id, message)


bot.polling(none_stop=True)
