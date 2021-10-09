import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="-", intents=intents)

token = "Your bot token"

@bot.event
async def on_ready():
    print("Online")

@bot.command()
async def dm(ctx):
    dm_message = "What you want to send to people here"
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            if member.id == bot.user.id:
                pass
            else:
                await member.send(dm_message)
                print(f"Sent to {member}")
                # To not be rate limited
                await asyncio.sleep(1)
        except:
            print(f"Couldn't send to {member}")


bot.run(token)
