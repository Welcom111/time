import telebot, time, subprocess
bot = telebot.TeleBot('КОД ВАШЕГО БОТА')

#переменные
shut0 = 'shutdown -a'
shut1 = 'shutdown -s -t 5400'
shut2 = 'shutdown -s -t 10800'
shut3 = 'shutdown -s -t 10'
shut4 = 'Shutdown -r -t 10'
shut5 = 'Rundll32.exe user32.dll,LockWorkStation'
shut6 = r"""powershell (Add-Type '[DllImport(\"user32.dll\")]^public static extern int SendMessage(int hWnd, int hMsg, int wParam, int lParam);' -Name a -Pas)::SendMessage(-1,0x0112,0xF170,2)"""
shut7 = 'shutdown -s -t 3600'
shut8 = 'Shutdown -r -t 3600'
shut9 = 'Shutdown -r -t 5400'
shut10 = 'shutdown -r -t 10800'
shut11 = 'shutdown -s -t 1800'
shut12 = '''"C:\Program Files\Getscreen\getscreen.exe"'''
shut13 = r"C:\Users\zevsk\Desktop\Nircmd\сделать потише.bat"
shut14 = r"C:\Users\zevsk\Desktop\Nircmd\сделать погромче.bat"
shut15 = r'start C:\Users\zevsk\Desktop\AHK\AutoHotkey.ahk pause","ground":"foreground","voice":"pause"'
shut16 = r"C:\Users\zevsk\Desktop\Nircmd\hyper x.vbs"
shut17 = r"C:\Users\zevsk\Desktop\Nircmd\Logitech.vbs"
shut18 = r"C:\Users\zevsk\Desktop\Nircmd\monitor.vbs"

#кнопки
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('заблокируй пк.')
keyboard1.row('погаси экраны.')
keyboard1.row('выключи пк через...')
keyboard1.row('мультимедиа')
#keyboard1.row('перезагрузи пк через...') скрыто из меню за редкостью использования
keyboard1.row('отмени выключение/перезагрузку.')
keyboard1.row('запусти удаленное управление пк.')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('10 секунд.')
keyboard2.row('30 минут.')
keyboard2.row('1 час.')
keyboard2.row('1,5 часа.')
keyboard2.row('3 часа.')
keyboard3 = telebot.types.ReplyKeyboardMarkup(True)
keyboard3.row('сделай потише.')
keyboard3.row('сделай погромче.')
keyboard3.row('play/pause.')
keyboard3.row('устройства по умолч.')
keyboard3.row('назад.')
keyboard4 = telebot.types.ReplyKeyboardMarkup(True)
keyboard4.row('hyper x')
keyboard4.row('logitech')
keyboard4.row('monitor')
keyboard4.row('назад.')

#старт кода
@bot.message_handler(commands=['start'])
def start_message(message):
    adm = [521397050]  # список из id пользователей
    if message.chat.id not in adm:
        bot.send_message(message.chat.id, 'Недостаточно прав для использования бота.', reply_markup=keyboard1)
    else:
        bot.send_message(message.chat.id, 'введите команду.', reply_markup=keyboard1)
@bot.message_handler(content_types=['text'])
def stt(message):
    adm = [521397050]  # список из id пользователей
    if message.chat.id not in adm:
        bot.send_message(message.chat.id, 'Недостаточно прав для использования бота.')
    else:
#заблокировать ПК
        if message.text == 'заблокируй пк.':
            bot.send_message(message.chat.id, "комп заблокирован.", reply_markup=keyboard1)
            p = subprocess.Popen(shut5, shell=True)
#отмена выключения
        if message.text == 'отмени выключение/перезагрузку.':
            bot.send_message(message.chat.id, "отменяю автовыключение/перезагрузку.", reply_markup=keyboard1)
            p = subprocess.Popen(shut0, shell=True)
#выключение ПК
        if message.text == 'выключи пк через...':
            bot.send_message(message.chat.id, "через сколько выключить пк?", reply_markup=keyboard2)
            bot.register_next_step_handler(message, timer)
#перезагрузка ПК
        if message.text == 'перезагрузи пк через...':
            bot.send_message(message.chat.id, "через сколько перезагрузить пк?", reply_markup=keyboard2)
            bot.register_next_step_handler(message, time)
#удаленное управление
        if message.text == 'запусти удаленное управление пк.':
            bot.send_message(message.chat.id, "Getscreen запущен.", reply_markup=keyboard1)
            p = subprocess.Popen(shut12, shell=True)
#мультимедиа
        if message.text == 'мультимедиа':
            bot.send_message(message.chat.id, "меню мультимедиа.", reply_markup=keyboard3)
            bot.register_next_step_handler(message, volume)
