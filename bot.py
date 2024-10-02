import os
import random
import asyncio
import discord

from commands.Commands import Commands
from events.Events import Events
from utils.CyberCup import CyberCup
from utils.HardwareExchangeProgram import HardwareExchangeProgram
from utils.RSS import RSS
from variables.variables import SERVER, TOKEN, debug
from utils.log import log


### Register intents and client ###
intents = discord.Intents.none()
intents.message_content = True
intents.members = True
intents.guilds = True
intents.guild_reactions = True
intents.guild_scheduled_events = True
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client=client)


@client.event
async def on_ready():

    Commands(client=client, tree=tree)
    Events(client=client)

    CyberCup(client=client, tree=tree)
    await client.wait_until_ready()

    await tree.sync(guild=discord.Object(id=SERVER))
    await client.wait_until_ready()

    client.loop.create_task(presence())
    await client.wait_until_ready()

    print(f'{client.user} is ready and listening')
    RSS(client=client)
    if debug >= 2:
        await log(client=client, content=f'{client.user} is ready and listening')


async def presence():
    presence_states = [
        discord.CustomActivity(name="I\'m blue, da ba dee da ba di"),
        discord.Activity(type=discord.ActivityType.watching,
                         name='John Hammond', url="https://www.youtube.com/@_JohnHammond"),
        discord.Activity(type=discord.ActivityType.watching, name='The PC Security Channel',
                         url="https://www.youtube.com/channel/UCKGe7fZ_S788Jaspxg-_5Sg"),
        discord.Activity(type=discord.ActivityType.watching,
                         name='NetworkChuck', url="https://www.youtube.com/@NetworkChuck"),
        discord.Activity(type=discord.ActivityType.watching,
                         name='HackerSploit', url="https://www.youtube.com/@HackerSploit"),
        discord.Activity(type=discord.ActivityType.watching,
                         name='Infosec', url="https://www.youtube.com/@InfosecEdu"),
        discord.Activity(type=discord.ActivityType.watching,
                         name='ComputerPhile', url="https://www.youtube.com/@Computerphile"),
        discord.Activity(type=discord.ActivityType.watching,
                         name='David Bombal', url="https://www.youtube.com/@davidbombal"),
        discord.Activity(type=discord.ActivityType.watching,
                         name='IppSec', url="https://www.youtube.com/channel/UCa6eh7gCkpPo5XXUDfygQQA"),
        discord.Activity(type=discord.ActivityType.watching,
                         name='Dion Training', url="https://www.youtube.com/@DionTraining/"),
        discord.Activity(type=discord.ActivityType.watching,
                         name='Hak5', url="https://www.youtube.com/@hak5"),
        discord.Activity(type=discord.ActivityType.watching,
                         name='NahamSec', url="https://www.youtube.com/@NahamSec"),
        discord.Activity(type=discord.ActivityType.playing,
                         name='with a Flipper Zero', url="https://flipperzero.one/"),
        discord.Activity(type=discord.ActivityType.playing, name='with a WiFi Pineapple',
                         url="https://shop.hak5.org/products/wifi-pineapple"),
        discord.Activity(type=discord.ActivityType.playing, name='with a Rubber Ducky',
                         url="https://shop.hak5.org/products/usb-rubber-ducky"),
        discord.Activity(type=discord.ActivityType.playing,
                         name='picoCTF', url="https://picoctf.org/"),
        discord.Activity(type=discord.ActivityType.playing,
                         name='Hack The Box', url="https://www.hackthebox.com/"),
        discord.Activity(type=discord.ActivityType.playing,
                         name='TryHackMe', url="https://tryhackme.com/"),
        discord.Activity(type=discord.ActivityType.playing,
                         name='Ghidra', url="https://ghidra-sre.org/"),
        discord.Activity(type=discord.ActivityType.listening,
                         name='The WAN Show'),
        discord.CustomActivity(name='Studying for Security+'),
    ]

    while not client.is_closed():
        status = random.choice(presence_states)
        await client.change_presence(activity=status)
        await asyncio.sleep(3600)

if __name__ == "__main__":
    client.run(token=TOKEN)
