import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '6724707153:AAGMxLSwLy9-MmsXguzSzt75hn7_qwUBWz8'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Мидлварь для удаления системных сообщений
class SystemMessagesFilter(BaseMiddleware):
    async def on_pre_process_message(self, message: types.Message, data: dict):
        if message.content_type in ['new_chat_members', 'left_chat_member', 'new_chat_photo', 'delete_chat_photo', 'group_chat_created']:
            await message.delete()

# Обработчик для приветственного сообщения и установки ограничений
@dp.message_handler(content_types=['new_chat_members'])
async def new_user_joined(message: types.Message):
    for user in message.new_chat_members:
        # Создаем кнопку
        inline_btn = InlineKeyboardButton('Перейти к обучению', url='https://t.me/c/1927931288/1/204')
        inline_kb = InlineKeyboardMarkup().add(inline_btn)
        # Отправляем приветственное сообщение
        welcome_text = (
            f"🌟 {user.full_name}, добро пожаловать на курс \"<b>Сексуальное Образование</b>\"! 🌟\n\n"
            "🔍<b>Навигация по Sex Education</b>✅\n\n"
            "📜 <a href=\"https://t.me/c/1927931288/1/204\">О нашем канале и программе обучения</a>\n"
            "🎓 <u><a href=\"https://t.me/c/1927931288/1/206\">Учебные классы</a></u><u>:</u>\n"
            "\u2003 💪 <a href=\"https://t.me/c/1927931288/3/248\">Тренировка члена</a>\n"
            "\u2003 🧠 <a href=\"https://t.me/c/1927931288/15/272\">Женская психология</a>\n"
            "\u2003 💘 <a href=\"https://t.me/c/1927931288/29/183\">Знакомства</a>\n"
            "\u2003 💏 <a href=\"https://t.me/c/1927931288/7/293\">Обучение сексу</a>\n"
            "\u2003 👅 <a href=\"https://t.me/c/1927931288/11/334\">Оральный секс / Кунилингус</a>\n"
            "\u2003 💦 <a href=\"https://t.me/c/1927931288/9/328\">Сквиртинг</a>\n"
            "\u2003 🚫 <a href=\"https://t.me/c/1927931288/13/319\">Анальный секс</a>\n"
            "\u2003 🤲 <a href=\"https://t.me/c/1927931288/5/312\">Эротический массаж</a>\n"
            "\u2003 🔞 <a href=\"https://t.me/c/1927931288/163/353\">Образовательное порно</a>\n\n"
            "<u>❗Специальные предложения:</u>\n"
            "💎 <a href=\"https://t.me/c/1927931288/444/522\">Пожизненный </a><b><a href=\"https://t.me/c/1927931288/444/522\">Premium</a></b><a href=\"https://t.me/c/1927931288/444/522\"> </a><b><a href=\"https://t.me/c/1927931288/444/522\">аккаунт PornHub </a></b><a href=\"https://t.me/c/1927931288/444/522\">всего за </a><b><a href=\"https://t.me/c/1927931288/444/522\">300₽</a></b><a href=\"https://t.me/c/1927931288/444/522\">!</a>\n"
            "💪 <a href=\"https://t.me/c/1927931288/571/587\">Онлайн тренинг по увеличению и укреплению члена - </a><b><a href=\"https://t.me/c/1927931288/571/587\">Penis Building </a></b>"
            # ... (здесь должен быть ваш HTML-текст приветственного сообщения)
        )
        welcome_message = await bot.send_message(
            chat_id=message.chat.id,
            text=welcome_text,
            parse_mode=types.ParseMode.HTML,
            reply_markup=inline_kb,  # Добавляем кнопку к сообщению
            disable_notification=True
        )
        # Устанавливаем ограничения для пользователя
        await bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=user.id,
            permissions=types.ChatPermissions(
                can_send_messages=False,
                can_send_media_messages=False,
                can_send_other_messages=False,
                can_add_web_page_previews=False
            )
        )
        # Удаляем приветственное сообщение через 60 секунд
        await asyncio.sleep(60)
        await bot.delete_message(chat_id=message.chat.id, message_id=welcome_message.message_id)

# Регистрируем мидлварь
dp.middleware.setup(SystemMessagesFilter())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
