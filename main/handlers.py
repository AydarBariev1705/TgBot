from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from keyboards import questionnaire_keyboard, check_keyboard
from utils import create_or_update_user


class Form(StatesGroup):
    name = State()
    lastname = State()
    check_state = State()


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message | CallbackQuery):
    await message.answer(
        "Добро пожаловать в бота!", reply_markup=questionnaire_keyboard()
    )


@router.callback_query(F.data == 'questionnaire')
@router.callback_query(F.data == 'incorrect')
async def callbacks_questionnaire(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer('Начнем анкетирование. Для начала укажи свое имя: ')
    await state.set_state(Form.name)


@router.message(F.text, Form.name)
async def lastname_questionnaire(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Супер!А теперь укажи свою фамилию: ')
    await state.set_state(Form.lastname)


@router.message(F.text, Form.lastname)
async def check_questionnaire(message: Message, state: FSMContext):
    await state.update_data(lastname=message.text)
    data = await state.get_data()
    text = f'Пожалуйста, проверьте все ли верно: \n\n' \
           f'<b>Имя</b>: {data.get("name")}\n' \
           f'<b>Фамилия</b>: {data.get("lastname")}\n'
    await message.answer(text, reply_markup=check_keyboard(), parse_mode='HTML')
    await state.set_state(Form.check_state)


@router.callback_query(F.data == 'correct', Form.check_state)
async def correct_questionnaire(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    lastname = data.get("lastname")
    tg_id = callback.from_user.id
    await create_or_update_user(
        tg_id=tg_id,
        name=name,
        lastname=lastname,
    )
    await callback.answer('Даные сохранены')
    await state.clear()


