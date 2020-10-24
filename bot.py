# bot py
import random
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
async def awwa(ctx):
    """Returns Appreciate Where We Are"""
    await ctx.send("appreciate where we are".title())

    
@bot.command()
async def bruh(ctx):
    """ Returns the dangBRUH emote ten times """
    dangBruh = ['<:dangBRUH:661420374390603776>',
                '<:dangBRUH:661420374390603776>',
                '<:dangBRUH:661420374390603776>',
                '<:dangBRUH:661420374390603776>',
                '<:dangBRUH:661420374390603776>',
                '<:dangBRUH:661420374390603776>',
                '<:dangBRUH:661420374390603776>',
                '<:dangBRUH:661420374390603776>',
                '<:dangBRUH:661420374390603776>',
                '<:dangBRUH:661420374390603776>']
    await ctx.send(' '.join(str(d) for d in dangBruh))


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


@bot.command()
async def danglishDict(ctx):
     """Returns a random entry from a danglish dictionary"""
# allocate the dictionary
     dangDict = {"3-2 Drop on Stenoma (phrase) -" : """Reference to an Ultima Online Forever Youtube videofrom 2013 titled "UOForver IDOC PvP." Used to denote when to drop in a Battle Royale game. Reference to an Ultima Online Forever Youtube video from 2013 titled "UOForever IDOC PvP"."Stenoma" is a misspelling of Stunoma, the username of a player who was being targeted in PvP combat in the video.""",
"Acquiesce (verb) -" : """To give something up or to concede. Also used interchangeably in place of the word "acquire," and sometimes abbreviated as "acq.""""",
"Andor Landor (noun) -" : """Misspelling of "Anor Londo," a city from Dark Souls. Used interchangably with seemingly and location.""" ,
"AWWA (phrase) -" : """Appreciate Where We Are. Originally used in Dan's "Getting Over it with Bennet Foddy" playthrough as a reminder that progress is temporary and to be thankful for each bit of progress made.""",
 "Ball Player (noun) -" : """A strong competitor, often used in the form of the phrase "they've got ball players too" to describe an enemy that is stronger than expected or remind oneself not to underestimate the enemy. """,
            "Cerso Yeet (proper noun) -" : """Dan's Dark Souls character, who has to date been played in: Dark Souls, Dark Souls 2, Dark Souls 3, Bloodborne, Demon's Souls, Sekiro: Shadows Die Twice, Enter the Gungeon, and Undertale. Partially named after Cersei Lannister from Game of Thrones.""", "Chip and a Chair (phrase) - " : """Poker phrase that refers to a player with a single chip and a seat at the table, despite being in the worst possible position, is still not completely out of the game yet. Synonymous with "It's not over until it's over.""""",
  "Coleman (noun) - " : ''' A player who \"camps\" in a shooter game. (Staying in one position and waiting for enemies.) Reference to the brand of camping equipment.''',
  'Crack Open a Cold One (phrase) -' : '''Catchphrase that precedes almost every Team Unity Tuesday intro, usually with a pop-top soda can sound effect (real or digital) to accompany it. \"Cracking open a cold one\" is a phrase that means to open a cold beverage (often a beer or soda) and relax. Abbreviated as COAC1.''',
  'DGDQ(phrase)-' : """Dan Gheesling Done Quick, a parody of AGDQ (Awesome Games Done Quick) and SGDQ (Summer Games Done Quick), large annual charity speedrunning events. Used to signify a speedrun attempt.""",
  "Dial In (verb) -" : "To focus on a difficult task in order to peform at the best possible capacity",
  "Frame Perfect (adjective) -" : '''So difficult so as to only be possible on an exact frame of gameplay. Also known as "Frame Perfecticity" or abbreviated as FP.''',
  "Front Seat (verb) -" : '''To give advice to someone when asked. The opposite of "backseating"'',
  "Good Eats or Good Wood (noun) -" : "Quality loot or performance. Can be used interchangeably with each other.,
  "Guldan Shower (noun) -" : r"""An infamous invention of Dan's in the Jackbox Party Pack 5 game Patently Stupid. Derived from the phrase "golden shower" and Gul'dan, a recurring antagonist in the Warcraft series.''',
  "Hash Brown (noun) -" : """Spike Trap block from the Mario series. Named after a supposed resemblance to the breakfast food.""",
  "Jail Cell Made Entirely of Cake (phrase) -" : ''' Rhetorical question often asked by Dan: "How do you get out of a jail cell made entirely out of cake? One bite at a time." Refers to the solution to a difficult or arduous task being slow, incremental progress.''',
  "Let's Go (phrase) -" : '''An exclamation that either signifies victory, excitement, or preparedness to move ahead''',
  "Little Brother (adjective) -" : '''Suggestive or inappropriate for a young audience. From "My little brother is watching." signifying there are young children who should not be exposed to the current topic or situation.''',
  "Minkus (adjective) -" : """ Spooky or unsettling. Misspellin of monkaS, a Better Twitch TV emote that denotes fear. Also a reference to Stuart Minkus from Boy Meets World, a Disney TV show.""",
  "Minkus (noun) - " : "Something that causes fear or unsettlement.",
  "Minus Tirth (noun) -" : "A castle or fortified location. Misspelling of Minas Tirith from Lord of the Rings.",
  "Pog (adjective)-" : '''Excited. Shortened form of PogChamp, a Twitch emote. Sometimes called "pogicity."''',
  "Pog (noun) -" : """Better Twitch TV version of PogChamp. Sometimes characterized as a liquid that either rains or is excreted from excitement.""",
  "ProgU (noun) -" : '''Used to denot progress and the excitement from achieving it. Portmanteau of "progress" and "ProgU," a Better Twitch TV emote similar to PogChamp or Pog.''',
  "Quay Bee Bee (noun) -" : '''Quality at-bats. At-bat is a baseball term for their team. Refers to teammates consistently doing well when their team needs them. The name refers to the abbreviation QAB as well as a similar-sounding "lyric" of the Animal Crossing song K.K. Cruisin'. ''',
  "Resin (noun) -" : '''An item or strategy that gives an undue or overpowered advantage, especially one that is easily obtained. Named after the Charcoal Pine Resin, Gold Pine Resin, and Rotten Pine Resin items from Dark Souls.''',
  "Run Your Sets (verb) -" : '''To follow through on one's planned goals. From a coaching/exercise term that reminds one that completing their exercise sets is necessary to acheive their goals.''',
  "Rick Grimes (noun) -" : '''A revolver. Reference to a magnum revolver used in The Walked Dead by the character of the same name. Can also be used to refer to ammo revolver.''',
  "Sit Yourself Down (phrase) -" : '''An exclamation, usually directed as a command towards a recently defeated opponent, telling them to sit down as they have been eliminated from the game.''',
  "Spicy (adjective) -" : "Tense, especially due to high difficulty.",
  "Tony Hawk (verb) -"  : "To switch direction mid-air. Named after the professional skater.",
  "Uncle Mo (noun) -" : "Personification of momentum, usually in a platformer."}
     result = key, val = random.choice(list(dangDict.items()))
     await ctx.send(result)

            
#@bot.listen('on_message')
#async def hugify(message):
#    """ The bot listens for a message that contains a dangHug currently throws """
#
    # we do not want the bot talking to itself
#    if message.author.id == bot.user.id:
#        return

    # we have the name and ID of a custom emoji.
#    dangHug = '<:dangHug:717258283353767959>'
#    await message.add_reaction(dangHug)

    
bot.run(TOKEN)
