from telebot import types

def TopUpdate(a = [['',''],['','']]):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(
        types.InlineKeyboardButton('Главное меню', callback_data='menu'),
        types.InlineKeyboardButton('Обновить', callback_data='update'))
    for i in range(len(a)):
        btn = types.InlineKeyboardButton(str(i+1) + '. ' + a[i][1] + ' ' + str(a[i][2]), callback_data=a[i][0])
        kb.add(btn)
    return kb


def MainMenu():
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(
        types.InlineKeyboardButton('Показать рейтинг',callback_data='update'),
        types.InlineKeyboardButton('Добавить шаурмечную', callback_data='add'))
    return kb


def addOtziv():
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(
        types.InlineKeyboardButton('Оценить шаурмечную', callback_data='addOtziv'),
        types.InlineKeyboardButton('Главное меню', callback_data='menu'))
    return kb


def deleteOtziv():
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(
        types.InlineKeyboardButton('Удалить свой отзыв', callback_data='deleteOtziv'),
        types.InlineKeyboardButton('Главное меню', callback_data='menu'))
    return kb
