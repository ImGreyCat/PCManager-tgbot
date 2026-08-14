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
        "msg.startedEXE": "🔌 .exe макроса запущен!",
        "msg.sendingAltF4": "Закрываю приложение спереди...",
        "msg.sentAltF4": "✅ Alt+F4 успешно отправлено!",
        "msg.minimizingAll": "Сворачиваю все приложения...",
        "msg.startsent_vid": "▶️ Клавиша старта отправлена, записываю видео...",
        "msg.startsent_novid": "▶️ Клавиша старта отправлена!",
        "msg.stopsent": "⏹ Клавиша стоп отправлена!",
        "msg.nokey": "❌ Не указана клавиша.\nСинтаксис: /keyboard <клавиша>",
        "msg.invalidkey": "❌ Неверно указано клавиша.\nСинтаксис: /keyboard <клавиша>\nКлавиши: a-z, 0-9, ctrl, alt, win, shift, space, enter",
        "msg.sentkey": "✅ Клавиша {SENTKEY} успешно отправлена!",
        "msg.sendingWinD": "Отправляю Win+D...",
        "msg.takingscreenshot": "Делаю скриншот...",
        "msg.recordingvideo": "Записываю видео...",
        "msg.checkingping": "Быстренько проверяю пинг с Telegram API...",
        "caption.screenshot": "[{NOW}] Скриншот",
        "caption.video": "[{NOW}] Видео",
        "msg.BON": "🟢 Бот онлайн!\nПК: *{HOSTNAME}*\nВремя: *{NOW}*",
        "msg.403": "❌ У вас нет разрешения на управление ботом.\nЕсли вы считаете, что я ошибаюсь, пожалуйста, напишите админу.",
        "msg.notanadmin": "❌ Недостаточно прав. Только администраторы могут использовать эту команду.",
        "msg.pendingstop": "*🛑 Запланирована остановка бота через {SHTDWNDELAY} секунд!*\n(!) Бот перестанет работать, но компьютер останется включённым.\n\nОстановка в: *{SHTDWNTIME}*\nОтменить: */cancelshutdown*",
        "msg.pendingshutdown": "*💤 Запланировано выключение компьютера через {SHTDWNDELAY} секунд!!*\n(!!!) После выключения бот перестанет работать!\n\nВыключение в: *{SHTDWNTIME}*\nОтменить: */cancelshutdown*",
        "msg.pendingreboot": "*🔄 Запланирована перезагрузка компьютера через {SHTDWNDELAY} секунд!*\n(!!) После перезагрузки бот может перестать работать\n\nПерезагрузка в: *{SHTDWNTIME}*\nОтменить: */cancelshutdown*",
        "msg.shtdwnnotpending": "Насколько мне известно, компьютер выключаться не собирался...",
        "msg.alrpending": "*Ошибка*: уже планируется *{PENDINGSHUTDOWNTYPE}* в *{SHTDWNTIME}*.\nНеобходимо сначала отменить это действие: */cancelshutdown*",
        "msg.cnclpendingshutdown": "✅ Успешно отменено запланированное действие: {TYPE}.",
        "msg.welcome": "\
Здравствуйте, {NAME}! ✅ Бот активен и вы имеете права на управление.\n\
Доступные команды:\n\
/start - получить это сообщение\n\
/launch - запустить .exe макроса\n\
/alt_f4 - закрыть приложение в фокусе\n\
/startmacro - послать старт\n\
/stopmacro - послать стоп\n\
/keyboard - послать клавишу на компьютер\n\
/screenshot - сделать скриншот\n\
/video - записать видео\n\
/stop - остановить бота\n\
/shutdown - выключить компьютер\n\
/reboot - перезагрузить компьютер\n\
/cancelshutdown - отменить запланированное действие\n\
/settings - просмотреть текущие настройки\n\
/info - посмотреть разную информацию о боте\n\n\
\
Сделано @ImGreyCat с <3",
        "msg.info": "\
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

        "msg.settings": "\
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
        "msg.updatedcmds": "Список команд обновлён успешно.\nВнимание! Вы можете не увидеть изменения, пока полностью не перезапустите Telegram.",
        "cmddesc.start": "Приветственное сообщение",
        "cmddesc.launch": "Запустить .exe макроса",
        "cmddesc.alt_f4": "[✨ Новое] Закрыть приложение в фокусе",
        "cmddesc.minimize_all": "[✨ Новое] Свернуть все приложения",
        "cmddesc.startmacro": 'Нажать кнопку "старт"',
        "cmddesc.stopmacro": 'Нажать кнопку "стоп"',
        "cmddesc.keyboard": '[✨ Новое] Отправить клавишу на компьютер',
        "cmddesc.screenshot": "Сделать скриншот",
        "cmddesc.video": "Записать видео",
        "cmddesc.stop": "[✨ Новое] Выключить бота",
        "cmddesc.shutdown": "[✨ Новое] Выключить компьютер",
        "cmddesc.reboot": "[✨ Новое] Перезагрузить компьютер",
        "cmddesc.cancelshutdown": "[✨ Новое] Отменить перезагрузку/выключение",
        "cmddesc.settings": "[✨ Новое] Получить текущие настройки",
        "cmddesc.changemacro": "[✨ Новое] Изменить текущий макрос",
        "cmddesc.info": "Разная информация о боте",
        "cmddesc.help": "[✨ Новое] Справка по командам",
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
        "msg.startedEXE": "🔌 Started macro .exe!",
        "msg.sendingAltF4": "Closing focused app...",
        "msg.sentAltF4": "✅ Sent Alt+F4 successfully!",
        "msg.startsent_vid": "▶️ Start key sent, recording a video...",
        "msg.startsent_novid": "▶️ Start key sent!",
        "msg.stopsent": "⏹ Stop key sent!",
        "msg.nokey": "❌ No key specified.\nSyntax: /keyboard <key>\nAvailable keys: a-z, 0-9, ctrl, alt, win, shift, space, enter",
        "msg.invalidkey": "❌ Invalid key specified.\nSyntax: /keyboard <key>\nAvailable keys: a-z, 0-9, ctrl, alt, win, shift, space, enter",
        "msg.sentkey": "✅ Sent key {SENTKEY} successfully!",
        "msg.sendingWinD": "Sending Win+D...",
        "msg.takingscreenshot": "Taking a screenshot...",
        "msg.checkingping": "Pinging the Telegram API real quick...",
        "caption.screenshot": "[{NOW}] Screenshot",
        "caption.video": "[{NOW}] Video",
        "msg.BON": "🟢 Now online!\nPC: *{HOSTNAME}*\nTime: *{NOW}*",
        "msg.403": "❌ You do not have permission to use the bot.\nIf you think I'm mistaken, please contact the admin.",
        "msg.notanadmin": "❌ Insufficient permissions. Only admins can use this command.",
        "msg.pendingstop": "*🛑 Bot stop scheduled in {SHTDWNDELAY} seconds!*\n(!) The bot will stop working, but the computer will keep running.\n\nStopping at: *{SHTDWNTIME}*\nCancel: */cancelshutdown*",
        "msg.pendingshutdown": "*💤 Computer shutdown scheduled in {SHTDWNDELAY} seconds!!*\n(!!!) The bot will stop working after shutdown!\n\nShutting down at: *{SHTDWNTIME}*\nCancel: */cancelshutdown*",
        "msg.pendingreboot": "*🔄 Computer reboot scheduled in {SHTDWNDELAY} seconds!*\n(!!) The bot may stop working after reboot\n\nRebooting at: *{SHTDWNTIME}*\nCancel: */cancelshutdown*",
        "msg.shtdwnnotpending": "As far as I can see, the computer doesn't have a scheduled shutdown...",
        "msg.alrpending": "*Error*: there's already a *{PENDINGSHUTDOWNTYPE}* pending at *{SHTDWNTIME}*.\nTo schedule a shutdown, please cancel this one first: */cancelshutdown*",
        "msg.cnclpendingshutdown": "✅ Cancelled pending {TYPE} successfully.",
        "msg.welcome": "\
Hey there {NAME}! ✅ The bot is online and you have permission to use it.\n\
Commands:\n\
/start - see this message\n\
/launch - launch macro .exe\n\
/alt_f4 - close focused app\n\
/startmacro - send start key\n\
/stopmacro - send stop key\n\
/keyboard - send a key of your choice\n\
/screenshot - take a screenshot\n\
/video - record a video\n\
/stop - stop bot\n\
/shutdown - shutdown pc\n\
/reboot - reboot pc\n\
/cancelshutdown - cancel pending shutdown\n\
/settings - view current settings\n\
/info - get various info\n\n\
\
Made by @ImGreyCat with <3",
        "msg.info": "\
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

        "msg.settings": "\
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
        "msg.updatedcmds": "Commands succesfully refreshed.\nPlease note that you might need to fully restart Telegram for the changes to show!",
        "cmddesc.start": "Welcome message",
        "cmddesc.launch": "Launch macro .exe",
        "cmddesc.alt_f4": "[✨ New] Close focused app",
        "cmddesc.minimize_all": "[✨ New] Minimize all apps",
        "cmddesc.startmacro": "Send start key",
        "cmddesc.stopmacro": "Send stop key",
        "cmddesc.keyboard": "[✨ New] Send key",
        "cmddesc.screenshot": "Take a screenshot",
        "cmddesc.video": "Record a video",
        "cmddesc.stop": "[✨ New] Stop the bot",
        "cmddesc.shutdown": "[✨ New] Turn off PC",
        "cmddesc.reboot": "[✨ New] Reboot PC",
        "cmddesc.cancelshutdown": "[✨ New] Cancel pending shutdown",
        "cmddesc.settings": "[✨ New] View current settings",
        "cmddesc.changemacro": "[✨ New] Change current macro",
        "cmddesc.info": "Various info",
        "cmddesc.help": "[✨ New] Command help",
    }
}