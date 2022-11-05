from PIL import Image
import random
import os
import webbrowser
import requests
import images
import glob
import time
from getpass import getpass

class Color:
    # text

    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'
    lightblue = '\033[94m'
    reset = '\033[37m'

class Background:
    # background

    black = '\033[40m'
    red = '\033[41m'
    green = '\033[42m'
    yellow = '\033[43m'
    blue = '\033[44m'
    magenta = '\033[45m'
    cyan = '\033[46m'
    white = '\033[47m'

class Font:
    bold = '\033[1m'
    end = '\033[0m'

print('loading OS')
print(f"{Color.blue}▒▒▒▒▒▒▒▒▒▒▒▒▒0%")
time.sleep(random.uniform(0.09, 0.5))
print(f"{Color.blue}██▒▒▒▒▒▒▒▒▒▒▒10%")
time.sleep(random.uniform(0.09, 0.5))
print(f"{Color.blue}███▒▒▒▒▒▒▒▒▒▒20%")
time.sleep(random.uniform(0.09, 0.5))
print(f"{Color.blue}████▒▒▒▒▒▒▒▒▒30%")
time.sleep(random.uniform(0.09, 0.5))
print(f"{Color.blue}█████▒▒▒▒▒▒▒▒40%")
time.sleep(random.uniform(0.09, 0.5))
print(f"{Color.blue}███████▒▒▒▒▒▒50%")
time.sleep(random.uniform(0.09, 0.5))
print(f"{Color.blue}█████████▒▒▒▒60%")
time.sleep(random.uniform(0.09, 0.5))
print(f"{Color.blue}██████████▒▒▒70%")
time.sleep(random.uniform(0.09, 0.5))
print(f"{Color.blue}███████████▒▒80%")
time.sleep(random.uniform(0.09, 0.5))
print(f"{Color.blue}████████████▒90%")
time.sleep(random.uniform(0.09, 0.5))
print(f"{Color.blue}█████████████100%{Color.reset}")
print(f"""
            {Color.yellow}{images.pyminiLogo}{Color.reset}
""")

for i in range(50):
    print("\n")

password = getpass(f"{Font.bold}{Color.red}Please Enter password(password wont be shown)\n{Color.yellow}")

with open("pymini3\\3.0\\password.txt", "r") as f:
    passwordTrue = f.read()
    if passwordTrue == None:
        print(f"{Color.reset}password doesn't exist\nPlease Enter a password")
        password_create = input(f"{Color.yellow}")
        print(Color.reset)
        fopen = open("pymini3\\3.0\\password.txt", "w")
        fopen.write(password_create)
    else:
        if password == passwordTrue:
            print("Entered To pyminiOS3")
            print(f"{Color.blue}{images.wallpaper1}{Color.reset}")
            main=input(f"{Color.yellow}")
            print(Color.reset)

            if main.lower() == "games":
                print()

            if main.lower() == "pshop":
                print("Welcome to PShop")
                

            if main.lower() == "broswer":
                print("welcome to glob")            
                print("Enter What you want (Url, google search)")
                broswer=input(f"{Font.bold}{Color.yellow}")
                print(Color.reset)
                if broswer == "url":
                    url=input(f"{Font.bold}{Color.yellow}")
                    print(Color.reset)
                    response = requests.get(f"https://{url}")
                    if response.status_code == 200:
                        webbrowser.open(url)
                    else:
                        print('Web site does not exist') 
                    
                if broswer == "search":
                    search=input(f"{Font.bold}{Color.yellow}")
                    print(Color.reset)
                    webbrowser.open(f"https://www.google.com/search?client=firefox-b-d&q={search}")

                
            if main.lower() == "photos":
                print("Do you want to enter the path or the file name and have us to research where it is? (path, file name)")
                Cphoto=input(Color.yellow+"")
                print(Color.reset)

                if Cphoto == 'path':
                    PhotoPath=input(f"Please enter the file path\n{Color.yellow}")
                    print(Color.reset)
                    img = Image.open(PhotoPath)
                    img.show()

                if Cphoto == "file name":
                    photoStyle=input(f"is it a png jpg what is it?\n{Color.yellow}")
                    photoName=input(f"Name\n{Color.yellow}")
                    File = glob.glob(f'**/{photoName}.{photoStyle}', recursive=True)
                    print(f"opening {File}...")
                    confirm = input(f"n/y\n{Color.yellow}")
                    if confirm == "y":
                        img = Image.open(f"{File}")
                        img.show()  