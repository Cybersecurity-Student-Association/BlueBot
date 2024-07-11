import discord
from embeds import clubinfo as embed_clubinfo, roles as embed_roles, rules as embed_rules


class EmbedCommands:
    def __init__(self, client: discord.Client, tree: discord.app_commands.CommandTree):
        self.client = client
        self.tree = tree

        self.register_EmbedCommands()

    def register_EmbedCommands(self):
        @self.tree.command(name="clubinfo", description="Posts information about the club")
        async def clubinfo(interaction: discord.Interaction):
            await interaction.response.send_message(embed=embed_clubinfo.clubinfo, ephemeral=True)

        @self.tree.command(name="rules", description="Posts the rules")
        async def rules(interaction: discord.Interaction):
            await interaction.response.send_message(embed=embed_rules.rules, ephemeral=True)

        @self.tree.command(name="roles", description="Posts the roles and their descriptions")
        async def roles(interaction: discord.Interaction):
            await interaction.response.send_message(embed=embed_roles.roles, ephemeral=True)
