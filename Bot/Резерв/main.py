import telebot
from telebot import types
import text

TOKEN = '6214187356:AAFpJfITT4_D3mXvpEW1mb1XMWGEdawU_YI'
bot = telebot.TeleBot(TOKEN)
#Cтартовая отправка фото и текста
@bot.message_handler(commands=['start'])
def send_photo(message):
    chat_id = message.chat.id
    photo = open('image/start.jpg', 'rb')
    bot.send_photo(chat_id, photo)
    bot.send_message(message.chat.id, text = text.privetstvie)
    main_menu (message)
# Меню - Главное + команда
@bot.message_handler(commands=['menu'])
def main_menu (message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(text = "\U0001f198Отримати допомогу")
    btn2 = types.KeyboardButton(text ="\U0001f64fДопомогти проекту")
    btn3 = types.KeyboardButton(text ="\U0001f3ebОсвітні заходи")
    btn4 = types.KeyboardButton(text="\U0001f9d1\U0001f3fb\u200D\U0001f91d\u200D\U0001f9d1\U0001f3fbПро нас")
    kb.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text='\U0001f447Для пересування по боту натискайте кнопки⌨️',reply_markup=kb)
# Меню допомогти
def main_help_project (message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(text = "Юридична консультація")
    btn2 = types.KeyboardButton(text = "Гуманітарна допомога")
    btn3 = types.KeyboardButton(text = "Реалізувати Вашу мрію")
    btn4 = types.KeyboardButton(text = "Допомога для ЗСУ")
    kb.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text='\U0001f447Для пересування по боту натискайте кнопки⌨️',reply_markup=kb)
