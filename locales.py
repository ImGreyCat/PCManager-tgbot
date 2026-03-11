# Custom locales file
# You can add localization to other languages here.
# en and ru will be ignored.
# If you don't need custom locales, you can delete this file or just ignore it. It does not break the bot.

# Available writing tools:
# Markdown styling (only in some messages), more info at https://core.telegram.org/bots/api#markdown-style
# \n -- newline

# Some fields have variables in them like this: {VARIABLE}.
# DO NOT translate or alter those, otherwise they won't be replaced with their actual values.
# the "lng" translation example will have all variables left and explained with comments for your convenience

# Note: bad localization may cause errors or instability in the bot. Please be careful when translating!

strings = {
    "lng": {
        "hi": "",
        "ru": "",
        "en": "",
        "other": "", # put your language's native name here (example: "日本語" [Japanese])
        "stop": "",
        "shutdown": "",
        "reboot": "",
        True: "",
        False: "",
        "unknown": "",
        "startedEXE_msg": "",
        "startsent_vid_msg": "",
        "startsent_novid_msg": "",
        "stopsent_msg": "",
        "takingscrshot_msg": "",
        "chkping_msg": "",
        "scrshot_capt": "{NOW}", # {NOW}: current time (HH:MM:SS)
        "vid_capt": "{NOW}",
        "BON_msg": "{HOSTNAME} {NOW}", # {HOSTNAME}: the pc name
        "err403msg": "",
        "notanadmin_msg": "",
        "pendingstop_msg": "{SHTDWNDELAY} {SHTDWNTIME}", # {SHTDWNDELAY}: count in seconds before pc shutdown/bot stop, {SHTDWNTIME}: the time at which the shutdown/stop occurs
        "pendingshutdown_msg": "{SHTDWNDELAY} {SHTDWNTIME}",
        "pendingreboot_msg": "{SHTDWNDELAY} {SHTDWNTIME}",
        "shtdwnnotpending_msg": "",
        "alrpending_msg": "{PENDINGSHUTDOWNTYPE} {SHTDWNTIME}", 
        "cnclpendingshutdown": "{TYPE}", # {TYPE}: type of the cancelled shutdown/stop
        "welcome_msg": "",
        "info_msg": "{NAME} {ISADMIN} {HOSTNAME} {SYSTEM} {RELEASE} {KERNELVER} {NOW} {PING} {HALFPING} {VERSION} {BUILD} {UPTIME} {TMSTATUS}",
        # {NAME} the user's name, {ISADMIN} user is an admin yes/no {{SYSTEM} {RELEASE} {KERNELVER} for most PCs will be like "Windows 11 (10.0.21000)" {PING} {VERSION} {BUILD} {UPTIME} of the bot {TMSTATUS} current testmode status
        "settings_msg": "{LANG} {HI} {STARTKEY} {STOPKEY} {KEYPRESSES} {SHTDWNDELAY} {RECONSTARTISON}"
        # {LANG} current language, {HI} greeting in that language, {KEYPRESSES} how many times bot sends the keys, {RECONSTARTISON} recording on /startmacro on or off
    },
# If you'd like to add a second custom locale, uncomment from here...
#    "lng2": {
#        "1": "",
#        "2": "",
#    }
# ... to here
}      

# Print a message and exit if user runs this as a script
if __name__ == "__main__":
    print("The config file isn't meant to be executed! Please run the main script instead.")
    input("Press Enter to exit...")
    raise SystemExit
