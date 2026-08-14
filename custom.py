### Custom commands file
# Create your custom features here! You'll be able to run any of these in your bot.
# This is an advanced feature. Creating custom commands requires Python knowledge. Use them only if you know what you're doing.
# [!!!] IMPORTANT: don't blindly paste code you don't understand here! it can make your bot and PC vulnerable!

### Useful helper functions:
from utils import *
# get_time(offset (int, in seconds) - outputs the time in HH:mm:ss (HH:mm:ss AM/PM for 12-hour time) + the offset in seconds (default 0)
# take_screenshot(chat_id)
# record_video_ram(chat_id, length (int, in seconds), bitrate (str, ####k))
# authenticate(user_id, target (str), adminOnly)
# is_admin(user_id) - returns "y" or "n"
# delete_msg(message)

# Note! All your custom commands will be added to the bot's menu.
# The menu refreshes automatically upon bot start, but to force clear and update it, run /upd_cmds.

### command list

CUSTOM_CMDS = [
    {"cmd": "custom", # the command name (/####)
     "desc": "Custom command", # the description to display in the bot's commands menu
     "func": "custom_cmd_func", # the name of function to run
     "admin": False}, # should the command be admin only?

    {"cmd": "custom2",
     "desc": "Custom command 2", 
     "func": "custom_cmd2_func",
     "admin": False},
]

COMMANDS_LKUP = {c["cmd"]: c for c in CUSTOM_CMDS}

### the command functions (make sure the function names match "func" for the corresponding command above!)

def custom_cmd_func(message):
    if not authenticate(message.from_user.id,"run the first custom command",COMMANDS_LKUP["custom"]["admin"]): # this is how the bot authenticates by default, make sure to change these values so everything works correctly
        return
    bot.reply_to(message,"hi there!")

def custom_cmd2_func(message):
    if not authenticate(message.from_user.id,"run the second custom command",COMMANDS_LKUP["custom2"]["admin"]):
      return
    bot.reply_to(message,"omg that's the second custom command")
