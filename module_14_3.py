from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import  FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text = 'Рассчитать')
button2 = KeyboardButton(text = 'Информация')
button3 = KeyboardButton(text = 'Купить')
kb.add(button, button2, button3)

ikb = InlineKeyboardMarkup()
ikb_button = InlineKeyboardButton(text = 'Продукт1', callback_data="product_buying")
ikb_button2 = InlineKeyboardButton(text = 'Продукт2', callback_data="product_buying")
ikb_button3 = InlineKeyboardButton(text = 'Продукт3', callback_data="product_buying")
ikb_button4 = InlineKeyboardButton(text = 'Продукт4', callback_data="product_buying")
ikb.add(ikb_button, ikb_button2,ikb_button3, ikb_button4)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)

@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await UserState.growth.set()
    await message.answer('Введите свой рост:')

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await UserState.weight.set()
    await message.answer('Введите свой вес:')

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    age = int(data.get('age'))
    growth = int(data.get('growth'))
    weight = int(data.get('weight'))

    bmr = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f'Ваша норма калорий: {bmr}')

    await state.finish()

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    with open ('image/1.jpg', "rb") as img1:
        await message.answer_photo(img1, "Название: Product1 | Описание: описание 1 | Цена: 100")
    with open('image/2.jpg', "rb") as img2:
        await message.answer_photo(img2, "Название: Product2 | Описание: описание 2 | Цена: 200")
    with open('image/3.jpg', "rb") as img3:
        await message.answer_photo(img3, "Название: Product3 | Описание: описание 3 | Цена: 300")
    with open('image/4.jpg', "rb") as img4:
        await message.answer_photo(img4, "Название: Product4 | Описание: описание 4 | Цена: 400",)
        await message.answer("Выберите продукт для покупки:", reply_markup=ikb)
        await call.answer()


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler()
async def all_messages(message):
    await message.answer("Введите команду /start, чтобы начать общение.")
    await call.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
