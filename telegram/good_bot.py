#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Codename Bot to reply to Telegram messages.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import codenamelist
import numpy as np
import ipgetter

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    start_text = 'Hi! This is the codenamebot.'
    start_text += '\nWrite /codename to generate a adjective-noun pair codename.'
    start_text += '\nMore commands coming soon.'

    update.message.reply_text(start_text)

def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('/generate is the only command so far')

def external_ip(bot, update):
    """Send external ip when /external_ip"""
    update.message.reply_text(my_external_ip)

def webserverupdate(bot, update):
    """Run github scipt"""
    update.message.reply_text("running github pull script")

def codename(bot, update):
    """Send a message when the command /generate is issued."""
    codename = codenames[r.randint(len(codenames))]
    update.message.reply_text(codename)

def echo(bot, update):
    """Echo the user message."""
    standard_response = " is not a recognized command. Use /help"
    response = update.message.text + standard_response
    update.message.reply_text(response)

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

# global stuff
r = np.random
codenames = []
my_external_ip = ipgetter.myip()

def main():
    print('generating list of codenames')
    global codenames
    codenames = codenamelist.generate()
    print('codenames generated')

    print('starting bot')
    """Start the bot."""
    #token = "73895804:AAGUxNLRfbfwFN_afyX-wuRqcmgE3yq2Kpw"
    token = ''
    with open("./creds/credentials.txt") as f:
        a = [line for line in f]
        token = a[0].strip()
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('webserverupdate', webserverupdate))
    dp.add_handler(CommandHandler('codename', codename))
    dp.add_handler(CommandHandler('external_ip', external_ip))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    print('bot now running')

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
    print('bot shutting down')

if __name__ == '__main__':
    main()
