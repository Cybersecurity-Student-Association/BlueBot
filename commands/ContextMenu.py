import discord

class ContextMenu:
    def __init__(self, client, tree, servers):
        self.client = client
        self.tree = tree
        self.servers = servers
        
        self.register_ContextMenu()

    def register_ContextMenu(self):
        @self.tree.context_menu(name="Get name")
        async def get_name(interaction: discord.Interaction, user: discord.Member):
            await interaction.response.send_message(f'You clicked on {user}', ephemeral=True)