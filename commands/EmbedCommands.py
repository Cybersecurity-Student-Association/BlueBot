import discord
from embeds import clubinfo as embed_clubinfo, roles as embed_roles, rules as embed_rules
from variables.variables import SERVER

class EmbedCommands:
    def __init__(self, client: discord.Client, tree: discord.app_commands.CommandTree):
        self.client = client
        self.tree = tree

        self.register_EmbedCommands()

    def register_EmbedCommands(self):
        @self.tree.command(name="clubinfo", description="Posts information about the club", guilds=[discord.Object(id=SERVER)])
        async def clubinfo(interaction: discord.Interaction):
            if interaction.guild_id != SERVER:
                interaction.response.send_message(content="This bot is not intended for this server.")
                return
            await interaction.response.send_message(embed=embed_clubinfo.clubinfo, ephemeral=True)

        @self.tree.command(name="rules", description="Posts the rules", guilds=[discord.Object(id=SERVER)])
        async def rules(interaction: discord.Interaction):
            if interaction.guild_id != SERVER:
                interaction.response.send_message(content="This bot is not intended for this server.")
                return
            await interaction.response.send_message(embed=embed_rules.rules, ephemeral=True)

        @self.tree.command(name="roles", description="Posts the roles and their descriptions", guilds=[discord.Object(id=SERVER)])
        async def roles(interaction: discord.Interaction):
            if interaction.guild_id != SERVER:
                interaction.response.send_message(content="This bot is not intended for this server.")
                return
            await interaction.response.send_message(embed=embed_roles.roles, ephemeral=True)
