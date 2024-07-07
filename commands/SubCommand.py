import discord
from discord.app_commands import Choice

class SubCommand:
    def __init__(self, client: discord.Client, tree: discord.app_commands.CommandTree, servers):
        self.client = client
        self.tree = tree
        self.servers = servers
        self.register_SubCommands()

    def register_SubCommands(self):
        @self.tree.command(name="fruits", description="sub-command description")
        @discord.app_commands.choices(fruits=[
            Choice(name='apple', value=1),
            Choice(name='banana', value=2),
            Choice(name='cherry', value=3),
        ])
        async def fruits(interaction: discord.Interaction, fruits: Choice[int]):
            await interaction.response.send_message(f'Your favourite fruit is {fruits.name}.', ephemeral=True)