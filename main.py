print("Starting up...")
import time
beginTime = time.time()

print("Importing config...")
try: # import config
    from config import *
except Exception as e:
    print("[ERROR] Cannot start: failed to import config! Please check it for any errors. (",e,")")
    input("Press Enter to exit...")
    raise SystemExit

try: # import dev copy of config file
    from devSettings import *
except:
    pass

print("Importing modules...")
try: # import modules
    import telebot
    import keyboard
    import platform
    import subprocess
    import threading
    from PIL import ImageGrab
    import io
    import socket
    import datetime
    import random
    from colorama import init, Fore, Back, Style
except ImportError as error:
    print("[ERROR] Something went wrong while importing one or more modules. Please make sure you have the default Python library and required modules installed before starting. (",error,")")
    input("Press Enter to exit...")
    raise SystemExit

CUSTOM_CMDS=[]
init(autoreset=True)

if useCustomCommands is True:
    print("[DEV] Importing custom commands")
    try:
        from custom import *
    except Exception as e:
        print(Fore.RED+f"[ERROR] Failed to import custom commands ({e})!")
        CUSTOM_CMDS=[]
    else:
        print(Fore.BLUE+"[DEV] Imported custom commands")

try:
    from locales import strings
    from locales import CMD_DESCRIPTIONS as customCMD_DESCRIPTIONS # importing custom locales
except ImportError:
    strings = {}
    customCMD_DESCRIPTIONS = {}
else:
    if not strings or not customCMD_DESCRIPTIONS:
        print(Fore.BLUE+"[DEV] No custom languages found")
    print(Fore.BLUE+f"[DEV] Imported custom languages: {', '.join(strings)}")

# ======== version setup ========
version = "rolling-developer"
build = "705"
hostname = socket.gethostname()
system = platform.system()
release = platform.release()
kernelver = platform.version()

if enableMultipleMacros == True:
    MACROS = {k.lower(): v for k, v in MACROS.items()}
    MacroPath = MACROS[defaultMacro]["path"]
    startkey = MACROS[defaultMacro]["startKey"]
    stopkey = MACROS[defaultMacro]["stopKey"]

# paths for shutdown commands
SHUTDOWN_PATH = rf"C:\Windows\System32\shutdown.exe -s -t {shtdwndelay}"
REBOOT_PATH = rf"C:\Windows\System32\shutdown.exe -r -t {shtdwndelay}"
CANCELSHUTDOWN_PATH = r"C:\Windows\System32\shutdown.exe -a"

# preset some values here to avoid errors
isPendingShutdown = False
pendingshutdowntype = "none"
shtdwntime= "none"

# add everybody from ADMINS to USERS
USERS.update(ADMINS)

# setup the testmode changes
if testmode == True:
    bypassSystemCheck = True
    print(Fore.YELLOW+"[WARN] testmode is on. see the config file to learn more about what it does")
    MacroPath = r"C:\Windows\System32\calc.exe"
    shtdwndelay = shtdwndelay*2
    SHUTDOWN_PATH = rf"C:\Windows\System32\shutdown.exe -s -t {shtdwndelay}"
    REBOOT_PATH = rf"C:\Windows\System32\shutdown.exe -r -t {shtdwndelay}"
    
if not system == "Windows" and bypassSystemCheck == False: # check the os
    print(Fore.RED + f"[ERROR] Cannot continue on your OS: {system}. To bypass this, set bypassSystemCheck to True in the config file.")
    input("Press Enter to exit...")
    raise SystemExit

if not USERS: # here we check if the userlist is empty and if it is we start in emergency mode to make adding users easier
    print(Fore.RED + "[ERROR] Cannot start normally without users! Please add at least one user or admin (see config file for instructions)")
    print("Connecting to Telegram Bot API and starting in emergency mode. Only /myid will be available.")
    bot = telebot.TeleBot(TOKEN)
    @bot.message_handler(commands=['myid'])
    def my_id(message):
        userid = message.from_user.id
        bot.reply_to(message,f"UserID: {userid}")
    print("Connected. You can use /myid to get your UserID. Use CTRL+C to stop the bot.")
    bot.infinity_polling()

