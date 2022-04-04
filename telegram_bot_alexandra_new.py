#подключение библиотек для телеграмм бота
from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters

#библиотека для запросов о погоде
import requests
#токен телеграмм-бота
bot_token = '5240414154:AAE0UH3m9VNEFpRToHhuYBLDmB-ZBIBiI60'

lang_text='ru'
city_text='Moscow'
#создание бота
#https://habr.com/ru/post/262247/
bot = Bot(bot_token)
#обработчик команд
updater = Updater(bot_token, use_context=True)
#ответ на запросы пользователя
dispatcher = updater.dispatcher


def start(update,context):
    global lang_text
    if lang_text == 'ru':
        context.bot.send_message(update.effective_chat.id, 'Привет! Волнует что за окном? 😉 \n'+
                             '/weather - погода сейчас 🌡️ \n'+
                                 '/clothes - что надеть \n '+
                            '/city - выбор города 🏙 \n'+
                             '/lang - выбор языка 🧏 \n')
    elif lang_text == 'en':
        context.bot.send_message(update.effective_chat.id, 'Hi! Worried about what is outside the window? 😉 \n'+
                             '/weather - weather now 🌡️ \n'+
                                '/clothes - what to wear \n '+
                            '/city - city selection \n'+
                             '/lang - language selection \n')
    elif lang_text == 'de':
        context.bot.send_message(update.effective_chat.id, 'Hallo! Besorgt darüber, was sich außerhalb des Fensters befindet? 😉 \n'+
                             '/weather - wetter jetzt 🌡️ \n'+
                                 '/clothes - was man anziehen soll \n '+
                            '/city - Städteauswahl \n'+
                             '/lang - Sprachauswahl \n')
#подпрограмма для старта бота
def lang(update, context):
    keyboard = [
        [InlineKeyboardButton("Русский", callback_data='1'), InlineKeyboardButton("English", callback_data='2')],
        [InlineKeyboardButton("Deutsch", callback_data='3')]]
    #context.bot.send_message(update.effective_chat.id, "Привет! Волнует что за окном? :-)")
    update.message.reply_text('Смена языка', reply_markup=InlineKeyboardMarkup(keyboard))
def russian():
    global lang_text
    lang_text = 'ru'
def english():
    global lang_text
    lang_text = 'en'
def deutsch():
    global lang_text
    lang_text = 'de'


