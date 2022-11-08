from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy_log import *
import random


def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi {update.effective_user.first_name}!')


def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/hi - команда приветствия\n/time - текущее время\n/help - помощь по командам\n/sum - сложить два числа\n/w_d - удалить слова, содержащие абв\n/mix - перемешать числа')


def time_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')


def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text  # ~input
    print(msg)
    items = msg.split() # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}')  # ~print


def w_d_command(update: Update, context: CallbackContext):
    log(update, context)
    input_text = update.message.text[4:] if len(update.message.text) > 4 else "" # ввод данных с отрезанием первых трёх символов
    input_text = words_delete(input_text)
    if input_text:
        update.message.reply_text(input_text)


def words_delete(input_text):
    if not input_text:
        return ""
    input_text = list(filter(lambda x: 'абв' not in x, input_text.split()))
    return " ".join(input_text)


def mix_command(update: Update, context: CallbackContext):
    log(update, context)
    input_text = update.message.text[4:] if len(update.message.text) > 4 else "" # ввод данных с отрезканием 
    randomlist = input_text.split() if input_text else []
    if not input_text:
        randomlist = random.sample(range(10), 5)
        update.message.reply_text(randomlist)
    random.shuffle(randomlist)
    update.message.reply_text(randomlist)


# import random
# randomlist = random.sample(range(10), 5)
# print(f"Original list: {randomlist}")
# random.shuffle(randomlist)
# print(f"Shuffled list: {randomlist}")

# def ran_command(update: Update, context: CallbackContext):
#     log(update, context)
#     input_text = update.message.text[4:] if len(update.message.text) > 4 else ""
#     randomlist = input_text.split() if input_text else []
#     if not input_text:
#         randomlist = random.sample(range(10), 5)
#     update.message.reply_text(randomlist)
#     random.shuffle(randomlist)
#     update.message.reply_text(randomlist
