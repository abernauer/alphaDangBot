# bot py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

description = '''An example dangbot for Dan Gheesling's discord server or guild


There are a number of utility commands shown here.'''


# get the path of the directory this files is in

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# establish the intents of the commands for the bot

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-------')


@bot.command()
async def goals(ctx):
    """Returns the three goals of the 596"""
    await ctx.send("1. clean. 2. positive. 3. entertainment".upper())


@bot.command()
async def bruh(ctx):
    """ Returns the dangBRUH emote ten times """
    await ctx.send(' '.join(['<:dangBRUH:661420374390603776>',
                             '<:dangBRUH:661420374390603776>',
                             '<:dangBRUH:661420374390603776>',
                             '<:dangBRUH:661420374390603776>',
                             '<:dangBRUH:661420374390603776>',
                             '<:dangBRUH:661420374390603776>',
                             '<:dangBRUH:661420374390603776>',
                             '<:dangBRUH:661420374390603776>',
                             '<:dangBRUH:661420374390603776>',
                             '<:dangBRUH:661420374390603776>']))


bot.run(TOKEN)
