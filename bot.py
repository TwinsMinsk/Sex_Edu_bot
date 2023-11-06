from telegram.ext import Updater, Filters, MessageHandler, CallbackContext
from telegram import Update, ChatPermissions
import time
import logging

# Вставьте ваш токен бота здесь
TOKEN = '6724707153:AAGMxLSwLy9-MmsXguzSzt75hn7_qwUBWz8'

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Функция для удаления всех системных сообщений
def delete_system_messages(update: Update, context: CallbackContext) -> None:
    message = update.message
    if message:
        # Удаляем сообщения о входе/выходе участников, о новых фото группы и т.д.
        context.bot.delete_message(chat_id=message.chat_id, message_id=message.message_id)

# Функция для отправки приветственного сообщения и его удаления через минуту
def welcome_message(update: Update, context: CallbackContext) -> None:
    new_members = update.message.new_chat_members
    for member in new_members:
        welcome_text = f"Привет, {member.full_name}! Добро пожаловать в группу!"
        welcome_message = context.bot.send_message(chat_id=update.message.chat_id, text=welcome_text)
        # Запланировать удаление приветственного сообщения через 60 секунд
        context.job_queue.run_once(delete_message, 60, context=(update.message.chat_id, welcome_message.message_id))

# Функция для удаления сообщения
def delete_message(context: CallbackContext) -> None:
    job = context.job
    chat_id, message_id = job.context
    context.bot.delete_message(chat_id=chat_id, message_id=message_id)

# Функция для ограничения новых пользователей
def restrict_new_members(update: Update, context: CallbackContext) -> None:
    new_members = update.message.new_chat_members
    for member in new_members:
        # Установить разрешения для нового пользователя
        permissions = ChatPermissions(can_send_messages=False)
        # Установить запрет на 24 часа (86400 секунд)
        context.bot.restrict_chat_member(chat_id=update.message.chat_id, user_id=member.id, permissions=permissions, until_date=time.time()+86400)

# Основная функция, где происходит инициализация бота и диспетчера
def main() -> None:
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN, use_context=True)

    # Получаем диспетчера для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчики для удаления всех системных сообщений
    dp.add_handler(MessageHandler(Filters.status_update, delete_system_messages))

    # Регистрируем обработчики для приветственных сообщений и ограничения новых пользователей
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome_message))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, restrict_new_members))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
