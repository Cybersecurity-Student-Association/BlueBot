import os
import random
import asyncio
import discord

from commands.Commands import Commands
from events.Events import Events
from variables.variables import SERVER, TOKEN


### Register intents and client ###
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)


### Slash Commands ###
tree = discord.app_commands.CommandTree(client=client)
servers = [discord.Object(id=SERVER)]


### Listeners ###

@client.event
async def on_ready():

    Commands(client=client, tree=tree, servers=servers)
    await client.wait_until_ready()
    Events(client=client)
    await client.wait_until_ready()

    await tree.sync()
    await client.wait_until_ready()

    client.loop.create_task(presence())
    await client.wait_until_ready()

    print(f'{client.user} is ready and listening')


async def presence():
    presence_states = [
        discord.CustomActivity(name="I\'m blue, da ba dee da ba di")
    ]

    while not client.is_closed():
        status = random.choice(presence_states)
        await client.change_presence(activity=status)
        await asyncio.sleep(3600)

if __name__ == "__main__":
    client.run(token=TOKEN)
