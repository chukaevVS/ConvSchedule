import telebot
from database_control import *
from student_info.student import *

token = ""
bot = telebot.TeleBot(token)

# --- AUTH STUDENT --- #

student = Student()

@bot.message_handler(commands = ['start'])
def start_message(message):
    student.set_chat_id(message.chat.id)
    bot.send_message(message.chat.id,
                     "Привет! Я буду помогать тебе не забывать вовремя делать домашнее задание, но сначала " +
                     "я задам тебе пару вопросов :) \n\n" +
                     "На каком направлении ты учишься? (Полное название)")

@bot.message_handler(content_types=['text'])
def get_direction_message(message):
    bot.send_message(message.chat.id,
                     "А на каком курсе?")
    student.set_direction(message.text)
    bot.register_next_step_handler(message, get_course)

def get_course(message):
    bot.send_message(message.chat.id,
                     "Интересно, а в какой ты группе? 🙃")
    student.set_course(message.text)
    bot.register_next_step_handler(message, get_group)

def get_group(message):
    bot.send_message(message.chat.id,
                     "Не забывай про домашку и хорошего тебя дня!😊")
    student.set_group(message.text)
    add_student(student)

# --- AUTH STUDENT --- #

bot.infinity_polling()
