from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from datetime import datetime as dt
from time import time


def log(update: Update, context: CallbackContext):
    time = dt.now().strftime('%Y-%m-%d-%H:%M')
    file = open('db.csv', 'a')
    file.write(f'{time},{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
    file.close()
