import sys, subprocess


if sys.platform.startswith('win'):
    code = subprocess.call("notepad")
    if code == 0:
        print("Notepad successfully executed")
    else:
        print("Starting notepad failed")
else:
    print(sys.platform)

