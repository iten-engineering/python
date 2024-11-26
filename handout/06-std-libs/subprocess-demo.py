import subprocess 

code = subprocess.call("notepad.exe")

if code == 0:    
    print("Success!")
else:    
    print("Error!")
