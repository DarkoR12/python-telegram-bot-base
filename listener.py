from telegram import *
from telegram.ext import *


def listener(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    user = update.effective_message.from_user
    chatID = update.effective_message.chat_id
    message = update.effective_message.text
    priv = chatID > 0
    # Si el mensaje está respondiendo a otro mensaje, podrás acceder a este otro con replyToMessage.text
    replyToMessage = update.effective_message.reply_to_message

    if priv and 'hola' in message.lower():
        update.message.reply_text('¡Hola! ¿Conoces a @HanzoBot?')