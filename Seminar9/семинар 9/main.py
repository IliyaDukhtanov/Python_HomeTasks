from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *

TOKEN = "D:\\Learning\\Practice\\Python\\telegram_bot_token.txt"
with open(TOKEN, "r", encoding="UTF-8") as f: 
    data = f.read()
updater = Updater(data) 

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
updater.dispatcher.add_handler(CommandHandler('w_d', w_d_command))
updater.dispatcher.add_handler(CommandHandler('mix', mix_command))

updater.start_polling()
updater.idle()
