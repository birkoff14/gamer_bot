#!/usr/bin/env python
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

import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Ni yo mismo se que hacer!')
    
    
def juegos_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /juegos is issued."""
    update.message.reply_text('Free fire, Pokemon, Mortal Kombat y más juegos')

def supapa_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /supapa is issued."""
    update.message.reply_text('El mejor programador en Banco Azteca Querétaro')
    
def mujeres_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /mujeres is issued."""
    update.message.reply_text('Podemos mandar nudes, pero necesitamos material del buen Paquito Zendejas')

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)
    
def games(update, context):
    if(update.message.text.upper().find("POKEMON") > 0):
        update.message.reply_text("Es el mejor juego del mundo")
    if(update.message.text.upper().find("MORTAL KOMBAT") > 0):
        update.message.reply_text("Ese juego esta bien aburrido")
    if(update.message.text.upper().find("BIENVENIDO") > 0):
        update.message.reply_text("Espero que este grupo este chido y no haya maricones :V")
    if(update.message.text.upper().find("MANUEL") > 0 or update.message.text.upper().find("MENESES") > 0):
        update.message.reply_text("Este chavo esta bien rifado para programar")

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1587088976:AAFlq-J786VMDpVU6mhFIr54Tp8sd-yGQ_Q", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("juegos", juegos_command))
    dispatcher.add_handler(CommandHandler("supapa", supapa_command))
    dispatcher.add_handler(CommandHandler("mujeres", mujeres_command))

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, games))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()