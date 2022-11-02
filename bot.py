from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters
from settings import TG_TOKEN
from utility import startmenu


def sms(bot, update):
    bot.message.reply_text('start')
    #print(bot.message)

def parrot(bot, update):
    print(bot.message.text) # display text send in chat
    print(bot.message) # display user information

def main():
    tg_bot = Updater(TG_TOKEN)
    tg_bot.dispatcher.add_handler(CommandHandler('start', sms))
    tg_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))
    tg_bot.start_polling()
    tg_bot.idle()


main()
