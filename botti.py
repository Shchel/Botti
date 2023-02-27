# @bot_english_botBot

from telebot import TeleBot
from telebot.types import Message
from telebot import types

bot = TeleBot('токен')


@bot.message_handler(commands=['start'])
def welcome(message: Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("ЕГЭ")
    btn2 = types.KeyboardButton("General English")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'''Привет, {message.from_user.first_name}, я Ботти.

С чем тебе помочь?''', reply_markup=markup)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEH3ZVj900NLn4ghuCH9DV8vnopLpCHZQAChQwAAvu02Umb_uv403P_my4E')


@bot.message_handler(commands=['help'])
def welcome(message: Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("ЕГЭ")
    btn2 = types.KeyboardButton("General English")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'''Попробуй нажать на кнопку "ЕГЭ" или "General English")

Что-то пошло не так? 
Остались вопросы? 
*Напиши @ChelpN и расскажи о проблеме*❤''', reply_markup=markup, parse_mode="Markdown")
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEH3bZj907tT0il-ZdkcNOqgsljDfIfDQACFBAAAjvtUEjxWqzBjpnHyi4E')


@bot.message_handler(content_types=['text'])
def start(message: Message):
    try:
        message_text = message.text.lower()
        if message_text.find("вернуться в начало") >= 0:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton("ЕГЭ")
            btn2 = types.KeyboardButton("General English")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, f'С чем тебе помочь?', reply_markup=markup)

        elif message_text == "general english":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton("To be")
            btn2 = types.KeyboardButton("Can")
            btn3 = types.KeyboardButton("Английский на слух")
            btn4 = types.KeyboardButton("Времена")
            btn5 = types.KeyboardButton("Ответь на вопросы")
            btn6 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

            bot.send_sticker(message.chat.id,
                             'CAACAgIAAxkBAAEHAAH2Y6ip7znqMVr0wDeo1c7nFj9vEjYAAmMOAAJY7XFL1OOkP8YgajcsBA')
            bot.send_message(message.chat.id, '''Хочешь подтянуть английский?
    
Выбери то, над чем хочешь поработать ♡''', reply_markup=markup)

        elif message_text == "английский на слух":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton("Песни")
            btn2 = types.KeyboardButton("Фильмы")
            btn3 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2, btn3)
            bot.send_sticker(message.chat.id,
                             'CAACAgIAAxkBAAEG_pljqCbHle9-FRaC7z409lIRSP8pvwACniEAAub9QEt-FQbL6Wz1viwE')
            bot.send_message(message.chat.id,
                             '''*Тренировка английского на слух* - это идеальный способ для улучшения понимания англоязычной речи, пополнения словарного запаса и улучшения произношения ! 🤩''',
                             reply_markup=markup, parse_mode="Markdown")

        elif message_text == "фильмы":
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.InlineKeyboardButton(text='Harry Potter', url='https://youtu.be/9gzpUaZGQKI')
            btn2 = types.InlineKeyboardButton(text='''Netflix's Wednesday''', url='https://youtu.be/rIRuoQMrCdg')
            btn3 = types.InlineKeyboardButton(text='Cinderella', url='https://youtu.be/cHWHY-JpAHw')
            btn4 = types.InlineKeyboardButton(text='Avatar', url='https://youtu.be/fRseMUZ2NOM')
            btn5 = types.InlineKeyboardButton(text='''Breakfast at Tiffany's''', url='https://youtu.be/8cAc2MUWfBU')
            btn6 = types.InlineKeyboardButton(text='SpongeBob SquarePants', url='https://youtu.be/JxWEAP0aAJQ')
            btn7 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn1, btn2, btn3, btn4, btn5, btn6)
            markup2.add(btn7)
            bot.send_message(message.from_user.id,
                             '''🗣️ Изучая английский язык по фильмам и сериалам, вы знакомитесь не с литературным, а с *реальным разговорным языком*. 
                             
Кроме того, при просмотре *любимого* фильма или сериала вы не устаете так быстро, как во время вылнения грамматических упражнений! ''',
                             reply_markup=markup2, parse_mode="Markdown")
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG_pVjqCZNfYy7yKIddfgDEw-uUyXb0gACXgAD4Ec7D5DZCc32QvJLLAQ')
            bot.send_message(message.from_user.id,
                             '''Но вот встает вопрос: *как* смотреть
   
*Я, Ботти, дам тебе несколько советиков:*

🌠 выписывай незнакомые слова в контексте (т.е. не "happiness", а "Your happiness is all that matters to me")

🌠 проговаривай вслух фразы, которые ты хочешь выучить

🌠 выбирай фильмы или сериалы, которые вам интересны и соответствуют текущему уровню владения языком


⬇ссылки на разборы фильмов/сериалов''',
                             reply_markup=markup1, parse_mode="Markdown")

        elif message_text == "to be":
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.InlineKeyboardButton(text='Игра кенгуру (удобнее с компьютера)',
                                              url='https://www.eslgamesplus.com/verb-to-be-auxiliary-verb-am-is-are-esl-grammar-activity/')
            btn2 = types.InlineKeyboardButton(text='Игра baamboozle', url='https://www.baamboozle.com/game/1140762')
            btn3 = types.InlineKeyboardButton(text='Игра baamboozle (ответь на вопросы)',
                                              url='https://www.baamboozle.com/game/928281')
            btn4 = types.InlineKeyboardButton(text='Игра baamboozle A1', url='https://www.baamboozle.com/game/116272')
            btn5 = types.InlineKeyboardButton(text='Тест am/is/are',
                                              url='https://myefe.ru/quizzes/tests-be-present-simple/test-1')
            btn6 = types.InlineKeyboardButton(text='Ещё тест am/is/are',
                                              url='https://english-rooms.com/test/beginner-grammar-test-amisare-to-be-present-forms')
            btn7 = types.InlineKeyboardButton(text='Теория, тест и игра',
                                              url='https://learnenglishkids.britishcouncil.org/present-simple-verb-be')
            btn8 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn2, btn3, btn4, btn1, btn5, btn6, btn7)
            markup2.add(btn8)
            bot.send_photo(message.from_user.id,
                           'https://sun9-west.userapi.com/sun9-40/s/v1/ig2/Wgd_VfnpWs18_dlufeqFFI6lXSjW1owUex3E4UhjSb59n0_N-cd_-jthj_1a49nQOlDsrScwpDg7m178lQX48E9F.jpg?size=905x1280&quality=96&type=album',
                           reply_markup=markup2)
            bot.send_message(message.from_user.id,
                             '''Ты можешь попрактиковаться там ⬇''',
                             reply_markup=markup1)

        elif message_text == "can":
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.InlineKeyboardButton(text='Игра can you...?', url='https://wordwall.net/ru/resource/6499603')
            btn2 = types.InlineKeyboardButton(text='Теория, тест и игра',
                                              url='https://learnenglishkids.britishcouncil.org/modals-can-and-cant')
            btn3 = types.InlineKeyboardButton(text='Игра baamboozle (ответь на вопросы)',
                                              url='https://www.baamboozle.com/game/122110')
            btn4 = types.InlineKeyboardButton(text='Игра baamboozle', url='https://www.baamboozle.com/game/54532')
            btn5 = types.InlineKeyboardButton(text='''Тест can/can't''',
                                              url='https://www.englishtestsonline.com/the-modal-verb-can-cant-test-a1-a2-level-exercises/')
            btn6 = types.InlineKeyboardButton(text='''Тест''',
                                              url='https://www.study.ru/courses/elementary/modalnyy-glagol-can-otricatelnye-i-voprositelnye-predlozheniya')
            btn7 = types.InlineKeyboardButton(text='''Тест can/can't''',
                                              url='https://test-english.com/grammar-points/a1/can-cant/')
            btn8 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
            markup2.add(btn8)
            bot.send_photo(message.from_user.id,
                           'https://sun9-west.userapi.com/sun9-61/s/v1/ig2/elTxvEeQY3oKdt8oTQpbD00Wi75mzXsuGyBzMDygNnJKo2GftDhWjbmZ-zwnS1tNy5HX6PLyAwmt8cnDBGB9jNEx.jpg?size=2066x1080&quality=95&type=album',
                           reply_markup=markup2)
            bot.send_message(message.from_user.id,
                             '''Ты можешь попрактиковаться там ⬇''',
                             reply_markup=markup1)

        elif message_text == "ответь на вопросы":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton("Хочу ещё вопрос")
            btn2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2)
            bot.send_photo(message.chat.id,
                           'https://sun9-west.userapi.com/sun9-64/s/v1/ig2/dKE1pPHyJmoTv5RG14RSr6o85nBGv6A4PQ92YFNJrFhU3vN_oavvc--vqetdPGVteedc431GzmuK1NwTp7prk9Dw.jpg?size=2069x1080&quality=95&type=album')
            bot.send_message(message.chat.id, '''*Попробуй ответить на вопросы*
    
Возможный вариант ответа:
    
||My favorite colour is pink||''', reply_markup=markup, parse_mode="MarkdownV2")

        elif message_text == "хочу ещё вопрос":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton("Скинь следующий вопрос")
            btn2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2)
            bot.send_photo(message.chat.id,
                           'https://sun9-west.userapi.com/sun9-12/s/v1/ig2/0Wl4dBbdXXKMC-oCRWWJ6qkuM_blvVs0qZJeWcvHLpgywOhUEev18OtQlqaKlrk6aijibH1OpaxqDOGdiFFILf-I.jpg?size=2069x1080&quality=95&type=album')
            bot.send_message(message.chat.id, '''Возможный вариант ответа:
    
||My favorite drink is lemonade||''', reply_markup=markup, parse_mode="MarkdownV2")

        elif message_text == "скинь следующий вопрос":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton("Следующий вопрос")
            btn2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2)
            bot.send_photo(message.chat.id,
                           'https://sun9-west.userapi.com/sun9-68/s/v1/ig2/hBzyUSGgtuLWhqcHn7SPLbu3hAg_ZVrtizMLbAQQhb5yt4HdZkiRtn23uYPVr8UhxJM7hR8y2DKVqTRRqt5G7zul.jpg?size=2069x1080&quality=95&type=album')
            bot.send_message(message.chat.id, '''Возможный вариант ответа:
            
||My favorite food is ramen noodles||''', reply_markup=markup, parse_mode="MarkdownV2")

        elif message_text == "следующий вопрос":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton("Ещё вопрос")
            btn2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2)
            bot.send_photo(message.chat.id,
                           'https://sun9-east.userapi.com/sun9-23/s/v1/ig2/ZdzfL9cc-RITnauOy2Wi4pXoR-vLgaJEDSe0HrPgd_FtLJ660dOTAvKgcMrK_7NntVA_zC0vJ6-8Wkh770m8YhJa.jpg?size=2069x1080&quality=95&type=album')
            bot.send_message(message.chat.id, '''Возможный вариант ответа:
    
||My favourite day of the week is Monday||''', reply_markup=markup, parse_mode="MarkdownV2")

        elif message_text == "ещё вопрос":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton("Хочу следующий вопрос")
            btn2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2)
            bot.send_photo(message.chat.id,
                           'https://sun9-west.userapi.com/sun9-52/s/v1/ig2/SmvD6YemfjTmk6bEeHhCy41Xw3HjW4nxIoCViuJg4w0lGgptVgWsl_jd4ebOWwyoBYIBcksCMGUxEqwXD5SyrflO.jpg?size=2069x1080&quality=95&type=album')
            bot.send_message(message.chat.id, '''Возможный вариант ответа:
    
||My school's number is 102||''', reply_markup=markup, parse_mode="MarkdownV2")

        elif message_text == "хочу следующий вопрос":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton("Отправь ещё вопрос")
            btn2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2)
            bot.send_photo(message.chat.id,
                           'https://sun9-east.userapi.com/sun9-28/s/v1/ig2/lf6L2eecmDdmG4UzcIr732Gk4QLVrJ7I68deva6xEZIf9adfzicaFUOtxnyR1uQOviTXW8ObjZosa2Oa2LsPdfkN.jpg?size=2069x1080&quality=95&type=album')
            bot.send_message(message.chat.id, '''Возможный вариант ответа:
    
||The weather is windy today||''', reply_markup=markup, parse_mode="MarkdownV2")

        elif message_text == "отправь ещё вопрос":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton("Скинь ещё вопрос")
            btn2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2)
            bot.send_photo(message.chat.id,
                           'https://sun9-west.userapi.com/sun9-56/s/v1/ig2/ecEHsbKWua2g_wKomxXy0atWZ6CqW7P57HsOf5nIYU4-jDzziqmIXZ5BLL55JbzUHwyKD6EG2I1mdm55dDuHUB1O.jpg?size=2069x1080&quality=95&type=album')
            bot.send_message(message.chat.id, '''Возможный вариант ответа:
    
||I am 16 years old||''', reply_markup=markup, parse_mode="MarkdownV2")

        elif message_text == "скинь ещё вопрос":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton("Отправь следующий вопрос")
            btn2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2)
            bot.send_photo(message.chat.id,
                           'https://sun9-east.userapi.com/sun9-44/s/v1/ig2/qwbd9wkrkiMXkNKVTlXs7GlcYvtV7hFi4TowJIDy7IALqCJp-B806OUShcISXbfF1Q9j70xQ2Nfge2z38G-WsibO.jpg?size=2069x1080&quality=95&type=album')
            bot.send_message(message.chat.id, '''Возможный вариант ответа:
    
||I am from Russia||''', reply_markup=markup, parse_mode="MarkdownV2")

        elif message_text == "отправь следующий вопрос":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.KeyboardButton("Вернуться в начало")
            btn2 = types.InlineKeyboardButton(text='Крутилка с вопросами for beginners',
                                              url='https://wordwall.net/resource/16451370')
            btn3 = types.InlineKeyboardButton(text='Крутилка с вопросами for beginners',
                                              url='https://wordwall.net/resource/26820354')
            btn4 = types.InlineKeyboardButton(text='Крутилка How do you feel when ...?',
                                              url='https://wordwall.net/ru/resource/51914146')
            btn5 = types.InlineKeyboardButton(text='Pre-Intermediate Questions',
                                              url='https://www.baamboozle.com/game/258020')
            btn6 = types.InlineKeyboardButton(text='Superhero Scene Question Answering',
                                              url='https://www.baamboozle.com/game/466486')
            markup.add(btn1)
            markup1.add(btn6, btn2, btn3, btn4, btn5)
            bot.send_photo(message.chat.id,
                           'https://sun9-east.userapi.com/sun9-76/s/v1/ig2/Ejg2UTe5TQi97VivGwaIt2dBjFSZOn1qDZgKtkY1LF6YX6gHaInxWBLZgsCcX4nXMlsoItsIlG9iiOX5RgF2BcI7.jpg?size=2069x1080&quality=95&type=album')
            bot.send_message(message.chat.id, '''Возможный вариант ответа:
    
||My surname is Ivanova||''', reply_markup=markup, parse_mode="MarkdownV2")
            bot.send_message(message.chat.id, '''Умничка, ты ответил на все вопросы😚
            
Если хочешь ещё попрактиковаться ⬇''', reply_markup=markup1)

        elif message_text == "песни" or message_text == "вернуться к списку песен":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton("pov - Ariana Grande")
            btn2 = types.KeyboardButton("As it was - Harry Styles")
            btn3 = types.KeyboardButton("Luxurious - Gwen Stefani")
            btn4 = types.KeyboardButton("After The Storm - Kali Uchis, Tyler, The Creator, Bootsy Collins")
            btn5 = types.KeyboardButton("Space Girl - Frances Forever")
            btn6 = types.KeyboardButton("Don't Start Now - Dua Lipa")
            btn7 = types.KeyboardButton("I Wanna Be Yours - Arctic Monkeys")
            btn10 = types.KeyboardButton("Looking out for you - Joy Again")
            btn11 = types.KeyboardButton("Love Yourself - Justin Bieber")
            btn9 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn10, btn11, btn9)
            bot.send_message(message.chat.id,
                             '''Выбери песню и попробуй во время прослушивания попытаться заполнить пропуски 😉''',
                             reply_markup=markup)

        elif message_text == "pov - ariana grande":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn_song1 = types.KeyboardButton("ответы pov - ariana grande")
            btn_song2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn_song1, btn_song2)
            bot.send_message(message.chat.id, 'Прослушай песню и заполни пропуски', reply_markup=markup)
            bot.send_photo(message.chat.id,
                           'https://sun9-west.userapi.com/sun9-53/s/v1/ig2/Bzs5snQEh7p0bZqagpiuGDKosmUJqtyKjKtiiK5oFYqWTcnsytjIVBHvVfuh74R8Ym-l11ws0Ejs8z7koULku7cU.jpg?size=1527x2160&quality=96&type=album')
            pov_ariana_grande = bot.send_audio(message.chat.id,
                                               'https://s296vlx.storage.yandex.net/get-mp3/e9e0c039a5cdc5f294abf1804d49c269/0005f094724e2905/rmusic/U2FsdGVkX18DbT04W8qAbPMaMhN79F3en7U-Rl4VPnNAf7RMjUNek15GBnM7HsqKWrjBL9acP-HVLUK8cobkyvDWe86PJwlALbm-j9XFhEc/47f5a377934f7e91aea505dfcb223c31fbcae5da58988aade3de65a6d21805f1/31683?track-id=73000149&play=false')

        elif message_text == "ответы pov - ariana grande":
            bot.send_photo(message.chat.id,
                           'https://sun3.userapi.com/sun3-12/s/v1/ig2/Wny1JNj4matgKVJvKykjYT1X45POfYO3wdXQU83hR-ZniVq410lc1yiSji0LKG2RruQOqNHeZGiggVSfmxIw8OeD.jpg?size=1527x2160&quality=96&type=album')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn_songs1 = types.KeyboardButton("Вернуться к списку песен")
            btn_songs2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn_songs1, btn_songs2)
            bot.send_sticker(message.chat.id,
                             'CAACAgIAAxkBAAEG_q5jqCrVRKYpHUkG40O0kAtSbSSXKwAC8hMAAuYvSEiwgF3RrT_5UCwE',
                             reply_markup=markup)

        elif message_text == "as it was - harry styles":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn_song1 = types.KeyboardButton("ответы as it was - harry styles")
            btn_song2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn_song1, btn_song2)
            bot.send_message(message.chat.id, 'Прослушай песню и заполни пропуски', reply_markup=markup)
            bot.send_photo(message.chat.id,
                           'https://sun3.userapi.com/sun3-10/s/v1/ig2/z75X7QaLo5kcQREq0kUhc8GvtkMB-Le-Z3MuGVU8Zfe28CkGkU7R-b94FFK1_rNOHwyaA_pO-NNeJLMhRMGnyqa5.jpg?size=1527x2160&quality=96&type=album')
            bot.send_audio(message.chat.id, 'https://muzgun.net/uploads/files/2022-09/Harry_Styles_-_As_It_Was.mp3')

        elif message_text == "ответы as it was - harry styles":
            bot.send_photo(message.chat.id,
                           'https://sun3.userapi.com/sun3-8/s/v1/ig2/gb9lzopR3FM98Jdbj1_frTwoIX0j5eGdWT1F9TN779yWzuIOVFG3_yKsylUY0JzlCJV4R1MRY0WQDppO93XN8uqw.jpg?size=1527x2160&quality=96&type=album')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn_songs1 = types.KeyboardButton("Вернуться к списку песен")
            btn_songs2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn_songs1, btn_songs2)
            bot.send_sticker(message.chat.id,
                             'CAACAgIAAxkBAAEG_sdjqCyraQeZW2QBanx3DxIXk9FB5AACZgcAAlwCZQPpnE2j2rCFTSwE',
                             reply_markup=markup)

        elif message_text == "luxurious - gwen stefani":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn_song1 = types.KeyboardButton("ответы luxurious - gwen stefani")
            btn_song2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn_song1, btn_song2)
            bot.send_message(message.chat.id, 'Прослушай песню и заполни пропуски', reply_markup=markup)
            bot.send_photo(message.chat.id,
                           'https://sun9-west.userapi.com/sun9-39/s/v1/ig2/3XEG_LI6kJFG3v1_7r5edhZ_-fcDVKJ2mixZeUY9v-MazazuJN-gqmKKD02C1Gn8RVGMwXhRNNL4snSILrK1MCZ2.jpg?size=1527x2160&quality=96&type=album')
            bot.send_audio(message.chat.id,
                           'https://s105sas.storage.yandex.net/get-mp3/a545c836ead034aeb6390315878516c0/0005f097e1912249/rmusic/U2FsdGVkX1-2NemPXFlwfkXWczXvfHyL4JjzCQHxo-V0k4rr1cqeTwCOetg-wVyiilastScPQzpNlugU8c56t43jiiKmBQWH2ld7aVVqzCw/1e0b4abb3f743b7e3971ae00ab936eafa0ee3f415050a7ade6eed9f8d27935f0/41343?track-id=10756&play=false')

        elif message_text == "ответы luxurious - gwen stefani":
            bot.send_photo(message.chat.id,
                           'https://sun3.userapi.com/sun3-16/s/v1/ig2/ONwHMdpWXMxSocfGO4H6L-jYbXZozLvL_30VHT3pgTk_fgA8aXpMjuBe-GPWVNI5UNOnu0i0JWDZveoCxjjJiHfs.jpg?size=1527x2160&quality=96&type=album')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn_songs1 = types.KeyboardButton("Вернуться к списку песен")
            btn_songs2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn_songs1, btn_songs2)
            bot.send_sticker(message.chat.id,
                             'CAACAgIAAxkBAAEG_sljqCy6QRsfEKTIG4_TuJn-XWoiHAACHAADXQWCFpMR4WhWKKc1LAQ',
                             reply_markup=markup)

        elif message_text == "after the storm - kali uchis, tyler, the creator, bootsy collins":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn_song1 = types.KeyboardButton("ответы after the storm")
            btn_song2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn_song1, btn_song2)
            bot.send_message(message.chat.id, 'Прослушай песню и заполни пропуски', reply_markup=markup)
            bot.send_photo(message.chat.id,
                           'https://sun3.userapi.com/sun3-17/s/v1/ig2/Vn9E2zINk2KsLkYeYib97ha9fSEWTL7xZ_T4VrXotypZrHs0TVIc0LHReZZyedeiMW2fLlQYE7nkjnWqdkdJjQNC.jpg?size=1527x2160&quality=96&type=album')
            bot.send_audio(message.chat.id,
                           'https://s27sas.storage.yandex.net/get-mp3/a6dc6a6e0f477e98ee8d3f711451dc24/0005f0984025e10b/rmusic/U2FsdGVkX1_dauEkFK0Wp3JEp-ybV_zPBZeX198TYk3WnykA8ANGft0WRxH-Y_q8vL11A7AsDsiAHwdPLeKNg5Kt7GfgNN-f0ADn1642NbU/8d52061b424cef985c0fcd49bc3704181bc2692cc895328faeae425af0507518/32535?track-id=38621750&play=false')

        elif message_text == "ответы after the storm":
            bot.send_photo(message.chat.id,
                           'https://sun9-north.userapi.com/sun9-81/s/v1/ig2/Lu287V7AiZK7Zp1Ndud2qFAap8-ROvSrQaLsNBXBzOc9pwfvQ86oyf54zggHCUW72IwB-Up26wblnncMZlGXvPqz.jpg?size=1527x2160&quality=96&type=album')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn_songs1 = types.KeyboardButton("Вернуться к списку песен")
            btn_songs2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn_songs1, btn_songs2)
            bot.send_sticker(message.chat.id,
                             'CAACAgIAAxkBAAEHkotj3NPLzYj1DflKz3d6zBq1HMUHsQACqQIAAlgEPy76wTeAIOkECS4E',
                             reply_markup=markup)

        elif message_text == "space girl - frances forever":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn_song1 = types.KeyboardButton("ответы space girl - frances forever")
            btn_song2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn_song1, btn_song2)
            bot.send_message(message.chat.id, 'Прослушай песню и заполни пропуски', reply_markup=markup)
            bot.send_photo(message.chat.id,
                           'https://sun9-west.userapi.com/sun9-38/s/v1/ig2/cpYTvhluEmJY3RMQlqzu7L3c4FhJtajwrl_65nNw8ND58l0owVkCVNhkcTyx5w9mfl3J52lzbI7d4z-NWXwYso8r.jpg?size=1527x2160&quality=96&type=album')
            bot.send_audio(message.chat.id,
                           'https://muzmo.cc/get/cuts/a7/62/a762177626d394b74ed1f85e79215133/71774046/Frances_Forever_-_Space_Girl_b128f0d231.mp3')

        elif message_text == "ответы space girl - frances forever":
            bot.send_photo(message.chat.id,
                           'https://sun9-west.userapi.com/sun9-49/s/v1/ig2/Rg4-viW48i81yTuM1gMV9Z-PAbuD8szc1tandQZq6j_4DMFVGV5llLQhWLYG-G3r5AxQa-uuZzzD5pUo4_sip2nx.jpg?size=1527x2160&quality=96&type=album')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn_songs1 = types.KeyboardButton("Вернуться к списку песен")
            btn_songs2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn_songs1, btn_songs2)
            bot.send_sticker(message.chat.id,
                             'CAACAgIAAxkBAAEHko1j3NPWgwaXRrNmsbAWNwuoY_e5jwAChQwAAvu02Umb_uv403P_my4E',
                             reply_markup=markup)

        elif message_text == "don't start now - dua lipa":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn_song1 = types.KeyboardButton("ответы don't start now - dua lipa")
            btn_song2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn_song1, btn_song2)
            bot.send_message(message.chat.id, 'Прослушай песню и заполни пропуски', reply_markup=markup)
            bot.send_photo(message.chat.id,
                           'https://sun9-west.userapi.com/sun9-39/s/v1/ig2/zpmEQdgOKF6O36DdpyR_XOz2T46aufnuI47_B8LIoRg0SoF7Az3eVlD8bBhb0yUmTvHZ1e6JLT_4wMrVUbLqMIL0.jpg?size=1527x2160&quality=96&type=album')
            bot.send_audio(message.chat.id,
                           'https://s199myt.storage.yandex.net/get-mp3/8e7f085b23845863103c621a898e6694/0005f0985a00da18/rmusic/U2FsdGVkX1_RPjD4shHBzGmJNScIXjiHlZdK8vItq21v_YOXSQPqrD7ukjqjYvwH6axZknUeJf2D-Q79DO2wJdv8Hby3SHbBNqI7ZkkWsHs/b96eee7ca634ae7f17454c08101df7f9b474148478a3865e9b6d7164214ffb63/28835?track-id=59412705&play=false')

        elif message_text == "ответы don't start now - dua lipa":
            bot.send_photo(message.chat.id,
                           'https://sun3.userapi.com/sun3-12/s/v1/ig2/gF2jBZZCHDugQ3K6ZkJbnr38DkW3X_wkHChL79ZiiSAq-8DKHhCqEgvi1lNM_MycSvsChOOKv-4ghpctf5Wrwkt5.jpg?size=1527x2160&quality=96&type=album')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn_songs1 = types.KeyboardButton("Вернуться к списку песен")
            btn_songs2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn_songs1, btn_songs2)
            bot.send_sticker(message.chat.id,
                             'CAACAgIAAxkBAAEHkpFj3NPeTv5Nl5ki2WAWLTRYDFMclAAC_xoAApegGUi0uIEiim_MKS4E',
                             reply_markup=markup)

        elif message_text == "i wanna be yours - arctic monkeys":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn_song1 = types.KeyboardButton("ответы i wanna be yours - arctic monkeys")
            btn_song2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn_song1, btn_song2)
            bot.send_message(message.chat.id, 'Прослушай песню и заполни пропуски', reply_markup=markup)
            bot.send_photo(message.chat.id,
                           'https://sun3.userapi.com/sun3-17/s/v1/ig2/Mgnh9aOnjeC9j5d2KaPCG_EwvmCpYW2DUwuAVwZ5xUFYQAXK51UWAK3Ru7e833HdRNufzSs0nKTr1gXOrRx1ETrr.jpg?size=1527x2160&quality=96&type=album')
            bot.send_audio(message.chat.id,
                           'https://s60iva.storage.yandex.net/get-mp3/f56199f87d05b8035aca7fb6b95b25a0/0005f0a9cadbbdf2/rmusic/U2FsdGVkX19yVcbzTDrXPIETLjtsKFKXVS97oJr_NK4X3zRnO17ZMOmO3JLIrv3gAQaOFs73jCPOixsCuO5O6heKd2GhLOWwhwbj21mUZP8/39f658df985d5c7e3991c1afffc3f03114aa4423aac06462e554bb162701da5a?track-id=44093415&play=false')

        elif message_text == "ответы i wanna be yours - arctic monkeys":
            bot.send_photo(message.chat.id,
                           'https://sun3.userapi.com/sun3-17/s/v1/ig2/A2XY6-rhQBxF9I30WTl7ATHvHGK0T7Zvmu89Ma3AKOSSY9Tn9lyqEZAMwfUXVAad5L4VrPyWMhm139ZOTSb9OKt2.jpg?size=1527x2160&quality=96&type=album')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn_songs1 = types.KeyboardButton("Вернуться к списку песен")
            btn_songs2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn_songs1, btn_songs2)
            bot.send_sticker(message.chat.id,
                             'CAACAgIAAxkBAAEHkpFj3NPeTv5Nl5ki2WAWLTRYDFMclAAC_xoAApegGUi0uIEiim_MKS4E',
                             reply_markup=markup)

        elif message_text == "looking out for you - joy again":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn_song1 = types.KeyboardButton("ответы looking out for you - joy again")
            btn_song2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn_song1, btn_song2)
            bot.send_message(message.chat.id, 'Прослушай песню и заполни пропуски', reply_markup=markup)
            bot.send_photo(message.chat.id,
                           'https://sun3.userapi.com/sun3-12/s/v1/ig2/sLa_mYkmD4CR4T0cA-WuBOsdX5kIgiKN5OrdjoGJc6klP5lfgah7g8ONHU3wlmjyUQJ_G-reM7vTzwR7fF_13LCr.jpg?size=1527x2160&quality=96&type=album')
            bot.send_audio(message.chat.id,
                           'https://song.lemuzika.pro/play/d33532303431363530318a3731353332b63432310200/9a4fe1dbec79fb8ebe03b01995cbd6bb/1.mp3')

        elif message_text == "ответы looking out for you - joy again":
            bot.send_photo(message.chat.id,
                           'https://sun9-north.userapi.com/sun9-81/s/v1/ig2/BFHq28cynwC694Jvs7ddxbilIyXpNL9r6RZig17wq6hMYXtrxMxA9PMC_OB3ln9EWKAYpVn4dWffgoL8_6DChQ15.jpg?size=1527x2160&quality=96&type=album')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn_songs1 = types.KeyboardButton("Вернуться к списку песен")
            btn_songs2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn_songs1, btn_songs2)
            bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAEHkpdj3NPqyCAPgmsyI0pnv7NDuWgf2QACfgAD-OAEAm80WVK20q79LgQ',
                             reply_markup=markup)

        elif message_text == "love yourself - justin bieber":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn_song1 = types.KeyboardButton("ответы love yourself - justin bieber")
            btn_song2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn_song1, btn_song2)
            bot.send_message(message.chat.id, 'Прослушай песню и заполни пропуски', reply_markup=markup)
            bot.send_photo(message.chat.id,
                           'https://sun3.userapi.com/sun3-16/s/v1/ig2/PZDucSHNQW9CaPToh-4Ev40DL8y0dM5c0R-PbwIbExWCDgnpDGow4dwMMoLDU9OEsZKpddetkQnZrTWdog3UHl02.jpg?size=1527x2160&quality=96&type=album')
            bot.send_audio(message.chat.id,
                           'https://s51vlx.storage.yandex.net/get-mp3/9a1fdbaff634a6cb13f392601497fb07/0005f0ac664a73ce/rmusic/U2FsdGVkX18UrMfZwsUqpdIAOnAaH_1GYef-KNxtuUhL8mFTQ1RWEwJZqBcFCysfshnVQyextDNWrpZvnMy_FSkvYd1W4KzCHSNHDqVqwI4/30953e0a8f1043362f1e4d1e5978696e44c8eb529acd6b303ebcfb86e4ec9cbf/36395?track-id=25960975&play=false')

        elif message_text == "ответы love yourself - justin bieber":
            bot.send_photo(message.chat.id,
                           'https://sun3.userapi.com/sun3-12/s/v1/ig2/cQMYYiznNPmZjfSOuuVtJQ7XneUbRHYH-N4N1HA_ykh7TaFI3G0cex1nW6FG032AGFS3Fi3FKxKNSdScMljSzNmt.jpg?size=1527x2160&quality=96&type=album')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn_songs1 = types.KeyboardButton("Вернуться к списку песен")
            btn_songs2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn_songs1, btn_songs2)
            bot.send_sticker(message.chat.id,
                             'CAACAgIAAxkBAAEHkplj3NPw1dzI8nGoc1AKYNFGCgABzusAAjABAAKDYhQnJg4kNOXzRtQuBA',
                             reply_markup=markup)

        elif message_text == "времена" or message_text == "вернуться к временам":
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn6 = types.InlineKeyboardButton(text='Определи название времени',
                                              url='https://www.baamboozle.com/game/233119')
            btn7 = types.InlineKeyboardButton(text='baamboozle', url='https://www.baamboozle.com/game/493479')
            btn8 = types.InlineKeyboardButton(text='Игра (удобнее с компьютера)',
                                              url='https://www.eslgamesplus.com/verb-tenses-interactive-grammar-game-for-esl-jeopardy-quiz-game/')
            btn1 = types.KeyboardButton("Present Tenses")
            btn2 = types.KeyboardButton("Past Tenses")
            btn3 = types.KeyboardButton("Future Tenses")
            btn5 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn6, btn7, btn8)
            markup2.add(btn1, btn2, btn3, btn5)
            bot.send_message(message.from_user.id, '''В грамматике английского языка насчитывают двенадцать времен, и каждое из них имеет свое название.
    
Для удобства времена английского языка можно объединить в группы:

👉 группа Present Tenses (настоящие времена)

👉 группа Past Tenses (прошедшие времена)

👉 группа Future Tenses (будущие времена)''', reply_markup=markup2)
            bot.send_message(message.from_user.id,
                             '''Практика всех времен ⬇''',
                             reply_markup=markup1)

        elif message_text == "present tenses":
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn6 = types.InlineKeyboardButton(text='baamboozle', url='https://www.baamboozle.com/game/86202')
            btn7 = types.InlineKeyboardButton(text='baamboozle', url='https://www.baamboozle.com/game/1123518')
            btn8 = types.InlineKeyboardButton(text='baamboozle', url='https://www.baamboozle.com/game/33250')
            btn9 = types.InlineKeyboardButton(text='Тест',
                                              url='https://www.englishtestsonline.com/present-tenses-test-b1-grammar-exercises/')
            btn10 = types.InlineKeyboardButton(text='Задания',
                                               url='https://english-practice.net/english-grammar-exercises-verbs-and-tenses-present-tenses/')
            btn11 = types.InlineKeyboardButton(text='Пропуски',
                                               url='https://wordwall.net/resource/3572732/present-tenses-upper-intermediate')
            btn1 = types.KeyboardButton("Present Simple")
            btn2 = types.KeyboardButton("Present Continuous")
            btn3 = types.KeyboardButton("Present Perfect")
            btn4 = types.KeyboardButton("Present Perfect Continuous")
            btn5 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn6, btn7, btn8, btn9, btn10, btn11)
            markup2.add(btn1, btn2, btn3, btn4, btn5)
            bot.send_message(message.from_user.id, '''Настоящее время описывает действие, которые происходит сейчас или каким-то образом связано с настоящим моментом.
    
В английском языке существует четыре формы настоящего времени:

✔ Present Simple - настоящее простое

✔ Present Continuous - настоящее длительное

✔ Present Perfect - настоящее совершённое

✔ Present Perfect Continuous - настоящее совершённое длительное''', reply_markup=markup2)
            bot.send_message(message.from_user.id, '''Практика present tenses ⬇''', reply_markup=markup1)

        elif message_text == "present simple":
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.InlineKeyboardButton(text='Игра', url='https://www.gamestolearnenglish.com/present-simple/')
            btn2 = types.InlineKeyboardButton(text='Тест (+ предложения)',
                                              url='https://myefe.ru/quizzes/tests-present-simple/test-1')
            btn3 = types.InlineKeyboardButton(text='Тест (- предложения)',
                                              url='https://myefe.ru/quizzes/tests-present-simple/test-4')
            btn4 = types.InlineKeyboardButton(text='Тест (? предложения)',
                                              url='https://myefe.ru/quizzes/tests-present-simple/test-5')
            btn5 = types.InlineKeyboardButton(text='Игра Present Simple vs Present Continuous',
                                              url='https://wordwall.net/ru/resource/17357480/present-simple-vs-present-continuous')
            btn6 = types.InlineKeyboardButton(text='baamboozle (пропуски)', url='https://www.baamboozle.com/game/25367')
            btn7 = types.InlineKeyboardButton(text='baamboozle (пропуски)', url='https://www.baamboozle.com/game/875')
            btn8 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
            btn9 = types.KeyboardButton("Вернуться к временам")
            markup2.add(btn8, btn9)
            bot.send_photo(message.from_user.id,
                           'https://sun9-east.userapi.com/sun9-57/s/v1/ig2/KVTGsiD_RY4axtWMytWsCnRvAf7SEfBUfW1HaTJdDDxqjQHO3reFwS0o65as9vlRaczZXzGallt662ZGtH5Oof-L.jpg?size=2560x1440&quality=96&type=album',
                           reply_markup=markup2)
            bot.send_message(message.from_user.id,
                             '''Ты можешь попрактиковаться там ⬇''',
                             reply_markup=markup1)

        elif message_text == "present continuous":
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.InlineKeyboardButton(text='am/is/are',
                                              url='https://vk.com/away.php?to=https%3A%2F%2Fagendaweb.org%2Fverbs%2Fpresent-continuous%2Findex.html&el=snippet')
            btn2 = types.InlineKeyboardButton(text='тест +/-/?',
                                              url='https://www.perfect-english-grammar.com/present-continuous-exercise-5.html')
            btn3 = types.InlineKeyboardButton(text='тест ?',
                                              url='https://www.perfect-english-grammar.com/present-continuous-exercise-3.html')
            btn4 = types.InlineKeyboardButton(text='baamboozle', url='https://www.baamboozle.com/game/45030')
            btn5 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://elt.oup.com/student/solutions/elementary/grammar/grammar_04_012e?cc=ru&selLanguage=ru')
            btn6 = types.InlineKeyboardButton(text='present simple/ present continuos',
                                              url='https://www.practisingenglish.com/english-grammar-exercises/present-continuous-simple2.htm')
            btn8 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn2, btn3, btn4, btn1, btn5, btn6)
            btn9 = types.KeyboardButton("Вернуться к временам")
            markup2.add(btn8, btn9)
            bot.send_photo(message.from_user.id,
                           'https://sun9-east.userapi.com/sun9-33/s/v1/ig2/f5bFjBCI4lzskugKXY1MZnvkulGI0CLIOtJrYxSWfh-9-dd8xcNcbwTDTFUkQoLgnnYr32sO2j4dR5XNugj6rVZy.jpg?size=2560x1440&quality=96&type=album',
                           reply_markup=markup2)
            bot.send_message(message.from_user.id,
                             '''Ты можешь попрактиковаться там ⬇''',
                             reply_markup=markup1)

        elif message_text == "present perfect":
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.InlineKeyboardButton(text='игра',
                                              url='https://www.gamestolearnenglish.com/perfect-tense-game/')
            btn2 = types.InlineKeyboardButton(text='тест',
                                              url='https://www.english-4u.de/en/tenses-exercises/present-perfect-simple.htm')
            btn3 = types.InlineKeyboardButton(text='тест',
                                              url='https://www.english-4u.de/en/grammar-tests/present-perfect-simple.htm')
            btn4 = types.InlineKeyboardButton(text='baamboozle', url='https://www.baamboozle.com/game/887276')
            btn5 = types.InlineKeyboardButton(text='составить предложения',
                                              url='https://www.perfect-english-grammar.com/present-perfect-exercise-4.html')
            btn6 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.practisingenglish.com/english-grammar-exercises/present-perfect-simple1.htm')
            btn7 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.really-learn-english.com/present-perfect-exercises.html#03')
            btn8 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn2, btn3, btn4, btn1, btn5, btn6, btn7)
            btn9 = types.KeyboardButton("Вернуться к временам")
            markup2.add(btn8, btn9)
            bot.send_photo(message.from_user.id,
                           'https://sun9-west.userapi.com/sun9-1/s/v1/ig2/8j_GrgHYAF3Zw0RAmgiofnyJCPAew3M-6CJRGzjHnuMuMvOd0JjKN2LzxJ_pkb-_YrJZb3y4KXP2zjSPrKPPGaa1.jpg?size=2560x1440&quality=96&type=album',
                           reply_markup=markup2)
            bot.send_message(message.from_user.id,
                             '''Ты можешь попрактиковаться там ⬇''',
                             reply_markup=markup1)

        elif message_text == "present perfect continuous":
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.InlineKeyboardButton(text='составить предложения',
                                              url='https://elt.oup.com/student/solutions/int/grammar/grammar_04_022e?cc=ru&selLanguage=ru')
            btn2 = types.InlineKeyboardButton(text='составить предложения',
                                              url='https://www.perfect-english-grammar.com/present-perfect-continuous-exercise-1.html')
            btn3 = types.InlineKeyboardButton(text='составить вопросы',
                                              url='https://www.perfect-english-grammar.com/present-perfect-continuous-exercise-2.html')
            btn4 = types.InlineKeyboardButton(text='baamboozle', url='https://www.baamboozle.com/game/55460')
            btn5 = types.InlineKeyboardButton(text='тест (с объяснением)',
                                              url='https://test-english.com/grammar-points/b1/present-perfect-simple-present-perfect-continuous/')
            btn6 = types.InlineKeyboardButton(text='тест',
                                              url='https://agendaweb.org/exercises/verbs/present-perfect-continuous/exercise-1')
            btn8 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn2, btn3, btn4, btn1, btn5, btn6)
            btn9 = types.KeyboardButton("Вернуться к временам")
            markup2.add(btn8, btn9)
            bot.send_photo(message.from_user.id,
                           'https://sun9-west.userapi.com/sun9-66/s/v1/ig2/FK1MSicBOeQgwDhzY2jYOLeGV6zBpEgr5fO8TlZvE2ODoVrnOrg52wC5gYI5zDsxrq_rrxOWXy4qoOy9_iFU90PO.jpg?size=2560x1440&quality=96&type=album',
                           reply_markup=markup2)
            bot.send_message(message.from_user.id,
                             '''Ты можешь попрактиковаться там ⬇''',
                             reply_markup=markup1)

        elif message_text == "past tenses":
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn6 = types.InlineKeyboardButton(text='baamboozle (пропуски)',
                                              url='https://www.baamboozle.com/game/667315')
            btn7 = types.InlineKeyboardButton(text='Определение времени',
                                              url='https://wordwall.net/ru/resource/29532350/english/past-times-verb-forms')
            btn8 = types.InlineKeyboardButton(text='Определение времени',
                                              url='https://wordwall.net/ru/resource/1884014/past-tenses')
            btn9 = types.InlineKeyboardButton(text='baamboozle (вопросы)', url='https://www.baamboozle.com/game/916602')
            btn10 = types.InlineKeyboardButton(text='Игра (удобнее с компьютера)',
                                               url='https://www.eslgamesplus.com/irregular-past-tense-esl-grammar-jeopardy-quiz-game/')
            btn11 = types.InlineKeyboardButton(text='Тест', url='https://www.native-english.ru/tests/past-tenses')
            btn1 = types.KeyboardButton("Past Simple")
            btn2 = types.KeyboardButton("Past Continuous")
            btn3 = types.KeyboardButton("Past Perfect")
            btn4 = types.KeyboardButton("Past Perfect Continuous")
            btn5 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn6, btn7, btn8, btn9, btn10, btn11)
            markup2.add(btn1, btn2, btn3, btn4, btn5)
            bot.send_message(message.from_user.id, '''Времена группы Past в английском языке необходимы для описания действий, произошедших в прошлом.
    
В английском языке существует четыре формы прошедшего времени:

✔ Past Simple - прошедшее простое

✔ Past Continuous - прошедшее длительное

✔ Past Perfect - прошедшее совершённое

✔ Past Perfect Continuous - прошедшее совершённое длительное''', reply_markup=markup2)
            bot.send_message(message.from_user.id, '''Практика past tenses ⬇''', reply_markup=markup1)

        elif message_text == "past simple":
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.InlineKeyboardButton(text='игра', url='https://www.gamestolearnenglish.com/past-tense-game/')
            btn2 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.practisingenglish.com/english-grammar-exercises/irregular-verbs-past_1.htm')
            btn3 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.practisingenglish.com/english-grammar-exercises/past-simple.htm')
            btn4 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.perfect-english-grammar.com/past-simple-exercise-8.html')
            btn5 = types.InlineKeyboardButton(text='baamboozle', url='https://www.baamboozle.com/game/116960')
            btn8 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn2, btn3, btn4, btn1, btn5)
            btn9 = types.KeyboardButton("Вернуться к временам")
            markup2.add(btn8, btn9)
            bot.send_photo(message.from_user.id,
                           'https://sun9-west.userapi.com/sun9-40/s/v1/ig2/9f4DMXh8xYX6-RWf04euI2oz6jl9WAXJj48JZ_xvTt7iTBsgA7F4opKFWgDTZzlw3Uv4DxahVj6evSsnngkcGeMC.jpg?size=2560x1440&quality=95&type=album',
                           reply_markup=markup2)
            bot.send_message(message.from_user.id,
                             '''Ты можешь попрактиковаться там ⬇''',
                             reply_markup=markup1)

        elif message_text == "past continuous":
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.perfect-english-grammar.com/past-continuous-exercise-3.html')
            btn2 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.perfect-english-grammar.com/past-continuous-exercise-2.html')
            btn3 = types.InlineKeyboardButton(text='baamboozle',
                                              url='https://www.baamboozle.com/search?param=past+continuous&language=&sort_by=featured&results_from=all&filter_questions_min=10')
            btn4 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.ego4u.com/en/cram-up/grammar/past-progressive/exercises')
            btn8 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn2, btn3, btn4, btn1)
            btn9 = types.KeyboardButton("Вернуться к временам")
            markup2.add(btn8, btn9)
            bot.send_photo(message.from_user.id,
                           'https://sun9-east.userapi.com/sun9-32/s/v1/ig2/BDVQWr-aW0RQk7CGYnlLmK4mCzO0UvwB651V2P0E2FjNG8t8cxLZo4CBjHpQw05YW2J6s47PsjtGl9P46WEhmOP9.jpg?size=2560x1440&quality=95&type=album',
                           reply_markup=markup2)
            bot.send_message(message.from_user.id,
                             '''Ты можешь попрактиковаться там ⬇''',
                             reply_markup=markup1)

        elif message_text == "past perfect":
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.InlineKeyboardButton(text='составить предложения',
                                              url='https://www.perfect-english-grammar.com/past-perfect-exercise-1.html')
            btn2 = types.InlineKeyboardButton(text='составить вопросы',
                                              url='https://www.perfect-english-grammar.com/past-perfect-exercise-2.html')
            btn3 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.englisch-hilfen.de/en/exercises/tenses/past_perfect_simple_past.htm')
            btn4 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.english-4u.de/en/tenses-exercises/past-simple-past-perfect.htm')
            btn5 = types.InlineKeyboardButton(text='baamboozle', url='https://www.baamboozle.com/game/75665')
            btn6 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.practisingenglish.com/english-grammar-exercises/past-perfect_compare.htm')
            btn8 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn2, btn3, btn4, btn1, btn5, btn6)
            btn9 = types.KeyboardButton("Вернуться к временам")
            markup2.add(btn8, btn9)
            bot.send_photo(message.from_user.id,
                           'https://sun9-east.userapi.com/sun9-31/s/v1/ig2/YmojSlod2y2ENdART5eThhv_b3Kt4sqrCm_rYq859Bbad0VCD7SlQES59qeTAsgc61-GWVuUQet6SkGK7p4au-eN.jpg?size=2560x1440&quality=95&type=album',
                           reply_markup=markup2)
            bot.send_message(message.from_user.id,
                             '''Ты можешь попрактиковаться там ⬇''',
                             reply_markup=markup1)

        elif message_text == "past perfect continuous":
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.perfect-english-grammar.com/past-perfect-continuous-exercise-1.html')
            btn2 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.perfect-english-grammar.com/past-perfect-continuous-exercise-3.html')
            btn3 = types.InlineKeyboardButton(text='baamboozle', url='https://www.baamboozle.com/game/1004696')
            btn4 = types.InlineKeyboardButton(text='пропуски', url='https://www.englishpage.com/verbpage/verbs13.htm')
            btn8 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn2, btn3, btn4, btn1)
            btn9 = types.KeyboardButton("Вернуться к временам")
            markup2.add(btn8, btn9)
            bot.send_photo(message.from_user.id,
                           'https://sun9-east.userapi.com/sun9-73/s/v1/ig2/YUCLFkcIj6XtkaINIguOX2qf6ym-w2DfGw2WUcbfI360XSajEjxEMgq-qjSuKDPZsTrLgm0ZmSZ9tbjSFwOOQ--D.jpg?size=2560x1440&quality=95&type=album',
                           reply_markup=markup2)
            bot.send_message(message.from_user.id,
                             '''Ты можешь попрактиковаться там ⬇''',
                             reply_markup=markup1)

        elif message_text == "future tenses":
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn6 = types.InlineKeyboardButton(text='baamboozle (пропуски)',
                                              url='https://www.baamboozle.com/game/275022')
            btn7 = types.InlineKeyboardButton(text='Составление предложения',
                                              url='https://wordwall.net/ru/resource/5604287/future-continuous-future-perfect-future-perfect-continuous')
            btn8 = types.InlineKeyboardButton(text='Тест',
                                              url='https://onlinetestpad.com/ru/test/2511-test-future-tenses-variant-1')
            btn9 = types.InlineKeyboardButton(text='baamboozle (пропуски)',
                                              url='https://www.baamboozle.com/game/770943')
            btn10 = types.InlineKeyboardButton(text='Крутилка',
                                               url='https://wordwall.net/ru/resource/32010767/future-continuous-future-perfect-simple-future-perfect')
            btn11 = types.InlineKeyboardButton(text='Тест', url='http://testyourenglish.org/test-59')
            btn1 = types.KeyboardButton("Future Simple")
            btn2 = types.KeyboardButton("Future Continuous")
            btn3 = types.KeyboardButton("Future Perfect")
            btn4 = types.KeyboardButton("Future Perfect Continuous")
            btn5 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn6, btn7, btn8, btn9, btn10, btn11)
            markup2.add(btn1, btn2, btn3, btn4, btn5)
            bot.send_message(message.from_user.id, '''Времена группы Future в английском языке необходимы для описания действий, которые произойдут в будущем.
            
В английском языке существует четыре формы будущего времени:

🧚🏻‍♀ ️Future Simple - будущее простое

🧚🏻‍♀ ️Future Continuous - будущее непрерывное

🧚🏻‍♀ ️Future Perfect - будущее совершённое

🧚🏻‍♀ ️Future Perfect Continuous - будущее совершённое непрерывное''', reply_markup=markup2)
            bot.send_message(message.from_user.id, '''Практика future tenses ⬇''', reply_markup=markup1)

        elif message_text == "future simple":
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.InlineKeyboardButton(text='игра', url='https://www.gamestolearnenglish.com/future-tense-game/')
            btn2 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.perfect-english-grammar.com/simple-future-exercise-1.html')
            btn3 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.perfect-english-grammar.com/simple-future-exercise-3.html')
            btn4 = types.InlineKeyboardButton(text='baamboozle', url='https://www.baamboozle.com/game/47021')
            btn5 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.grammarism.com/future-simple-exercises/')
            btn6 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.engblocks.com/grammar/exercises/tenses/future-simple-mixed/')
            btn8 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn2, btn3, btn4, btn1, btn5, btn6)
            btn9 = types.KeyboardButton("Вернуться к временам")
            markup2.add(btn8, btn9)
            bot.send_photo(message.from_user.id,
                           'https://sun9-east.userapi.com/sun9-35/s/v1/ig2/he-OhBcJYP8WjORy0y2vE6sGJWAu6FGRljXC2yil4FC666rJYsstLvo4IMXEJjnC7S66t7c6jrYMAd0ogwI2EvCt.jpg?size=2560x1440&quality=95&type=album',
                           reply_markup=markup2)
            bot.send_message(message.from_user.id,
                             '''Ты можешь попрактиковаться там ⬇''',
                             reply_markup=markup1)

        elif message_text == "future continuous":
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.perfect-english-grammar.com/future-continuous-exercise-1.html')
            btn2 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.perfect-english-grammar.com/future-continuous-exercise-3.html')
            btn3 = types.InlineKeyboardButton(text='baamboozle', url='https://www.baamboozle.com/game/838429')
            btn4 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://agendaweb.org/exercises/verbs/future/future-continuous')
            btn5 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.really-learn-english.com/future-progressive-exercises.html#01')
            btn8 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn2, btn3, btn4, btn1, btn5)
            btn9 = types.KeyboardButton("Вернуться к временам")
            markup2.add(btn8, btn9)
            bot.send_photo(message.from_user.id,
                           'https://sun9-west.userapi.com/sun9-2/s/v1/ig2/-sgXE1Stj4cX8FiuXAKlSvI8NMY5ieLSUxBoBSEEL4Pv8eQrR4xaWhsSPecrszjhCuq2CmYJg1GvZJ11_XT2sstX.jpg?size=2560x1440&quality=95&type=album',
                           reply_markup=markup2)
            bot.send_message(message.from_user.id,
                             '''Ты можешь попрактиковаться там ⬇''',
                             reply_markup=markup1)

        elif message_text == "future perfect":
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.perfect-english-grammar.com/future-perfect-exercise-1.html')
            btn2 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.perfect-english-grammar.com/future-perfect-exercise-4.html')
            btn3 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://test-english.com/grammar-points/b1-b2/future-continuous-and-future-perfect/')
            btn4 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.montsemorales.com/gramatica/FutPerf.htm')
            btn5 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.really-learn-english.com/future-perfect-exercises.html#01')
            btn6 = types.InlineKeyboardButton(text='офлайн формат',
                                              url='http://grammar-tei.com/future-perfect-uprazhneniya-s-otvetami/')
            btn8 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn2, btn3, btn4, btn1, btn5, btn6)
            btn9 = types.KeyboardButton("Вернуться к временам")
            markup2.add(btn8, btn9)
            bot.send_photo(message.from_user.id,
                           'https://sun9-east.userapi.com/sun9-35/s/v1/ig2/M_Lz4WALdqXm7EBvaOkvNcwTRQkTxF3WDNZe_s8Z36aPReWxWVnW4QnjdW-Z9U1HYGzOS_mF_yCu2A-ksEXFPe7d.jpg?size=2560x1440&quality=95&type=album',
                           reply_markup=markup2)
            bot.send_message(message.from_user.id,
                             '''Ты можешь попрактиковаться там ⬇''',
                             reply_markup=markup1)

        elif message_text == "future perfect continuous":
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.perfect-english-grammar.com/future-perfect-continuous-exercise-1.html')
            btn2 = types.InlineKeyboardButton(text='пропуски',
                                              url='https://www.perfect-english-grammar.com/future-perfect-continuous-exercise-4.html')
            btn3 = types.InlineKeyboardButton(text='baamboozle', url='https://www.baamboozle.com/game/1104528')
            btn4 = types.InlineKeyboardButton(text='тест',
                                              url='https://www.englishclub.com/grammar/verb-tenses_future-perfect-continuous-quiz.php')
            btn5 = types.InlineKeyboardButton(text='тест',
                                              url='https://www.examenglish.com/grammar/future_perfect_continuous.htm')
            btn8 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn2, btn3, btn4, btn1, btn5)
            btn9 = types.KeyboardButton("Вернуться к временам")
            markup2.add(btn8, btn9)
            bot.send_photo(message.from_user.id,
                           'https://sun9-west.userapi.com/sun9-62/s/v1/ig2/DALbOh5AiMKJppXos1nhsqm18_qRReM2HcslvSCVjN8eZSpbChJmdN_kIyNUvtbsARlByktUkAPcyAHc5TwTOq3K.jpg?size=2560x1440&quality=95&type=album',
                           reply_markup=markup2)
            bot.send_message(message.from_user.id,
                             '''Ты можешь попрактиковаться там ⬇''',
                             reply_markup=markup1)

        elif message_text == "егэ":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item_ege1 = types.KeyboardButton("Аудирование")
            item_ege2 = types.KeyboardButton("Чтение")
            item_ege3 = types.KeyboardButton("Грамматика и лексика")
            item_ege4 = types.KeyboardButton("Письменная речь")
            item_ege5 = types.KeyboardButton("Устная часть")
            item_ege6 = types.KeyboardButton("Вернуться в начало")
            markup.add(item_ege1, item_ege2, item_ege3, item_ege4, item_ege5, item_ege6)
            bot.send_message(message.chat.id, '''*В настоящее время в ЕГЭ по английскому языку входит:*
    
🧐 Аудирование    
    
🧐 Чтение

🧐 Грамматика и лексика

🧐 Письменная речь

🧐 Устная часть
''', reply_markup=markup, parse_mode="Markdown")
            bot.send_message(message.chat.id, '''Что тебя интересует?''', reply_markup=markup)

        elif message_text == "аудирование" or message_text == "вернуться к аудированию":
            markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton("Задание 1")
            btn2 = types.KeyboardButton("Задание 2")
            btn3 = types.KeyboardButton("Задания 3-9")
            btn4 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn1, btn2, btn3, btn4)
            markup = types.InlineKeyboardMarkup(row_width=2)
            first_button = types.InlineKeyboardButton(text="⬅", callback_data="to_3")
            second_button = types.InlineKeyboardButton(text="➡", callback_data="to_2")
            markup.add(first_button, second_button)
            bot.send_message(message.chat.id, '''*Аудирование состоит из трех типов заданий👂:*
    
1⃣ прослушивание текстов и соотнесение их с утверждениями

2⃣ прослушивание диалога и определение степени соответствия утверждений данному диалогу

3⃣ прослушивание интервью и ответы на вопросы к нему
''', reply_markup=markup, parse_mode="Markdown")
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG_rBjqCrhrBXE4EqGZJ1JVVLe_lChIAACggADYqijKqFi3BdkQWFWLAQ',
                             reply_markup=markup1)

        elif message_text == "задание 1":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton("Практика 1 задания")
            btn2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, '''🧐 *Высказывание и утверждение*🧐
    
Установление соответствия между высказываниями каждого говорящего и утверждениями''', reply_markup=markup,
                             parse_mode="Markdown")

        elif message_text == "практика 1 задания":
            markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn2 = types.KeyboardButton("Вернуться к аудированию")
            btn3 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn2, btn3)
            bot.send_message(message.chat.id,
                             '''Напомню, что *формулировка задания звучит следующим образом:* “Вы услышите 6 высказываний. Установите соответствие между высказываниями каждого говорящего А-F и утверждениями, данными в списке 1-7. Используйте каждое утверждение, обозначенное соответствующей цифрой, только один раз. В задании есть одно лишнее утверждение. Вы услышите запись дважды.”''',
                             reply_markup=markup1, parse_mode="Markdown")
            markup = types.InlineKeyboardMarkup(row_width=2)
            first_button = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_1_2")
            second_button = types.InlineKeyboardButton(text="ответы ", callback_data="ege_ex_1_1_answer")
            markup.add(second_button, first_button)
            bot.send_message(message.chat.id, '''1. The speaker was glad when she/he was given more serious work to do.
            
2. The speaker learned nothing important at work.

3. The speaker did not want to take any responsibility.

4. The speaker didn’t mind doing a lot of things during work practice.

5. The speaker wants to do the same kind of work in the future.

6. The speaker has a different idea of the profession after completing the practice.

7. The speaker felt rather nervous before starting work.''', reply_markup=markup)
            bot.send_audio(message.chat.id, audio='https://tonail.com/gia/ege/audirovaniye/audirovaniye_1_11.mp3')

        elif message_text == "задание 2":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton("Практика 2 задания")
            btn2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, '''🧐 *диалог и утверждение *🧐

Определение степени соответствия утверждений диалогу: 

✅ true – соответствует, 

❎ false – не соответствует, 

😐 not stated – об этом не было речи.''', reply_markup=markup, parse_mode="Markdown")

        elif message_text == "практика 2 задания":
            markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn2 = types.KeyboardButton("Вернуться к аудированию")
            btn3 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn2, btn3)
            bot.send_message(message.chat.id,
                             '''В общем виде *задание формулируется следующим образом*: “Вы услышите диалог. Определите, какие из приведённых утверждений соответствуют содержанию текста (True), какие не соответствуют (False) и о чём в тексте не сказано, то есть на основании текста нельзя дать ни положительного, ни отрицательного ответа (Not stated). Вы услышите запись дважды.”''',
                             reply_markup=markup1, parse_mode="Markdown")
            markup = types.InlineKeyboardMarkup(row_width=2)
            first_button = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_2_2")
            second_button = types.InlineKeyboardButton(text="ответы ", callback_data="ege_ex_2_1_answer")
            markup.add(second_button, first_button)
            bot.send_message(message.chat.id, '''A) A lot of people went to Michaels photography exhibition.

B) Michael has paid for lessons in photography.

C) Michael is not fond of colour photography.

D) Denise doesn’t know how to use the camera on her phone.

E) Michael uses a camera phone to take a lot of photos.

F) Michael’s mum has stopped using traditional film.

G) Michael’s mum wants him to learn how to develop photos from film.''', reply_markup=markup)
            bot.send_audio(message.chat.id, audio='https://tonail.com/audio/ege/interview2-7.mp3')

        elif message_text == "задания 3-9":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton("Практика заданий 3-9")
            btn2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, '''🪐 *Интервью и вопросы к нему*🪐

Прослушивание интервью и ответы на вопросы по его содержанию.

Это третье (и последнее) задание в разделе аудирования ЕГЭ по английскому языку. Считается, что данное задание является самым трудным😨, рассчитанным на детальное понимание звучащего текста. И на самом деле, для его успешного выполнения требуется особая тренировка.''',
                             reply_markup=markup, parse_mode="Markdown")

        elif message_text == "практика заданий 3-9":
            markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn2 = types.KeyboardButton("Вернуться к аудированию")
            btn3 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn2, btn3)
            bot.send_message(message.chat.id,
                             '''В общем виде *задание формулируется следующим образом*: “Вы услышите интервью. В заданиях 3–9 запишите в поле ответа цифру 1, 2 или 3, соответствующую выбранному Вами варианту ответа. Вы услышите запись дважды.”''',
                             reply_markup=markup1, parse_mode="Markdown")
            markup = types.InlineKeyboardMarkup(row_width=2)
            first_button = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_3_2")
            second_button = types.InlineKeyboardButton(text="ответы ", callback_data="ege_ex_3_1_answer")
            markup.add(second_button, first_button)
            bot.send_message(message.chat.id, '''1. What is true about the art in Karen’s gallery?
1) Nothing in the basement was undamaged.
2) Most of the art on the main floor was undamaged.
3) Some basement collections were undamaged.

2. Some of the damaged paintings in Karen’s basement can be repaired …
1) by Karen herself.
2) by experts.
3) by the artists.

3. Which option does Karen prefer for recovering the cost of the art?
1) Repairing it and selling it at a discount.
2) Waiting for her insurance company to pay in full.
3) Asking the artists to claim on their insurance.

4. An artist that Karen knows …
1) luckily had her work insured.
2) will need two years to repair the damage.
3) couldn’t afford insurance.

5. What happened to some public works of art?
1) They were damaged in the storm.
2) They were completely lost in the storm.
3) They were placed under protective material.

6. The institute for art conservation …
1) was extremely busy round the time of the storm.
2) received flood damage as a result of the storm.
3) was physically removing structures from art centres.

7. What does Karen hope will result from the storm?
1) The art world will help communities rebuild.
2) Artists may draw inspiration from the storms effect.
3) People will value art more highly.''', reply_markup=markup)
            bot.send_audio(message.chat.id, audio='https://tonail.com/audio/ege/interview-4.mp3')

        elif message_text == "чтение" or message_text == "вернуться к чтению":
            markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton("Задание 10")
            btn2 = types.KeyboardButton("Задание 11")
            btn3 = types.KeyboardButton("Задания 12-18")
            btn4 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn1, btn2, btn3, btn4)
            markup = types.InlineKeyboardMarkup(row_width=2)
            first_button = types.InlineKeyboardButton(text="⬅", callback_data="reading_to_3")
            second_button = types.InlineKeyboardButton(text="➡", callback_data="reading_to_2")
            markup.add(first_button, second_button)
            bot.send_message(message.chat.id, '''*Чтение состоит из трех типов заданий:*

🧸 подбор заголовков к текстам (задание 10)

🧸 вставка в текст пропущенных фраз (задание 11)

🧸 чтение текста и ответы на вопросы к нему (задания 12-18)''', reply_markup=markup, parse_mode="Markdown")
            bot.send_sticker(message.chat.id,
                             'CAACAgIAAxkBAAEG_rJjqCroTzWNZA3BZLTZY43pN5XkhwAChhEAAn3MmEt9UI1vjmtzXSwE',
                             reply_markup=markup1)

        elif message_text == "задание 10":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.KeyboardButton("Вернуться к чтению")
            btn2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2)
            btn3 = types.InlineKeyboardButton(text='сайт для практики',
                                              url='https://tonail.com/тексты-и-заголовки/')
            markup1.add(btn3)
            bot.send_message(message.chat.id, '''😊 *Тексты и заголовки*😊

*Задание формулируется следующим образом*: “Установите соответствие между заголовками 1–8 и текстами A–G. Используйте каждую цифру только один раз. В задании один заголовок лишний.”''',
                             reply_markup=markup, parse_mode="Markdown")
            bot.send_message(message.chat.id, 'Ты можешь попрактиковаться там ⬇', reply_markup=markup1)

        elif message_text == "задание 11":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.KeyboardButton("Вернуться к чтению")
            btn2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2)
            btn3 = types.InlineKeyboardButton(text='сайт для практики',
                                              url='https://tonail.com/текст-и-пропущенные-части/')
            markup1.add(btn3)
            bot.send_message(message.chat.id, '''😄 *Текст и пропущенные части*😄

*Задание формулируется следующим образом*: “Прочитайте текст и заполните пропуски A–F частями предложений, обозначенными цифрами 1–7. Одна из частей в списке 1–7 лишняя. Занесите цифры, обозначающие соответствующие части предложений, в таблицу.”''',
                             reply_markup=markup, parse_mode="Markdown")
            bot.send_message(message.chat.id, 'Ты можешь попрактиковаться там ⬇', reply_markup=markup1)

        elif message_text == "задания 12-18":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.KeyboardButton("Вернуться к чтению")
            btn2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2)
            btn3 = types.InlineKeyboardButton(text='сайт для практики',
                                              url='https://tonail.com/чтение-текста-и-ответы-на-вопросы/')
            markup1.add(btn3)
            bot.send_message(message.chat.id, '''🫶 *Текст и ответы на вопросы*🫶

*Задание формулируется следующим образом*: “Прочитайте текст и выполните задания 12–18. В каждом задании запишите в поле ответа цифру 1, 2, 3 или 4, соответствующую выбранному Вами варианту ответа.”''',
                             reply_markup=markup, parse_mode="Markdown")
            bot.send_message(message.chat.id, 'Ты можешь попрактиковаться там ⬇', reply_markup=markup1)

        elif message_text == "грамматика и лексика" or message_text == "вернуться к лексике и грамматике":
            markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton("Задания 19-24")
            btn2 = types.KeyboardButton("Задания 25-29")
            btn3 = types.KeyboardButton("Задания 30-36")
            btn4 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn1, btn2, btn3, btn4)
            markup = types.InlineKeyboardMarkup(row_width=2)
            first_button = types.InlineKeyboardButton(text="⬅", callback_data="grammar1")
            second_button = types.InlineKeyboardButton(text="➡", callback_data="grammar3")
            markup.add(first_button, second_button)
            bot.send_message(message.chat.id, '''Лексика и грамматика состоит из трех типов заданий:

😊 грамматическая трансформация (грамматическое преобразования, *изменение* грамматической формы)

🗣️ лексическая трансформация (лексическое преобразование, *образование* нового однокоренного слова)

📨 *вставка* в текст пропущенных слов
                                                                                                                    ''',
                             reply_markup=markup, parse_mode="Markdown")
            bot.send_sticker(message.chat.id,
                             'CAACAgIAAxkBAAEG_r1jqCse-DVATgwLuIANAAE-Gb38wUEAApsIAAJcAmUD9K3r4Nij-CksBA',
                             reply_markup=markup1)

        elif message_text == "письменная речь" or message_text == "вернуться к письменной речи":
            markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn4 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn4)
            markup = types.InlineKeyboardMarkup(row_width=2)
            first_button = types.InlineKeyboardButton(text="⬅", callback_data="writing3")
            second_button = types.InlineKeyboardButton(text="➡", callback_data="writing2")
            markup.add(first_button, second_button)
            bot.send_message(message.chat.id, '''

💌 Для выполнения заданий этого раздела потренируйтесь различать *нейтральный* и *неофициальный* стили.

📝 Например, в эссе *нельзя* использовать *well, actually, anyway*: это *informal words*.

🥇 Здесь требуется *индивидуальная* подготовка.''',
                             reply_markup=markup, parse_mode="Markdown")
            bot.send_sticker(message.chat.id,
                             'CAACAgIAAxkBAAEG_sVjqCymGRT--Bk9X3qh7Y_72pELjwAC_gIAAlwCZQPigns-eWCFDiwE',
                             reply_markup=markup1)

        elif message_text == "задания 19-24":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton("Практика заданий 19-24")
            btn2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, '''🧶 *Изменение* грамматической *формы* слов таким образом, чтобы они грамматически *соответствовали* содержанию текстов.

*Формулировка задания звучит следующим образом:*

"Прочитайте приведённые ниже *тексты*. * Преобразуйте*, если необходимо, слова, напечатанные заглавными буквами в конце строк, обозначенных номерами 19–24, так, чтобы они *грамматически* соответствовали содержанию текстов. Заполните пропуски полученными словами. Каждый пропуск соответствует отдельному заданию из группы 19–24".''',
                             reply_markup=markup, parse_mode="Markdown")

        elif message_text == "задания 25-29":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton("Практика заданий 25-29")
            btn2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id,
                             '''Образование новых однокоренных слов таким образом, чтобы они по своему значению соответствовали содержанию текстов.
Формулировка задания звучит следующим образом:

"*Прочитайте* приведённый ниже текст. *Образуйте* от слов, напечатанных *заглавными* буквами в *конце строк*, обозначенных номерами 25–29, однокоренные слова так, чтобы они *грамматически* и *лексически* соответствовали содержанию текста.  *Заполните* пропуски полученными словами. Каждый пропуск соответствует *отдельному* заданию из группы 25–29."''',
                             reply_markup=markup, parse_mode="Markdown")

        elif message_text == "задания 30-36":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton("Практика заданий 30-36")
            btn2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id,
                             '''🗃️ Заполнение пропусков в тексте. Для каждого пропуска предложены несколько вариантов вставки. Необходимо выбрать правильное слово-вставку.

*Формулировка задания звучит следующим образом:*

"Прочитайте текст с пропусками, обозначенными номерами 30–36. Эти номера соответствуют заданиям 30–36, в которых представлены возможные варианты ответов. Запишите в поле ответа цифру 1, 2, 3 или 4, соответствующую выбранному Вами варианту ответа."
''',
                             reply_markup=markup, parse_mode="Markdown")

        elif message_text == "практика заданий 19-24":
            markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton("Вернуться к лексике и грамматике")
            btn2 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn1, btn2)
            markup = types.InlineKeyboardMarkup(row_width=2)
            first_button = types.InlineKeyboardButton(text="ответы", callback_data="grammar_2539answ")
            second_button = types.InlineKeyboardButton(text="➡", callback_data="grammarnext1")
            markup.add(first_button, second_button)
            bot.send_message(message.chat.id, '''*Sepak takraw*

Have you heard of sepak takraw? It’s a sport in Southeast Asia which *( PLAY )* like volleyball, except players use their feet to kick the ball and not their hands.

The sport has been around since the 15th century, with records *( SHOW )* that it was played by one of the royal families of the Malay region at that time.

The word ‘sepak’ is Malay for ‘kick’ and ‘takraw’ is Thai for ‘woven ball’; thus, the name of the sport literally means ‘kick ball’. The combination of these words from different languages represents a symbol of solidarity between two of the *( POWERFUL )* countries in the region.

        ''', reply_markup=markup, parse_mode="Markdown")
            bot.send_sticker(message.chat.id,
                             'CAACAgIAAxkBAAEG_sFjqCyJIsQq7SFM0Xxx9GGg7QRf6gACkQsAAtS-QEgFySl9f2kQuiwE',
                             reply_markup=markup1)

        elif message_text == "практика заданий 25-29":
            markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn2 = types.KeyboardButton("Вернуться к лексике и грамматике")
            btn3 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn2, btn3)
            markup = types.InlineKeyboardMarkup(row_width=2)
            first_button = types.InlineKeyboardButton(text="ответы", callback_data="answ1")
            second_button = types.InlineKeyboardButton(text="➡", callback_data="задание26")
            markup.add(first_button, second_button)
            bot.send_message(message.chat.id, '''A Typical Day

My job would probably rank as one of the most *( POPULAR )* but I really like it. I am an accountant and I work from 9 am until 6 pm (although it takes an hour by train to reach my office in The City).

People think that accountancy involves working all day long with numbers and that it is really boring. But they could not be more wrong. My work is exciting, challenging, varied and both personally and professionally rewarding. Being involved with the *( COMMERCE )* world is also, at times, really good fun.

I deal mainly with new, start-up businesses and typically I see about three clients *( DAY )*. Either I go out to their offices or they visit me and I often have lunch with a client. Over the years some of them have become friends and I know their wives and families.

The main task is to check their financial figures are correct and it is true that this part is tough work. But in *( ADD )* my job is to advise and help them.

Many new businesses have a rather *( ANXIETY )* time trying to build up customers and make profits. They are encouraged and even relieved when I explain to them that it is not normal to make profits immediately. It can take years before a business is functioning correctly.

Probably my biggest contribution is to advise them of the most efficient way to invest in their businesses.

Very often, a small change can make a big *( DIFFER )* in business. When they take my advice and I see a new company or business begin to succeed — it is really satisfying. I feel as if I was part of the success story and a member of their team.

        ''', reply_markup=markup, parse_mode="Markdown")
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG_sNjqCyYz3n8HiRrMd5ffqDDmPpjoQACdQADaQHUBdcDXQuvU456LAQ',
                             reply_markup=markup1)

        elif message_text == "практика заданий 30-36":
            markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn2 = types.KeyboardButton("Вернуться к лексике и грамматике")
            btn3 = types.KeyboardButton("Вернуться в начало")
            markup1.add(btn2, btn3)
            markup = types.InlineKeyboardMarkup(row_width=2)
            first_button = types.InlineKeyboardButton(text="ответы", callback_data="ответы30")
            second_button = types.InlineKeyboardButton(text="➡", callback_data="задание31")
            markup.add(first_button, second_button)
            bot.send_message(message.chat.id, '''E-mail is electronic mail, a *kind / method / system / opportunity* of sending messages via a computer to other users. It’s a wonderful new way of communicating! E-mail is cheaper than normal mail and even if you send your message *abroad / away / aside / alive* it only costs the same as a local telephone call. This is because your message
goes to computer called a mail server and then it is *traffic / translated / transmitted / transferred* across the Net via other mail servers to its destination.
E-mail is also much quicker and can arrive at most destinations in a minute. In fact, ordinary mail is so slow by comparison that Net users call it ‘snail mail’.
With e-mail you also have to know someone’s address and everyone on the Net has their own *people / personal / individual / men’s* e-mail address. An e-mail address has two main sections: the user’s name and the domain name. The user’s name is usually the name or nickname of the person using e-mail, for example ‘Paul’. This is *followed / gone / set / got* by the symbol @ which means ‘at’. Then there is the domain name which gives information about the computer, for example ‘home’, the type of *scope / form / organisation / way* , for example ‘com’, means a commercial and its location. So a complete e-mail address might look something like this: Paul@home.com.uk.
E-mail addresses can be *difficult / easy / simple / complicated* so write them down carefully. Then you will have the address at the top of their message and you can just press ‘reply’.''',
                             reply_markup=markup, parse_mode="Markdown")
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG_rljqCsLjiYOWyDPjzu_Nu85akKDtwACIwADXQWCFiBh-3UK1EC0LAQ',
                             reply_markup=markup1)

        elif message_text == "устная часть" or message_text == "вернуться к устной части":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton("Задание 1️⃣")
            btn2 = types.KeyboardButton("Задание 2️⃣")
            btn3 = types.KeyboardButton("Задание 3️⃣")
            btn4 = types.KeyboardButton("Задание 4️⃣")
            btn5 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2, btn3, btn4, btn5)
            bot.send_message(message.chat.id, '''Устная часть также называется *говорением*. Она состоит из четырех заданий:

🗣️ Чтение текста (проверка произношения) 📚

🗣️ Постановка прямых вопросов ❔

🗣️ Условное интервью 📸

🗣️ Сравнение фотографий ▶️''',
                             reply_markup=markup, parse_mode="Markdown")

        elif message_text == "задание 1️⃣":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.KeyboardButton("Вернуться к устной части")
            btn2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2)
            btn3 = types.InlineKeyboardButton(text='сайт для практики',
                                              url='https://tonail.com/егэ-чтение-отрывка-вслух/')
            btn4 = types.InlineKeyboardButton(text='сайт для практики',
                                              url='https://en-ege.sdamgia.ru/test?filter=all&category_id=48&sort=ids')
            markup1.add(btn3, btn4)
            bot.send_message(message.chat.id, '''📚 *Чтение вслух небольшого текста научно-популярного характера.*📚
             
Время на подготовку – 1,5 минуты.''', reply_markup=markup, parse_mode="Markdown")
            bot.send_message(message.chat.id, 'Ты можешь попрактиковаться там ⬇', reply_markup=markup1)

        elif message_text == "задание 2️⃣":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.KeyboardButton("Вернуться к устной части")
            btn2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2)
            btn3 = types.InlineKeyboardButton(text='сайт для практики',
                                              url='https://en-ege.sdamgia.ru/test?filter=all&category_id=52&sort=ids')
            markup1.add(btn3)
            bot.send_message(message.chat.id, '''❔ *Предлагается ознакомиться с рекламным объявлением и задать пять вопросов* (с 2022 г. – 4 вопроса) *на основе ключевых слов.*❔
             
Время на подготовку – 1,5 минуты.''', reply_markup=markup, parse_mode="Markdown")
            bot.send_message(message.chat.id, 'Ты можешь попрактиковаться там ⬇', reply_markup=markup1)

        elif message_text == "задание 3️⃣":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.KeyboardButton("Вернуться к устной части")
            btn2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2)
            btn3 = types.InlineKeyboardButton(text='сайт для практики',
                                              url='https://en-ege.sdamgia.ru/test?filter=all&category_id=55&sort=ids')
            markup1.add(btn3)
            bot.send_message(message.chat.id,
                             '''📸 Вам предлагается принять участие в условном *интервью*, ответив на *пять* вопросов.📸''',
                             reply_markup=markup, parse_mode="Markdown")
            bot.send_message(message.chat.id, 'Ты можешь попрактиковаться там ⬇', reply_markup=markup1)

        elif message_text == "задание 4️⃣":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            markup1 = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.KeyboardButton("Вернуться к устной части")
            btn2 = types.KeyboardButton("Вернуться в начало")
            markup.add(btn1, btn2)
            btn3 = types.InlineKeyboardButton(text='сайт для практики',
                                              url='https://en-ege.sdamgia.ru/test?filter=all&category_id=59&sort=ids')
            markup1.add(btn3)
            bot.send_message(message.chat.id,
                             '''▶️Тебе предстоит сделать *высказывание* – голосовое сообщение другу с рассказом на определенную тему *с опорой на две фотографии*.▶️''',
                             reply_markup=markup, parse_mode="Markdown")
            bot.send_message(message.chat.id, 'Ты можешь попрактиковаться там ⬇', reply_markup=markup1)

        else:
            bot.send_message(message.chat.id, "Я тебя не понял")
            bot.send_sticker(message.chat.id,
                             'CAACAgIAAxkBAAEH3ahj9027BmelBiSb-GPafFHDvG-lGQACcQ0AAgQyqEuhRb_JTgw56y4E')

    except:
        pass


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    def add_first_task(text_task, answers, next_task):
        keyboard = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="ответы", callback_data=f"{answers}")
        btn2 = types.InlineKeyboardButton(text="➡", callback_data=f"{next_task}")
        keyboard.add(btn1, btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'''{text_task}''',
                              reply_markup=keyboard, parse_mode="Markdown")

    def add_task(text_task, answers, next_task, previous_task):
        keyboard = types.InlineKeyboardMarkup()
        btn0 = types.InlineKeyboardButton(text="⬅", callback_data=f"{previous_task}")
        btn1 = types.InlineKeyboardButton(text="ответы", callback_data=f"{answers}")
        btn2 = types.InlineKeyboardButton(text="➡", callback_data=f"{next_task}")
        keyboard.add(btn0, btn1, btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'''{text_task}''',
                              reply_markup=keyboard, parse_mode="Markdown")

    def add_last_task(text_task, answers, previous_task):
        keyboard = types.InlineKeyboardMarkup()
        btn0 = types.InlineKeyboardButton(text="⬅", callback_data=f"{previous_task}")
        btn1 = types.InlineKeyboardButton(text="ответы", callback_data=f"{answers}")
        keyboard.add(btn0, btn1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'''{text_task}''',
                              reply_markup=keyboard, parse_mode="Markdown")

    def add_answer(answer_text, previous_grammar):
        keyboard = types.InlineKeyboardMarkup()
        btn2 = types.InlineKeyboardButton(text="Вернуться к заданию", callback_data=f"{previous_grammar}")
        keyboard.add(btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=answer_text,
                              reply_markup=keyboard, parse_mode="Markdown")

    try:
        if call.data == "to_2":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="to_1")
            btn2 = types.InlineKeyboardButton(text="➡", callback_data="to_3")
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''Для успешной сдачи аудирования нужно хорошо и быстро воспринимать английскую речь на слух 😱
        
