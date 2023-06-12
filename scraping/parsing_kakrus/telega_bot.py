# import json
# import telebot
# from telebot import types
# from parse import parse_news
# token = '6171840213:AAFyDjmSk84vk7BkWyiiIhLjhJUvmxc3cWc'

# bot = telebot.TeleBot(token)
# keyboard = types.ReplyKeyboardMarkup()
# btn1 = types.KeyboardButton('Foto')
# btn2 = types.KeyboardButton('Opisanie')
# keyboard.add(btn1, btn2)

# def read_news():
#     with open('data.json',) as file:
#         data = json.load(file)
#     return data

# @bot.message_handler(commands=['start'])
# def start_parse(message):
#     print('!!!!!')
#     bot.send_message(message.chat.id, 'Hello, we started to parse some articles! plz wait a few seconds...')
#     print('started')
#     parse_news()
#     print('parsed')
#     data = read_news()
#     for x in data:
#         print(x)
#         bot.send_message(message.chat.id, f'{x} -->{data[x]["title"]}*', parse_mode='Markdown')

#     bot_message = bot.send_message(message.chat.id, 'Choice number of artcle for detail info()-')
#     bot.polling()

# import json
# import telebot
# from telebot import types
# from parse import parse_news

# token = '6171840213:AAFyDjmSk84vk7BkWyiiIhLjhJUvmxc3cWc'

# bot = telebot.TeleBot(token)

# keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
# btn1 = types.KeyboardButton('photo')
# btn2 = types.KeyboardButton('Description')
# keyboard.add(btn1, btn2)

# def read_news():
#     with open('data.json') as file:
#         data = json.load(file)
#     return data

# @bot.message_handler(commands=['start'])
# def start_parse(message):
#     print('!!!!!')
#     bot.send_message(message.chat.id, 'Hello, we started to parse some arcticles! Please wait a few seconds...')
#     print('started')
#     parse_news()
#     print('parsed')
#     data = read_news()
#     for x in data:
#         print(x)
#         bot.send_message(message.chat.id, f'{x} --> *{data[x]["title"]}*', parse_mode='Markdown')

#     bot_message = bot.send_message(message.chat.id, 'Choice number of article for detail info(1-20): ')
#     bot.register_next_step_handler(bot_message, check_number)

# def check_number(message):
#     nums = [str(x) for x in range(1, 21)]
#     if message.text not in nums:
#         print(message.text)
#         bot_message = bot.send_message(message.chat.id, 'Invalid number! You must choose number in range 1 to 20:')
#         bot.register_next_step_handler(bot.message, check_number)
#     else:
#         data = read_news()
#         bot_message = bot.send_message(message.chat.id, f'{data[message.text]["title"]}\nYou can see Description of this news and photo', reply_markup=keyboard)
#         bot.register_next_step_handler(bot_message, show_info, message.text, data)
# def show_info(message, number, data):
#     if message.text.lower() == 'photo':
#         bot.send_message(message.chat.id, data[number]['img'])
#         bot_message = bot.send_message(message.chat.id, 'Choice number of article for detail info(1-20): ')
#         bot.register_next_step_handler(bot_message, check_number)
#     else:
#         bot.send_message(message.chat.id, data[number]['desc'] )
#         bot_message = bot.send_message(message.chat.id, 'Choice number of article for detail info(1-20): ')
#         bot.register_next_step_handler(bot_message, check_number)


# bot.polling()

import json
import telebot
from telebot import types
from parse import parse_news

token = '6171840213:AAFyDjmSk84vk7BkWyiiIhLjhJUvmxc3cWc'

bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('Photo')
btn2 = types.KeyboardButton('Description')
keyboard.add(btn1, btn2)

def read_news():
    with open('data.json') as file:
        data = json.load(file)
    return data

@bot.message_handler(commands=['start'])
def start_parse(message):
    print('!!!!!')
    bot.send_message(message.chat.id, 'Hello, we started to parse some articles! Please wait a few seconds...')
    print('started')
    parse_news()
    print('parsed')
    data = read_news()
    for x in data:
        print(x)
        bot.send_message(message.chat.id, f'{x} --> *{data[x]["title"]}*', parse_mode='Markdown')

    bot_message = bot.send_message(message.chat.id, 'Choose a number for detailed information about the article (1-20): ')
    bot.register_next_step_handler(bot_message, check_number)

def check_number(message):
    nums = [str(x) for x in range(1, 21)]
    if message.text not in nums:
        bot_message = bot.send_message(message.chat.id, 'Invalid number! You must choose a number in the range from 1 to 20!')
        bot.register_next_step_handler(bot_message, check_number)
    else:
        data = read_news()
        number = int(message.text) - 1
        bot_message = bot.send_message(message.chat.id, f'{data[str(number+1)]["title"]}\n\nYou can see the description and photo of this news!', reply_markup=keyboard)
        bot.register_next_step_handler(bot_message, lambda m: show_info(m, number, data))

def show_info(message, number, data):
    if message.text.lower() == 'photo':
        bot.send_message(message.chat.id, data[str(number+1)]['img'])
    else:
        bot.send_message(message.chat.id, data[str(number+1)]['desc'])
        
    bot_message = bot.send_message(message.chat.id, 'Choose a number for detailed information about the article (1-20): ')
    bot.register_next_step_handler(bot_message, check_number)

bot.polling()