# ----- define locales ----- #
# strings[language]["keyname"].format(valueplaceholder=value) -> "corresponding string"
strings = {
    # RUSSIAN
    "ru": {
        "hi": "привет!",
        "ru": "Русский",
        "en": "Английский",
        "y": "да",
        "n": "нет",
        "stop": "остановка",
        "shutdown": "выключение",
        "reboot": "перезагрузка",
        True: "вкл.",
        False: "выкл.",
        "unknown": "неизвестно",
        "done": "Готово!",
        "startedEXE_msg": "🔌 .exe макроса запущен!",
        "sendingAltF4_msg": "Закрываю приложение спереди...",
        "sentAltF4_msg": "✅ Alt+F4 успешно отправлено!",
        "minimizingAll_msg": "Сворачиваю все приложения...",
        "startsent_vid_msg": "▶️ Клавиша старта отправлена, записываю видео...",
        "startsent_novid_msg": "▶️ Клавиша старта отправлена!",
        "stopsent_msg": "⏹ Клавиша стоп отправлена!",
        "nokey_msg": "❌ Не указана клавиша.\nСинтаксис: /keyboard <клавиша>",
        "invalidkey_msg": "❌ Неверно указано клавиша.\nСинтаксис: /keyboard <клавиша>\nКлавиши: a-z, 0-9, ctrl, alt, win, shift, space, enter",
        "sentkey_msg": "✅ Клавиша {SENTKEY} успешно отправлена!",
        "takingscrshot_msg": "Делаю скриншот...",
        "recordingvid_msg": "Записываю видео...",
        "chkping_msg": "Быстренько проверяю пинг с Telegram API...",
        "scrshot_capt": "[{NOW}] Скриншот",
        "vid_capt": "[{NOW}] Видео",
        "BON_msg": "🟢 Бот онлайн!\nПК: *{HOSTNAME}*\nВремя: *{NOW}*",
        "err403msg": "❌ У вас нет разрешения на управление ботом.\nЕсли вы считаете, что я ошибаюсь, пожалуйста, напишите админу.",
        "notanadmin_msg": "❌ Недостаточно прав. Только администраторы могут использовать эту команду.",
        "pendingstop_msg": "*🛑 Запланирована остановка бота через {SHTDWNDELAY} секунд!*\n(!) Бот перестанет работать, но компьютер останется включённым.\n\nОстановка в: *{SHTDWNTIME}*\nОтменить: */cancelshutdown*",
        "pendingshutdown_msg": "*💤 Запланировано выключение компьютера через {SHTDWNDELAY} секунд!!*\n(!!!) После выключения бот перестанет работать!\n\nВыключение в: *{SHTDWNTIME}*\nОтменить: */cancelshutdown*",
        "pendingreboot_msg": "*🔄 Запланирована перезагрузка компьютера через {SHTDWNDELAY} секунд!*\n(!!) После перезагрузки бот может перестать работать\n\nПерезагрузка в: *{SHTDWNTIME}*\nОтменить: */cancelshutdown*",
        "shtdwnnotpending_msg": "Насколько мне известно, компьютер выключаться не собирался...",
        "alrpending_msg": "*Ошибка*: уже планируется *{PENDINGSHUTDOWNTYPE}* в *{SHTDWNTIME}*.\nНеобходимо сначала отменить это действие: */cancelshutdown*",
        "cnclpendingshutdown": "✅ Успешно отменено запланированное действие: {TYPE}.",
        "welcome_msg": "\
Здравствуйте, {NAME}! ✅ Бот активен и вы имеете права на управление.\n\
Доступные команды:\n\
/start - получить это сообщение\n\
/launch - запустить .exe макроса\n\
/alt_f4 - закрыть приложение в фокусе\n\
/startmacro - послать старт\n\
/stopmacro - послать стоп\n\
/keyboard - послать клавишу на компьютер\n\
/screenshot - сделать скриншот\n\
/video - записать видео на 15 секунд\n\
/stop - остановить бота\n\
/shutdown - выключить компьютер\n\
/reboot - перезагрузить компьютер\n\
/cancelshutdown - отменить запланированное действие\n\
/settings - просмотреть текущие настройки\n\
/info - посмотреть разную информацию о боте\n\n\
\
Сделано @ImGreyCat с <3",
        "info_msg": "\
*ℹ️ Информация и статус*\n\n\
\
*🔑 Авторизация*\n\
Ваше имя: *{NAME}*\n\
Базовые права: *да*\n\
Права администратора: *{ISADMIN}*\n\n\
\
*🖥 Компьютер*\n\
Имя: *{HOSTNAME}*\n\
Система: *{SYSTEM} {RELEASE} ({KERNELVER})*\n\
Время: *{NOW}*\nПинг до Telegram API (RTT): *{PING} мс *\n\n\
\
*🤖 Бот*\n\
Версия: *{VERSION} (сборка {BUILD})*\n\
Время работы: *{UPTIME}*\n\
Время на запуск: *{TOOKTOSTART} сек.*\n\
🧪 Тестовый режим: *{TMSTATUS}*\
",

        # ------------

        "settings_msg": "\
*⚙️ Настройки бота*\n\
Их можно изменить в файле конфигурации.\n\n\
\
🏳️ Язык: *{LANG} ({HI})*\n\
▶️ Кнопка старт: *{STARTKEY}*\n\
⏹ Кнопка стоп: *{STOPKEY}*\n\n\
\
> ⌨️ Кол-во нажатий старт/стоп: *{KEYPRESSES}*\n\
Бот отправляет старт/стоп это кол-во раз.\n\n\
\
> ⏱ Задержка выключения (сек.): *{SHTDWNDELAY}*\n\
Столько секунд бот будет ждать перед выключением/перезагрузкой.\n\n\
\
> 🎥 Запись при старте: *{RECONSTARTISON}*\n\
Будет ли бот записывать видео при /startmacro?\
",
        "updatedcmds_msg": "Список команд обновлён успешно.\nВнимание! Вы можете не увидеть изменения, пока полностью не перезапустите Telegram.",
        "start_cmd": "Приветственное сообщение",
        "launch_cmd": "Запустить .exe макроса",
        "alt_f4_cmd": "[✨ Новое] Закрыть приложение в фокусе",
        "minimize_all_cmd": "[✨ Новое] Свернуть все приложения",
        "startmacro_cmd": 'Нажать кнопку "старт"',
        "stopmacro_cmd": 'Нажать кнопку "стоп"',
        "keyboard_cmd": '[✨ Новое] Отправить клавишу на компьютер',
        "screenshot_cmd": "Сделать скриншот",
        "video_cmd": "Записать видео",
        "stop_cmd": "[✨ Новое] Выключить бота",
        "shutdown_cmd": "[✨ Новое] Выключить компьютер",
        "reboot_cmd": "[✨ Новое] Перезагрузить компьютер",
        "cancelshutdown_cmd": "[✨ Новое] Отменить перезагрузку/выключение",
        "settings_cmd": "[✨ Новое] Получить текущие настройки",
        "changemacro_cmd": "[✨ Новое] Изменить текущий макрос",
        "info_cmd": "Разная информация о боте",
    },

    # ENGLISH
    "en": {
        "hi": "hi!",
        "ru": "Russian",
        "en": "English",
        "y": "yes",
        "n": "no",
        "stop": "stop",
        "shutdown": "shutdown",
        "reboot": "reboot",
        True: "on",
        False: "off",
        "unknown": "unknown",
        "done": "Done!",
        "startedEXE_msg": "🔌 Started macro .exe!",
        "sendingAltF4_msg": "Closing focused app...",
        "sentAltF4_msg": "✅ Sent Alt+F4 successfully!",
        "startsent_vid_msg": "▶️ Start key sent, recording a video...",
        "startsent_novid_msg": "▶️ Start key sent!",
        "stopsent_msg": "⏹ Stop key sent!",
        "nokey_msg": "❌ No key specified.\nSyntax: /keyboard <key>\nAvailable keys: a-z, 0-9, ctrl, alt, win, shift, space, enter",
        "invalidkey_msg": "❌ Invalid key specified.\nSyntax: /keyboard <key>\nAvailable keys: a-z, 0-9, ctrl, alt, win, shift, space, enter",
        "sentkey_msg": "✅ Sent key {SENTKEY} successfully!",
        "takingscrshot_msg": "Taking a screenshot...",
        "chkping_msg": "Pinging the Telegram API real quick...",
        "scrshot_capt": "[{NOW}] Screenshot",
        "vid_capt": "[{NOW}] Video",
        "BON_msg": "🟢 Now online!\nPC: *{HOSTNAME}*\nTime: *{NOW}*",
        "err403msg": "❌ You do not have permission to use the bot.\nIf you think I'm mistaken, please contact the admin.",
        "notanadmin_msg": "❌ Insufficient permissions. Only admins can use this command.",
        "pendingstop_msg": "*🛑 Bot stop scheduled in {SHTDWNDELAY} seconds!*\n(!) The bot will stop working, but the RPC will keep running.\n\nStopping at: *{SHTDWNTIME}*\nCancel: */cancelshutdown*",
        "pendingshutdown_msg": "*💤 Computer shutdown scheduled in {SHTDWNDELAY} seconds!!*\n(!!!) The bot will stop working after shutdown!\n\nShutting down at: *{SHTDWNTIME}*\nCancel: */cancelshutdown*",
        "pendingreboot_msg": "*🔄 Computer reboot scheduled in {SHTDWNDELAY} seconds!*\n(!!) The bot may stop working after reboot\n\nRebooting at: *{SHTDWNTIME}*\nCancel: */cancelshutdown*",
        "shtdwnnotpending_msg": "As far as I can see, the computer doesn't have a scheduled shutdown...",
        "alrpending_msg": "*Error*: there's already a *{PENDINGSHUTDOWNTYPE}* pending at *{SHTDWNTIME}*.\nTo schedule a shutdown, please cancel this one first: */cancelshutdown*",
        "cnclpendingshutdown": "✅ Cancelled pending {TYPE} successfully.",
        "welcome_msg": "null",
        "info_msg": "\
*ℹ️ Info and status*\n\n\
\
*🔑 Authorization*\n\
Your name: *{NAME}*\n\
Default permissions: *yes*\n\
Admin permissions: *{ISADMIN}*\n\n\
\
*🖥 Computer*\n\
Hostname: *{HOSTNAME}*\n\
System: *{SYSTEM} {RELEASE} ({KERNELVER})*\n\
Time: *{NOW}*\nPing to Telegram API (RTT): *{PING} ms*\n\n\
\
*🤖 Bot*\n\
Version: *{VERSION} (build {BUILD})*\n\
Uptime: *{UPTIME}*\n\
Startup time: *{TOOKTOSTART} sec*\n\
🧪 Testmode: *{TMSTATUS}*\
",

        # ------------

        "settings_msg": "\
*⚙️ Bot settings*\n\
You can change these in the configuration file.\n\n\
\
🏳️ Language: *{LANG}: {HI}*\n\
▶️ Start button: *{STARTKEY}*\n\
⏹ Stop button: *{STOPKEY}*\n\n\
\
🡒 ⌨️ Start/stop button presses: *{KEYPRESSES}*\n\
The bot sends start/stop this amount of times.\n\n\
\
🡒 ⏱ Shutdown delay (s.): *{SHTDWNDELAY}*\n\
The bot will wait for this amount of seconds before shutdown.\n\n\
\
🡒 🎥 Record on start: *{RECONSTARTISON}*\n\
Should the bot record a video on /startmacro?\
",
        "updatedcmds_msg": "Commands succesfully refreshed.\nPlease note that you might need to fully restart Telegram for the changes to show!",
        "start_cmd": "Welcome message",
        "launch_cmd": "Launch macro .exe",
        "alt_f4_cmd": "[✨ New] Close focused app",
        "minimize_all_cmd": "[✨ New] Minimize all apps",
        "startmacro_cmd": "Send start key",
        "stopmacro_cmd": "Send stop key",
        "keyboard_cmd": "[✨ New] Send key",
        "screenshot_cmd": "Take a screenshot",
        "video_cmd": "Record a video",
        "stop_cmd": "[✨ New] Stop the bot",
        "shutdown_cmd": "[✨ New] Turn off PC",
        "reboot_cmd": "[✨ New] Reboot PC",
        "cancelshutdown_cmd": "[✨ New] Cancel pending shutdown",
        "settings_cmd": "[✨ New] View current settings",
        "changemacro_cmd": "[✨ New] Change current macro",
        "info_cmd": "Various info",
    }
}

