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
    from utils import *
    from strings import strings
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
    print(Fore.BLUE+"[DEV] Importing custom commands")
    try:
        from custom import *
    except Exception as e:
        print(Fore.RED+f"[ERROR] Failed to import custom commands ({e})!")
        CUSTOM_CMDS=[]
    else:
        print(Fore.BLUE+"[DEV] Imported custom commands")
try:
    from locales import strings as strs
    from locales import CMD_DESCRIPTIONS as customCMD_DESCRIPTIONS # importing custom locales
except ImportError:
    strs = {}
    customCMD_DESCRIPTIONS = {}
else:
    if not strs or not customCMD_DESCRIPTIONS:
        print(Fore.BLUE+"[DEV] No custom languages found")
    print(Fore.BLUE+f"[DEV] Imported custom languages: {', '.join(strs)}")
strings.update(strs)

# ======== version setup ========
version = "rolling-developer"
build = "706"
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
    print(Fore.RED + f"[ERROR] Cannot continue on your OS: {system}. To bypass this, set bypassSystemCheck to True in the config file.\nPlease note that doing this is not officially supported and will cause issues.")
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

macroManagementCommands = [
    {"cmd": "launch",
     "desc": strings[language]["cmddesc.launch"],
     "func": "launchpad_func",
     "admin": True},

    {"cmd": "startmacro",
     "desc": strings[language]["cmddesc.startmacro"],
     "func": "startmacro_func",
     "admin": False},

    {"cmd": "stopmacro",
     "desc": strings[language]["cmddesc.stopmacro"],
     "func": "stopmacro_func",
     "admin": False},

    {"cmd": "changemacro",
     "desc": strings[language]["cmddesc.changemacro"],
     "func": "changemacro_func",
     "admin": True},
]

captureCommands = [
    {"cmd": "screenshot",
     "desc": strings[language]["cmddesc.screenshot"],
     "func": "screenshot_func",
     "admin": False},

    {"cmd": "video",
     "desc": strings[language]["cmddesc.video"],
     "func": "video_func",
     "admin": False},
]

shutdownCommands = [
    {"cmd": "stop",
     "desc": strings[language]["cmddesc.stop"],
     "func": "stop_func",
     "admin": True},

    {"cmd": "shutdown",
     "desc": strings[language]["cmddesc.shutdown"],
     "func": "shutdown_func",
     "admin": True},

    {"cmd": "reboot",
     "desc": strings[language]["cmddesc.reboot"],
     "func": "reboot_func",
     "admin": True},

    {"cmd": "cancelshutdown",
     "desc": strings[language]["cmddesc.cancelshutdown"],
     "func": "cancel_shutdown_func",
     "admin": True},
]

COMMANDS = [
    {"cmd": "start",
     "desc": strings[language]["cmddesc.start"],
     "func": "start_func",
     "admin": False},

    {"cmd": "alt_f4",
     "desc": strings[language]["cmddesc.alt_f4"],
     "func": "closeapp_func",
     "admin": True},

    {"cmd": "minimize_all",
     "desc": strings[language]["cmddesc.minimize_all"],
     "func": "minimize_all_func",
     "admin": True},

    {"cmd": "keyboard",
     "desc": strings[language]["cmddesc.keyboard"],
     "func": "keyboard_func",
     "admin": False},

    {"cmd": "settings",
     "desc": strings[language]["cmddesc.settings"],
     "func": "settings_func",
     "admin": False},

    {"cmd": "info",
     "desc": strings[language]["cmddesc.info"],
     "func": "info_func",
     "admin": False},

]

if enableMacroModule == True:
    COMMANDS.extend(macroManagementCommands)
if enableCaptures == True:
    COMMANDS.extend(captureCommands)
if enableShutdowns == True:
    COMMANDS.extend(shutdownCommands)
if enableCaptures != True:
    recordOnStart=False

COMMANDS.extend(CUSTOM_CMDS)
COMMANDS_LKUP = {c["cmd"]: c for c in COMMANDS}

from bot import bot

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
    bot.send_photo(chat_id, bio, caption=strings[language]["caption.screenshot"].format(NOW=get_time())) # sends the taken screenshot right away

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
    bot.send_video(chat_id, video_buffer,caption=strings[language]["caption.video"].format(NOW=get_time()))

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
            bot.send_message(uid,strings[language]["msg.BON"].format(HOSTNAME=hostname,NOW=now),parse_mode="Markdown")
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
    bot.reply_to(message,strings[language]["msg.welcome"].format(NAME=USERS[message.from_user.id]))

