from core.utils.plugins import *

import discord


def div_lst(lst: list, size):
    return [lst[i: i + size] for i in range(0, len(lst), size)]

'''async def cns_webhook(guild, channel_list, amount, content):
    webhooks = []
    for channel in channel_list:
        available_whs = await channel.webhooks()

        if available_whs: 
            webhook = available_whs[0]
            cur_time = datetime.now().strftime("[%H %M %S]")
            print(f"{b}{cur_time} {grn}[SUCESS]  {b}»   {faded(f'got available webhook')}")
        else:
            webhook = await channel.create_webhook(name= "NukerMadebyFinger-Dc:fg27")
            cur_time = datetime.now().strftime("[%H %M %S]")
            print(f"{b}{cur_time} {grn}[SUCESS]  {b}»   {faded(f'created webhook')}")

        
        guild_webhooks = await guild.webhooks()
        print("Available Webhooks in Guild:", len([wh.name for wh in guild_webhooks]), end= "\n")
    
    for _ in range(amount):
        for webhook in webhooks:
            await webhook.send(content= content, username ="NukerMadebyFinger-Dc:fg27")
            cur_time = datetime.now().strftime("[%H %M %S]")
            print(f"{b}{cur_time} {grn}[SUCESS]  {b}»   {faded(f'sent {content}')}")
            await asyncio.sleep(0.1)'''

async def spam_channel(guild, channel_list, amount, content):
    for _ in range(amount):
        for channel in channel_list:
            await channel.send(content)
            cur_time = datetime.now().strftime("[%H %M %S]")
            print(f"{b}{cur_time} {grn}[SUCESS]  {b}»   {faded(f'sent {content}')}")
            



async def sac_init(guild_id, amount, content, token):
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
            for divd_channel in chunked_list:
                task = spam_channel(guild, divd_channel, amount= amount, content= content)
                tasks.append(task)
                await asyncio.sleep(0.4)

            await asyncio.gather(*tasks)
        
        except discord.HTTPException as e:
            if e.status == 429:
                retry_after = int(e.response.headers.get("Retry-After", 3))
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




async def spammallchannel():
    while True:
        cls()

        print(banner)
        print(credits)
        print(spam_all_channel_menu)

        GUILD_ID = get_int_input(f"        {w}[{faded('?')}{w}] {faded('Enter guild id ')}  {b}→ {w}")
        amount = get_int_input(f"        {w}[{faded('?')}{w}] {faded('Enter number of message for each channels ')}  {b}→ {w}")
        content = input(f"        {w}[{faded('?')}{w}] {faded('Enter content of message to send ')}  {b}→ {w}")

        confrm = cf()
        if confrm == "yes": pass 
        elif confrm == "no" or confrm == "back": return
        elif confrm == "edit": continue

        cls()

        await sac_init(GUILD_ID, amount, content, TOKEN)
        

        break
    return

