import telebot
from telebot import types
import random

token = '5827903141:AAG1MLbBs9PU42OFnXgYFqVl3-2Rvu7vpV0'
bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('Play!')
btn2 = types.KeyboardButton('No! Thanks')
keyboard.add(btn1, btn2)



@bot.message_handler(commands=['start', 'game'])
def start_message(message):
    bot_message = bot.send_message(message.chat.id, 'Hello King, начнем игру?', reply_markup=keyboard)
    bot.register_next_step_handler(bot_message, check_answer)

def check_answer(message):
    if message.text == 'Play!': 
        bot.send_message(message.chat.id, 'Ok! тогда лови правила игры:\nНужно угадать число от 1 до 10. у тебя будет 3 попытки. ели не угаlаешь то я тебя повешу')
        number = random.randint(1, 10)
        print(number, '!!!!!')
        game(message, 3, number)
    elif message.text == 'No! Thanks':
        bot.send_message(message.chat.id, 'Goodbye!!')

    else:
        bot_message = bot.send_message(message.chat.id, 'va vveli:', reply_markup=keyboard)
        bot.register_next_step_handler(bot_message, check_answer)

def game(message, attems, number):
    message_bot = bot.send_message(message.chat.id, 'Выбери число:')
    bot.register_next_step_handler(message_bot, check_number, attems-1, number)

def check_number(message,attems, number):
    if message.text == str(number):
        bot.send_message(message.chat.id, 'Вы победили! Нарекаю вас удачливым!')
    elif attems == 0:
        bot.send_message(message.chat.id, 'ты проиграл!!!')
    else:
        bot.send_message(message.chat.id, 'Нет, ты не угадал. попробуй еще раз!')
        game(message, attems, number)

    
    

bot.polling()