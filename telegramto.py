import telebot
from telebot import types
import json
import os

TOKEN = '7255359172:AAGvAVDQMwjBw0FXH_3-Gu41lEgj-B1237E'
bot = telebot.TeleBot(TOKEN)

SUBSCRIBERS_FILE = 'subscribers.json'

def load_subscribers():
    if os.path.exists(SUBSCRIBERS_FILE):
        with open(SUBSCRIBERS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_subscribers():
    with open(SUBSCRIBERS_FILE, 'w') as f:
        json.dump(subscribers, f)

subscribers = load_subscribers()

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.chat.id in subscribers:
        button = types.KeyboardButton("Отписаться от уведомлений")
    else:
        button = types.KeyboardButton("Включить уведомления")
    markup.add(button)
    if message.text != "Клавиатура обновлена":
        bot.send_message(message.chat.id, "Клавиатура обновлена", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Включить уведомления")
def ask_password(message):
    bot.send_message(message.chat.id, "Введите пароль")
    bot.register_next_step_handler(message, process_password)

@bot.message_handler(func=lambda message: message.text == "Отписаться от уведомлений")
def unsubscribe(message):
    if message.chat.id in subscribers:
        subscribers.remove(message.chat.id)
        save_subscribers()
        bot.send_message(message.chat.id, "Вы отписались от уведомлений.")
    else:
        bot.send_message(message.chat.id, "Вы не подписаны на уведомления.")
    
    start(message)

def process_password(message):
    password = message.text.strip()
    correct_password = "1123"

    if password == correct_password:
        if message.chat.id not in subscribers:
            subscribers.append(message.chat.id)
            save_subscribers()
            bot.send_message(message.chat.id, "Вы подписались на уведомления!")
        else:
            subscribers.remove(message.chat.id)
            save_subscribers()
            bot.send_message(message.chat.id, "Вы отписались от уведомлений.")
        start(message)
    else:
        bot.send_message(message.chat.id, "Неверный пароль. Попробуйте снова:")
        bot.register_next_step_handler(message, process_password)

def send_tg(form_data):
    for user_id in subscribers:
        bot_message = f"{form_data['name']}\n"
        bot_message += f"{form_data['phone']}\n"
        if form_data['comment']:
            bot_message += f"Коммент: {form_data['comment']}"
        bot.send_message(user_id, bot_message)

def start_bot():
    bot.polling()

if __name__ == "__main__":
    bot.polling()