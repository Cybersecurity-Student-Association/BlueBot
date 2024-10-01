import hashlib
import discord
from variables.variables import SERVER

class HashingCommands:
    def __init__(self, client: discord.Client, tree: discord.app_commands.CommandTree):
        self.client = client
        self.tree = tree
        self.register_HashingCommands()

    def register_HashingCommands(self):
        @self.tree.command(name="md5", description="Get the MD5 hash for a string", guilds=[discord.Object(id=SERVER)])
        async def md5(interaction: discord.Interaction, string: str):
            if interaction.guild_id != SERVER:
                interaction.response.send_message(content="This bot is not intended for this server.")
                return
            await interaction.response.send_message(hashlib.md5(string.encode('utf-8')).hexdigest(), ephemeral=True)

        @self.tree.command(name="sha1", description="Get the SHA1 hash for a string", guilds=[discord.Object(id=SERVER)])
        async def sha1(interaction:discord.Interaction, string: str):
            if interaction.guild_id != SERVER:
                interaction.response.send_message(content="This bot is not intended for this server.")
                return
            await interaction.response.send_message(hashlib.sha1(string.encode('utf-8')).hexdigest(), ephemeral=True)

        @self.tree.command(name="sha256", description="Get the SHA256 hash for a string", guilds=[discord.Object(id=SERVER)])
        async def sha256(interaction: discord.Interaction, string: str):
            if interaction.guild_id != SERVER:
                interaction.response.send_message(content="This bot is not intended for this server.")
                return
            await interaction.response.send_message(hashlib.sha256(string.encode('utf-8')).hexdigest(), ephemeral=True)

        @self.tree.command(name="sha512", description="Get the SHA512 hash for a string", guilds=[discord.Object(id=SERVER)])
        async def sha512(interaction: discord.Interaction, string: str):
            if interaction.guild_id != SERVER:
                interaction.response.send_message(content="This bot is not intended for this server.")
                return
            await interaction.response.send_message(hashlib.sha512(string.encode('utf-8')).hexdigest(), ephemeral=True)
