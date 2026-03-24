# PCManager-tgbot
A Telegram bot for managing your computer and game macros remotely\
Built with pytelegrambotapi on pure spaghetti code!\
<img width="269" height="246" alt="funnyscreenshot" src="https://github.com/user-attachments/assets/65fc9f48-58e3-48f0-99f8-e854b1812a3a" />

# Features
- Setting up multiple users/admins
- Launching your preferred macro's .exe
- Starting/stopping your preferred macro
- Sending any keys to the keyboard
- Taking screenshots and recording videos from your screen
- Shutting down or rebooting the PC
- Using a proxy to connect to Telegram
- Can't find your favorite feature here? Create it using custom commands! 

# Quick Setup
1. **Download the release**\
You can get the latest release [here](https://github.com/ImGreyCat/PCManager-tgbot-dev/releases/latest).
2. **Extract the files**
3. **Set up your config in config.py**
4. **Launch PCManager.exe**
5. **You're ready to go!**

# Manual Setup
You can download the rolling version of the code to try new features before releases! Here's how to do it:

> [!NOTE]
> Linux and macOS *are* technically supported, but the bot is mostly designed for Windows.
> To start on these OSes, set bypassSystemCheck to True in the config file.

1. **Download the source code**\
Click the green Code button, then download ZIP to download the code.
   
2. **Install ffmpeg**
> **For Windows: download the build from gyan.dev (personally recommend this)**\
> [Download this 7z archive](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z) and extract it to C:\ffmpeg

> **Add ffmpeg to PATH**\
> Open Search, find and open "Edit the system environment variables", then add C:\ffmpeg\bin to the system Path variable.

> **For Linux/macOS:**\
> Install ffmpeg with your system's package manager.

3. **Install Python**

Visit https://www.python.org/downloads/windows/ to download and install Python.\
Make sure to install the built-in library as well. 

4. **Install requirements**
> **Automatic installation with pip**\
> Launch the [requirements.py](requirements.py) file to automatically install all requirements with pip.

> **[requirements.txt](requirements.txt)**\
> This file has all required modules for manual installation. 

# Need help?
If you have any questions, found a bug, or need help, simply open an issue [here](https://github.com/ImGreyCat/PCManager-tgbot-dev/issues/new/choose).
Feel free to also create pull requests.

# To do

 - [X] Add custom commands support
 - [ ] Move to asynchronous 
 - [ ] Support for multiple macro .exes and launching them separately
 - [ ] De-spaghetti the code

## RAT Note
This bot is not a RAT (Remote Access Trojan). It's designed only for personal convenience and should only be used on computers you own or have explicit permission to access.
Requests for malicious/troll features will be rejected.
