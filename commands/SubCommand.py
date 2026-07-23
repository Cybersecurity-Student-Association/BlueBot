import discord
from discord.app_commands import Choice

class SubCommand:
    def __init__(self, client: discord.Client, tree: discord.app_commands.CommandTree):
        self.client = client
        self.tree = tree
        self.register_SubCommands()

    def register_SubCommands(self):
        @self.tree.command(name="fruits", description="Example command with options")
        @discord.app_commands.choices(fruits=[
            Choice(name='apple', value=1),
            Choice(name='banana', value=2),
            Choice(name='cherry', value=3),
            Choice(name='dragon fruit', value=4),
            Choice(name='elderberry', value=5),
            Choice(name='fig', value=6),
            Choice(name='grape', value=7),
            Choice(name='honeydew', value=7),
        ])
        async def fruits(interaction: discord.Interaction, fruits: Choice[int]):
            await interaction.response.send_message(f'Your favorite fruit is {fruits.name}.', ephemeral=True)