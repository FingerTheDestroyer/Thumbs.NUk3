from core.utils.plugins import *

import discord


async def create_emojis(file_path, amnt, name, guild):
    with open(file_path, "rb") as f:
        image_data = f.read()
        for _ in range(amnt):
            await guild.create_custom_emoji(name = name, image = image_data)
            cur_time = datetime.now().strftime("[%H:%M:%S]")
            print(f"{b}{cur_time} {grn}[SUCESS]  {b}»   {faded('created an emoji')}")
            
            await asyncio.sleep(0.5)


async def ce_init(guild_id, amount, file_path, name, token):
    intents = discord.Intents.all()
    bot = discord.Client(intents= intents)
    
    @bot.event
    async def on_ready():
        cur_time = datetime.now().strftime("[%H:%M:%S]")
        st = str(bot.user.name) + " loaded"
        print(f"{b}{cur_time} {grn}[CONNECTED]  {b}»   {faded(st)}")

        guild = bot.get_guild(guild_id)

        tasks = []

        try: 
            amnt = amount // 10
            amnt_l = amnt - (amnt // 10)

            if amount > 10: 
                tasks.append(create_emojis(file_path, amnt_l, name, guild))
            else:
                amnt = 1
            for _ in range(amount):
                tasks.append(create_emojis(file_path, amnt, name, guild))
            
            await asyncio.gather(*tasks)
        
        except discord.HTTPException as e:
            if e.status == 429:
                retry_after = int(e.response.headers.get("Retry-After", 5))
                print(f"{b}{cur_time} {r}[RATELIMIT]  {b}»   {faded(f'Ratelimited, retry after {retry_after} seconds')}")


        except Exception as e:
            cur_time = datetime.now().strftime("[%H:%M:%S]")
            print(f"{b}{cur_time} {r}[FAILURE]  {b}»   {faded(f'Issues arisen: {e}')}")
        
        finally: 
            await bot.close()
    
    try: 
        await bot.start(token)
    finally:
        await bot.close()






async def createemoji():
    while True:
        cls()

        print(banner)
        print(credits)
        print(create_emoji_menu)

        GUILD_ID = get_int_input(f"        {w}[{faded('?')}{w}] {faded('Enter guild id ')}  {b}→ {w}")
        file_path = (input(f"        {w}[{faded('?')}{w}] {faded('Enter file path ')}  {b}→ {w}").strip('"').replace(" ", "_"))
        file_path = rf"{file_path}"
        name = input(f"        {w}[{faded('?')}{w}] {faded('Enter name of new emojis ')}  {b}→ {w}")
        amount = get_int_input(f"        {w}[{faded('?')}{w}] {faded('Enter number of emojis to create ')}  {b}→ {w}")

        confrm = cf()
        if confrm == "yes": pass 
        elif confrm == "no" or confrm == "back": return
        elif confrm == "edit": continue

        cls()

        await ce_init(GUILD_ID, amount, file_path, name, TOKEN)
        break
    return