macroManagementCommands = [
    {"cmd": "launch",
     "desc": strings[language]["launch_cmd"],
     "func": "launchpad_func",
     "admin": True},

    {"cmd": "startmacro",
     "desc": strings[language]["startmacro_cmd"],
     "func": "startmacro_func",
     "admin": False},

    {"cmd": "stopmacro",
     "desc": strings[language]["stopmacro_cmd"],
     "func": "stopmacro_func",
     "admin": False},

    {"cmd": "changemacro",
     "desc": strings[language]["changemacro_cmd"],
     "func": "changemacro_func",
     "admin": True},
]

COMMANDS = [
    {"cmd": "start",
     "desc": strings[language]["start_cmd"],
     "func": "start_func",
     "admin": False},
    
    # {"cmd": "launch",
    #  "desc": strings[language]["launch_cmd"],
    #  "func": "launchpad_func",
    #  "admin": True},

    {"cmd": "alt_f4",
     "desc": strings[language]["alt_f4_cmd"],
     "func": "closeapp_func",
     "admin": True},

    {"cmd": "minimize_all",
     "desc": strings[language]["minimize_all_cmd"],
     "func": "minimize_all_func",
     "admin": True},
    
    # {"cmd": "startmacro",
    #  "desc": strings[language]["startmacro_cmd"],
    #  "func": "startmacro_func",
    #  "admin": False},
    #
    # {"cmd": "stopmacro",
    #  "desc": strings[language]["stopmacro_cmd"],
    #  "func": "stopmacro_func",
    #  "admin": False},

    {"cmd": "keyboard",
     "desc": strings[language]["keyboard_cmd"],
     "func": "keyboard_func",
     "admin": False},
    
    {"cmd": "screenshot",
     "desc": strings[language]["screenshot_cmd"],
     "func": "screenshot_func",
     "admin": False},

    {"cmd": "video",
     "desc": strings[language]["video_cmd"],
     "func": "video_func",
     "admin": False},

    {"cmd": "stop",
     "desc": strings[language]["stop_cmd"],
     "func": "stop_func",
     "admin": True},

    {"cmd": "shutdown",
     "desc": strings[language]["shutdown_cmd"],
     "func": "shutdown_func",
     "admin": True},

    {"cmd": "reboot",
     "desc": strings[language]["reboot_cmd"],
     "func": "reboot_func",
     "admin": True},

    {"cmd": "cancelshutdown",
     "desc": strings[language]["cancelshutdown_cmd"],
     "func": "cancel_shutdown_func",
     "admin": True},

    {"cmd": "settings",
     "desc": strings[language]["settings_cmd"],
     "func": "settings_func",
     "admin": False},

    # {"cmd": "changemacro",
    #  "desc": strings[language]["changemacro_cmd"],
    #  "func": "changemacro_func",
    #  "admin": True},

    {"cmd": "info",
     "desc": strings[language]["info_cmd"],
     "func": "info_func",
     "admin": False}
]

