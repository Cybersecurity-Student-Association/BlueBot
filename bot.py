import os
import random
import asyncio
import discord

from commands.Commands import Commands
from events.Events import Events
from utils.RSS import RSS
from variables.variables import SERVER, TOKEN
from utils.log import log
from utils.HardwareExchangeProgram import HardwareExchangeProgram


### Register intents and client ###
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
intents.guild_reactions = True
intents.guild_scheduled_events = True
client = discord.Client(intents=intents)


### Slash Commands ###
tree = discord.app_commands.CommandTree(client=client)
servers = [discord.Object(id=SERVER)]


### Listeners ###

@client.event
async def on_ready():

    Commands(client=client, tree=tree, servers=servers)
    Events(client=client)
    HardwareExchangeProgram(client=client, tree=tree)
    await client.wait_until_ready()

    await tree.sync()
    await client.wait_until_ready()

    client.loop.create_task(presence())
    await client.wait_until_ready()

    print(f'{client.user} is ready and listening')
    #await log(client=client, content=f'{client.user} is ready and listening')


async def presence():
    presence_states = [
        #discord.CustomActivity(name="I\'m blue, da ba dee da ba di"),
        discord.Activity(type=discord.ActivityType.watching, name='John Hammond'),
        discord.Activity(type=discord.ActivityType.watching, name='The PC Security Channel'),
        discord.Activity(type=discord.ActivityType.watching, name='NetworkChuck'),
        discord.Activity(type=discord.ActivityType.watching, name='HackerSploit'),
        discord.Activity(type=discord.ActivityType.watching, name='Infosec'),
        discord.Activity(type=discord.ActivityType.watching, name='ComputerPhile'),
        discord.Activity(type=discord.ActivityType.watching, name='David Bombal'),
        discord.Activity(type=discord.ActivityType.watching, name='Dion Training'),
        discord.Activity(type=discord.ActivityType.watching, name='Hak5'),
        discord.Activity(type=discord.ActivityType.watching, name='NahamSec'),
        discord.Activity(type=discord.ActivityType.playing, name='with a Flipper Zero'),
        discord.Activity(type=discord.ActivityType.playing, name='with a WiFi Pineapple'),
        discord.Activity(type=discord.ActivityType.playing, name='with a Rubber Ducky'),
        discord.Activity(type=discord.ActivityType.playing, name='Vulnhub'),
        discord.Activity(type=discord.ActivityType.playing, name='picoCTF'),
        discord.Activity(type=discord.ActivityType.playing, name='Hack The Box'),
        discord.Activity(type=discord.ActivityType.playing, name='TryHackMe'),
        discord.Activity(type=discord.ActivityType.playing, name='Ghidra'),
        discord.Activity(type=discord.ActivityType.listening, name='The WAN Show'),
        discord.CustomActivity(name='Studying for Security+'),
    ]

    while not client.is_closed():
        status = random.choice(presence_states)
        await client.change_presence(activity=status)
        await asyncio.sleep(3600)

if __name__ == "__main__":
    client.run(token=TOKEN)