def clothes(update, context):
    global lang_text
    global city_text
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city_text+'&appid=b81c955812292d68b40fa34cea554708&units=metric&lang='+lang_text)
    response2 = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=55&lon=37&exclude=hourly&appid=b81c955812292d68b40fa34cea554708&units=metric&lang="+lang_text)
    temp = response.json()['main']
    temp = temp['temp']
    temp_like = response.json()['main']
    temp_like = temp_like['feels_like']
    humidity = response.json()['main']
    humidity = humidity['humidity']
    wind= response.json()['wind']
    wind = wind['speed']
    if lang_text == 'ru':
        if temp>0 and temp <5:
            update.message.reply_text('Сегодня можно без шапки, но советую взять с собой шарф)')
        if temp>5 and temp <10:
            update.message.reply_text('Всё еще думаешь о шарфе с шапкой? Забудь! Тепло же))')
        if temp>-10 and temp <0:
            update.message.reply_text('Уже забыл о шарфе и шапке? Быстро одевай, а то заболеешь! 🥶')
        if temp>10 and temp <15:
            update.message.reply_text('Смело одевай толстовку с желеткой и иди гулять!')
        if temp>15 and temp<20:
            update.message.reply_text('Одевай что-нибудь потеплее, сейчас не так уж и тепло')
        if temp>20:
            update.message.reply_text('Ура, уже тепло! Но не забудь одеть кепку.')
        if temp<-10:
            update.message.reply_text('Твоя мама попросила напомнить тебе, чтобы ты не забыл одеть подштанники! 😂')
    if lang_text == 'en':
        if temp>0 and temp <5:
            update.message.reply_text('Today you can go without a hat, but I advise you to take a scarf with you')
        if temp>5 and temp <10:
            update.message.reply_text('Still thinking about a scarf with a hat? Forget it! Its warm)')
        if temp>-10 and temp <0:
            update.message.reply_text('Have you already forgotten about the scarf and hat? Get dressed quickly, or you will get sick 🥶')
        if temp>10 and temp <15:
            update.message.reply_text('Feel free to put on a hoodie with a vest and go for a walk!)')
        if temp>15 and temp<20:
            update.message.reply_text('Wear something warmer, it is not that warm right now')
        if temp>20:
            update.message.reply_text('Hooray, it is already warm! But do not forget to wear a cap.')
        if temp<-10:
            update.message.reply_text('Your mom asked me to remind you not to forget to put on your underpants! 😂')
    if lang_text == 'de':
        if temp>0 and temp <5:
            update.message.reply_text('Heute können Sie ohne Mütze, aber ich rate Ihnen, einen Schal mitzunehmen')
        if temp>5 and temp <10:
            update.message.reply_text('Denkst du immer noch an den Schal mit der Mütze? Vergiss es! Wärme ist gleich)')
        if temp>-10 and temp <0:
            update.message.reply_text('Hast du den Schal und die Mütze vergessen? Zieh dich schnell an, sonst wirst du krank 🥶')
        if temp>10 and temp <15:
            update.message.reply_text('Zieh ein Sweatshirt mit einer Weste an und geh spazieren!)')
        if temp>15 and temp<20:
            update.message.reply_text('Zieh etwas Wärmeres an, jetzt ist es nicht so warm')
        if temp>20:
            update.message.reply_text('Hurra, es ist warm! Aber vergiss nicht, deine Mütze anzuziehen.')
        if temp<-10:
            update.message.reply_text('Deine Mutter hat dich gebeten, dich daran zu erinnern, dass du nicht vergisst, die Unterhosen anzuziehen. 😂')

    


#клавиатура услуг
def city(update, context):
    global lang_text
    if lang_text=='ru':
        keyboard = [
        [InlineKeyboardButton("Москва", callback_data='4'), InlineKeyboardButton("Санкт-Петербург", callback_data='5')],
        [InlineKeyboardButton("Сочи", callback_data='5'), InlineKeyboardButton("Краснодар", callback_data='6')],
        [InlineKeyboardButton("Казань", callback_data='7'), InlineKeyboardButton("Екатерибург", callback_data='8')],
        [InlineKeyboardButton("Красноярск", callback_data='9'), InlineKeyboardButton("Владивосток", callback_data='10')]
        ]
    if lang_text=='en':
        keyboard = [
        [InlineKeyboardButton("Moscow", callback_data='4'), InlineKeyboardButton("St. Petersburg", callback_data='5')],
        [InlineKeyboardButton("Sochi", callback_data='5'), InlineKeyboardButton("Krasnodar", callback_data='6')],
        [InlineKeyboardButton("Kazan", callback_data='7'), InlineKeyboardButton("Ekaterinburg", callback_data='8')],
        [InlineKeyboardButton("Krasnoyarsk", callback_data='9'), InlineKeyboardButton("Vladivostok", callback_data='10')]
        ]
    if lang_text=='de':
        keyboard = [
        [InlineKeyboardButton("Moskau", callback_data='4'), InlineKeyboardButton("St. Petersburg", callback_data='5')],
        [InlineKeyboardButton("Sotschi", callback_data='5'), InlineKeyboardButton("Krasnodar", callback_data='6')],
        [InlineKeyboardButton("Kasan", callback_data='7'), InlineKeyboardButton("Jekaterinburg", callback_data='8')],
        [InlineKeyboardButton("Krasnojarsk", callback_data='9'), InlineKeyboardButton("Wladiwostok", callback_data='10')]
        ]
    update.message.reply_text('Город', reply_markup=InlineKeyboardMarkup(keyboard))