if enableMacroModule == True:
    COMMANDS.extend(macroManagementCommands)
COMMANDS.extend(CUSTOM_CMDS)
COMMANDS_LKUP = {c["cmd"]: c for c in COMMANDS}

# -------------------- initialize bot -------------------- #
bot = telebot.TeleBot(TOKEN)
if useProxy is True: # logic to connect through proxy
    print("Connecting to Telegram through proxy...")
    if proxyUsername and proxyPassword:
        # Authenticated format: protocol://user:pass@ip:port
        proxy_url = f"{proxyType}://{proxyUsername}:{proxyPassword}@{proxyIP}:{proxyPort}"
    else:
        # Standard format: protocol://ip:port
        proxy_url = f"{proxyType}://{proxyIP}:{proxyPort}"
    telebot.apihelper.proxy = {'http': proxy_url, 'https': proxy_url}
    try:
        me = bot.get_me()
        print(Fore.CYAN+f"Proxy connection successful as @{me.username}")
    except Exception as e:
        print(Fore.RED+f"[ERROR] Proxy connection failed: {e}")
        input("The bot can't continue running. Press Enter to exit...")
        raise SystemExit
else: # connection without a proxy
    print("Connecting to Telegram...")
    try:
        me = bot.get_me()
        print(f"Connected as @{me.username}")
    except Exception as e:
        print(Fore.RED+f"[ERROR] Failed to connect to Telegram: {e}")
        input("The bot can't continue running. Press Enter to exit...")
        raise SystemExit

