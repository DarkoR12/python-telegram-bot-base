#!/usr/bin/env python3
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
  ____    _    ____  _  _____  ____  _ ____  
 |  _ \  / \  |  _ \| |/ / _ \|  _ \/ |___ \ 
 | | | |/ _ \ | |_) | ' / | | | |_) | | __) |
 | |_| / ___ \|  _ <| . \ |_| |  _ <| |/ __/ 
 |____/_/   \_\_| \_\_|\_\___/|_| \_\_|_____|                      

TUTORIAL BÁSICO PARA BOTS DE TELEGRAM POR DARKOR12
V13.15

DOCUMENTACIÓN: https://python-telegram-bot.readthedocs.io/en/stable/index.html
WIKI: https://github.com/python-telegram-bot/python-telegram-bot/wiki
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from telegram import *  # Aquí importo toda la librería, pero puedes importar solo lo que necesites
from telegram.ext import *

import os
import sys
from threading import Thread
from random import randint

import listener


# Función que será ejecutada cuando alguien inicie el bot por primera vez y haga click en "START"
def start(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    user = update.effective_message.from_user
    chatID = update.effective_message.chat_id
    if not args:
        # https://t.me/HanzoBot?start=TOKEN
        # Si alguien entra a un enlace como este y le da a "START", tu bot recibirá el TOKEN en args
        pass

    bot.sendMessage(chatID, 'Hola, esto es un mensaje de prueba!')  # Puedes añadir botones, markdown, html...
    update.message.reply_text('Hola pero respondiendo al mensaje')  # Aquí igual
    print(f"{user.name} ({user.id} ~ {chatID}) -> /start")


def d(update: Update, context: CallbackContext):
    '''
    Función para tirar dados con /d
    - /d           Tira un dado de 20
    - /d X         Tira un dado de X
    '''
    args = context.args
    try:
        dice_size = int(args[0]) if args else 20
    except ValueError:
        update.message.reply_text('ERROR 🐡')
        return

    result = randint(1, dice_size)
    update.message.reply_text(f'El resultado es {result} 🎲')


def error(update: Update, context: CallbackContext):
    print(f'Update "{update}" caused error "{error}"')


def otherUpdates(update: Update, context: CallbackContext):
    '''
    A esta función llegan todos los updates de cosas como:
    - Alguien ha salido del grupo
    - Alguien ha entrado al grupo
    - Al grupo X se ha convertido en supergrupo
    '''
    m = update.message


def main():
    updater = Updater('tu:token')  # El TOKEN de tu bot creado con @BotFather
    dp = updater.dispatcher  # Dispatcher de los eventos

    def addC(filter, handler, **args):  # Función auxiliar
        dp.add_handler(CommandHandler(filter, handler, **args))

    def addM(filter, handler, **args):  # Función auxiliar
        dp.add_handler(MessageHandler(filter, handler, **args))

    addC('start', start)  # Con addC añades un handler para comandos "/" y con addM para recibir todos los mensajes
    addC('d', d, run_async=True)  # Puedes hacer que se ejecuten en paralelo con run_async

    addM(Filters.text, listener.listener)  # A esta función entrarán todos los mensajes de texto

    def stop_and_restart():  # Función auxiliar para reiniciar el bot
        updater.stop()
        os.execl(sys.executable, sys.executable, *sys.argv)

    def restart(update: Update, context: CallbackContext):
        update.message.reply_text('Restarting')
        Thread(target=stop_and_restart).start()

    addC('restart', restart, filters=Filters.user(username='@DarkoR12'))
    # Con este filtro puedes limitar el acceso a la función, también puedes realizar la comprobación a mano desde dentro de la función

    # Log all errors
    dp.add_error_handler(error)

    # Cualquier otro update no capturado entra aquí
    addM(Filters.all, otherUpdates)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
