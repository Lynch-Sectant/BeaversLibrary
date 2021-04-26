# Импортируем необходимые классы.
from telegram.ext import Updater
from telegram.ext import CommandHandler
from time import localtime, asctime
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove


TOKEN = '1562678469:AAElhuGF-neaanXq-pRzuDgFCdwZMGi_vkg'


reply_keyboard = [['/start', '/end', '/info', '/login'],
                  ['/time', '/error', '/hide']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

updater = Updater(TOKEN, use_context=True)

def time(update, context):
    t = localtime()
    update.message.reply_text(asctime(t))

def error(update, context):
    update.message.reply_text('ВОЗМОЖНЫЕ ПРИЧИНЫ ПРОБЛЕМЫ')

def info(update, context):
    update.message.reply_text('Создатели: Lynch-Sectant, ArtyomAzuka, Lesnihiy.  '
                              'Сайт нужен для публикации различных литературных произведений')

def login(update, context):
    update.message.reply_text("Чтобы зарегестрироватья нужен логин и пароль. "
                              "Наш сайт доступен по ссылке : *ссылка*")

def start(update, context):
    update.message.reply_text(
        "Я бот-справочник. Какая информация вам нужна?",
        reply_markup=markup
    )

def end(update, context):
    update.message.reply_text(
        "Обидно.",
        reply_markup=ReplyKeyboardRemove()
                              )

def hide(update, context):
    update.message.reply_text('прячу',
        reply_markup=ReplyKeyboardRemove()
                              )


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("time", time))
    dp.add_handler(CommandHandler("error", error))
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("login", login))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("end", end))
    dp.add_handler(CommandHandler("hide", hide))
    updater.start_polling()
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
