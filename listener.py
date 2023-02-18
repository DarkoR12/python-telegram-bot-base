from telegram import *
from telegram.ext import *

from time import sleep


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

    if 'gato' in message.lower():
        bot.send_chat_action(id, action=ChatAction.UPLOAD_PHOTO)
        sleep(1)
        bot.sendPhoto(chat_id=id, photo='https://i.ibb.co/Dp4dqJC/IMG-7920.jpg')