print("Syncing command list...")
bot.set_my_commands([telebot.types.BotCommand(c["cmd"], c["desc"]) for c in COMMANDS]) # creates command list for every cmd
print("Synced!")

# ------------------ helper functions ------------------  #

# take a screenshot and send it to chat_id
def take_screenshot(chat_id):
    screenshot = ImageGrab.grab()
    bio = io.BytesIO()
    bio.name = "screenshot.png"
    screenshot.save(bio, "PNG")
    bio.seek(0)
    bot.send_photo(chat_id, bio, caption=strings[language]["scrshot_capt"].format(NOW=get_time())) # sends the taken screenshot right away

# record a video into RAM
# supports length and bitrate options
def record_video_ram(chat_id=None, length=videoLength, bitrate="4000k"):
    now = get_time()
    print(f"[DEBUG] [{now}] video requested for chat {chat_id}, recording now...")
    cmd = [
        "ffmpeg",
        "-f", "gdigrab",
        "-framerate", "60", 
        "-i", "desktop",
        "-t", f"{length}", # this is the video length
        "-vcodec", "libx265", # change this to "libx264" if the video doesn't play
        "-b:v", f"{bitrate}", # this is the bitrate
        "-preset", "ultrafast",
        "-pix_fmt", "yuv420p",
        "-movflags", "frag_keyframe+empty_moov",
        "-f", "mp4",
        "pipe:1" # makes the video save to ram
    ]
    print(f"[DEBUG] ffmpeg arguments: {cmd}")
    # This flag prevents the console window from appearing on Windows. We use 0x08000000 directly to avoid import errors on different OS types
    CREATE_NO_WINDOW = 0x08000000
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        creationflags=CREATE_NO_WINDOW
    )

    video_bytes, err = process.communicate()
    if process.returncode != 0:
        print(Fore.RED+f"[DEBUG] [ERROR] ffmpeg error: {err.decode()}")

    video_buffer = io.BytesIO(video_bytes)
    video_buffer.name = "recording.mp4"  # telegram requires a filename so we're setting it here
    now = get_time()
    print(f"[DEBUG] [{now}] finished recording, sending...")
    bot.send_chat_action(chat_id, 'upload_video')
    bot.send_video(chat_id, video_buffer,caption=strings[language]["vid_capt"].format(NOW=get_time()))

def manage_macro(action):
    count = keyPresses
    if action == "start":
        key=startkey
    if action== "stop":
        key=stopkey
    if action!="start" and action!="stop":
        print(Fore.RED+f"[ERROR] invalid action passed to manage_macro(): {action}")
        return
    for i in range(count):
        sentTimes = i+1
        keyboard.send(key)
        print(f"Sent {key} ({sentTimes}/{count})")
        time.sleep(1)
    print("Finished sending")
    return

# returns current time like 12:34:56 with the offset in seconds
def get_time(offset=0):
    is24hr = use24HourTime
    now = datetime.datetime.now() + datetime.timedelta(seconds=offset) # gets current time and adds the offset in seconds
    if is24hr == True:
        formatted_time = now.strftime("%H:%M:%S")
        return formatted_time
    formatted_time = now.strftime("%I:%M:%S %p")
    return formatted_time # format and return

