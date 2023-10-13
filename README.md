# Deleting-Windows-Temp-Files-using-python-script
Python Script for deleting temp files from Windows Local Data folder for anyone who always faces issues with Storage overload. Feel free to modify the code according to your needs :)

To automatically run a Python script when you open your laptop, you can set it up as a startup task. Here's how you can do it:

1. Create a Batch File:

First, create a batch file (.bat) to run your Python script. Please create a new text file and rename it to something like run_clean_temp.bat.

Edit the batch file with a text editor and add the following line:
@pythonw.exe C:\path\to\your\script.py
Note: Replace C:\path\to\your\script.py with the actual path to your Python script.

2. Move the Batch File:

Move the run_clean_temp.bat file to a location where it won't be moved or deleted accidentally. For example, you could place it in your user's Startup folder.

To do this, press Win + R, type shell: startup and press Enter. This will open your user's Startup folder. Place the batch file here.

3. Configure Python Environment:

Ensure that Python is installed on your system and that the path to the Python executable is included in your system's PATH environment variable. This will allow the batch file to find and execute the Python interpreter.

4. Test the Setup:

Restart your computer to see if the Python script runs automatically after startup.

Please be careful when automatically running scripts on startup, since they can possibly cause unexpected behavior if not designed carefully. Make sure your script is well-tested and safe to run on startup.

