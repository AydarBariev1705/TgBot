from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def questionnaire_keyboard():
    keyboard = InlineKeyboardBuilder()
    questionnaire = InlineKeyboardButton(
        text='Start questionnaire',
        callback_data='questionnaire')
    keyboard.add(questionnaire)

    return keyboard.adjust(1).as_markup()


def check_keyboard():
    keyboard = InlineKeyboardBuilder()
    correct = InlineKeyboardButton(
        text='Все верно!',
        callback_data='correct')
    incorrect = InlineKeyboardButton(
        text='Не верно!',
        callback_data='incorrect')
    keyboard.add(correct)
    keyboard.add(incorrect)

    return keyboard.adjust(2).as_markup()
