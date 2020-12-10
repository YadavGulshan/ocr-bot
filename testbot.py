#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import json
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import requests

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from traceback import print_exc
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! Gulshan')
    update.message.reply_text(
        'https://stackoverflow.com/questions/12277933/send-data-from-a-textbox-into-flask')


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def convert_image(update, context):
    # print(update.message)
    file_name = "test.jpg"
    update.message.reply_text("woah I know this is an image, You idiot !")
    file_id = update.message.photo[-1].file_id
    newfile = context.bot.get_file(file_id)
    newfile.download(file_name)  # downloading image to server
    # using tesseract.
    try:
        ocred_stuff = (pytesseract.image_to_string(
            # Image.open(file_name), lang='hin'))
            Image.open(file_name), lang='eng'))
    except Exception:
        print_exc()
    if ocred_stuff is not None:
        update.message.reply_text(ocred_stuff)
    else:
        upate.message.reply_text(
            "Sorry I can't understand the texts written in image.")
    print("process completed")
    os.remove(file_name)
    ########################


def main():

    token = "1323879880:AAH1wCHjPvrpy2fUSdNFiGbCMFQz7CwA21s"

    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, echo))
    dispatcher.add_handler(MessageHandler(Filters.photo, convert_image))
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

# heroku setup : https://towardsdatascience.com/deploy-python-tesseract-ocr-on-heroku-bbcc39391a8d
# how to use env variables: https://www.nylas.com/blog/making-use-of-environment-variables-in-python/
# ocr space eg: https://github.com/UsergeTeam/Userge/blob/beta/userge/plugins/utils/ocr.py
# check the errors from line no. 74
