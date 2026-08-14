import datetime
from config import *
from bot import bot
from strings import *
from colorama import Fore

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
        bot.send_message(user_id, strings[language]["msg.notanadmin"],parse_mode="Markdown")
    print(f"[AUTH] {user_id} tried requesting to {target}, but isn't a user")
    bot.send_message(user_id, strings[language]["msg.403"],parse_mode="Markdown")
    return False