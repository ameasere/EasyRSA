# Automatically run CMD commands to compile files
import os
import subprocess

# Get the current working directory
cwd = os.getcwd()
# Remove the "automation" part, replace with UI
cwd = cwd.replace("automation", "UI")
# For file in this folder, run a shell command
for file in os.listdir(cwd):
    # If the file is a .ui file
    if file.endswith(".ui"):
        # Get the file name without the extension
        file_name = file.split(".")[0]
        # Run the shell command
        # Get file with entire path
        file = cwd + "\\" + file
        print(u"\u001b[35;1m Compiling: %s \u001b[0m" % file_name)
        command = "pyside6-uic %s > ui_%s.py" % (file, file_name)
        subprocess.call(command, shell=True)
        print(u"\u001b[32;1m Compiled: %s \u001b[0m" % file_name)
