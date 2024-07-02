import discord
from embeds import clubinfo, roles, rules


class EmbedCommands:
    def __init__(self, client: discord.Client, tree: discord.app_commands.CommandTree, servers):
        self.client = client
        self.tree = tree
        self.servers = servers

        self.register_EmbedCommands()

    def register_EmbedCommands(self):
        @self.tree.command(name="clubinfo", description="Posts the specified embed in the channel where the command was sent.")
        async def roles(interaction: discord.Interaction):
            await interaction.response.send_message(embed=clubinfo.clubinfo, ephemeral=True)

        @self.tree.command(name="rules", description="Posts the specified embed in the channel where the command was sent.")
        async def roles(interaction: discord.Interaction):
            await interaction.response.send_message(embed=rules.rules, ephemeral=True)

        @self.tree.command(name="roles", description="Posts the specified embed in the channel where the command was sent.")
        async def roles(interaction: discord.Interaction):
            await interaction.response.send_message(embed=roles.roles, ephemeral=True)