def button(update, context):
    global city_text
    query = update.callback_query
    query.answer()
    if query.data == "1":
        russian()
        context.bot.send_message(update.effective_chat.id, 'Язык сменили на русский' )
        context.bot.send_message(update.effective_chat.id, 'Привет! Волнует что за окном? 😉 \n'+
                             '/weather - погода сейчас 🌡️ \n'+
                                 '/clothes - что надеть \n '+
                            '/city - выбор города 🏙️ \n'+
                             '/lang - выбор языка 🧏 \n')
    elif query.data == "2":
        english()
        context.bot.send_message(update.effective_chat.id, 'Language is english')
        context.bot.send_message(update.effective_chat.id, 'Hi! Worried about what is outside the window? 😉 \n'+
                             '/weather - weather now 🌡️ \n'+
                                 '/clothes - what to wear \n '+
                            '/city - city selection 🏙️ \n'+
                             '/lang - language selection 🧏 \n')
    elif query.data == "3":
        deutsch()
        context.bot.send_message(update.effective_chat.id, 'Sprache deutsch')
        context.bot.send_message(update.effective_chat.id, 'Hallo! Besorgt darüber, was sich außerhalb des Fensters befindet? 😉 \n'+
                             '/weather - wetter jetzt 🌡️ \n'+
                                '/clothes - was man anziehen soll \n '+
                            '/city - Städteauswahl 🏙️ \n'+
                             '/lang - Sprachauswahl 🧏 \n')
    elif query.data == "4":
        city_text = 'Moscow'
        if lang_text == 'ru':
            context.bot.send_message(update.effective_chat.id, 'Привет! Волнует что за окном? 😉 \n'+
                             '/weather - погода сейчас 🌡️ \n'+
                            '/clothes - что надеть \n '+
                            '/city - выбор города 🏙 \n'+
                             '/lang - выбор языка 🧏 \n')
        elif lang_text == 'en':
            context.bot.send_message(update.effective_chat.id, 'Hi! Worried about what is outside the window? 😉 \n'+
                             '/weather - weather now 🌡️ \n'+
                            '/clothes - what to wear \n '+       
                            '/city - city selection \n'+
                             '/lang - language selection \n')
        elif lang_text == 'de':
            context.bot.send_message(update.effective_chat.id, 'Hallo! Besorgt darüber, was sich außerhalb des Fensters befindet? 😉 \n'+
                             '/weather - wetter jetzt 🌡️ \n'+
                            '/clothes - was man anziehen soll \n '+
                            '/city - Städteauswahl \n'+
                             '/lang - Sprachauswahl \n')
    elif query.data == "5":
        city_text = 'St. Petersburg'
        if lang_text == 'ru':
            context.bot.send_message(update.effective_chat.id, 'Привет! Волнует что за окном? 😉 \n'+
                             '/weather - погода сейчас 🌡️ \n'+
                             '/clothes - что надеть \n '+
                            '/city - выбор города 🏙 \n'+
                             '/lang - выбор языка 🧏 \n')
        elif lang_text == 'en':
            context.bot.send_message(update.effective_chat.id, 'Hi! Worried about what is outside the window? 😉 \n'+
                             '/weather - weather now 🌡️ \n'+
                            '/clothes - what to wear \n '+ 
                            '/city - city selection \n'+
                             '/lang - language selection \n')
        elif lang_text == 'de':
            context.bot.send_message(update.effective_chat.id, 'Hallo! Besorgt darüber, was sich außerhalb des Fensters befindet? 😉 \n'+
                             '/weather - wetter jetzt 🌡️ \n'+
                             '/clothes - was man anziehen soll \n '+        
                            '/city - Städteauswahl \n'+
                             '/lang - Sprachauswahl \n')
    elif query.data == "6":
        city_text = 'Sochi'
        if lang_text == 'ru':
            context.bot.send_message(update.effective_chat.id, 'Привет! Волнует что за окном? 😉 \n'+
                             '/weather - погода сейчас 🌡️ \n'+
                            '/clothes - что надеть \n '+
                            '/city - выбор города 🏙 \n'+
                             '/lang - выбор языка 🧏 \n')
        elif lang_text == 'en':
            context.bot.send_message(update.effective_chat.id, 'Hi! Worried about what is outside the window? 😉 \n'+
                             '/weather - weather now 🌡️ \n'+
                             '/clothes - was man anziehen soll \n '+           
                            '/city - city selection \n'+
                             '/lang - language selection \n')
        elif lang_text == 'de':
            context.bot.send_message(update.effective_chat.id, 'Hallo! Besorgt darüber, was sich außerhalb des Fensters befindet? 😉 \n'+
                             '/weather - wetter jetzt 🌡️ \n'+
                            '/clothes - was man anziehen soll \n '+  
                            '/city - Städteauswahl \n'+
                             '/lang - Sprachauswahl \n')
    elif query.data == "7":
        city_text = 'Kazan'
        if lang_text == 'ru':
            context.bot.send_message(update.effective_chat.id, 'Привет! Волнует что за окном? 😉 \n'+
                             '/weather - погода сейчас 🌡️ \n'+
                            '/clothes - что надеть \n '+         
                            '/city - выбор города 🏙 \n'+
                             '/lang - выбор языка 🧏 \n')
        elif lang_text == 'en':
            context.bot.send_message(update.effective_chat.id, 'Hi! Worried about what is outside the window? 😉 \n'+
                             '/weather - weather now 🌡️ \n'+
                             '/clothes - was man anziehen soll \n '+               
                            '/city - city selection \n'+
                             '/lang - language selection \n')
        elif lang_text == 'de':
            context.bot.send_message(update.effective_chat.id, 'Hallo! Besorgt darüber, was sich außerhalb des Fensters befindet? 😉 \n'+
                             '/weather - wetter jetzt 🌡️ \n'+
                            '/clothes - was man anziehen soll \n '+           
                            '/city - Städteauswahl \n'+
                             '/lang - Sprachauswahl \n')
    elif query.data == "8":
        city_text = 'Ekaterinburg'
        if lang_text == 'ru':
            context.bot.send_message(update.effective_chat.id, 'Привет! Волнует что за окном? 😉 \n'+
                             '/weather - погода сейчас 🌡️ \n'+
                            '/clothes - что надеть \n '+    
                            '/city - выбор города 🏙 \n'+
                             '/lang - выбор языка 🧏 \n')
        elif lang_text == 'en':
            context.bot.send_message(update.effective_chat.id, 'Hi! Worried about what is outside the window? 😉 \n'+
                             '/weather - weather now 🌡️ \n'+
                            '/clothes - was man anziehen soll \n '+        
                            '/city - city selection \n'+
                             '/lang - language selection \n')
        elif lang_text == 'de':
            context.bot.send_message(update.effective_chat.id, 'Hallo! Besorgt darüber, was sich außerhalb des Fensters befindet? 😉 \n'+
                             '/weather - wetter jetzt 🌡️ \n'+
                            '/clothes - was man anziehen soll \n '+   
                            '/city - Städteauswahl \n'+
                             '/lang - Sprachauswahl \n')
    elif query.data == "9":
        city_text = 'Krasnoyarsk'
        if lang_text == 'ru':
            context.bot.send_message(update.effective_chat.id, 'Привет! Волнует что за окном? 😉 \n'+
                             '/weather - погода сейчас 🌡️ \n'+
                            '/clothes - что надеть \n '+          
                            '/city - выбор города 🏙 \n'+
                             '/lang - выбор языка 🧏 \n')
        elif lang_text == 'en':
            context.bot.send_message(update.effective_chat.id, 'Hi! Worried about what is outside the window? 😉 \n'+
                             '/weather - weather now 🌡️ \n'+
                             '/clothes - was man anziehen soll \n '+          
                            '/city - city selection \n'+
                             '/lang - language selection \n')
        elif lang_text == 'de':
            context.bot.send_message(update.effective_chat.id, 'Hallo! Besorgt darüber, was sich außerhalb des Fensters befindet? 😉 \n'+
                             '/weather - wetter jetzt 🌡️ \n'+
                            '/clothes - was man anziehen soll \n '+          
                            '/city - Städteauswahl \n'+
                             '/lang - Sprachauswahl \n')
    elif query.data == "10":
        city_text = 'Vladivostok'
        if lang_text == 'ru':
            context.bot.send_message(update.effective_chat.id, 'Привет! Волнует что за окном? 😉 \n'+
                            '/weather - погода сейчас 🌡️ \n'+
                            '/clothes - что надеть \n '+            
                            '/city - выбор города 🏙 \n'+
                             '/lang - выбор языка 🧏 \n')
        elif lang_text == 'en':
            context.bot.send_message(update.effective_chat.id, 'Hi! Worried about what is outside the window? 😉 \n'+
                            '/weather - weather now 🌡️ \n'+
                            '/city - city selection \n'+       
                            '/city - city selection \n'+
                             '/lang - language selection \n')
        elif lang_text == 'de':
            context.bot.send_message(update.effective_chat.id, 'Hallo! Besorgt darüber, was sich außerhalb des Fensters befindet? 😉 \n'+
                            '/weather - wetter jetzt 🌡️ \n'+
                            '/city - Städteauswahl \n'+
                            '/city - Städteauswahl \n'+
                             '/lang - Sprachauswahl \n')
                            

