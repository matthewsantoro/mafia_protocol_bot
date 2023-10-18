from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.fsm.context import FSMContext
from bot.utils.game_session import GameSession, get_list_players, RoleEnum
from bot.keyboards.game_session import set_role, choose_player, nomination
from bot.utils.states import OrderGame
from bot.utils.CustomCallBack import RoleCallback

router = Router()


@router.message(F.text.lower() == "а")
async def create_game(message: Message, state: FSMContext):
    await message.answer(
        "Введите список игроков одним списком",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(OrderGame.enter_players)


@router.message(OrderGame.enter_players)
async def entering_players(message: Message, state: FSMContext):
    game = GameSession(players=get_list_players())
    await state.update_data(game=game)
    await message.answer('FIY: Стадия выбора игроков пропушен на время разработки')
    await message.answer('Назначьте активные роли игроков', reply_markup=set_role())
    await state.set_state(OrderGame.role_selection)


@router.callback_query(OrderGame.role_selection, F.data.startswith('add'))
async def choose(callback: CallbackQuery):
    await callback.message.edit_text('Выберете номер игрока', reply_markup=choose_player(callback.data.split('_')[1]))


@router.callback_query(OrderGame.role_selection, RoleCallback.filter())
async def add_role(callback: CallbackQuery, state: FSMContext):
    _, role, player_pos = callback.data.split(':')
    player_pos = int(player_pos)
    data = await state.get_data()
    game = data['game']
    match role:
        case RoleEnum.SHERIFF:
            game.active_roles.sheriff = player_pos
        case RoleEnum.DON:
            game.active_roles.don = player_pos
        case RoleEnum.MAF:
            if len(game.active_roles.mafia) == 2:
                game.active_roles.mafia.pop(0)
            game.active_roles.mafia.append(player_pos)

    await state.update_data(game=game)

    if game.active_roles.don and game.active_roles.sheriff and len(game.active_roles.mafia) == 2:
        await callback.message.answer(
            f'Отлично! Роли назначены.<span class="tg-spoiler">Шериф: {game.active_roles.sheriff} Дон:{game.active_roles.don} мафия:{" ".join(list(map(str, game.active_roles.mafia)))}</span>')
        await state.set_state(OrderGame.nomination)
        await callback.message.answer('Стадия выставления кандидатур', reply_markup=nomination())

    await callback.message.edit_text('Назначьте активные роли игроков', reply_markup=set_role())
