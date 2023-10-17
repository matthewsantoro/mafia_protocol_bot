from aiogram.filters.callback_data import CallbackData


class RoleCallback(CallbackData, prefix='role'):
    role : str
    number : str