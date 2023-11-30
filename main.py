from env import BOT_TOKEN
import telebot
import random
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['info'])
def send_info(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Привет! Я бот созданный Райымкуловым Дидаром! Дата моего создания 30.11.2023 г. ")


if __name__ == "__main__":
    bot.polling(none_stop=True)