def launchpad_func(message):
    if not authenticate(message.from_user.id,"launch the macro .exe",COMMANDS_LKUP["launch"]["admin"]):
        return
    subprocess.Popen(MacroPath)
    bot.reply_to(message, strings[language]["msg.startedEXE"])

def closeapp_func(message):
    if not authenticate(message.from_user.id,"close the app in the front",COMMANDS_LKUP["alt_f4"]["admin"]):
        return
    sent = bot.send_message(message.chat.id,strings[language]["msg.sendingAltF4"])
    keyboard.press('alt')
    keyboard.press('f4')
    keyboard.release('f4')
    keyboard.release('alt')
    delete_msg(sent)
    bot.reply_to(message,strings[language]["msg.sentAltF4"])

def minimize_all_func(message):
    if not authenticate(message.from_user.id,"minimize all apps",COMMANDS_LKUP["minimize_all"]["admin"]):
        return
    sent = bot.send_message(message.chat.id,"msg.sendingWinD")
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
        bot.reply_to(message, strings[language]["msg.startsent_vid"])
        chat_id = message.chat.id
        record_video_ram(chat_id)
        return
    bot.reply_to(message, strings[language]["msg.startsent_novid"])

def stopmacro_func(message):
    if not authenticate(message.from_user.id, "send the stop key",COMMANDS_LKUP["stopmacro"]["admin"]):
        return
    manage_macro("stop")
    bot.reply_to(message, strings[language]["msg.stopsent"])

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
        bot.reply_to(message,strings[language]["msg.nokey"])
        print(Fore.YELLOW+f"[WARN] Key not specified")
        return
    
    if keyToSend is not None:
        try:
            keyboard.send(keyToSend)
        except ValueError:
            bot.reply_to(message,strings[language]["msg.invalidkey"])
            print(Fore.YELLOW+f"[WARN] Invalid key specified")
            return
        bot.reply_to(message,strings[language]["msg.sentkey"].format(SENTKEY=keyToSend))

def screenshot_func(message):
    if not authenticate(message.from_user.id, "take a screenshot",COMMANDS_LKUP["screenshot"]["admin"]):
        return
    sent = bot.reply_to(message,strings[language]["msg.takingscreenshot"])
    take_screenshot(message.chat.id)
    delete_msg(sent)
    
def video_func(message):
    if not authenticate(message.from_user.id, "record a video",COMMANDS_LKUP["video"]["admin"]):
        return
    sent = bot.send_message(message.chat.id,strings[language]["msg.recordingvideo"],parse_mode="Markdown")
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
    sent = bot.send_message(message.chat.id,strings[language]["msg.checkingping"])
    ping2=time.time()
    delete_msg(sent)
    ping=round((ping2-ping1)*1000,1) # this is RTT
    bot.reply_to(message, strings[language]["msg.info"].format(NAME=USERS[message.from_user.id],ISADMIN=strings[language][is_admin(message.from_user.id)],HOSTNAME=hostname,SYSTEM=system,RELEASE=release,KERNELVER=kernelver,NOW=get_time(),PING=ping,VERSION=version,BUILD=build,UPTIME=uptime,TOOKTOSTART=tookToStart,TMSTATUS=tmstatus), parse_mode="Markdown")

# unfortunately i couldn't find a way to avoid using so much "global" statements
def stop_func(message):
    global isPendingShutdown
    global pendingshutdowntype
    global shtdwntime
    global stopTimer
    
    if not authenticate(message.from_user.id,"stop the bot",COMMANDS_LKUP["stop"]["admin"]):
        return
    if isPendingShutdown == True:
        print(Fore.YELLOW+"[WARN] user",message.from_user.id,"tried initiating a bot stop, but there's already a",pendingshutdowntype,"at",shtdwntime,"pending")
        bot.reply_to(message, strings[language]["msg.alrpending"].format(PENDINGSHUTDOWNTYPE=pendingshutdowntype,SHTDWNTIME=shtdwntime), parse_mode="Markdown")
        return
    stopTimer = threading.Timer(shtdwndelay, stop_bot)
    stopTimer.start()
    isPendingShutdown = True
    pendingshutdowntype = strings[language]["stop"]
    shtdwntime = get_time(shtdwndelay)
    print(Fore.YELLOW+f"[!] Bot stop requested by {message.from_user.id}, stopping at {shtdwntime}...")
    bot.reply_to(message, strings[language]["msg.pendingstop"].format(SHTDWNDELAY=shtdwndelay,SHTDWNTIME=shtdwntime), parse_mode="Markdown")
    return