Если вовремя начать подготовку, то без результата ты точно не останешься!😆''', reply_markup=keyboard)

        elif call.data == "to_1":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="to_3")
            btn2 = types.InlineKeyboardButton(text="➡", callback_data="to_2")
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''Аудирование состоит из трех типов заданий👂:
        
1⃣ прослушивание текстов и соотнесение их с утверждениями

2⃣ прослушивание диалога и определение степени соответствия утверждений данному диалогу

3⃣ прослушивание интервью и ответы на вопросы к нему
        ''', reply_markup=keyboard)

        elif call.data == "to_3":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="to_2")
            btn2 = types.InlineKeyboardButton(text="➡", callback_data="to_1")
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''*Пару советов для развития аудирования:*
    
😉 Слушай всё всегда и везде: смотри фильмы, слушайте музыку и подкасты на английском языке🎵

😉 При выполнении аудирования, *подчеркни ключевые слова*. Важно научиться воспринимать информацию и акцентировать внимание именно на тех моментах, о которых спрашивают

😉 *слушай два раза*
Когда ты слышишь текст впервые, ты успеваешь уловить только общий смысл. А значит, можешь пропустить какую-нибудь важную деталь или не расслышать отрицание в предложении и в результате - допустить ошибку 🥸

😉 *анализируй ошибки* 🤓
Если при практике ты допустил ошибку, открой тест и найди место, которое плохо понял. Найди в словаре незнакомые слова. Если нужно, проверь как они произносятся.''',
                                  parse_mode="Markdown", reply_markup=keyboard)

        elif call.data == "ege_ex_1_1":

            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="ответы", callback_data="ege_ex_1_1_answer")
            btn2 = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_1_2")
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''1. The speaker was glad when she/he was given more serious work to do.
                
2. The speaker learned nothing important at work.

3. The speaker did not want to take any responsibility.

4. The speaker didn’t mind doing a lot of things during work practice.

5. The speaker wants to do the same kind of work in the future.

6. The speaker has a different idea of the profession after completing the practice.

7. The speaker felt rather nervous before starting work.''', reply_markup=keyboard)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=(call.message.message_id + 1),
                                   media=types.InputMedia(type='audio',
                                                          media=(
                                                              'https://tonail.com/gia/ege/audirovaniye/audirovaniye_1_11.mp3')))

        elif call.data == "ege_ex_1_1_answer":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="задание", callback_data="ege_ex_1_1")
            btn2 = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_1_2")
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''A – 6
    
