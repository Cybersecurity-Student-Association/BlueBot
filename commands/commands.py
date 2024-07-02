import datetime, time
import discord
from commands.HashingCommands import HashingCommands

class Commands:
    def __init__(self, client: discord.Client, tree: discord.app_commands.CommandTree, servers):
        self.client = client
        self.tree = tree
        self.servers = servers

        self.startTime = time.time()

        self.register_Commands()
        HashingCommands(client=client, tree=tree, servers=servers)
    def register_Commands(self):
        @self.tree.command(name="ping", description="Gives latency between you and the bot")
        async def ping(interaction: discord.Interaction):
            await interaction.response.send_message(f'Pong: {round(self.client.latency, 3)}ms', ephemeral=True)


        @self.tree.command(name="uptime", description="Uptime of BlueBot")
        async def uptime(interaction: discord.Interaction):
            await interaction.response.send_message(str(datetime.timedelta(seconds=int(round(time.time()-self.startTime)))), ephemeral=True)