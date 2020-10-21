# bot py
import os
import discord
import aiohttp
import re
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


@bot.command()
async def schedule(ctx):
    """Returns the most current schedule"""
    async with aiohttp.ClientSession() as session:
        async with session.get('https://decapi.me/twitter/latest/dangheesling?search=*Show%20Schedule%20for%20Week*') as resp:
            respText = await resp.text()
            dateFor = re.search('(?:\*Show Schedule for Week\* of)\s+(.\S*)', respText).group(1)
            sched = re.search('(?:\(All Times EST\) )(.*)', respText).group(1)
            formatS = re.sub(r'(.\s?\S{,5}\:\s{1,2}\d{1,2}AM|.\s?\S{,5}\:\s{1,2}\d{1,2}PM)',r'\n\n\1',sched)
            buildEmbed = discord.Embed(title=f'Show Schedule for Week of {dateFor}', description=f'https://twitch.tv/dangheesling{formatS}', color=0xFF0000)
            await ctx.send(embed=buildEmbed)

bot.run(TOKEN)
