import telebot
import config
from keyboards import TopUpdate, MainMenu, addOtziv, deleteOtziv
from fuctions import BaseData, addBaseData, findBaseData, addStarBaseData, userInBaseData, deleteOtzivBaseData, amountBaseData


bot = telebot.TeleBot(config.token)


class A:
    name = False
    star = False
    address = False

chek = A()
adding = A()


class B:
    id = False
    star = False

chk = B()
addOtz = B()


@bot.message_handler(commands="start")
def StartMessage(message):
    bot.send_message(chat_id=message.chat.id, text="Главное меню", reply_markup=MainMenu())


@bot.callback_query_handler(func=lambda call:True)
def callback_func(query):
    data = query.data
    if data == "update":
        try:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text="Рейтинг шаурмечных:" , reply_markup=TopUpdate(BaseData()))
        except:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text="Изменений нет", reply_markup=TopUpdate(BaseData()))
    elif data == "add":
        bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='Введите название')
        chek.name = True
    elif data == "menu":
        bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='Главное меню', reply_markup=MainMenu())
    elif data == "addOtziv":
        if userInBaseData(query.from_user.id,addOtz.id):
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='Вы уже оставляли оценку',reply_markup=deleteOtziv())
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='Отправьте оценку от 1 до 5')
            chk.star = True
            chek.star = True
    elif data == "deleteOtziv":
        deleteOtzivBaseData(query.from_user.id,addOtz.id)
        bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='Главное меню', reply_markup=MainMenu())
    else:
        b = findBaseData(data)
        bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,text=f'Страница шаурмечной\n\nНазвание: {b[0][1]}\nАдрес: {b[0][3]}\nРейтинг: {b[0][2]}\nКоличество оценок: {amountBaseData(data)}',reply_markup=addOtziv())
        addOtz.id = data


@bot.message_handler(func=lambda message:True, content_types='text')
def default_command(message):
    if chek.name == True:
        adding.name = message.text
        chek.name = False
        bot.send_message(chat_id=message.chat.id, text='Отправьте адрес шаурмечной (населённый пункт, улица, дом)')
        chek.address = True
    elif chek.address:
        adding.address = message.text
        chek.address = False
        bot.send_message(chat_id=message.chat.id, text='Отправьте оценку от 1 до 5')
        chek.star = True
    elif chek.star:
        try:
            if int(message.text) in [1,2,3,4,5]:
                if chk.star:
                    addOtz.star = message.text
                    chek.star = False
                    chk.star = False
                    addStarBaseData(addOtz.id,addOtz.star,str(message.from_user.id))
                    bot.send_message(chat_id=message.chat.id, text="Главное меню", reply_markup=MainMenu())
                else:
                    adding.star = message.text
                    chek.star = False
                    addBaseData(adding.name,adding.star,str(message.from_user.id),adding.address)
                    bot.send_message(chat_id=message.chat.id, text="Главное меню", reply_markup=MainMenu())
            else:
                bot.send_message(chat_id=message.chat.id, text="Отправьте цифру от 1 до 5!")
        except:
            bot.send_message(chat_id=message.chat.id, text="Отправьте цифру от 1 до 5!")


bot.polling()