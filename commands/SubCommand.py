import discord


class SubCommand:
    def __init__(self, client: discord.Client, tree: discord.app_commands.CommandTree, servers):
        self.client = client
        self.tree = tree
        self.servers = servers

        self.group = discord.app_commands.Group(
            name="parent", description="This is a description")

        self.register_SubCommands()

    def register_SubCommands(self):
        @self.tree.command(name="top-command", description="top-command description")
        async def top_command(self):
            print()

        @self.tree.command(name="sub-command", description="sub-command description")
        async def sub_command(self, interaction):
            await interaction.response.send_message("Hello from sub-command", ephemeral=True)