# authenticates user, also gets their admin status
def authenticate(user_id, target="do unknown action", adminOnly=False, alwaysAllow=False):
    isauser=False
    isanadmin=False
    if user_id in USERS:
        isauser=True
    if user_id in ADMINS:
        isanadmin=True
    if alwaysAllow == True:
        print(f"{user_id} requested to {target} (authentication not required)")
        return isauser, isanadmin
    if adminOnly==False and (isauser==True):
        print(f"[AUTH] {user_id} requested to {target}")
        return True
    if adminOnly==True and isanadmin==True:
        print(Fore.MAGENTA+f"[ADMIN] {user_id} requested to {target}")
        return True
    if adminOnly==True and (isauser==True and isanadmin==False):
        print(f"[AUTH] {user_id} tried requesting to {target}, but isn't an admin")
        bot.send_message(user_id, strings[language]["notanadmin_msg"],parse_mode="Markdown")
    print(f"[AUTH] {user_id} tried requesting to {target}, but isn't a user")
    bot.send_message(user_id, strings[language]["err403msg"],parse_mode="Markdown")
    return False

def is_admin(user_id):
    admin="n"
    if user_id in ADMINS:
        admin="y"
    return admin

def notify_online(force=False):
    if bonEnabled == False and force!=True:
        return
    if not testmode == True or force==True: # ensures that testmode is off
        now = get_time()
        for uid in USERS:
            print(f"Sending BON to {uid}")
            bot.send_message(uid,strings[language]["BON_msg"].format(HOSTNAME=hostname,NOW=now),parse_mode="Markdown")
    return

def get_uptime():
    uptimeS = int(time.time()) - starttime
    uptime = datetime.timedelta(seconds=int(uptimeS))
    return uptime

def delete_msg(message): # deletes the message passed to the function
    msgid = message.message_id
    chatid = message.chat.id
    print("[DEBUG] deleting message",msgid,"from chat", chatid)
    bot.delete_message(chatid,msgid,5)

def stop_bot():
    bot.stop_polling()
    time.sleep(3)
    input("Bot stopped, press Enter to exit...")
    raise SystemExit

#
# ------------------- commands and their functions -------------------
#
def start_func(message):
    if not authenticate(message.from_user.id,"get the welcome message",COMMANDS_LKUP["start"]["admin"]):
        return
    bot.reply_to(message,strings[language]["welcome_msg"].format(NAME=USERS[message.from_user.id]))

def launchpad_func(message):
    if not authenticate(message.from_user.id,"launch the macro .exe",COMMANDS_LKUP["launch"]["admin"]):
        return
    subprocess.Popen(MacroPath)
    bot.reply_to(message, strings[language]["startedEXE_msg"])

def closeapp_func(message):
    if not authenticate(message.from_user.id,"close the app in the front",COMMANDS_LKUP["alt_f4"]["admin"]):
        return
    sent = bot.send_message(message.chat.id,strings[language]["sendingAltF4_msg"])
    keyboard.press('alt')
    keyboard.press('f4')
    keyboard.release('f4')
    keyboard.release('alt')
    delete_msg(sent)
    bot.reply_to(message,strings[language]["sentAltF4_Msg"])

def minimize_all_func(message):
    if not authenticate(message.from_user.id,"minimize all apps",COMMANDS_LKUP["minimize_all"]["admin"]):
        return
    sent = bot.send_message(message.chat.id,"Отправляю Win+D...")
    keyboard.send("win")
    keyboard.press('d')
    keyboard.release('win')
    keyboard.release('d')
    delete_msg(sent)
    bot.reply_to(message,strings[language]["done"])

def startmacro_func(message):
    if not authenticate(message.from_user.id,"send the start key",COMMANDS_LKUP["startmacro"]["admin"]):
        return
    manage_macro("start")
    if recordOnStart == True:
        bot.reply_to(message, strings[language]["startsent_vid_msg"])
        chat_id = message.chat.id
        record_video_ram(chat_id)
        return
    bot.reply_to(message, strings[language]["startsent_novid_msg"])

def stopmacro_func(message):
    if not authenticate(message.from_user.id, "send the stop key",COMMANDS_LKUP["stopmacro"]["admin"]):
        return
    manage_macro("stop")
    bot.reply_to(message, strings[language]["stopsent_msg"])

def keyboard_func(message):
    global keyToSend
    keyToSend = None
    if not authenticate(message.from_user.id,"send a key to the keyboard",COMMANDS_LKUP["keyboard"]["admin"]):
        return
    parts = message.text.split()
    try:
        keyToSend = parts[1].lower()
    except IndexError:
        pass
        bot.reply_to(message,strings[language]["nokey_msg"])
        print(Fore.YELLOW+f"[WARN] Key not specified")
        return
    
    if keyToSend is not None:
        try:
            keyboard.send(keyToSend)
        except ValueError:
            pass
            bot.reply_to(message,strings[language]["invalidkey_msg"])
            print(Fore.YELLOW+f"[WARN] Invalid key specified")
            return
        bot.reply_to(message,strings[language]["sentkey_msg"].format(SENTKEY=keyToSend))

def screenshot_func(message):
    if not authenticate(message.from_user.id, "take a screenshot",COMMANDS_LKUP["screenshot"]["admin"]):
        return
    sent = bot.reply_to(message,strings[language]["takingscrshot_msg"])
    take_screenshot(message.chat.id)
    delete_msg(sent)
    
