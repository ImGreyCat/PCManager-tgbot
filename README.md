# PCManager-tgbot
A Telegram bot for managing your computer and game macros remotely
<img width="539" height="492" alt="funnyscreenshot" src="https://github.com/user-attachments/assets/65fc9f48-58e3-48f0-99f8-e854b1812a3a" />

# Features
- Setting up multiple users/admins
- Launching your preferred macro's .exe
- Starting/stopping your preferred macro
- Sending any keys to the keyboard
- Taking screenshots and recording videos from your screen
- Shutting down or rebooting the PC

# Setup
## Windows
1. Install ffmpeg
> **Download the build from gyan.dev (personally recommend this)**\
> [Download this 7z archive](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z) and extract it to C:\ffmpeg

> **Add ffmpeg to PATH**\
> Open Search, find and open "Edit the system environment variables", then add C:\ffmpeg\bin to the system Path variable.

2. Install Python

Visit https://www.python.org/downloads/windows/ to download and install Python.\
Make sure to install the built-in library as well. 

3. Install requirements
> **Automatic installation with pip**\
> Launch the [requirements.py](requirements.py) file to automatically install all requirements with pip.

> **[requirements.txt](requirements.txt)**\
> This file has all required modules for manual installation. 

# To do

 - [ ] Add custom commands support
 - [ ] Move to asynchronous 
 - [ ] Support for multiple macro .exes and launching them separately
 - [ ] De-spaghetti the code 