# Меню - про нас
def menu_about_us (message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(text = "🧑‍💼Наші засновники")
    btn2 = types.KeyboardButton(text = "👪Наша команда")
    btn3 = types.KeyboardButton(text = "🥇Наші досягнення")
    btn4 = types.KeyboardButton(text = "\u23EAВ головне меню")
    btn5 = types.KeyboardButton(text = "💬Ми в соціальних мережах")
    kb.add(btn1, btn2, btn3, btn4,btn5)
    bot.send_message(message.chat.id, text='\U0001f447Для пересування по боту натискайте кнопки⌨️',reply_markup=kb)
#Назад и в главное меню - по кнопке: Про нас
def vozvrat (message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(text = "\U0001f519Назад")
    btn2 = types.KeyboardButton(text = "\u23EAВ головне меню")
    kb.add(btn1, btn2)
    bot.send_message(message.chat.id, text='\U0001f447Для пересування по боту натискайте кнопки⌨️',reply_markup=kb)

# Команда share
@bot.message_handler(commands=['share'])
def share (message):
        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_message(message.chat.id, text=text.zag_share, parse_mode='HTML')
        bot.send_message(message.chat.id, text=text.osn_share, parse_mode='HTML')
# Обработка сообщений
@bot.message_handler(content_types=['text'])
def func(message):
    chat_id = message.chat.id 
    if (message.text == "\U0001f198Отримати допомогу"):
        main_help_project(message)
    elif (message.text == "\U0001f9d1\U0001f3fb\u200D\U0001f91d\u200D\U0001f9d1\U0001f3fbПро нас"):
        menu_about_us (message)
# Наші засновники
    elif(message.text == "🧑‍💼Наші засновники"):
        bot.send_chat_action(message.chat.id, 'typing')
        photo = open('image/team/gatesh.jpg', 'rb')
        bot.send_photo(chat_id, photo)
        bot.send_message(message.chat.id, text=text.vadim_gatezh, parse_mode='HTML')
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1= types.InlineKeyboardButton(text='Facebook', url='https://www.facebook.com/vadim.gatezh')
        btn2= types.InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/v_gatezh')
        btn3= types.InlineKeyboardButton(text='Telegram channel', url='https://t.me/v_gatezh_novyny')
        kb.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Соціальна мережа:", reply_markup = kb)
        
        photo = open('image/team/visotskiy.jpg', 'rb')
        bot.send_photo(chat_id, photo)
        bot.send_message(message.chat.id, text=text.pavlo_vysotsky, parse_mode='HTML')
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1= types.InlineKeyboardButton(text='Facebook', url='https://www.facebook.com/profile.php?id=100015205090408')
        kb.add(btn1)
        bot.send_message(message.chat.id, "Соціальна мережа:", reply_markup = kb)

        vozvrat (message)
# Наша команда
    elif(message.text == "👪Наша команда"):
        bot.send_chat_action(message.chat.id, 'typing')
        photo = open('image/team/mironuk.jpg', 'rb')
        bot.send_photo(chat_id, photo)
        bot.send_message(message.chat.id, text=text.anna_mironyuk, parse_mode='HTML')
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1= types.InlineKeyboardButton(text='Facebook', url='https://www.facebook.com/anya.myroniuk')
        kb.add(btn1)
        bot.send_message(message.chat.id, "Соціальна мережа", reply_markup = kb)

        photo = open('image/team/merezhuk.jpg', 'rb')
        bot.send_photo(chat_id, photo)
        bot.send_message(message.chat.id, text=text.anastasia_merezhuk, parse_mode='HTML')
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1= types.InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/merranst')
        kb.add(btn1)
        bot.send_message(message.chat.id, "Соціальна мережа", reply_markup = kb)

        photo = open('image/team/semenchuk.jpg', 'rb')
        bot.send_photo(chat_id, photo)
        bot.send_message(message.chat.id, text=text.anastasia_semenchuk, parse_mode='HTML')
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1= types.InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/nastia_semenchuk')
        kb.add(btn1)
        bot.send_message(message.chat.id, "Соціальна мережа", reply_markup = kb)

        photo = open('image/team/birkova.jpg', 'rb')
        bot.send_photo(chat_id, photo)
        bot.send_message(message.chat.id, text=text.julia_birkova, parse_mode='HTML')

        photo = open('image/team/bagirov.jpg', 'rb')
        bot.send_photo(chat_id, photo)
        bot.send_message(message.chat.id, text=text.vagif_bagirov, parse_mode='HTML')

        photo = open('image/team/shaporda.jpg', 'rb')
        bot.send_photo(chat_id, photo)
        bot.send_message(message.chat.id, text=text.anastasia_shaporda, parse_mode='HTML')
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1= types.InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/shaporda.design')
        kb.add(btn1)
        bot.send_message(message.chat.id, "Соціальна мережа", reply_markup = kb)

        photo = open('image/team/torska.jpg', 'rb')
        bot.send_photo(chat_id, photo)
        bot.send_message(message.chat.id, text=text.khrystyna_torska, parse_mode='HTML')
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1= types.InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/kristorska')
        kb.add(btn1)
        bot.send_message(message.chat.id, "Соціальна мережа", reply_markup = kb)

        photo = open('image/team/bondarenko.jpg', 'rb')
        bot.send_photo(chat_id, photo)
        bot.send_message(message.chat.id, text=text.olga_bondarenko, parse_mode='HTML')

        vozvrat (message)
# Ми в соціальних мережах
    elif(message.text == "💬Ми в соціальних мережах"):
        bot.send_chat_action(message.chat.id, 'typing')
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1= types.InlineKeyboardButton(text='Website', url='https://www.caringgeneration.org.ua')
        btn2= types.InlineKeyboardButton(text='Facebook', url='https://www.facebook.com/people/%D0%91%D0%BB%D0%B0%D0%B3%D0%BE%D0%B4%D1%96%D0%B9%D0%BD%D0%B0-%D0%9E%D1%80%D0%B3%D0%B0%D0%BD%D1%96%D0%B7%D0%B0%D1%86%D1%96%D1%8F-%D0%93%D1%80%D0%BE%D0%BC%D0%B0%D0%B4%D1%81%D1%8C%D0%BA%D0%B8%D0%B9-%D1%80%D1%83%D1%85-%D0%9F%D0%BE%D0%BA%D0%BE%D0%BB%D1%96%D0%BD%D0%BD%D1%8F-%D0%BD%D0%B5%D0%B1%D0%B0%D0%B9%D0%B4%D1%83%D0%B6%D0%B8%D1%85/100086522064845')
        btn3= types.InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/caringgeneration_in_ua/')
        btn4= types.InlineKeyboardButton(text='Telegram channel', url='https://t.me/caringgeneration_in_ua')
        kb.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, "Соціальна мережа:", reply_markup = kb)

        vozvrat (message)
    elif(message.text == "🥇Наші досягнення"):
        bot.send_chat_action(message.chat.id, 'typing')
        photo_paths = text.img_invincibility
        media_group = [telebot.types.InputMediaPhoto(open(path, "rb").read()) for path in photo_paths]
        # media_group = []
        # for path in photo_paths:
        #     with open(path, "rb") as f:
        #         media_group.append(telebot.types.InputMediaPhoto(f.read()))
        bot.send_media_group(message.chat.id, media=media_group)
        bot.send_message(message.chat.id, text=text.help_points_of_invincibility, parse_mode='HTML')

        photo_paths = text.img_donetsk
        media_group = [telebot.types.InputMediaPhoto(open(path, "rb").read()) for path in photo_paths]
        bot.send_media_group(message.chat.id, media=media_group)
        bot.send_message(message.chat.id, text=text.trip_to_donetsk_region, parse_mode='HTML')

        photo_paths = text.img_herson
        media_group = [telebot.types.InputMediaPhoto(open(path, "rb").read()) for path in photo_paths]
        bot.send_media_group(message.chat.id, media=media_group)
        bot.send_message(message.chat.id, text=text.herson, parse_mode='HTML')
              
        vozvrat (message)

    elif(message.text == "\u23EAВ головне меню"):
        main_menu (message)
    elif(message.text == "\U0001f519Назад"):
        menu_about_us (message)
    else:
        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_message(message.chat.id, text=text.nezrozymiv, parse_mode='HTML')
        photo = open('image/nezrozymiv.jpg', 'rb')
        bot.send_photo(chat_id, photo)
bot.polling(non_stop=True)