from aiogram import types
from loader import dp
import random

@dp.message_handler(commands=['start'])
async def start_game(message):
    await message.answer('Давай начнем!')
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('Начать игру')
    markup.add(itembtn1)
    await message.answer(message.chat.id, "Выберите:", reply_markup=markup)
@dp.message_handler(content_types=['text'])
async def game_start(message):
    if message.text == 'Начать игру':
        await message.answer(message.chat.id, 'Игра началась! Вы ходите первым.')
        board = [['-','-','-'], ['-','-','-'], ['-','-','-']]
        for row in board:
            await message.answer(message.chat.id, '\n'.join(row))
        move = 0
        while True:
            if move % 2 == 0:
                await message.answer(message.chat.id, 'Введите координаты в формате x,y (от 0 до 2):')
                @dp.message_handler(content_types=['text'])
                async def get_move(m):
                    coords = m.text.split(',')
                    if len(coords) != 2:
                        await message.answer(m.chat.id, 'Некорректные координаты.')
                        return
                    x = int(coords[0])
                    y = int(coords[1])
                    if not (0 <= x <= 2 and 0 <= y <= 2):
                        await message.answer(m.chat.id, 'Координаты должны быть от 0 до 2.')
                        return
                    if board[x][y] != '-':
                        await message.answer(m.chat.id, 'Эта клетка уже занята.')
                        return
                    board[x][y] = 'X'
                    for row in board:
                        await message.answer(m.chat.id, '\n'.join(row))
                    move += 1
            else:  
                while True:  
                    x = random.randint(0, 2)
                    y = random