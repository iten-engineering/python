# =============================================================================
# Python examples - standard libraries sys & subprocess
# =============================================================================

import subprocess
print(dir(subprocess))

code = subprocess.call("notepad.exe")
if code == 0:
    print("Success!")
else:
    print("Error!")

# =============================================================================
# The end.