def shutdown_func(message):
    global isPendingShutdown
    global pendingshutdowntype
    global shtdwntime
    
    if not authenticate(message.from_user.id,"turn off the computer",COMMANDS_LKUP["shutdown"]["admin"]):
        return
    if isPendingShutdown == True:
        print(Fore.YELLOW+f"[DEBUG] [WARN] user {message.from_user.id} tried initiating a shutdown, but there's already a {pendingshutdowntype} at {shtdwntime} pending")
        bot.reply_to(message, strings[language]["msg.alrpending"].format(PENDINGSHUTDOWNTYPE=pendingshutdowntype,SHTDWNTIME=shtdwntime), parse_mode="Markdown")
        return
    subprocess.Popen(SHUTDOWN_PATH)
    isPendingShutdown = True
    pendingshutdowntype = strings[language]["shutdown"]
    shtdwntime = get_time(shtdwndelay)
    print(Fore.YELLOW+f"[!] Shutdown requested by {message.from_user.id}, shutting down at {shtdwntime}...")
    bot.reply_to(message, strings[language]["msg.pendingshutdown"].format(SHTDWNDELAY=shtdwndelay,SHTDWNTIME=shtdwntime),parse_mode="Markdown")
    return

def reboot_func(message):
    global isPendingShutdown
    global pendingshutdowntype
    global shtdwntime
    
    if not authenticate(message.from_user.id,"reboot the computer",COMMANDS_LKUP["reboot"]["admin"]):
        return
    if isPendingShutdown == True:
        print(Fore.YELLOW+f"[WARN] user {message.from_user.id} tried initiating a shutdown, but there's already a {pendingshutdowntype} at {shtdwntime} pending")
        bot.reply_to(message, strings[language]["msg.alrpending"].format(PENDINGSHUTDOWNTYPE=pendingshutdowntype,SHTDWNTIME=shtdwntime), parse_mode="Markdown")
        return
    subprocess.Popen(REBOOT_PATH)
    isPendingShutdown = True
    pendingshutdowntype = strings[language]["reboot"]
    shtdwntime = get_time(shtdwndelay)
    print(Fore.YELLOW+f"[!] Reboot requested by {message.from_user.id}, rebooting at {shtdwntime}...")
    bot.reply_to(message, strings[language]["msg.pendingreboot"].format(SHTDWNDELAY=shtdwndelay,SHTDWNTIME=shtdwntime), parse_mode="Markdown")
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
        bot.reply_to(message, strings[language]["msg.shtdwnnotpending"], parse_mode="Markdown")
        return
        
    subprocess.Popen(CANCELSHUTDOWN_PATH)
    if pendingshutdowntype == "stop":
        stopTimer.cancel()
    print(Fore.GREEN+f"Pending shutdown cancelled by {message.from_user.id}")
    bot.reply_to(message,strings[language]["msg.cnclpendingshutdown"].format(TYPE=pendingshutdowntype), parse_mode="Markdown")
    isPendingShutdown = False
    return

def settings_func(message):
    if not authenticate(message.from_user.id,"view current settings",COMMANDS_LKUP["settings"]["admin"]):
        return
    recOnStartIsOn=strings[language][recordOnStart]
    bot.reply_to(message, strings[language]["msg.settings"].format(LANG=strings[language][language],HI=strings[language]["hi"],STARTKEY=startkey,STOPKEY=stopkey,KEYPRESSES=keyPresses,SHTDWNDELAY=shtdwndelay,RECONSTARTISON=recOnStartIsOn), parse_mode="Markdown")
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
    isuser, isadmin = authenticate(message.from_user.id,"get the help message",alwaysAllow=True)
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
    bot.reply_to(message,strings[language]["msg.updatedcmds"])

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
