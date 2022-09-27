from aiogram import Router
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from database_control import *
from student_info.student import *

router = Router()
student = Student()

class StartState(StatesGroup):
    choosing_direction = State()
    choosing_course = State()
    choosing_group = State()

@router.message(Command(commands=["start"]))
async def start_func(message: Message, state: FSMContext):
    student.set_chat_id(message.chat.id)
    if (check_student(message.chat.id)):
        await message.answer("Привет! А мы уже знакомы :) \nВыбери функцию, которой хочешь воспользоваться.")
    else:
        await message.answer("Привет! Я буду помогать тебе не забывать вовремя делать домашнее задание, но сначала " +
                             "я задам тебе пару вопросов :) \n\n" +
                             "На каком факультете ты учишься? (Полное название)")
        await state.set_state(StartState.choosing_direction)


@router.message(StartState.choosing_direction)
async def get_direction(message: Message, state: FSMContext):
    student.set_direction(message.text)
    await message.answer("А на каком курсе?")
    await state.set_state(StartState.choosing_course)

@router.message(StartState.choosing_course)
async def get_course(message: Message, state: FSMContext):
    await message.answer("Интересно, а в какой ты группе? 🙃")
    student.set_course(message.text)
    await state.set_state(StartState.choosing_group)

@router.message(StartState.choosing_group)
async def get_group(message: Message, state: FSMContext):
    student.set_group(message.text)
    add_student(student)
    await message.answer("Не забывай про домашку и хорошего тебя дня!😊")
    await state.clear()



