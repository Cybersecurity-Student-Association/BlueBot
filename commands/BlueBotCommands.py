import discord
from embeds import clubinfo, roles, rules
from utils.isOfficer import isOfficer
from utils.log import log

class BlueBotCommands:
    def __init__(self, client: discord.Client, tree: discord.app_commands.CommandTree, servers):
        self.client = client
        self.tree = tree
        self.servers = servers
        self.register_BlueBotCommands()

    def register_BlueBotCommands(self):
        @self.tree.command(name="send_embed", description="update an embed")
        async def send_embed(interaction: discord.Interaction, channel_id: str, embed_name: str):
            if not isOfficer(interaction=interaction):
                return
            
            if embed_name == "clubinfo":
                await self.client.get_channel(int(channel_id)).send(embed=clubinfo.clubinfo)
                await interaction.response.send_message("Done", ephemeral=True)
                await log(client=self.client, interaction=interaction, content=f"<@{interaction.user.id}> sent the {embed_name} embed in <#{channel_id}>.")
                return
            elif embed_name == "roles":
                await self.client.get_channel(int(channel_id)).send(embed=roles.roles)
                await interaction.response.send_message("Done", ephemeral=True)
                await log(client=self.client, interaction=interaction, content=f"<@{interaction.user.id}> sent the {embed_name} embed in <#{channel_id}>.")
                return
            elif embed_name == "rules":
                await self.client.get_channel(int(channel_id)).send(embed=rules.rules)
                await interaction.response.send_message("Done", ephemeral=True)
                await log(client=self.client, interaction=interaction, content=f"<@{interaction.user.id}> sent the {embed_name} embed in <#{channel_id}>.")
                return
            await interaction.response.send_message("Not a valid embed", ephemeral=True)

        @self.tree.command(name="send", description="Send a message on behalf of BlueBot")
        async def send(interaction: discord.Interaction, target_channel_id: str, target_message_id: str):
            if not isOfficer(interaction=interaction):
                return
            message_content = await self.client.get_guild(int(interaction.guild_id)).get_channel(int(interaction.channel_id)).fetch_message(int(target_message_id))
            await self.client.get_channel(int(target_channel_id)).send(content=message_content.content)
            await log(client=self.client, interaction=interaction, content=f"<@{interaction.user.id}> sent https://discord.com/channels/{interaction.guild_id}/{interaction.channel_id}/{target_message_id} in <#{target_channel_id}>.")
            await interaction.response.send_message("Done", ephemeral=True)
        
        @self.tree.command(name="edit", description="Replace one of BlueBot's messages with another")
        async def edit(interaction: discord.Interaction, original_channel_id: str, original_message_id: str, new_message_id: str):
            if not isOfficer(interaction=interaction):
                return
            old_message = await self.client.get_channel(int(original_channel_id)).fetch_message(int(original_message_id))
            new_message = await self.client.get_channel(interaction.channel_id).fetch_message(int(new_message_id))
            await old_message.edit(content=new_message.content)
            await log(client=self.client, interaction=interaction, content=f"<@{interaction.user.id}> edited BlueBot's https://discord.com/channels/{interaction.guild_id}/{original_channel_id}/{original_message_id} with https://discord.com/channels/{interaction.guild_id}/{interaction.channel_id}/{new_message_id}")
            await interaction.response.send_message("Done", ephemeral=True)