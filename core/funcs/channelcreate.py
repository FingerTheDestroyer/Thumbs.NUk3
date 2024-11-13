from core.utils.plugins import *

import discord


async def mass_channels(name, amnt, guild):
    for _ in range(amnt):
        await guild.create_text_channel(name)
        cur_time = datetime.now().strftime("[%H:%M:%S]")
        print(f"{b}{cur_time} {grn}[SUCESS]  {b}»   {faded('created a channel')}")


async def cc_init(guild_id, name, amount, token):
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
                tasks.append(mass_channels(name, amnt_l, guild))
            else:
                amnt = 1
            for _ in range(amount):
                tasks.append(mass_channels(name, amnt, guild))
            
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
 

async def channelcreate():
    while True:
        cls()

        print(banner)
        print(credits)
        print(channel_create_menu)

        GUILD_ID = get_int_input(f"        {w}[{faded('?')}{w}] {faded('Enter guild id ')}  {b}→ {w}")
        amount = get_int_input(f"        {w}[{faded('?')}{w}] {faded('Enter number of channel to create ')}  {b}→ {w}")
        name = input(f"        {w}[{faded('?')}{w}] {faded('Enter name of new channels ')}  {b}→ {w}")

        confrm = cf()
        if confrm == "yes": pass 
        elif confrm == "no" or confrm == "back": return
        elif confrm == "edit": continue            
        
        cls()

        await cc_init(GUILD_ID, name, amount, TOKEN)
        break
    return

        



