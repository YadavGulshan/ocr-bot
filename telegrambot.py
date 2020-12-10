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


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        'Hi! Gulshan\nWhat You want me to do ?\nOCR an Image containing\n1.English')
    # update.message.reply_text(
    #     'https://stackoverflow.com/questions/12277933/send-data-from-a-textbox-into-flask')


# def checkif(update, context):

#     check_lang = int(update.message.text)
#     print(update.message.text)
#     if(check_lang == 1):
#         language = 'eng'
#         # convert_image(update,context,language)
#         # print(language)
#         return language
#     else:
#         language = 'hin'
#         return language
#         # update.message.reply_text(update.message.text)
#         # print("got something baby")


def convert_image(update, context):
    # print(update.message)
    file_name = "test.jpg"
    update.message.reply_text("woah I know this is an image, You idiot !")
    file_id = update.message.photo[-1].file_id
    newfile = context.bot.get_file(file_id)
    newfile.download(file_name)  # downloading image to server
    # using tesseract.
    # language = checkif
    try:
        update.message.reply_text("trying............................")
        ocred_stuff = (pytesseract.image_to_string(
            # Image.open(file_name), lang='hin'))
            Image.open(file_name), lang='eng'))
        if ocred_stuff is not None:
            update.message.reply_text(ocred_stuff)
            update.message.reply_text("done buddy !")
        else:
            update.message.reply_text(
                "Sorry I can't understand the texts written in image.")
        print("process completed")
    except Exception:
        print_exc()
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

    # check if the user is saying 1 or 2 acc to language
    # do you want to ocr a image ?

    dispatcher.add_handler(MessageHandler(
        Filters.photo, convert_image))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
