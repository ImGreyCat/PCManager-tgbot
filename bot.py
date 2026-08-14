import telebot
from config import *
from colorama import Fore
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