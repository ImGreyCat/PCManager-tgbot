import PyInstaller.__main__

print("Building binary with PyInstaller...")
try:
    PyInstaller.__main__.run([
        'main.py',
        '-y',
        '--clean',
        '--exclude-module', 'config',
        '--exclude-module', 'custom',
        '--exclude-module', 'devSettings',
        '--exclude-module', 'locales',
        '--name=PCManager',
        # '--icon=icon.ico'
    ])
except Exception as e:
    print(f"Something went wrong!\n{e}")
else:
    print("All done!")