B – 4

C – 2

D – 7

E – 1

F – 5

Помни, что сам процесс обучения основан на ошибках. Так что не переживай, если что-то неправильно )''',
                                  reply_markup=keyboard)

        elif call.data == "ege_ex_1_2":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="ege_ex_1_1")
            btn2 = types.InlineKeyboardButton(text="ответы", callback_data="ege_ex_1_2_answer")
            btn3 = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_1_3")
            keyboard.add(btn1, btn2, btn3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''1. Writing Valentines has a very long history.
                
2. It’s another time to spend money.

3. Valentines make a big business.

4. There’s always something against the Day.

5. It’s a traditional Valentine’s Day present and no one should spare money for it.

6. Its traditions tend to fade.

7. Even journalists need information about Valentine’s Day.''', reply_markup=keyboard)

            bot.edit_message_media(chat_id=call.message.chat.id, message_id=(call.message.message_id + 1),
                                   media=types.InputMedia(type='audio',
                                                          media=(
                                                              'https://tonail.com/audio/gia/ege-audirovaniye_1_14.mp3')))

        elif call.data == "ege_ex_1_2_answer":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="ege_ex_1_1")
            btn2 = types.InlineKeyboardButton(text="задание", callback_data="ege_ex_1_2")
            btn3 = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_1_3")
            keyboard.add(btn1, btn2, btn3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''A – 2
    
B – 5

C – 1

D – 3

E – 4

F – 7

Помни, что сам процесс обучения основан на ошибках. Так что не переживай, если что-то неправильно )''',
                                  reply_markup=keyboard)

        elif call.data == "ege_ex_1_3":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="ege_ex_1_2")
            btn2 = types.InlineKeyboardButton(text="ответы", callback_data="ege_ex_1_3_answer")
            btn3 = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_1_4")
            keyboard.add(btn1, btn2, btn3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''1. The speaker wants to have own TV set.
                    
2. The speaker’s sorry about people’s unwillingness of getting art.

3. The speaker considers the art of entertainment is dying.

4. The speaker doesn’t like screen version.

5. The speaker hasn’t enough time for favourite occupation.

6. The speaker thinks it’s better to associate.

7. The speaker is disappointed at the absence of teens’ entertainment.''',
                                  reply_markup=keyboard)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=(call.message.message_id + 1),
                                   media=types.InputMedia(type='audio',
                                                          media=(
                                                              'https://tonail.com/audio/gia/ege-audirovaniye_1_20.mp3')))

        elif call.data == "ege_ex_1_3_answer":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="ege_ex_1_2")
            btn2 = types.InlineKeyboardButton(text="задание", callback_data="ege_ex_1_3")
            btn3 = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_1_4")
            keyboard.add(btn1, btn2, btn3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''A – 4
    
B – 6

C – 5

D – 7

E – 1

F – 2

Помни, что сам процесс обучения основан на ошибках. Так что не переживай, если что-то неправильно )''',
                                  reply_markup=keyboard)

        elif call.data == "ege_ex_1_4":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="ege_ex_1_3")
            btn2 = types.InlineKeyboardButton(text="ответы", callback_data="ege_ex_1_4_answer")
            btn3 = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_1_5")
            keyboard.add(btn1, btn2, btn3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''1. A perfect friend never gossips.
                    
2. A friend in need is a friend indeed.

3. A perfect friend is not always ideal.

4. True friends always share everything with us.

5. A true friend will never abandon you.

6. A perfect friend is always honest.

7. A true friend is the greatest of all blessings.''',
                                  reply_markup=keyboard)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=(call.message.message_id + 1),
                                   media=types.InputMedia(type='audio',
                                                          media=('https://tonail.com/audio/gia/116r625.mp3')))

        elif call.data == "ege_ex_1_4_answer":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="ege_ex_1_3")
            btn2 = types.InlineKeyboardButton(text="задание", callback_data="ege_ex_1_4")
            btn3 = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_1_5")
            keyboard.add(btn1, btn2, btn3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''A – 2
    
B – 6

С – 4

D – 1

E – 3

F – 5

Помни, что сам процесс обучения основан на ошибках. Так что не переживай, если что-то неправильно )''',
                                  reply_markup=keyboard)

        elif call.data == "ege_ex_1_5":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="ege_ex_1_4")
            btn2 = types.InlineKeyboardButton(text="ответы", callback_data="ege_ex_1_5_answer")
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''1. I respected the teacher because of his attitude to me.
        
2. I was fortunate enough to have great teachers at school.

3. My level of knowledge increased due to my favourite teacher.

4. I was bored by the teacher and the subject.

5. I was taught not to be afraid of stating my point of view.

6. I thought that the teacher was too strict to me.

7. I was humiliated by the attitude of my teacher.''',
                                  reply_markup=keyboard)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=(call.message.message_id + 1),
                                   media=types.InputMedia(type='audio',
                                                          media=('https://tonail.com/audio/gia/66r6y.mp3')))

        elif call.data == "ege_ex_1_5_answer":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="ege_ex_1_4")
            btn2 = types.InlineKeyboardButton(text="задание", callback_data="ege_ex_1_5")
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''A – 2
    
