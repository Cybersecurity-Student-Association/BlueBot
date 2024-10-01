import datetime
import time
import discord

from commands.BlueBotCommands import BlueBotCommands
from commands.HashingCommands import HashingCommands
from commands.EmbedCommands import EmbedCommands

from variables.variables import SERVER


class Commands:
    def __init__(self, client: discord.Client, tree: discord.app_commands.CommandTree):
        self.client = client
        self.tree = tree

        self.startTime = time.time()

        self.register_Commands()
        HashingCommands(client=client, tree=tree)
        BlueBotCommands(client=client, tree=tree)
        EmbedCommands(client=client, tree=tree)

    def register_Commands(self):
        @self.tree.command(name="ping", description="Gives latency between you and the bot")
        async def ping(interaction: discord.Interaction):
            if interaction.guild_id != SERVER:
                interaction.response.send_message(content="This bot is not intended for this server.")
                return
            await interaction.response.send_message(f'Pong: {round(self.client.latency, 5)}ms', ephemeral=True)

        @self.tree.command(name="uptime", description="Uptime of BlueBot")
        async def uptime(interaction: discord.Interaction):
            if interaction.guild_id != SERVER:
                interaction.response.send_message(content="This bot is not intended for this server.")
                return
            await interaction.response.send_message(str(datetime.timedelta(seconds=int(round(time.time()-self.startTime)))), ephemeral=True)

        @self.tree.command(name="github", description="Github repository for BlueBot")
        async def github(interaction: discord.Interaction):
            await interaction.response.send_message("https://github.com/Cybersecurity-Student-Association/BlueBot", ephemeral=True)
