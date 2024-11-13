from core.utils.plugins import *
from core.funcs.channelcreate import *
from core.funcs.channeldelete import *
from core.funcs.spamallchannel import *
from core.funcs.fullnuke import *
from core.funcs.createemoji import *
from core.funcs.deleteemojis import *

import os
import sys
import asyncio




async def main():
    while True:
        cls()
        os.system("title Thumbs.NUk3")

        print(banner)
        print(credits)
        print(menu)
        

        choice = input(f"        {w}[{faded('?')}{w}] {faded('Choose an option')} {b}→ {w}").strip().lower()

        if choice == "1":
            await channelcreate()
            input("press enter to go back")
            continue

        if choice == "2":
            await channeldelete()
            input("press enter to go back")
            continue
        
        if choice == "3":
            await spammallchannel()
            input("press enter to go back")
            continue

        if choice == "4":
            await fullnuke()
            input("press enter to go back")
            continue
        
        if choice == "5":
            await createemoji()
            input("press enter to go back")
            continue
        
        if choice == "6":
            await deleteemoji()
            input("press enter to go back")
            continue


        if choice == "e":
            sys.exit(0)
        
        else:
            continue


if __name__ == "__main__":
    asyncio.run(main())