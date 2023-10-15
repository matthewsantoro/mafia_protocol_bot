from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from bot.keyboards.main_menu import main_menu

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Добро пожаловать, это тестовая версия бота. Созданного @matthewsantoro для протоколирования игры "
        "мафия.Выбери необходимый пункт из меню.",
        reply_markup=main_menu()
    )





@router.message(F.text.lower() == "помощь")
async def answer_no(message: Message):
    await message.answer(
        "Жаль...",
        reply_markup=ReplyKeyboardRemove()
    )
