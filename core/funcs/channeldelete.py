from core.utils.plugins import *

import discord


def div_lst(lst: list, size):
    return [lst[i: i + size] for i in range(0, len(lst), size)]

async def mass_delete(channel_list: list):
    for channel in channel_list:
        await channel.delete()
        cur_time = datetime.now().strftime("[%H:%M:%S]")
        print(f"{b}{cur_time} {grn}[SUCESS]  {b}»   {faded('deleted a channel')}")


async def cd_init(guild_id, token):
    intents = discord.Intents.all()
    bot = discord.Client(intents= intents)

    @bot.event
    async def on_ready():
        cur_time = datetime.now().strftime("[%H:%M:%S]")
        st = str(bot.user.name) + " loaded"
        print(f"{b}{cur_time} {grn}[CONNECTED]  {b}»   {faded(st)}")
        
        guild = bot.get_guild(guild_id)
        channel_list = guild.channels
        size = (len(channel_list) // 10) + 1
        chunked_list = div_lst(channel_list, size)
        
        try: 
            tasks = []
            for i in range(len(chunked_list)):
                task = mass_delete(chunked_list[i])
                tasks.append(task)

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

                


async def channeldelete():
    while True:
        cls()

        print(banner)
        print(credits)
        print(channel_delete_menu)

        GUILD_ID = get_int_input(f"        {w}[{faded('?')}{w}] {faded('Enter guild id ')}  {b}→ {w}")
        #amount = int(input(faded("Enter amount of channels to delete: ")))
        
        confrm = cf()
        if confrm == "yes": pass 
        elif confrm == "no" or confrm == "back": return
        elif confrm == "edit": continue   

        cls()

        await cd_init(GUILD_ID, TOKEN)
        break
    return