import telebot
import utils
TOKEN = "7345251836:AAHV3g5t32hBY9A-FAZoMTGjFydxAMkuL7M"
bot = telebot.TeleBot(TOKEN)
keyboard_0 = telebot.types.InlineKeyboardMarkup()
keyboard_1 = telebot.types.InlineKeyboardMarkup()
keyboard_3 = telebot.types.InlineKeyboardMarkup()
sp_1 =["Python ","Scratch", "Roblox ","WEB разработка","Game ART"]
for i in sp_1:
    btn_get_photo = telebot.types.InlineKeyboardButton(i, callback_data=sp_1.index(i))
    keyboard_0.add(btn_get_photo)
i = "Поставить оценку"
btn_get_photo = telebot.types.InlineKeyboardButton(i, callback_data=i)
keyboard_3.add(btn_get_photo)
i = "Рейтинг преподавателей"
btn_get_photo = telebot.types.InlineKeyboardButton(i, callback_data=i)
keyboard_3.add(btn_get_photo)
i = "Поставить лайк"
btn_get_photo = telebot.types.InlineKeyboardButton(i, callback_data="1")
keyboard_1.add(btn_get_photo)
i = "Поставить дизлайк"
btn_get_photo = telebot.types.InlineKeyboardButton(i, callback_data="-1")
keyboard_1.add(btn_get_photo)
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Действия: ', reply_markup=keyboard_3)
g =''
h = False
@bot.callback_query_handler(func=lambda callback: True)
def handle_callback(callback):
    global g
    if callback.data in "+-":
        gh = open("text.txt")
        f = gh.split("\n")
        gh.close()
        p=[]
        gh = open("text.txt",mode = 'w')
        for i in f:
            p = i.split()
            if g == p[0]:
                gh.write(f"{p[0]} {p[1]+int(callback.data)}\n")
            else:
                gh.write(f"{p[0]} {p[1]}\n")
        gh.close()
    elif callback.data =="Поставить оценку":
        bot.send_message(callback.message.chat.id, 'Выбери курс:', reply_markup=keyboard_0)
    elif callback.data == "Рейтинг преподавателей":
        sp = utils.top_prepod()
        print(sp)
        for i in range(len(sp)):
            st = f"{i+1}. {sp[i]}"
            bot.send_message(callback.message.chat.id, st)
    elif callback.data != "+" and callback.data != "-":
        a = callback.data
        sp_2 = ["Назад","Илья","Кирилл", "Маша ","Настя","Данил"]
        keyboard_3 = telebot.types.InlineKeyboardMarkup()
        keyboard_3.add(sp_2[0])
        if a!=4:
            s = 0
            for i in range(1+a,sp_2):
                s+=1
                keyboard_3.add(sp_2[i])
                if s == 2:
                    break
        bot.edit_message_text(text = "Выбери преподователя:",chat_id= callback.message.chat.id,message_id=callback.message.id)
        bot.edit_message_reply_markup(reply_markup=keyboard_3 ,chat_id= callback.message.chat.id,message_id=callback.message.id)
    else:
        bot.send_message(callback.message.chat.id, 'Выбери оценку:', reply_markup=keyboard_1)
        g = callback.data

bot.polling(non_stop=True, interval=1)