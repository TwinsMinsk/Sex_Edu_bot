from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Привет! Я ваш Telegram бот.')

def main():
    # Создайте Updater и передайте ему токен вашего бота.
    updater = Updater("6724707153:AAGMxLSwLy9-MmsXguzSzt75hn7_qwUBWz8", use_context=True)

    # Получите диспетчера для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируйте команду /start
    dp.add_handler(CommandHandler("start", start))

    # Начните поиск обновлений
    updater.start_polling()

    # Остановите бота, если был нажат Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