#https://openweathermap.org/current
#сайт, который предоставляе информацию о погоде через API

def weather(update, context):
    global lang_text
    global city_text
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city_text+'&appid=b81c955812292d68b40fa34cea554708&units=metric&lang='+lang_text)
    response2 = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=55&lon=37&exclude=hourly&appid=b81c955812292d68b40fa34cea554708&units=metric&lang="+lang_text)
    temp = response.json()['main']
    temp = temp['temp']
    temp_like = response.json()['main']
    temp_like = temp_like['feels_like']
    humidity = response.json()['main']
    humidity = humidity['humidity']
    wind= response.json()['wind']
    wind = wind['speed']
    if lang_text == 'ru':
        update.message.reply_text('Температура сейчас: '+ str(temp)+' ℃'+'\n'+'Температура ощущается: '+ str(temp_like)+' ℃'+'\n'+'Влажность: '+str(humidity)+' %'+'\n'+'Скорость ветра: '+str(wind)+' м/с')
    if lang_text == 'en':
        update.message.reply_text('Temperature now: '+ str(temp)+' ℃'+'\n'+'The temperature is felt: '+ str(temp_like)+' ℃'+'\n'+'Humidity: '+str(humidity)+' %'+'\n'+'Wind speed: '+str(wind)+' m/s')
    if lang_text == 'de':
        update.message.reply_text('Temperatur jetzt: '+ str(temp)+' ℃'+'\n'+'Die Temperatur ist zu spüren: '+ str(temp_like)+' ℃'+'\n'+'Feuchtigkeit: '+str(humidity)+' %'+'\n'+'Windgeschwindigkeit: '+str(wind)+' Frau')

    
    
start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)

clothes_handler = CommandHandler('clothes', clothes)
dispatcher.add_handler(clothes_handler)

city_handler = CommandHandler('city', city)
dispatcher.add_handler(city_handler)

weather_handler = CommandHandler('weather', weather)
dispatcher.add_handler(weather_handler)

lang_handler = CommandHandler('lang', lang)
dispatcher.add_handler(lang_handler)

button_handler = CallbackQueryHandler(button)
dispatcher.add_handler(button_handler)
#запуск бота
updater.start_polling()
#режим ожидания
updater.idle()