#погаси экраны
        if message.text == 'погаси экраны.':
            bot.send_message(message.chat.id, "экраны погашены.", reply_markup=keyboard1)
            p = subprocess.Popen(shut6, shell=True)
#время до выключения
def timer(message):
    if message.text == '10 секунд.':
        bot.send_message(message.chat.id, "выключаю комп через 10 секунд.", reply_markup=keyboard1)
        p = subprocess.Popen(shut3, shell=True)
        bot.register_next_step_handler(message, stt)
    if message.text == '30 минут.':
        bot.send_message(message.chat.id, "выключаю комп через 30 минут.", reply_markup=keyboard1)
        p = subprocess.Popen(shut11, shell=True)
        bot.register_next_step_handler(message, stt)
    if message.text == '1 час.':
        bot.send_message(message.chat.id, "выключаю комп через 1 час.", reply_markup=keyboard1)
        p = subprocess.Popen(shut7, shell=True)
        bot.register_next_step_handler(message, stt)
    if message.text == '1,5 часа.':
        bot.send_message(message.chat.id, "выключаю комп через 1,5 часа.", reply_markup=keyboard1)
        p = subprocess.Popen(shut1, shell=True)
        bot.register_next_step_handler(message, stt)
    if message.text == '3 часа.':
        bot.send_message(message.chat.id, "выключаю комп через 3 часа.", reply_markup=keyboard1)
        p = subprocess.Popen(shut2, shell=True)
        bot.register_next_step_handler(message, stt)
#время до перезагрузки
def time(message):
    if message.text == '10 секунд.':
        bot.send_message(message.chat.id, "перезагружаю комп через 10 секунд.", reply_markup=keyboard1)
        p = subprocess.Popen(shut3, shell=True)
        bot.register_next_step_handler(message, stt)
        if message.text == '1 час.':
            bot.send_message(message.chat.id, "перезагружаю комп через 1 час.", reply_markup=keyboard1)
            p = subprocess.Popen(shut8, shell=True)
            bot.register_next_step_handler(message, stt)
    if message.text == '1,5 часа.':
        bot.send_message(message.chat.id, "перезагружаю комп через 1,5 часа.", reply_markup=keyboard1)
        p = subprocess.Popen(shut9, shell=True)
        bot.register_next_step_handler(message, stt)
    if message.text == '3 часа.':
        bot.send_message(message.chat.id, "перезагруждаю комп через 3 часа.", reply_markup=keyboard1)
        p = subprocess.Popen(shut10, shell=True)
        bot.register_next_step_handler(message, stt)
#мультимедиа
def volume(message):
    if message.text == 'сделай потише.':
        bot.send_message(message.chat.id, "сделоно потише.", reply_markup=keyboard3)
        p = subprocess.Popen(shut13, shell=True)
        bot.register_next_step_handler(message, volume)
    if message.text == 'сделай погромче.':
        bot.send_message(message.chat.id, "сделоно погромче.", reply_markup=keyboard3)
        p = subprocess.Popen(shut14, shell=True)
        bot.register_next_step_handler(message, volume)
    if message.text == 'назад.':
        bot.send_message(message.chat.id, "главное меню", reply_markup=keyboard1)
        bot.register_next_step_handler(message, stt)
    if message.text == 'play/pause.':
        bot.send_message(message.chat.id, "проигрователь остановлен/воспроизведен", reply_markup=keyboard3)
        p = subprocess.Popen(shut15, shell=True)
        bot.register_next_step_handler(message, volume)
    if message.text == 'устройства по умолч.':
        bot.send_message(message.chat.id, "выберите устройство.", reply_markup=keyboard4)
        bot.register_next_step_handler(message, device)
#выбрать устройство вывода/записи
def device(message):
    if message.text == 'hyper x':
        bot.send_message(message.chat.id, "устройство изменено.", reply_markup=keyboard3)
        p = subprocess.Popen(shut16, shell=True)
        bot.register_next_step_handler(message, volume)
    if message.text == 'logitech':
        bot.send_message(message.chat.id, "устройство изменено.", reply_markup=keyboard3)
        p = subprocess.Popen(shut17, shell=True)
        bot.register_next_step_handler(message, volume)
    if message.text == 'монитор':
        bot.send_message(message.chat.id, "устройство изменено.", reply_markup=keyboard3)
        p = subprocess.Popen(shut18, shell=True)
        bot.register_next_step_handler(message, volume)
    if message.text == 'назад.':
        bot.send_message(message.chat.id, "меню мультимедиа.", reply_markup=keyboard3)
        bot.register_next_step_handler(message, volume)  
        

bot.polling(none_stop=True, interval=0)