B – 5

С – 7

D – 3

E – 1

F – 4

Помни, что сам процесс обучения основан на ошибках. Так что не переживай, если что-то неправильно )''',
                                  reply_markup=keyboard)

        elif call.data == "reading_to_1":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="reading_to_3")
            btn2 = types.InlineKeyboardButton(text="➡", callback_data="reading_to_2")
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''*Чтение состоит из трех типов заданий:*

🧸 подбор заголовков к текстам (задание 10)

🧸 вставка в текст пропущенных фраз (задание 11)

🧸 чтение текста и ответы на вопросы к нему (задания 12-18)''', reply_markup=keyboard, parse_mode="Markdown")


        elif call.data == "reading_to_2":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="reading_to_1")
            btn2 = types.InlineKeyboardButton(text="➡", callback_data="reading_to_3")
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='''Во время выполнения всех трех заданий из раздела “Чтение” рекомендую не обращать внимание на незнакомые слова, *они итак встретятся*🥹. 
                                      
Если вокруг них сосредоточен основной смысл вопроса, *не паникуйте*, что не сможете дать правильный ответ, не зная этого слова. 😏 *Сможете*. 😏 Тексты ЕГЭ стараются построить так, чтобы по контексту можно было угадать значение непонятного выражения.🥳''',
                                  reply_markup=keyboard, parse_mode="Markdown")

        elif call.data == "reading_to_3":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="reading_to_2")
            btn2 = types.InlineKeyboardButton(text="➡", callback_data="reading_to_1")
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''*Пару советов для развития аудирования:*
                
