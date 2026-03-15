# Custom commands file
# Create your custom features here! You'll be able to run any of these in your bot.
# That's only for advanced coders, so only create these if you know what you're doing.

# Useful helper functions:
# get_time(offset (int, in seconds) - outputs the time in HH:mm:ss (HH:mm:ss AM/PM for 12-hour time) + the offset in seconds (default 0)
# take_screenshot(chat_id)
# record_video_ram(chat_id, length (int, in seconds), bitrate (str, ####k))
# authenticate(user_id, target (str), adminOnly)
# is_admin(user_id) - returns "y" or "n"
# delete_msg(message)

# command list

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

# the command functions

def custom_cmd_func(message):
    if not authenticate(message.from_user.id,"run the first custom command",COMMANDS_LKUP["custom"]["admin"]): # this is how the bot authenticates by default, make sure to change these values so everything works correctly
        return
    bot.reply_to(message,"hi there!")

def custom_cmd2_func(message):
    if not authenticate(message.from_user.id,"run the second custom command",COMMANDS_LKUP["custom2"]["admin"]):
      return
    bot.reply_to(message,"omg that's the second custom command")
