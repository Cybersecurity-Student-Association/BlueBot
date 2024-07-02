import discord
from embeds import clubinfo, roles, rules


class OptionCommand:
    def __init__(self, client: discord.Client, tree: discord.app_commands.CommandTree, servers):
        self.client = client
        self.tree = tree
        self.servers = servers

        self.register_OptionCommands()

    def register_OptionCommands(self):
        @self.tree.command(name="embed", description="Posts the specified embed in the channel where the command was sent.")
        async def embed(interaction: discord.Interaction, choice: str):
            if choice == "rules":
                await interaction.response.send_message(embed=rules.rules, ephemeral=True)
            elif choice == "roles":
                await interaction.response.send_message(embed=roles.roles, ephemeral=True)
            elif choice == "clubinfo":
                await interaction.response.send_message(embed=clubinfo.clubinfo, ephemeral=True)
            else:
                await interaction.response.send_message(content="invalid choice. Valid choices: clubinfo, roles, rules")