🎀 Если ты не знаком с темой, о которой говорится в тексте, ❌ не впадай в панику. ❌ Для того, чтобы найти ответы в тексте, не нужно иметь специальных знаний;

🎀 Если тебе даны задания, в которых вместо пробелов нужно вставить фразы, *прочитай предложение до пропусков и после*. Постарайся ___догадаться___, что именно пропущено. Включи свое логическое мышление!

🎀 Не трать много времени на один какой-нибудь вопрос. Ты всегда сможешь *вернуться* к нему потом;

🎀 Сначала нужно прочитать *весь текст*, чтобы понять его смысл, т.к. как в чтении, как и в аудировании, могут быть использованы хитрые приемы;

🎀 Готовясь к ЕГЭ, *читай как можно больше текстов разных жанров и обогащай свою лексику*.''',
                                  parse_mode="Markdown", reply_markup=keyboard)

        elif call.data == "ege_ex_2_1":

            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="ответы", callback_data="ege_ex_2_1_answer")
            btn2 = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_2_2")
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''A) A lot of people went to Michaels photography exhibition.
    
B) Michael has paid for lessons in photography.

C) Michael is not fond of colour photography.

D) Denise doesn’t know how to use the camera on her phone.

E) Michael uses a camera phone to take a lot of photos.

F) Michael’s mum has stopped using traditional film.

G) Michael’s mum wants him to learn how to develop photos from film.''', reply_markup=keyboard)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=(call.message.message_id + 1),
                                   media=types.InputMedia(type='audio',
                                                          media=(
                                                              'https://tonail.com/audio/ege/interview2-7.mp3')))

        elif call.data == "ege_ex_2_1_answer":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="задание", callback_data="ege_ex_2_1")
            btn2 = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_2_2")
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''A)TRUE
    
B) FALSE

C) TRUE

D) FALSE

E) NOT STATED

F) TRUE

G) NOT STATED

Помни, что сам процесс обучения основан на ошибках. Так что не переживай, если что-то неправильно )''',
                                  reply_markup=keyboard)

        elif call.data == "ege_ex_2_2":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="ege_ex_2_1")
            btn2 = types.InlineKeyboardButton(text="ответы", callback_data="ege_ex_2_2_answer")
            btn3 = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_2_3")
            keyboard.add(btn1, btn2, btn3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''A) Jim hasn’t had a cold for a long time.
    
B) The last time Jim had a cold was when they were to visit aunt Emily.

C) Maggie bought the grapes for Jim at the nearest shop.

D) Being ill Jim hasn’t lost his appetite.

E) Jim tried to convince Maggie that his medicine was quite useless.

F) Jim preferred to read a newspaper because he doesn’t like detective stories.

G) Jim is fond of fishing.''', reply_markup=keyboard)

            bot.edit_message_media(chat_id=call.message.chat.id, message_id=(call.message.message_id + 1),
                                   media=types.InputMedia(type='audio',
                                                          media=(
                                                              'https://tonail.com/audio/gia/interview2-21.mp3')))

        elif call.data == "ege_ex_2_2_answer":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="ege_ex_2_1")
            btn2 = types.InlineKeyboardButton(text="задание", callback_data="ege_ex_2_2")
            btn3 = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_2_3")
            keyboard.add(btn1, btn2, btn3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''A) TRUE
    
B) FALSE

C) NOT STATED

D) TRUE

E) TRUE

F) FALSE

G) TRUE

Помни, что сам процесс обучения основан на ошибках. Так что не переживай, если что-то неправильно )''',
                                  reply_markup=keyboard)

        elif call.data == "ege_ex_2_3":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="ege_ex_2_2")
            btn2 = types.InlineKeyboardButton(text="ответы", callback_data="ege_ex_2_3_answer")
            btn3 = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_2_4")
            keyboard.add(btn1, btn2, btn3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''A) The transport Minister left his post because of the gossips
    
B) The Prime Minister opened the Conference on the Environment

C) A lot of working places for engineers will be opened in Wales.

D) The inflation process is slightly increasing nowadays

E) The dangerous criminal got away from the prison.

F) A racing pigeon saved on the board of the ship crossing the ocean

G) Finally the speaker tells the weather forecast.''',
                                  reply_markup=keyboard)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=(call.message.message_id + 1),
                                   media=types.InputMedia(type='audio',
                                                          media=(
                                                              'https://tonail.com/audio/gia/interview2-19.mp3')))

        elif call.data == "ege_ex_2_3_answer":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="ege_ex_2_2")
            btn2 = types.InlineKeyboardButton(text="задание", callback_data="ege_ex_2_3")
            btn3 = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_2_4")
            keyboard.add(btn1, btn2, btn3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''A) TRUE
    
B) NOT STATED

C) NOT STATED

D) FALSE

E) TRUE

F) TRUE

G) FALSE

