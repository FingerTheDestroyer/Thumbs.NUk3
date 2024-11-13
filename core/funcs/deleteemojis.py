from core.utils.plugins import *

import discord

def div_lst(lst: list, size):
    return [lst[i: i + size] for i in range(0, len(lst), size)]

async def delete_emoji(emoji_list):
    for emoji in emoji_list:
        await emoji.delete()
        cur_time = datetime.now().strftime("[%H:%M:%S]")
        print(f"{b}{cur_time} {grn}[SUCESS]  {b}»   {faded('deleted an emoji')}")
        await asyncio.sleep(0.5)


async def de_init(guild_id, token):
    intents = discord.Intents.all()
    bot = discord.Client(intents= intents)

    @bot.event
    async def on_ready():
        cur_time = datetime.now().strftime("[%H:%M:%S]")
        st = str(bot.user.name) + " loaded"
        print(f"{b}{cur_time} {grn}[CONNECTED]  {b}»   {faded(st)}")

        guild = bot.get_guild(guild_id)
        
        emoji_list = guild.emojis
        size = (len(emoji_list) // 2) + 1
        chunked_list = div_lst(emoji_list, size)
        tasks = []

        try:
            for divd_lst in chunked_list:
                task = delete_emoji(divd_lst)
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





async def deleteemoji():
    while True:
        cls()

        print(banner)
        print(credits)
        print(delet_emoji_menu)

        GUILD_ID = get_int_input(f"        {w}[{faded('?')}{w}] {faded('Enter guild id ')}  {b}→ {w}")

        confrm = cf()
        if confrm == "yes": pass 
        elif confrm == "no" or confrm == "back": return
        elif confrm == "edit": continue

        cls()

        await de_init(GUILD_ID, TOKEN)
        break
    return