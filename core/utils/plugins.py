from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from colorama import Fore, Style
from datetime import datetime

import os
import fade
import asyncio

grn = '\x1b[38;5;46m'
r = '\x1b[38;5;196m'
b = Fore.LIGHTBLACK_EX
w = Fore.WHITE

def faded(text):
    faded = ""
    blue = 255
    val = ( 255 // len(list(text))) - 5
    for char in list(text):
        faded += (f"\033[38;2;255;0;{blue}m{char}\033[0m")
        if not blue == 0:
            blue -= val
            if blue < 0:
                blue = 0
    return faded

def cls():
    os.system('cls')

with open("token.txt", "r") as f:
    TOKEN = f.readline().strip()


def get_int_input(text):
    while True: 
        ans = input(text).strip()
        if ans.isdigit(): break
        else: 
            print(f"        {w}[{faded('!')}{w}] {faded('Only input numbers !')}")
    
    return int(ans)


def cf():
    while True:
        ans = input(f"        {w}[{faded('?')}{w}] {faded('Are you sure? (y/n/options) ')}  {b}→ {w}").strip().lower()
        if ans == "y": return "yes"
        elif ans == "n": return "no"
        elif ans == "1": return "edit"
        elif ans == "2": return "back"
        else: pass



banner = fade.pinkred('''
                      ________                    __      _   __      __  _____
                     /_  __/ /_  __  ______ ___  / /_    / | / /_  __/ /_|__  /
                      / / / __ \/ / / / __ `__ \/ __ \  /  |/ / / / / //_//_ < 
                     / / / / / / /_/ / / / / / / /_/ / / /|  / /_/ / ,< ___/ / 
                    /_/ /_/ /_/\__,_/_/ /_/ /_/_.___(_)_/ |_/\__,_/_/|_/____/  ''')

credits = f'''                                     {b}Made by: {faded("Finger")}   {b}discord: {faded("fg27")}
'''

#print(banner)

menu = f'''
            {w}[{faded("1")}{w}] {faded("create channels")}           {w}[{faded("4")}{w}] {faded("Full Nuke")}                   {w}[{faded("e")}{w}] {faded("exit")}
            {w}[{faded("2")}{w}] {faded("delete all channels")}       {w}[{faded("5")}{w}] {faded("Create emojis (slow)")}
            {w}[{faded("3")}{w}] {faded("spam all channels")}         {w}[{faded("6")}{w}] {faded("Delete all emojis (slow)")}       
            

'''

channel_create_menu = f'''
            {w}[{faded("INFO")}{w}] {faded("This tool mass create channels")}

            {w}[{faded("OPTIONS")}{w}]
            {w}[{faded("1")}{w}] {faded("Edit")}
            {w}[{faded("2")}{w}] {faded("Return")}

'''

channel_delete_menu = f'''             
            {w}[{faded("INFO")}{w}] {faded("This tool mass create channels")}

            {w}[{faded("OPTIONS")}{w}]
            {w}[{faded("1")}{w}] {faded("Edit")}
            {w}[{faded("2")}{w}] {faded("Return")}

'''

full_nuke_menu = f'''             
            {w}[{faded("INFO")}{w}] {faded('delete all channels, create channels and spam')}

            {w}[{faded("OPTIONS")}{w}]
            {w}[{faded("1")}{w}] {faded("Edit")}
            {w}[{faded("2")}{w}] {faded("Return")}

'''

spam_all_channel_menu = f'''             
            {w}[{faded("INFO")}{w}] {faded("spam every channels")}

            {w}[{faded("OPTIONS")}{w}]
            {w}[{faded("1")}{w}] {faded("Edit")}
            {w}[{faded("2")}{w}] {faded("Return")}

'''

create_emoji_menu = f'''             
            {w}[{faded("INFO")}{w}] {faded("create emojis")}

            {w}[{faded("OPTIONS")}{w}]
            {w}[{faded("1")}{w}] {faded("Edit")}
            {w}[{faded("2")}{w}] {faded("Return")}

'''

delet_emoji_menu = f'''             
            {w}[{faded("INFO")}{w}] {faded("create emojis")}

            {w}[{faded("OPTIONS")}{w}]
            {w}[{faded("1")}{w}] {faded("Edit")}
            {w}[{faded("2")}{w}] {faded("Return")}

'''