def video_func(message):
    if not authenticate(message.from_user.id, "record a video",COMMANDS_LKUP["video"]["admin"]):
        return
    sent = bot.send_message(message.chat.id,strings[language]["recordingvid_msg"],parse_mode="Markdown")
    record_video_ram(message.chat.id)
    delete_msg(sent)

def info_func(message):
    if not authenticate(message.from_user.id,"request info",COMMANDS_LKUP["info"]["admin"]):
        return
    if testmode is not True and testmode is not False: # if else if else if else
        tmstatus=strings[language]["unknown"]
    else:
        tmstatus=strings[language][testmode]
    uptime = get_uptime()
    ping1= time.time()
    sent = bot.send_message(message.chat.id,strings[language]["chkping_msg"])
    ping2=time.time()
    delete_msg(sent)
    ping=round((ping2-ping1)*1000,1) # this is RTT
    bot.reply_to(message, strings[language]["info_msg"].format(NAME=USERS[message.from_user.id],ISADMIN=strings[language][is_admin(message.from_user.id)],HOSTNAME=hostname,SYSTEM=system,RELEASE=release,KERNELVER=kernelver,NOW=get_time(),PING=ping,VERSION=version,BUILD=build,UPTIME=uptime,TOOKTOSTART=tookToStart,TMSTATUS=tmstatus), parse_mode="Markdown")

# unfortunately i couldn't find a way to avoid using so much "global" statements
def stop_func(message):
    global isPendingShutdown
    global pendingshutdowntype
    global shtdwntime
    global stopTimer
    
    if not authenticate(message.from_user.id,"stop the bot",COMMANDS_LKUP["stop"]["admin"]):
        return
    if isPendingShutdown == True:
        print(Fore.YELLOW+"[DEBUG] [WARN] user",message.from_user.id,"tried initiating a bot stop, but there's already a",pendingshutdowntype,"at",shtdwntime,"pending")
        bot.reply_to(message, strings[language]["alrpending_msg"].format(PENDINGSHUTDOWNTYPE=pendingshutdowntype,SHTDWNTIME=shtdwntime), parse_mode="Markdown")
        return
    stopTimer = threading.Timer(shtdwndelay, stop_bot)
    stopTimer.start()
    isPendingShutdown = True
    pendingshutdowntype = strings[language]["stop"]
    shtdwntime = get_time(shtdwndelay)
    print(Fore.YELLOW+f"[!] Bot stop requested by {message.from_user.id}, stopping at {shtdwntime}...")
    bot.reply_to(message, strings[language]["pendingstop_msg"].format(SHTDWNDELAY=shtdwndelay,SHTDWNTIME=shtdwntime), parse_mode="Markdown")
    return

def shutdown_func(message):
    global isPendingShutdown
    global pendingshutdowntype
    global shtdwntime
    
    if not authenticate(message.from_user.id,"turn off the RPC",COMMANDS_LKUP["shutdown"]["admin"]):
        return
    if isPendingShutdown == True:
        print(Fore.YELLOW+f"[DEBUG] [WARN] user {message.from_user.id} tried initiating a shutdown, but there's already a {pendingshutdowntype} at {shtdwntime} pending")
        bot.reply_to(message, strings[language]["alrpending_msg"].format(PENDINGSHUTDOWNTYPE=pendingshutdowntype,SHTDWNTIME=shtdwntime), parse_mode="Markdown")
        return
    subprocess.Popen(SHUTDOWN_PATH)
    isPendingShutdown = True
    pendingshutdowntype = strings[language]["shutdown"]
    shtdwntime = get_time(shtdwndelay)
    print(Fore.YELLOW+f"[!] Shutdown requested by {message.from_user.id}, shutting down at {shtdwntime}...")
    bot.reply_to(message, strings[language]["pendingshutdown_msg"].format(SHTDWNDELAY=shtdwndelay,SHTDWNTIME=shtdwntime),parse_mode="Markdown")
    return

def reboot_func(message):
    global isPendingShutdown
    global pendingshutdowntype
    global shtdwntime
    
    if not authenticate(message.from_user.id,"reboot the RPC",COMMANDS_LKUP["reboot"]["admin"]):
        return
    if isPendingShutdown == True:
        print(Fore.YELLOW+f"[DEBUG] [WARN] user {message.from_user.id} tried initiating a shutdown, but there's already a {pendingshutdowntype} at {shtdwntime} pending")
        bot.reply_to(message, strings[language]["alrpending_msg"].format(PENDINGSHUTDOWNTYPE=pendingshutdowntype,SHTDWNTIME=shtdwntime), parse_mode="Markdown")
        return
    subprocess.Popen(REBOOT_PATH)
    isPendingShutdown = True
    pendingshutdowntype = strings[language]["reboot"]
    shtdwntime = get_time(shtdwndelay)
    print(Fore.YELLOW+f"[!] Reboot requested by {message.from_user.id}, rebooting at {shtdwntime}...")
    bot.reply_to(message, strings[language]["pendingreboot_msg"].format(SHTDWNDELAY=shtdwndelay,SHTDWNTIME=shtdwntime), parse_mode="Markdown")
    return

