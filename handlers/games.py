from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from bot.utils.states import OrderGame
from aiogram.fsm.context import FSMContext
from bot.utils.game_session import GameSession, get_list_players
from bot.keyboards.game_session import nomination

router = Router()


@router.message(OrderGame.enter_players)
async def entering_players(message: Message, state: FSMContext):
    game = GameSession(players=get_list_players())
    await state.update_data(game=game)
    await message.answer('Пока игроки забиваются автоматически')
    await message.answer('День.Выберите кого выставвили', reply_markup=nomination())


@router.message(F.text.lower() == "а")
async def create_game(message: Message, state: FSMContext):
    await message.answer(
        "Введите список игроков одним списком",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(OrderGame.enter_players)