Помни, что сам процесс обучения основан на ошибках. Так что не переживай, если что-то неправильно )''',
                                  reply_markup=keyboard)

        elif call.data == "ege_ex_2_4":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="ege_ex_2_3")
            btn2 = types.InlineKeyboardButton(text="ответы", callback_data="ege_ex_2_4_answer")
            btn3 = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_2_5")
            keyboard.add(btn1, btn2, btn3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''A) When we are telling a lie, it’s normal.
    
B) Lying is a way to persuade the other people

C) Lying is an essential part of many kinds of sport

D) Actors should be good at lying

E) Film makers try to deceive the audience

F) Sometimes it’s better to keep silence

G) Our life is possible without telling a lie.''',
                                  reply_markup=keyboard)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=(call.message.message_id + 1),
                                   media=types.InputMedia(type='audio',
                                                          media='https://tonail.com/audio/gia/interview2-16.mp3'))

        elif call.data == "ege_ex_2_4_answer":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="ege_ex_2_3")
            btn2 = types.InlineKeyboardButton(text="задание", callback_data="ege_ex_2_4")
            btn3 = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_2_5")
            keyboard.add(btn1, btn2, btn3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''A) TRUE
    
B) FALSE

C) TRUE

D) TRUE

E) TRUE

F) NOT STATED

G) FALSE

Помни, что сам процесс обучения основан на ошибках. Так что не переживай, если что-то неправильно )''',
                                  reply_markup=keyboard)

        elif call.data == "ege_ex_2_5":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="ege_ex_2_4")
            btn2 = types.InlineKeyboardButton(text="ответы", callback_data="ege_ex_2_5_answer")
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''A) Matthew is good at cooking.
    
В) Jill wants to cook something simple.

С) Matthew’s grandmother is an immigrant.

D) In Jill’s family, soup is a common dish.

E) Matthew prefers Hungarian cuisine to French.

F) Jill will have to buy special equipment to make Hungarian soup.

G) Jill has decided what soup to cook.''',
                                  reply_markup=keyboard)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=(call.message.message_id + 1),
                                   media=types.InputMedia(type='audio',
                                                          media='https://tonail.com/audio/gia/interview4e1031.mp3'))

        elif call.data == "ege_ex_2_5_answer":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="ege_ex_2_4")
            btn2 = types.InlineKeyboardButton(text="задание", callback_data="ege_ex_2_5")
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''A) NOT STATED
    
В) TRUE

С) TRUE

D) FALSE

E) NOT STATED

F) FALSE

G) FALSE

Помни, что сам процесс обучения основан на ошибках. Так что не переживай, если что-то неправильно )''',
                                  reply_markup=keyboard)

        elif call.data == "ege_ex_3_1":

            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="ответы", callback_data="ege_ex_3_1_answer")
            btn2 = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_3_2")
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''1. What is true about the art in Karen’s gallery?
1) Nothing in the basement was undamaged.
2) Most of the art on the main floor was undamaged.
3) Some basement collections were undamaged.

2. Some of the damaged paintings in Karen’s basement can be repaired …
1) by Karen herself.
2) by experts.
3) by the artists.

3. Which option does Karen prefer for recovering the cost of the art?
1) Repairing it and selling it at a discount.
2) Waiting for her insurance company to pay in full.
3) Asking the artists to claim on their insurance.

4. An artist that Karen knows …
1) luckily had her work insured.
2) will need two years to repair the damage.
3) couldn’t afford insurance.

5. What happened to some public works of art?
1) They were damaged in the storm.
2) They were completely lost in the storm.
3) They were placed under protective material.

6. The institute for art conservation …
1) was extremely busy round the time of the storm.
2) received flood damage as a result of the storm.
3) was physically removing structures from art centres.

7. What does Karen hope will result from the storm?
1) The art world will help communities rebuild.
2) Artists may draw inspiration from the storms effect.
3) People will value art more highly.''', reply_markup=keyboard)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=(call.message.message_id + 1),
                                   media=types.InputMedia(type='audio',
                                                          media=(
                                                              'https://tonail.com/audio/ege/interview-4.mp3')))

        elif call.data == "ege_ex_3_1_answer":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="задание", callback_data="ege_ex_3_1")
            btn2 = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_3_2")
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''1 – 3

2 – 2

3 – 2

4 – 3

5 – 3

6 – 1

7 – 2

Помни, что сам процесс обучения основан на ошибках. Так что не переживай, если что-то неправильно )''',
                                  reply_markup=keyboard)

        elif call.data == "ege_ex_3_2":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="ege_ex_3_1")
            btn2 = types.InlineKeyboardButton(text="ответы", callback_data="ege_ex_3_2_answer")
            btn3 = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_3_3")
            keyboard.add(btn1, btn2, btn3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''1. The idea of becoming a photographer
1) came to Chris after seeing big sculptures.
2) was the result of his work with sculptures.
3) made him lose interest in sculptures.

2.Chris assisted the photographer who
1) had the latest photographic equipment.
2) gave Chris valuable professional advice.
3) used to ask Chris challenging questions.

3. According to Chris, working as an assistant is a good way into a career because you can
1) get a better understanding of the profession.
2) learn the basic techniques of taking pictures.
3) make friends with a lot of talented people.

4. The reason for buying a plastic camera was that it
1) allowed him to take original pictures.
2) was not very expensive.
3) was light to carry around.

5. Chris uses the phrase “That got the ball rolling” to say that
1) he became popular with the dancers.
2) he suddenly got very rich.
3) his art became more dance-oriented.

6. Chris goes to the dance performances because
1) the choreographer recommends him to see the piece.
2) it is always interesting for him to be at the premiere.
3) he wants to find the links between them and his work.

7. Chris thinks that dancers are great to work with because they
1) are lively and enthusiastic.
2) can cope with any problem.
3) can work long hours.
''', reply_markup=keyboard)

            bot.edit_message_media(chat_id=call.message.chat.id, message_id=(call.message.message_id + 1),
                                   media=types.InputMedia(type='audio',
                                                          media='https://tonail.com/audio/ege/interview-8.mp3'))

        elif call.data == "ege_ex_3_2_answer":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="ege_ex_3_1")
            btn2 = types.InlineKeyboardButton(text="задание", callback_data="ege_ex_3_2")
            btn3 = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_3_3")
            keyboard.add(btn1, btn2, btn3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''1 – 2

2 – 2

3 – 1

4 – 1

5 – 3

6 – 3

7 – 1

Помни, что сам процесс обучения основан на ошибках. Так что не переживай, если что-то неправильно )''',
                                  reply_markup=keyboard)

        elif call.data == "ege_ex_3_3":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="ege_ex_3_2")
            btn2 = types.InlineKeyboardButton(text="ответы", callback_data="ege_ex_3_3_answer")
            btn3 = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_3_4")
            keyboard.add(btn1, btn2, btn3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''1. What’s the main role of English in India according to the speaker?
1) Connecting India with the rest of the world.
2) Enabling communication between the country peoples.
3) Serving as the language of Indian Mass Media.

2. Which of the following is TRUE about Indian English?
1) It is similar to Australian English.
2) It exists only in local newspapers
3) It has specific features in grammar as well as in vocabulary and phonetics.

3. What, according to the speaker, partly explains the specifics of Indian English?
1) Structure of local languages.
2) Indian history and culture.
3) Education traditions in India.

4. Which of the following is mentioned as a grammatical feature of Indian English?
1) Overuse of the definite article.
2) Use of a plural form of a certain word in relation to a single object.
3) Avoiding use of progressive tense.

5. Which of the following phrases is used in Indian English for “How can I help you?”?
1) Hello, what do you want?
2) Tell me…
3) Where are you put up?

6. What does the speaker say about the language of Indian teenagers?
1) It consists of slang mostly.
2) It’s devised to confuse older people.
3) It makes Indian English more modem.

7. What is the basic direction of changes in modem Indian English according to the speaker?
1) Simplification.
2) Purification.
3) Localization.''',
                                  reply_markup=keyboard)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=(call.message.message_id + 1),
                                   media=types.InputMedia(type='audio',
                                                          media=(
                                                              'https://tonail.com/audio/gia/interview-12.mp3')))

        elif call.data == "ege_ex_3_3_answer":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="ege_ex_3_2")
            btn2 = types.InlineKeyboardButton(text="задание", callback_data="ege_ex_3_3")
            btn3 = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_3_4")
            keyboard.add(btn1, btn2, btn3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''1 – 2

2 – 3

3 – 1

4 – 2

5 – 2

6 – 3

7 – 1

Помни, что сам процесс обучения основан на ошибках. Так что не переживай, если что-то неправильно )''',
                                  reply_markup=keyboard)

        elif call.data == "ege_ex_3_4":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="ege_ex_3_3")
            btn2 = types.InlineKeyboardButton(text="ответы", callback_data="ege_ex_3_4_answer")
            btn3 = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_3_5")
            keyboard.add(btn1, btn2, btn3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''1. Since her win, Daisy has been …
1) enjoying time off with her family.
2) meeting her fans.
3) answering questions about it.

2. The competition is for…
1) amateur chefs
2) chefs from regional cities.
3) trainee chefs.

3. Daisy believes she succeeded because …
1) she was most concerned with the taste of the food.
2) she cooked her own favourites for the show
3) she combined tasty and health-giving foods.

4. When Daisy was given the unusual foods, she …
1) cooked them more than once.
2) broke the rules of the contest.
3) failed to meet her usual standards.

5. Daisy decided to create a pizza using …
1) meat.
2) fish.
3) fruit.

6. The problem with one of Daisy’s starters was the
1) temperature.
2) presentation.
3) seasoning.

7. For the future, Daisy is most interested in …
1) working with other successful people from the show.
2) improving her skills in the kitchen even more.
3) having a career in culinary publishing.''',
                                  reply_markup=keyboard)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=(call.message.message_id + 1),
                                   media=types.InputMedia(type='audio',
                                                          media=('https://tonail.com/audio/gia/interview-2311.mp3')))

        elif call.data == "ege_ex_3_4_answer":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="ege_ex_3_3")
            btn2 = types.InlineKeyboardButton(text="задание", callback_data="ege_ex_3_4")
            btn3 = types.InlineKeyboardButton(text="➡", callback_data="ege_ex_3_5")
            keyboard.add(btn1, btn2, btn3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''1 – 3

2 – 1

3 – 1

4 – 3

5 – 2

6 – 1

7 – 3

Помни, что сам процесс обучения основан на ошибках. Так что не переживай, если что-то неправильно )''',
                                  reply_markup=keyboard)

        elif call.data == "ege_ex_3_5":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="ege_ex_3_4")
            btn2 = types.InlineKeyboardButton(text="ответы", callback_data="ege_ex_3_5_answer")
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''1. Algae is
1) out of control.
2) highly concentrated.
3) a plant-like creature.

2. Red tides are
1) always the same colour.
2) many different colours.
3) never colourless.

3. Water pollution is
1) a natural phenomenon.
2) caused by humans.
3) increased by algae.

4. High levels of nitrates and phosphates in the ocean
1) kill algae.
2) encourage the growth of algae.
3) are common in unpolluted waters.

5. Red tides that produce toxins
1) kill off fish.
2) must not be fished in.
3) can cause death in humans.

6. The term ‘algal bloom’
1) is unpopular with scientists.
2) is popular with the public.
3) refers to red tides.

7. When asked where red tides occur, Dr Samuel says they are
1) rare in freshwater bodies.
2) common near shorelines.
3) an exclusively marine phenomenon.''',
                                  reply_markup=keyboard)
            bot.edit_message_media(chat_id=call.message.chat.id, message_id=(call.message.message_id + 1),
                                   media=types.InputMedia(type='audio',
                                                          media=('https://tonail.com/audio/gia/interview-7541.mp3')))

        elif call.data == "ege_ex_3_5_answer":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="ege_ex_3_4")
            btn2 = types.InlineKeyboardButton(text="задание", callback_data="ege_ex_3_5")
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''1 – 3

2 – 2

3 – 2

4 – 2

5 – 2

6 – 3

7 – 2

Помни, что сам процесс обучения основан на ошибках. Так что не переживай, если что-то неправильно )''',
                                  reply_markup=keyboard)

        elif call.data == "grammar3":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="grammar1")
            btn2 = types.InlineKeyboardButton(text="➡", callback_data="grammar1")
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''*Несколько общих советов по выполнению:*

🥸 Читать *весь* текст, потому что подсказка о грамматической форме может быть не в этом *конкретном* предложении, а в предыдущем. Или в следующем.

✅ Если вы правильно определили *форму*, позаботьтесь ещё её правильным написанием. При *корявой* орфографии не зачтут. *Проверьте еще раз.*

✍ Если не понимаете, напишите хоть что-нибудь, мало ли.''', reply_markup=keyboard, parse_mode="Markdown")
        elif call.data == "grammar1":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="grammar3")
            btn2 = types.InlineKeyboardButton(text="➡", callback_data="grammar3")
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''*Лексика* и *грамматика* состоит из *трех* типов заданий:

😊 грамматическая трансформация (грамматическое преобразования, *изменение* грамматической формы)

🗣️ лексическая трансформация (лексическое преобразование, *образование* нового однокоренного слова)

📨 *вставка* в текст пропущенных слов
                                                                                                                    ''',
                                  reply_markup=keyboard, parse_mode="Markdown")
        elif call.data == "grammar_2539answ":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="Вернуться к заданию", callback_data="grammar2539back")
            keyboard.add(btn1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''Sepak takraw

Have you heard of sepak takraw? It’s a sport in Southeast Asia which *IS PLAYED* like volleyball, except players use their feet to kick the ball and not their hands.

The sport has been around since the 15th century, with records *SHOWING* that it was played by one of the royal families of the Malay region at that time.

The word ‘sepak’ is Malay for ‘kick’ and ‘takraw’ is Thai for ‘woven ball’; thus, the name of the sport literally means ‘kick ball’. The combination of these words from different languages represents a symbol of solidarity between two of the *MOST POWERFUL* countries in the region.

        ''',
                                  reply_markup=keyboard, parse_mode="Markdown")
        elif call.data == "grammar2539back":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="ответы", callback_data="grammar_2539answ")
            btn2 = types.InlineKeyboardButton(text="➡", callback_data="grammarnext1")
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''Sepak takraw

Have you heard of sepak takraw? It’s a sport in Southeast Asia which *( PLAY )* like volleyball, except players use their feet to kick the ball and not their hands.

The sport has been around since the 15th century, with records *( SHOW )* that it was played by one of the royal families of the Malay region at that time.