def cancel_shutdown_func(message):
    global isPendingShutdown
    global pendingshutdowntype
    global shtdwntime
    global stopTimer
    
    if not authenticate(message.from_user.id,"cancel pending shutdown",COMMANDS_LKUP["cancelshutdown"]["admin"]):
        return
    if isPendingShutdown == False:
        print(Fore.YELLOW+f"[WARN] {message.from_user.id} tried cancelling a shutdown, but there isn't one pending")
        bot.reply_to(message, strings[language]["shtdwnnotpending_msg"], parse_mode="Markdown")
        return
        
    subprocess.Popen(CANCELSHUTDOWN_PATH)
    if pendingshutdowntype == "stop":
        stopTimer.cancel()
    print(Fore.GREEN+f"Pending shutdown cancelled by {message.from_user.id}")
    bot.reply_to(message,strings[language]["cnclpendingshutdown"].format(TYPE=pendingshutdowntype), parse_mode="Markdown")
    isPendingShutdown = False
    return

def settings_func(message):
    if not authenticate(message.from_user.id,"view current settings",COMMANDS_LKUP["settings"]["admin"]):
        return
    recOnStartIsOn=strings[language][recordOnStart]
    bot.reply_to(message, strings[language]["settings_msg"].format(LANG=strings[language][language],HI=strings[language]["hi"],STARTKEY=startkey,STOPKEY=stopkey,KEYPRESSES=keyPresses,SHTDWNDELAY=shtdwndelay,RECONSTARTISON=recOnStartIsOn), parse_mode="Markdown")
    return

def changemacro_func(message):
    global macro, MacroPath, startkey, stopkey
    if not authenticate(message.from_user.id,"change the current macro",COMMANDS_LKUP["changemacro"]["admin"]):
        return
    args = message.text.split()
    macro = " ".join(args[1:]).lower()
    MacroPath = MACROS[macro]["path"]
    startkey = MACROS[macro]["startKey"]
    stopkey = MACROS[macro]["stopKey"]
    print(f"Set current macro to {macro}")

def help_func(message):
    isuser, isadmin = authenticate(message.from_user.id,"to get the help message",alwaysAllow=True)
    print(f"User: {isuser}, Admin: {isadmin}")


# --------- bind all commands so they work --------- #

for cmd in COMMANDS: # for every command in vocabulary COMMANDS, do:
    func = globals()[cmd["func"]] # find the function in "func" that corresponds to "cmd" in vocabulary
    bot.message_handler(commands=[cmd["cmd"]])(func) # create a handler for the found command and bind it to its found function

# ----- create development (hidden) commands ----- #
@bot.message_handler(commands=['myid'])
def my_id(message):
    userid = message.from_user.id
    bot.reply_to(message,f"UserID: `{userid}`",parse_mode="Markdown")

@bot.message_handler(commands=['testBON'])
def test_bot_online_notification(message):
    if not authenticate(message.from_user.id,"test the BON"):
            return
    if testmode == False:
        print(Fore.RED+"[ERROR] This command cannot be used outside of testmode")
        return
    notify_online(True)

@bot.message_handler(commands=['screenshit'])
def schreenshit(message):
    if not authenticate(message.from_user.id):
        return
    bot.reply_to(message, '"screenshit" 😭🙏🏿')
    take_screenshot(message.chat.id)

@bot.message_handler(commands=['upd_cmds'])
def clr_func(message):
    if not authenticate(message.from_user.id):
        return
    bot.delete_my_commands(language_code="")
    bot.set_my_commands([telebot.types.BotCommand(c["cmd"], c["desc"]) for c in COMMANDS])
    bot.reply_to(message,strings[language]["updatedcmds_msg"])

@bot.message_handler(commands=['setlang'])
def setlang(message):
    global language
    if not authenticate(message.from_user.id):
        return
    parts = message.text.split()
    language = parts[1].lower()
    bot.reply_to(message,f"Set language to {language}")

@bot.message_handler(commands=['hi'])
def hi(message):
    replies = ['!!!!', '! :D', ' :3', ' ^_^', '', ' :]', ' ;3', '!! >_<', ' ^w^', '!! >w<', ' •ᴗ•']
    append = random.choice(replies)
    time.sleep(random.uniform(0.5,1.25))
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(random.uniform(0.4,2.6))
    bot.reply_to(message,strings[language]["hi"]+append)


# ------------------- start bot ------------------- #
# ---- everything here will execute on startup ---- #
notify_online()
telebot.apihelper.READ_TIMEOUT = 60
telebot.apihelper.CONNECT_TIMEOUT = 60
starttime = time.time() # saves the startup time to calculate uptime later when needed
tookToStart = round(starttime-beginTime,2)
print(Fore.GREEN+f"Bot started successfully! (took {tookToStart} seconds)")
bot.infinity_polling() # this makes the bot run even if there's an error somewhere
