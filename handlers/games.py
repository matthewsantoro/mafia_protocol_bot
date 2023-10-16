from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from bot.utils.states import OrderGame
from aiogram.fsm.context import FSMContext
from bot.utils.game_session import GameSession, get_list_players
from bot.keyboards.game_session import nomination, set_role, choose_player

router = Router()


@router.message(OrderGame.enter_players)
async def entering_players(message: Message, state: FSMContext):
    game = GameSession(players=get_list_players())
    await state.update_data(game=game)
    await message.answer('FIY: Стадия выбора игроков пропушен на время разработки')
    await message.answer('Назначьте активные роли игроков', reply_markup=set_role())
    await state.set_state(OrderGame.role_selection)


@router.message(F.text.lower() == "а")
async def create_game(message: Message, state: FSMContext):
    await message.answer(
        "Введите список игроков одним списком",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(OrderGame.enter_players)


@router.callback_query(OrderGame.role_selection, F.data == 'add_sheriff')
async def add_sheriff(callback: CallbackQuery, state: FSMContext):
    await state.update_data(pick_role=F.data)
    await callback.message.answer('Выберете номер игрока', reply_markup=choose_player())


@router.callback_query(OrderGame.role_selection, F.data.startswith('player'))
async def add_role(callback: CallbackQuery, state: FSMContext):
    await state.update_data(pick_role=F.data)
    await callback.message.edit_text('Выберете номер игрока')
