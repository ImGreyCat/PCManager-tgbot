# Configuration file

# ========== Connection ==========

# the bot token to connect to Telegram API
# to create a bot, use @BotFather on Telegram and follow its instructions
TOKEN = ""

# whether to send a message to all users when the bot starts
# if on, will prevent the bot from starting if at least one of the users didn't send any command/message to the bot before
bonEnabled = True
# default: True

# should the bot connect using a proxy?
useProxy = False
# default = False

# proxy settings
proxyType = "" # options: "socks5", "http", "https"
proxyIP = ""
proxyPort = 0
proxyUsername = ""
proxyPassword = ""
# set both username and password to "" if proxy doesn't require authentication

# ========== Regional ==========

# language to use
# available languages are en (english) and ru (russian)
language = ""

# use 12-hour or 24-hour time
use24HourTime = True
# default: True

# ========== Remote computer ==========

# how long the recorded videos will be in seconds
videoLength = 15
# default: 15

# how long to wait in seconds before stopping the bot or shutting down/rebooting
shtdwndelay=60
# default: 60
# 0 = instant

# ========== User setup ==========

# the following users will be able to access the bot and its commands
# admins will have all permissions of a regular user and will also be able to run admin-only commands
# to add somebody here, put in their telegram user id followed by a colon and their name in brackets, then a commma 
# [!] note 1: the bot will refer to the users using the name you put in, not their telegram name
# [!] note 2: don't add a user both to the users list and the admins list, pick just one
# it will also send all of them the Bot Online notification if set up to do so
#
# here's an example of a user setup with 2 users and 1 admin:
# USERS = {
#     1234567890: "buddy",
#     1234567891: "friend",
# }
#
# ADMINS = {
#     9876543210: "Admin",
# }

USERS = {

}

ADMINS = {

}

# ========== Macro ==========

# path to your preferred macro's .exe here (C:\Users\User\...)
MacroPath = r""

# start and stop keys
startkey = ""
stopkey = ""

# how many times to send keys to the computer on /startmacro and /stopmacro.
# there will always be a 1-second delay between presses to avoid lag
keyPresses = 1
# default: 1
# it's not recommended to increase this unless your macro often doesn't start/stop from the first key press

# should the bot record a video when the macro is started?
recordOnStart = True
# default: True

# (in development) use multimacro?
enableMultipleMacros = True

MACROS = {
    "macro 2": {
        "path": r"",
        "startKey": "Win",
        "stopKey": "Space",
    },

    "macro 2": {
        "path": r"",
        "startKey": "Win",
        "stopKey": "Space",
    }
}

defaultMacro="macro 1"

# ========== Developer ==========

# whether to use custom commands or not
# if on, the bot will also accept commands set up in the custom.py file
# please note that issues with custom commands ON will not be accepted, because they may cause stability issues and stuff
useCustomCommands = False
# default: False

# system check bypass toggle
# setting this to True will disable the check for the OS of your PC
# the bot is generally built to work just on Windows, so it's not recommended to use linux/macOS
bypassSystemCheck = False
# default and recommended: False

# test mode switch
# if True, the following will change:
#   - you'll get a warning in the console every time you start the bot
#   - system check will be disabled
#   - test bot token will be used
#   - launchpad will launch calculator instead of the macro .exe
#   - shutdown delay will be double
#   - bot online notification won't be sent
# this is only intended for development and testing, so please keep it False unless you know what you're doing.
testmode = False
# default and recommended: False

# Print a message and exit if this file is executed
if __name__ == "__main__":
    print("The config file can't be executed. Please run the main script instead.")
    print("To edit this file, right click it > Open With > choose your preferred text editor.")
    input("Press Enter to exit...")
    raise SystemExit