The word ‘sepak’ is Malay for ‘kick’ and ‘takraw’ is Thai for ‘woven ball’; thus, the name of the sport literally means ‘kick ball’. The combination of these words from different languages represents a symbol of solidarity between two of the *( POWERFUL )* countries in the region.

        ''',
                                  reply_markup=keyboard, parse_mode="Markdown")
        elif call.data == "grammar_2539answ2":
            keyboard = types.InlineKeyboardMarkup()
            btn2 = types.InlineKeyboardButton(text="Вернуться к заданию", callback_data="grammarnext1")
            keyboard.add(btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''Michelle’s big night

Michelle was quite nervous about her performance in the school play. She thought she would feel *BETTER*, though, if her brother Frank came to see to the show.

She asked him, even begged him to be there, *THINKING* he might just say yes but then not turn up. ‘I promise you, Michelle. I’ll be sitting in the front row from the beginning to the end of the play.’

On the night of the show, Michelle did wonderfully. As a show of support, her brother clapped the *LOUDEST* of everyone in the theatre.

        ''',
                                  reply_markup=keyboard, parse_mode="Markdown")
        elif call.data == "grammar_2539answ3":
            keyboard = types.InlineKeyboardMarkup()
            btn2 = types.InlineKeyboardButton(text="Вернуться к заданию", callback_data="grammarnext2")
            keyboard.add(btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''Bad day

Eugene wasn’t having a good day. First, while he was pouring coffee into his mug at home in the morning, his hand slipped and he accidentally *SPILT (можно SPILLED)* coffee all over the kitchen worktop.

He went to wipe up the spill with a sponge and knocked the mug onto the floor, where it broke into several pieces. Upset and *FRUSTRATED*, he left home without having any coffee at all.

At work, he ran into a colleague, literally, and nearly knocked her over. ‘I’m so sorry, Michelle. Are you OK?’ he said quickly. She wasn’t amused and told him to watch where he *WAS GOING*.

He *COULD NOT (можно COULDN’T)* wait for the dav to end, and iust as it did, he realised he had a report to finish. ‘What a terrible day. I should have stayed in bed this morning!’ he said, as he prepared to stay late at work.

        ''',
                                  reply_markup=keyboard, parse_mode="Markdown")
        elif call.data == "grammar_2539answ4":
            keyboard = types.InlineKeyboardMarkup()
            btn2 = types.InlineKeyboardButton(text="Вернуться к заданию", callback_data="grammarnext3")
            keyboard.add(btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''City of Westminster

The City of Westminster is the borough of London that contains Buckingham Palace, the Houses of Parliament and the Prime Minister’s residence. It is located on the northern banks of the River Thames in the centre of London, and it’s one of the *MOST EXPENSIVE* places to live in the UK.

The borough is of great historical interest, and almost four fifths of *ITS* buildings are part of a designated conservation area.

Of all the tourists that visit London, approximately 95% of them tour the City of Westminster, which *ACCOUNTS* for about 28 million visitors each year.

Other sites within the borough are Piccadilly Circus, Kensington Gardens, the headquarters of many global corporations and several renowned learning institutes. The borough has 27 tube stations and IS *CONNECTED* to south London by seven bridges.
        ''',
                                  reply_markup=keyboard, parse_mode="Markdown")
        elif call.data == "grammar_2539answ5":
            keyboard = types.InlineKeyboardMarkup()
            btn2 = types.InlineKeyboardButton(text="Вернуться к заданию", callback_data="grammarnext4")
            keyboard.add(btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''VIDEO GAMES
Like the television set before it. the video game console is now *TAKING* over living rooms in the US.

Americans spend *MORE MONEY* on video games than on movies and nearly half the country plays.

The first video game, Pong, *WAS INVENTED* in 1972.

Since then, video games *HAVE BECOME* ‘the major cultural activity of the generation aged 30 and below’, according to James Paul Gee, a professor of education.

They have the same importance to this generation that movies had for *EARLIER* generations,’ he says.

‘Even *THOSE* children who can’t understand the lessons they are taught in their schools can discuss the stories in video games at a very sophisticated level,’ he says.

But in some *PEOPLE’S* opinion, many of the games are much too violent and they have a bad effect on the brain.''',
                                  reply_markup=keyboard, parse_mode="Markdown")
        elif call.data == "grammar_2539answ6":
            add_answer("""*Imperial Porcelain Factory*

The Imperial Porcelain Factory has been making fine porcelain in Russia for centuries. The factory, founded in 1744, was Empress Elizabeth’s idea with the aim of *CREATING* ceramic art.

After Empress Elizabeth, consecutive monarchs kept the factory busy with orders and allowed it to produce the *FINEST* quality porcelain and ceramic plates, vases, tea sets and the like.

In the 1940s, the factory began to produce its famous cobalt net pattern, which consisted of intersecting lines of deep blue forming a geometric pattern on a white background. The edges of the dishes *WERE HIGHLIGHTED* in exquisite 22-karat gold.
        """, 'grammarnext5')

        elif call.data == "grammar_2539answ7":
            add_answer("""*FOSTERING*

Foster families are very important. Some *CHILDREN* are unable to live with their parents for various reasons. Foster families give them a home.

The child usually stays with the family for a limited amount of time, unlike adoption, which is permanent. The family *CHOSEN* to look after a child is trained to deal with any problems that may come up.

Although it is not always the case, the child often develops a very close relationship with *THEIR* foster family. This relationship can be very important to the person as they grow up.

*JOHN DALTON*

The scientist John Dalton, born in 1766, was colour blind. He *COULD NOT* tell the difference between red and green.

He was the first researcher to write about the condition, and it *IS CALLED* Daltonism sometimes even today because of that.

However, that was not his only contribution to science.

Dalton believed that matter is composed of atoms and that chemical reactions involve rearranging but not destroying atoms. *THINKING* these atoms were like hard spheres, he got a friend to make wooden models.
These were the *EARLIEST* models of atoms, and you can still see them today at the Science Museum in London.""",
                       'grammarnext6')
        elif call.data == "ответы26":
            add_answer('''*Manchester*

Manchester is a city in England. Its population is about 530 thousand people. The *LOCAL* authority is Manchester City Council.

The history of Manchester began with the *ROMANS*. They built a fort there. It was established about 20 centuries ago.

In 2014, Manchester was ranked as a beta world city, the highest — *RANKED* British city apart from London.

After London and Edinburgh Manchester is the third city in the UK that people choose to visit. It is known for its architecture, music, sports clubs, culture, transport *CONNECTIONS* and a lot more. Moreover, the world’s first inter-city passenger railway station was built there.

*Cambridge*

Cambridge is a university city. It is situated on the River Cam which is approximately 80 km north of London. The population of the city is about 125 thousand people and the fifth part of it consists of students and there are almost no *UNEMPLOYED* people living in the city.

Everyone knows that this city is home to the University of Cambridge that was founded in 1209. The university has one of the largest legal deposit libraries in the world. The skyline of Cambridge is arrayed by several college *BUILDINGS*, a church, a hospital and a chapel tower.''',
                       'задание26')

        elif call.data == "grammarnext1":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="ответы", callback_data="grammar_2539answ2")
            btn2 = types.InlineKeyboardButton(text="➡", callback_data="grammarnext2")
            btn0 = types.InlineKeyboardButton(text="⬅", callback_data="grammar2539back")
            keyboard.add(btn0, btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''Michelle’s big night

Michelle was quite nervous about her performance in the school play. She thought she would feel *( GOOD )* , though, if her brother Frank came to see to the show.

She asked him, even begged him to be there, *( THINK )* he might just say yes but then not turn up. ‘I promise you, Michelle. I’ll be sitting in the front row from the beginning to the end of the play.’

On the night of the show, Michelle did wonderfully. As a show of support, her brother clapped the *( LOUD )* of everyone in the theatre.

''',
                                  reply_markup=keyboard, parse_mode="Markdown")
        elif call.data == "grammarnext2":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="ответы", callback_data="grammar_2539answ3")
            btn2 = types.InlineKeyboardButton(text="➡", callback_data="grammarnext3")
            btn0 = types.InlineKeyboardButton(text="⬅", callback_data="grammarnext1")
            keyboard.add(btn0, btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''Bad day

Eugene wasn’t having a good day. First, while he was pouring coffee into his mug at home in the morning, his hand slipped and he accidentally *( SPILL )* coffee all over the kitchen worktop.

He went to wipe up the spill with a sponge and knocked the mug onto the floor, where it broke into several pieces. Upset and *( FRUSTRATE )*, he left home without having any coffee at all.

At work, he ran into a colleague, literally, and nearly knocked her over. ‘I’m so sorry, Michelle. Are you OK?’ he said quickly. She wasn’t amused and told him to watch where he *( GO )*.

He *( CAN NOT )* wait for the dav to end, and iust as it did, he realised he had a report to finish. ‘What a terrible day. I should have stayed in bed this morning!’ he said, as he prepared to stay late at work.

''',
                                  reply_markup=keyboard, parse_mode="Markdown")
        elif call.data == "grammarnext3":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="ответы", callback_data="grammar_2539answ4")
            btn2 = types.InlineKeyboardButton(text="➡", callback_data="grammarnext4")
            btn0 = types.InlineKeyboardButton(text="⬅", callback_data="grammarnext2")
            keyboard.add(btn0, btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''City of Westminster

The City of Westminster is the borough of London that contains Buckingham Palace, the Houses of Parliament and the Prime Minister’s residence. It is located on the northern banks of the River Thames in the centre of London, and it’s one of the *( EXPENSIVE )* places to live in the UK.

The borough is of great historical interest, and almost four fifths of *( IT )* buildings are part of a designated conservation area.

Of all the tourists that visit London, approximately 95% of them tour the City of Westminster, which *( ACCOUNT )* for about 28 million visitors each year.

Other sites within the borough are Piccadilly Circus, Kensington Gardens, the headquarters of many global corporations and several renowned learning institutes. The borough has 27 tube stations and *( CONNECT )* to south London by seven bridges.

''',
                                  reply_markup=keyboard, parse_mode="Markdown")
        elif call.data == "grammarnext4":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="ответы", callback_data="grammar_2539answ5")
            btn2 = types.InlineKeyboardButton(text="➡", callback_data="grammarnext5")
            btn0 = types.InlineKeyboardButton(text="⬅", callback_data="grammarnext3")
            keyboard.add(btn0, btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='''VIDEO GAMES
Like the television set before it. the video game console is now *( TAKE )* over living rooms in the US.

Americans spend *( MONEY )* on video games than on movies and nearly half the country plays.

The first video game, Pong, *( INVENT )* in 1972.

Since then, video games *( BECOME )* ‘the major cultural activity of the generation aged 30 and below’, according to James Paul Gee, a professor of education.

They have the same importance to this generation that movies had for *( EARLY )* generations,’ he says.

‘Even *( THAT )* children who can’t understand the lessons they are taught in their schools can discuss the stories in video games at a very sophisticated level,’ he says.

But in some *( PEOPLE )* opinion, many of the games are much too violent and they have a bad effect on the brain.

        ''',
                                  reply_markup=keyboard, parse_mode="Markdown")

        elif call.data == "grammarnext5":
            add_task('''Imperial Porcelain Factory

The Imperial Porcelain Factory has been making fine porcelain in Russia for centuries. The factory, founded in 1744, was Empress Elizabeth’s idea with the aim of *( CREATE )* ceramic art.

After Empress Elizabeth, consecutive monarchs kept the factory busy with orders and allowed it to produce the *( FINE )* quality porcelain and ceramic plates, vases, tea sets and the like.

In the 1940s, the factory began to produce its famous cobalt net pattern, which consisted of intersecting lines of deep blue forming a geometric pattern on a white background. The edges of the dishes *( HIGHLIGHT )* in exquisite 22-karat gold.

''', 'grammar_2539answ6', 'grammarnext6', 'grammarnext4')

        elif call.data == "grammarnext6":
            add_last_task('''FOSTERING

Foster families are very important. Some *( CHILD )* are unable to live with their parents for various reasons. Foster families give them a home.

The child usually stays with the family for a limited amount of time, unlike adoption, which is permanent. The family *( CHOOSE )* to look after a child is trained to deal with any problems that may come up.

Although it is not always the case, the child often develops a very close relationship with *( THEY )* foster family. This relationship can be very important to the person as they grow up.

JOHN DALTON

The scientist John Dalton, born in 1766, was colour blind. He *( NOT CAN )* tell the difference between red and green.

He was the first researcher to write about the condition, and it *( CALL )* Daltonism sometimes even today because of that.

However, that was not his only contribution to science.

Dalton believed that matter is composed of atoms and that chemical reactions involve rearranging but not destroying atoms. *( THINK )* these atoms were like hard spheres, he got a friend to make wooden models.
These were the *( EARLY )* models of atoms, and you can still see them today at the Science Museum in London.''',
                          'grammar_2539answ7', 'grammarnext5')

        elif call.data == "answ1":
            add_answer('''*A Typical Day*

My job would probably rank as one of the most *UNPOPULAR* but I really like it. I am an accountant and I work from 9 am until 6 pm (although it takes an hour by train to reach my office in The City).

People think that accountancy involves working all day long with numbers and that it is really boring. But they could not be more wrong. My work is exciting, challenging, varied and both personally and professionally rewarding. Being involved with the *COMMERCIAL* world is also, at times, really good fun.

I deal mainly with new, start-up businesses and typically I see about three clients *DAILY*. Either I go out to their offices or they visit me and I often have lunch with a client. Over the years some of them have become friends and I know their wives and families.

The main task is to check their financial figures are correct and it is true that this part is tough work. But in *ADDITION* my job is to advise and help them.

Many new businesses have a rather *ANXIOUS* time trying to build up customers and make profits. They are encouraged and even relieved when I explain to them that it is not normal to make profits immediately. It can take years before a business is functioning correctly.

Probably my biggest contribution is to advise them of the most efficient way to invest in their businesses.

Very often, a small change can make a big *DIFFERENCE* in business. When they take my advice and I see a new company or business begin to succeed — it is really satisfying. I feel as if I was part of the success story and a member of their team.''',
                       'start_25_29')
        elif call.data == "start_25_29":
            add_first_task('''A Typical Day

My job would probably rank as one of the most *( POPULAR )* but I really like it. I am an accountant and I work from 9 am until 6 pm (although it takes an hour by train to reach my office in The City).

People think that accountancy involves working all day long with numbers and that it is really boring. But they could not be more wrong. My work is exciting, challenging, varied and both personally and professionally rewarding. Being involved with the *( COMMERCE )* world is also, at times, really good fun.

I deal mainly with new, start-up businesses and typically I see about three clients *( DAY ). Either I go out to their offices or they visit me and I often have lunch with a client. Over the years some of them have become friends and I know their wives and families.

The main task is to check their financial figures are correct and it is true that this part is tough work. But in *( ADD )* my job is to advise and help them.

Many new businesses have a rather *( ANXIETY )* time trying to build up customers and make profits. They are encouraged and even relieved when I explain to them that it is not normal to make profits immediately. It can take years before a business is functioning correctly.

Probably my biggest contribution is to advise them of the most efficient way to invest in their businesses.

Very often, a small change can make a big *( DIFFER )* in business. When they take my advice and I see a new company or business begin to succeed — it is really satisfying. I feel as if I was part of the success story and a member of their team.

''', 'answ1', 'задание26')
        elif call.data == "задание26":
            add_task('''Manchester

Manchester is a city in England. Its population is about 530 thousand people. The *( LOCALITY )* authority is Manchester City Council.

The history of Manchester began with the *( ROME )*. They built a fort there. It was established about 20 centuries ago.

In 2014, Manchester was ranked as a beta world city, the highest — *( RANK )* British city apart from London.

After London and Edinburgh Manchester is the third city in the UK that people choose to visit. It is known for its architecture, music, sports clubs, culture, transport *( CONNECT ) *and a lot more. Moreover, the world’s first inter-city passenger railway station was built there.

Cambridge

Cambridge is a university city. It is situated on the River Cam which is approximately 80 km north of London. The population of the city is about 125 thousand people and the fifth part of it consists of students and there are almost no *( EMPLOY )* people living in the city.

Everyone knows that this city is home to the University of Cambridge that was founded in 1209. The university has one of the largest legal deposit libraries in the world. The skyline of Cambridge is arrayed by several college* ( BUILD )*, a church, a hospital and a chapel tower.

''', 'ответы26', 'задание27', "задание25")

        # 27

        elif call.data == "задание27":
            add_task('''

The need for change in our *( DAY )* lives and the movements of our government is the and growing. 

Because so many *( DIFFER )* fa ctors come into play; voting, governmental issues, desire to stick to routine, many people don’t consider that what they do will affect future generations.

If humans continue moving forward in such a *( HARM )* way towards the future, then there will be no future to consider. 

Although it’s true that we cannot physically stop our ozone layer from *( THIN )* (and scientists are still having trouble figuring out what is causing it exactly,) there are still so many things we can do to try put a dent in what we already know. 

By raising *( AWARE )* in your local community and within your families about these issues, you can help contribute to a more Environmentally conscious and *( FRIEND )* place for you to live.''',
                     'ответы27', 'задание28', "задание26")


        elif call.data == "ответы27":
            add_answer("""

The need for change in our *DAILY* lives and the movements of our government is the and growing.

Because so many *DIFFERENT* factors come into play; voting, governmental issues, desire to stick to routine, many people don’t consider that what they do will affect future generations.

If humans continue moving forward in such a *HARMFUL* way towards the future, then there will be no future to consider.

Although it’s true that we cannot physically stop our ozone layer from *THINNING* (and scientists are still having trouble figuring out what is causing it exactly,) there are still so many things we can do to try put a dent in what we already know.

By raising *AWARENESS* in your local community and within your families about these issues, you can help contribute to a more Environmentally conscious and *FRIENDLY* place for you to live.""",
                       'задание27')

        # 28

        elif call.data == "задание28":
            add_task('''*THE BRITISH AND THE ENVIRONMENT*

Air quality in London has improved since the *( INTRODUCE )* of the congestion charge, which makes people pay to take their cars into central London.

After decades of being driven away by pollution, *( CREATE )* such as otters which used to be endangered species are returning to British rivers.

‘The British are realising that their day-to-day *( CHOOSE )* have an impact on the environment.

And they are realising that these things directly *( EFFECT )* their families’ health,’ says recycling campaigner Georgina Bloomfield from the organisation Friends of the Earth.

So more and more British people are washing out jam jars and putting them in recycling bins or writing to local *( POLITICS )* about the environment.

It seems that most British people want to make a *( DIFFERENT )* – and that’s exactly what they’re doing.
        ''', 'ответы28', 'задание29', "задание27")


        elif call.data == "ответы28":
            add_answer("""*THE BRITISH AND THE ENVIRONMENT*

Air quality in London has improved since the *INTRODUCTION* of the congestion charge, which makes people pay to take their cars into central London.

After decades of being driven away by pollution, *CTREATURES* such as otters which used to be endangered species are returning to British rivers.

‘The British arc realising that their day-to-day *CHOICES* have an impact on the environment.

And they are realising that these things directly *AFFECT* their families’ health,’ says recycling campaigner Georgina Bloomfield from the organisation Friends of the Earth.

So more and more British people are washing out jam jars and putting them in recycling bins or writing to local *POLITICIANS* about the environment.

It seems that most British people want to make a *DIFFERENCE* – and that’s exactly what they’re doing.
        """, 'задание28')

        # 30

        elif call.data == "задание29":
            add_last_task('''*Computer Addiction*

Excessive computer use can become really *(ADDICT)*. And it doesn’t only mean playing computer games.

Wireless connection to the Internet has brought the world closer to people making them to *(GRADUAL)* withdraw into an artificial world of communication.

Lots of young people find virtual reality more attractive than their everyday lives. This of course leads to *(DESIRABLE)* effects.

Teenagers become irresponsible in their everyday lives. Computer addiction makes them neglect school work and their everyday *(RESPONSIBLE)*.

Computer addicts become isolated, anti-social and *(CAPABLE)* of dealing with each other directly.

Their lives become *(AIM)* without going online to check their email or to chat, and they become totally dependent on their computers.
        ''', 'ответы29', 'задание28')

        elif call.data == "ответы29":
            add_answer("""*Computer Addiction*

Excessive computer use can become really *ADDICTIVE*. And it doesn’t only mean playing computer games.

Wireless connection to the Internet has brought the world closer to people making them to *GRADUALLY* withdraw into an artificial world of communication.

Lots of young people find virtual reality more attractive than their everyday lives. This of course leads to *UNDESIRABLE* effects.

Teenagers become irresponsible in their everyday lives. Computer addiction makes them neglect school work and their everyday *RESPONSIBLITIES*.

Computer addicts become isolated, anti-social and *INCAPABLE* of dealing with each other directly.

Their lives become *AIMLESS* without going online to check their email or to chat, and they become totally dependent on their computers.
                """, 'задание29')

        elif call.data == "ответы30":
            add_answer("""*E-mail*

E-mail is electronic mail, a *METHOD* of sending messages via a computer to other users.

It’s a wonderful new way of communicating! E-mail is cheaper than normal mail and even if you send your message *ABROAD* it only costs the same as a local telephone call. This is because your message goes to computer called a mail server and then it is *TRANSFERRED* across the Net via other mail servers to its destination.

E-mail is also much quicker and can arrive at most destinations in a minute.

In fact, ordinary mail is so slow by comparison that Net users call it ‘snail mail’.

With e-mail you also have to know someone’s address and everyone on the Net has their own *PERSONAL* e-mail address.

An e-mail address has two main sections: the user’s name and the domain name.The user’s name is usually the name or nickname of the person using e-mail, for example ‘Paul’.

This is *FOLLOWED* by the symbol @ which means ‘at’. Then there is the domain name which gives information about the computer, for example ‘home’, the type of *ORGANISATIONS* , for example ‘com’, means a commercial and its location. So a complete e-mail address might look something like this: Paul@home.com.uk.

E-mail addresses can be *COMPLICATED* so write them down carefully.

Then you will have the address at the top of their message and you can just press ‘reply’.""",
                       'задание31')

        # 31

        elif call.data == "задание31":
            add_task('''In the family business

Working with my father is in many ways a blessing; I don’t have to climb my way up the career ladder and I have guaranteed job security. But it’s also harder than working elsewhere, because I have more to prove. He’s the best businessman I know, and one day I’ll have to fill his big *BOOTS / TRAINERS / SHOES / SLIPPERS*.

I help my father run Tropifresh, a fruit and vegetable wholesaler at New Market in London, which my dad started in 1983. I was 25 when I decided *TO ENJOY / TO CONTACT / TO CONNECT / TO JOIN* the family business. After completing my geography degree at University College London in 2011, I worked in PR for a while and worked part-time for my father to earn some much-needed money. I eventually went on some business trips with him, where I realized I would love to give it a try. Father was actually surprised — at one point he warned me *AGAINST / OPPOSITE / FROM / OUT OF* it, simply because of the *STRONG / LONG / BIG / LARGE* hours and hard work.

A lot of my job involves developing the website — skills my father, as an old-school trader, does not have — so he trusts me with it. My father and I are a good team; we’re able to *DO / WALK / MAKE / TAKE* a compromise, we rarely argue. We know each other inside out, and it helps greatly.

I hope to take *UP / ON / AWAY / OVER* Tropifresh one day. My loyalty is to the business, rather than my father. All of my friends have gone into more traditional jobs, such as medicine or accounting. But I’ve always known I wanted to be self-employed and the opportunity to expand the business is *AMUSING / AMAZING / AMUSED / AMAZED*!

''', 'ответы31', 'задание32', "задание30")

        elif call.data == "ответы31":
            add_answer("""In the family business

Working with my father is in many ways a blessing; I don’t have to climb my way up the career ladder and I have guaranteed job security. But it’s also harder than working elsewhere, because I have more to prove. He’s the best businessman I know, and one day I’ll have to fill his big *SHOES*.

I help my father run Tropifresh, a fruit and vegetable wholesaler at New Market in London, which my dad started in 1983. I was 25 when I decided *TO JOIN* the family business. After completing my geography degree at University College London in 2011, I worked in PR for a while and worked part-time for my father to earn some much-needed money. I eventually went on some business trips with him, where I realized I would love to give it a try. Father was actually surprised — at one point he warned me *AGAINST* it, simply because of the *LONG* hours and hard work.

A lot of my job involves developing the website — skills my father, as an old-school trader, does not have — so he trusts me with it. My father and I are a good team; we’re able to *MAKE* a compromise, we rarely argue. We know each other inside out, and it helps greatly.

I hope to take *OVER* Tropifresh one day. My loyalty is to the business, rather than my father. All of my friends have gone into more traditional jobs, such as medicine or accounting. But I’ve always known I wanted to be self-employed and the opportunity to expand the business is *AMAZING*!
        """, 'задание31')

        # 32

        elif call.data == "задание32":
            add_task('''Virtual teacher

Eurotalk is a London-based company that makes language-learning software. *SUBSEQUENTLY / INCREASINGLY / RESPECTIVELY / RECENTLY*, their Onebillion project has been in the news, especially since their maths learning app for children in the Republic of Malawi (Africa) was shown to improve learning. It turned out that children using the app tripled their knowledge of maths *FOR / IN / OVER / AT* just eight weeks.

The name Onebillion *ARRIVES / DEPARTS / COMES / GOES* from the goal of reaching one billion children. This is more or less the number of children who don’t have the opportunity to learn basic skills. Primary education has been free in Malawi since 1994, and the one million increase in student enrolment has put *PRESSURE / WEIGHT / DIFFICULTY / FORCE* on teachers, classrooms and resources.

Children are put in groups of 30 or even 60 and taken to a special classroom to spend 30 minutes every other day with the device. One tablet device can be used by ten or twelve children each day. Each Oneclass is managed by an international volunteer and there is a virtual teacher guiding the student through the app. All of the children in Oneclass are learning at their own pace.

The apps are designed to be as culturally friendly as possible. The project works closely with the education ministry in Malawi to *DO / MAKE / APPEAR / EMERGE* sure there are no cultural misunderstandings.

The project is funded by people in wealthier countries who buy their own language version of the app. Every single penny that the company earns from selling those apps goes towards developing literacy material in Malawi. The key to the success of the app is how it takes *CHANCE / OPPORTUNITY / BENEFIT / ADVANTAGE* of the enthusiasm of young children to learn. The children are like sponges, they absorb so much information at this age and this is why they are getting *SUCH / THAT / SO / WHAT* a good learning result
        ''', 'ответы32', 'задание33', "задание31")

        elif call.data == "ответы32":
            add_answer("""Virtual teacher

Eurotalk is a London-based company that makes language-learning software. *RECENTLY*, their Onebillion project has been in the news, especially since their maths learning app for children in the Republic of Malawi (Africa) was shown to improve learning. It turned out that children using the app tripled their knowledge of maths *IN* just eight weeks.

The name Onebillion *COMES* from the goal of reaching one billion children. This is more or less the number of children who don’t have the opportunity to learn basic skills. Primary education has been free in Malawi since 1994, and the one million increase in student enrolment has put *PRESSURE* on teachers, classrooms and resources.

Children are put in groups of 30 or even 60 and taken to a special classroom to spend 30 minutes every other day with the device. One tablet device can be used by ten or twelve children each day. Each Oneclass is managed by an international volunteer and there is a virtual teacher guiding the student through the app. All of the children in Oneclass are learning at their own pace.

The apps are designed to be as culturally friendly as possible. The project works closely with the education ministry in Malawi to *MAKE* sure there are no cultural misunderstandings.

The project is funded by people in wealthier countries who buy their own language version of the app. Every single penny that the company earns from selling those apps goes towards developing literacy material in Malawi. The key to the success of the app is how it takes *ADVANTAGE* of the enthusiasm of young children to learn. The children are like sponges, they absorb so much information at this age and this is why they are getting *SUCH* a good learning result
        """, 'задание32')

        # 33

        elif call.data == "задание33":
            add_task('''*Globalization and Communication Growth*


The 21st century has *STARTED / BEGAN / USHERED / LAUNCHED* in a new era in man’s ongoing quest for a better life and a better world. For the first time in history, we can now claim to live in ‘One World.’ Globalization has removed many of the gaps that have existed between and among nations. While the physical divide is still present, the *CAUSE / IMPACT / CONSEQUENCES / RESULT* of the Information Highway on how we communicate and live in the present day is simply staggering. Rapid improvements in information technology have allowed us to exchange information and communicate almost everywhere, anywhere, and anytime.


Globalization, as a general term, is best understood as the spread of ideas about the environment, democracy, human rights, and less complicated issues like fashion and fads. Global exchange is now taking place as the market of ideas, culture, and beliefs expand through the use of technology. The nature of business and how it is done has also improved by *BONDS / GAPS / JUMPS / LEAPS* and bounds because of globalization.


An example of the remarkable effects of globalization is the invention of the telephone and the television. Television has enabled young people and adults to have the ability to share cultural and ethnic experiences with others. Telephones have also greatly improved communication. Gone are the weeks and even months of waiting for a letter. Anybody can talk to anyone who has another phone *REGARDLESS / DESPITE / NOTWITHSTANDING / BECAUSE* of distance or location on the planet. With the aid of satellites, 3rd generation phones allow us to make a phone call, send a video, or even receive an e-mail. These *BREAKBEATS / BREAKDOWNS / BREAKOUTS / BREAKTHROUGHS* in communication have revolutionized business, commerce, and even the personal lives and relationships of millions of people.


Because of the electronic media, vast amounts of important information can reach any parts of the globe in *ANY / NO / NONE OF / SOME* time. Business establishments, whether big or small, are using the Internet in many ways to build or expand their company’s growth. With the ever improving technology come new markets, high *ACCESS / CLAIM / DEMAND / RISE* for products, and also greater competition. Making investments in information and communication technology is now a must for any business enterprise.
        ''', 'ответы33', 'задание34', "задание32")

        elif call.data == "ответы33":
            add_answer("""*Globalization and Communication Growth*

The 21st century has *USHERED* in a new era in man’s ongoing quest for a better life and a better world. For the first time in history, we can now claim to live in ‘One World.’ Globalization has removed many of the gaps that have existed between and among nations. While the physical divide is still present, the *IMPACT* of the Information Highway on how we communicate and live in the present day is simply staggering. Rapid improvements in information technology have allowed us to exchange information and communicate almost everywhere, anywhere, and anytime.

Globalization, as a general term, is best understood as the spread of ideas about the environment, democracy, human rights, and less complicated issues like fashion and fads. Global exchange is now taking place as the market of ideas, culture, and beliefs expand through the use of technology. The nature of business and how it is done has also improved by *LEAPS* and bounds because of globalization.

An example of the remarkable effects of globalization is the invention of the telephone and the television. Television has enabled young people and adults to have the ability to share cultural and ethnic experiences with others. Telephones have also greatly improved communication. Gone are the weeks and even months of waiting for a letter. Anybody can talk to anyone who has another phone *REGARDLESS* of distance or location on the planet. With the aid of satellites, 3rd generation phones allow us to make a phone call, send a video, or even receive an e-mail. These *BREAKTHROUGHS* in communication have revolutionized business, commerce, and even the personal lives and relationships of millions of people.

Because of the electronic media, vast amounts of important information can reach any parts of the globe in *NO* time. Business establishments, whether big or small, are using the Internet in many ways to build or expand their company’s growth. With the ever improving technology come new markets, high *DEMAND* for products, and also greater competition. Making investments in information and communication technology is now a must for any business enterprise.
        """, 'задание33')

        # 34

        elif call.data == "задание34":
            add_task('''Luck

About forty years ago I was an instructor in the military academy at Woolwich. I was present in one of the sections when young Scoresby *UNDERTOOK / UNDERSCORED / UNDERSTOOD / UNDERWENT* his preliminary examination. I was touched to the quick with pity because the rest of the class answered up brightly and handsomely while he didn’t know anything, so to speak. All the compassion in me was aroused in his behalf. I understood that when he came to be examined again, he would be flung over, so it would be simply a harmless act of *CHARITY / CRUELTY / LOYALTY / BRAVERY* to ease his fall as much as I could.

I took him aside, and found that he knew a little of Caesar’s history; and as he didn’t know anything else, I went to work and drilled him like a galley slave on a certain line of stock questions concerning Caesar which I knew would be used. You won’t believe me but he went through with flying *MARKS / GRADES / COLOURS / BANNERS* on examination day! He went through on that purely superficial ‘cram,’ and got compliments too, while others, who knew a thousand times more than he, got plucked. *UNDER / IN / WITH / BY* some strangely lucky accident, he was asked no question outside of the narrow limits of his drill.

It was stupefying. Now of course the thing that would *FIND / EXPOSE / DENOUNCE / INJURE* him and kill him at last was mathematics. I *SUGGESTED / SETTLED / SOLVED / RESOLVED* to make his death as easy as I could. So I drilled him and crammed him just on the line of questions which the examiners would be most likely to use, and then launched him on his fate. Well, try to *CONCEIVE / IMAGINE / PREDICT / FORTELL* of the result: to my consternation, he took the first prize! And with it he got a perfect ovation in the way of compliments.
        ''', 'ответы34', 'задание35', "задание33")

        elif call.data == "ответы34":
            add_answer("""Luck

About forty years ago I was an instructor in the military academy at Woolwich. I was present in one of the sections when young Scoresby *UNDERWENT* his preliminary examination. I was touched to the quick with pity because the rest of the class answered up brightly and handsomely while he didn’t know anything, so to speak. All the compassion in me was aroused in his behalf. I understood that when he came to be examined again, he would be flung over, so it would be simply a harmless act of *CHARITY* to ease his fall as much as I could.

I took him aside, and found that he knew a little of Caesar’s history; and as he didn’t know anything else, I went to work and drilled him like a galley slave on a certain line of stock questions concerning Caesar which I knew would be used. You won’t believe me but he went through with flying *COLOURS* on examination day! He went through on that purely superficial ‘cram,’ and got compliments too, while others, who knew a thousand times more than he, got plucked. *BY* some strangely lucky accident, he was asked no question outside of the narrow limits of his drill.

It was stupefying. Now of course the thing that would *EXPOSE* him and kill him at last was mathematics. I *RESOLVED* to make his death as easy as I could. So I drilled him and crammed him just on the line of questions which the examiners would be most likely to use, and then launched him on his fate. Well, try to *CONCEIVE* of the result: to my consternation, he took the first prize! And with it he got a perfect ovation in the way of compliments.
        """, 'задание34')

        # 35

        elif call.data == "задание35":
            add_task('''The Guest

‘The landscape seen from our windows is certainly charming,’ said Annabel; ‘those cherry orchards and green meadows, and the river winding along the valley. However, nothing ever happens here. Rather dreadful, isn’t it?’

‘On the *CONTRAST / CONTRARY / INSIDE / OPPOSITE*,’ said Matilda, ‘I find it soothing and restful; but then, you see, I’ve lived in countries where things do happen, especially when you’re not ready for them happening all at once.’

‘That, of course, makes a *STATEMENT / SPLASH / MOVE / DIFFERENCE*,’ said Annabel.

‘I’ll never forget,’ said Matilda, ‘the occasion when the Bishop of Bequar *PAID / SENT / MADE / GAVE* us an unexpected visit.’

‘I thought that out there you were always prepared for emergency guests turning *TO / OVER / UP / IN*,’ said Annabel.

‘I was quite prepared for half a dozen Bishops,’ said Matilda, ‘but it was rather disconcerting to find out that this particular one was a distant cousin of mine, belonging to a branch of the family that had quarrelled bitterly and offensively with our branch about a Crown Derby dessert service. To make *ISSUES / MATTERS / PROBLEMS / SITUATION* worse, my husband was away, talking sense to a village community that believed one of their leading men was a were-tiger.’

‘A what tiger?’

‘A were-tiger; you’ve heard of were-wolves, haven’t you, a mixture of wolf and human being and demon? Well, in those parts they have were-tigers, or think they have, and I must say that in this case they had every ground for thinking so. However, as we gave *IN / UP / AWAY / OUT* witchcraft prosecutions about three hundred years ago, we don’t like to have other people keeping up our discarded practices.’

‘I hope you weren’t unkind to the Bishop,’ said Annabel.

‘Well, of course he was my guest, so I had to be outwardly polite to him, but he was tactless enough to rake up the incidents of the old quarrel, and from that moment we were scarcely on speaking *CONDITIONS / RELATIONSHIPS / RELATIONS / TERMS*.

''', 'ответы35', 'задание36', "задание34")

        elif call.data == "ответы35":
            add_answer("""The Guest

‘The landscape seen from our windows is certainly charming,’ said Annabel; ‘those cherry orchards and green meadows, and the river winding along the valley. However, nothing ever happens here. Rather dreadful, isn’t it?’

‘On the *CONTRARY*,’ said Matilda, ‘I find it soothing and restful; but then, you see, I’ve lived in countries where things do happen, especially when you’re not ready for them happening all at once.’

‘That, of course, makes a *DIFFERENCE*,’ said Annabel.

‘I’ll never forget,’ said Matilda, ‘the occasion when the Bishop of Bequar *PAID* us an unexpected visit.’

‘I thought that out there you were always prepared for emergency guests turning *UP*,’ said Annabel.

‘I was quite prepared for half a dozen Bishops,’ said Matilda, ‘but it was rather disconcerting to find out that this particular one was a distant cousin of mine, belonging to a branch of the family that had quarrelled bitterly and offensively with our branch about a Crown Derby dessert service. To make *MATTERS* worse, my husband was away, talking sense to a village community that believed one of their leading men was a were-tiger.’

‘A what tiger?’

‘A were-tiger; you’ve heard of were-wolves, haven’t you, a mixture of wolf and human being and demon? Well, in those parts they have were-tigers, or think they have, and I must say that in this case they had every ground for thinking so. However, as we gave *UP* witchcraft prosecutions about three hundred years ago, we don’t like to have other people keeping up our discarded practices.’

‘I hope you weren’t unkind to the Bishop,’ said Annabel.

‘Well, of course he was my guest, so I had to be outwardly polite to him, but he was tactless enough to rake up the incidents of the old quarrel, and from that moment we were scarcely on speaking *TERMS*.
        """, 'задание35')

        # 36

        elif call.data == "задание36":
            add_last_task('''Squirrel

It was when Squirrel Nutkin appeared at the October Board meeting that Mr. Ramsay began to *ACQUIRE / ENQUIRE / INQUIRE / REQUIRE* his reputation for eccentricity. And that's putting it *MILD / MILDER / MILDEST / MILDLY*.To be fair, there were people who said at the time that there was nothing wrong in wearing a glove puppet to a Board meeting. However, there were more who disagreed, and several who thought that Mr. Ramsay was off his chump. The matter was hotly disputed in the company's offices, on the shop floor, in the canteen.

It happened during Mr. Giles's monthly overlong summary of the company's financial position. Two factors were making the prospects for Ramsay & Co look bleak.

The first of these factors spoke for itself. There were simply fewer items of hosiery being sold. Whether this was due to the long hot summer combined with the undoubted increase *AT / IN / OF / TO* the uptake of feminine trousers, or it was a sign of continued recession was not for him to say. Ramsay & Co simply had to *COMMENT / COPE / DEAL / FACE* the facts, whether they liked them or not, and accept what the market was telling them. Reality didn't always turn *IN / ON / OUT / UP* the way people wanted it to.

The second factor, however, was where they could do something about. Ramsay & Co's costs were inordinately high compared to those of its competitors, who had been cutting back on staff over the last five years, reducing their workforce to one-fifth of its previous level. It was high *PRICE / MOMENT / TIME / WAY* that Ramsay & Co got itself into a similar position.

None of the Board members was surprised at what Mr. Giles had to say. He had, after all, said it all before, many times, over the past several months. Mr. Ramsay had, until now, always stubbornly resisted him. This time, though, what happened was different from all the previous occasions. Mr. Ramsay had never before produced a glove puppet from underneath the table. He had never had a squirrel sitting on his left hand during a presentation.

The only two pairs of eyes in the room focused on Mr. Giles during his summation of the company's position were those of Mr. Ramsay and the squirrel, both of whom were shaking their heads very slightly. The other Board members were sitting shocked with their mouths wide open and were *WATCHING / STARING / SEEING / OBSERVING* at the puppet.
        ''', 'ответы36', 'задание35')

        elif call.data == "ответы36":
            add_answer("""Squirrel

It was when Squirrel Nutkin appeared at the October Board meeting that Mr. Ramsay began to *ACQUIRE* his reputation for eccentricity. And that's putting it *MILDLY*.To be fair, there were people who said at the time that there was nothing wrong in wearing a glove puppet to a Board meeting. However, there were more who disagreed, and several who thought that Mr. Ramsay was off his chump. The matter was hotly disputed in the company's offices, on the shop floor, in the canteen.

It happened during Mr. Giles's monthly overlong summary of the company's financial position. Two factors were making the prospects for Ramsay & Co look bleak.

The first of these factors spoke for itself. There were simply fewer items of hosiery being sold. Whether this was due to the long hot summer combined with the undoubted increase *IN* the uptake of feminine trousers, or it was a sign of continued recession was not for him to say. Ramsay & Co simply had to *FACE* the facts, whether they liked them or not, and accept what the market was telling them. Reality didn't always turn *OUT* the way people wanted it to.

The second factor, however, was where they could do something about. Ramsay & Co's costs were inordinately high compared to those of its competitors, who had been cutting back on staff over the last five years, reducing their workforce to one-fifth of its previous level. It was high *TIME* that Ramsay & Co got itself into a similar position.

None of the Board members was surprised at what Mr. Giles had to say. He had, after all, said it all before, many times, over the past several months. Mr. Ramsay had, until now, always stubbornly resisted him. This time, though, what happened was different from all the previous occasions. Mr. Ramsay had never before produced a glove puppet from underneath the table. He had never had a squirrel sitting on his left hand during a presentation.

The only two pairs of eyes in the room focused on Mr. Giles during his summation of the company's position were those of Mr. Ramsay and the squirrel, both of whom were shaking their heads very slightly. The other Board members were sitting shocked with their mouths wide open and were *STARING* at the puppet.
        """, 'задание36')
        elif call.data == 'writing2':
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="writing1")
            btn2 = types.InlineKeyboardButton(text="➡", callback_data="writing3")
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='''Письмо состоит из *двух* типов заданий:

1️⃣ написание письма *личного* характера

2️⃣ написание *эссе* (сочинения)''',
                                  reply_markup=keyboard, parse_mode="Markdown")
        elif call.data == 'writing3':
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="Эссе Задание 38",
                                              url='https://youtu.be/K0at8-uWUnE')

            btn2 = types.InlineKeyboardButton(text="Личное электронное письмо",
                                              url='http://ege-oge-english.ru/letter-ege/')
            keyboard.add(btn1, btn2)
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="writing2")

            btn2 = types.InlineKeyboardButton(text="➡", callback_data="writing1")

            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='''📺Для *подробной* разборки этих заданий, советуем посмотреть пару *видео* и *сайтов*''',
                                  reply_markup=keyboard, parse_mode="Markdown")
        elif call.data == 'writing1':
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="⬅", callback_data="writing3")
            btn2 = types.InlineKeyboardButton(text="➡", callback_data="writing2")
            keyboard.add(btn1, btn2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='''

💌 Для выполнения заданий этого раздела потренируйтесь различать *нейтральный* и *неофициальный* стили.

📝 Например, в эссе *нельзя* использовать *well, actually, anyway*: это *informal words*.

🥇 Здесь требуется *индивидуальная* подготовка.''',
                                  reply_markup=keyboard, parse_mode="Markdown")

    except:
        pass
        # bot.send_message(call.message.chat.id, 'что-то пошло не так')


@bot.message_handler(content_types=['sticker'])
def start(message: Message):
    try:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEH3b9j90_ku2aRgBicfC7B9AAB28C_aVkAAtMBAALb-vQ4njtkDFtchnMuBA')

    except:
        pass


@bot.message_handler(content_types=['voice'])
def start(message: Message):
    try:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEH3c1j91IXJ9VVfN0sZV7Uy3gWO0svCgACGAkAAlwCZQPIbUU60LzB3i4E')
        bot.send_message(message.chat.id, 'Классно прикольно, однако я не распознаю голосовые сообщения((')

    except:
        pass


bot.polling()
