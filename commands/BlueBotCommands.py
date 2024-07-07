import discord
from embeds import clubinfo, roles, rules
from utils.isOfficer import isOfficer
from utils.log import log
from utils.get_channel_by_name import get_channel_by_name
from variables.channels import *


class BlueBotCommands:
    def __init__(self, client: discord.Client, tree: discord.app_commands.CommandTree, servers):
        self.client = client
        self.tree = tree
        self.servers = servers

        self.all_channels = []
        self.all_channels.append(discord.app_commands.Choice(
            name=welcome_channel_name, value=1))
        self.all_channels.append(discord.app_commands.Choice(
            name=log_channel_name, value=2))
        self.all_channels.append(discord.app_commands.Choice(
            name=rss_channel_name, value=3))
        self.all_channels.append(discord.app_commands.Choice(
            name=event_threads_channel_name, value=4))
        self.all_channels.append(discord.app_commands.Choice(
            name=rules_channel_name, value=5))
        self.all_channels.append(discord.app_commands.Choice(
            name=club_information_channel_name, value=6))
        self.all_channels.append(discord.app_commands.Choice(
            name=resources_channel_name, value=7))
        self.all_channels.append(discord.app_commands.Choice(
            name=stuff_to_check_out_channel_name, value=8))

        self.valid_embeds = []
        self.valid_embeds.append(
            discord.app_commands.Choice(name="clubinfo", value=1))
        self.valid_embeds.append(
            discord.app_commands.Choice(name="roles", value=2))
        self.valid_embeds.append(
            discord.app_commands.Choice(name="rules", value=3))

        self.register_BlueBotCommands()

    def register_BlueBotCommands(self):
        @self.tree.command(name="send_embed", description="update an embed")
        @discord.app_commands.choices(channel=self.all_channels)
        @discord.app_commands.choices(embed_name=self.valid_embeds)
        async def send_embed(interaction: discord.Interaction, channel: discord.app_commands.Choice[int], embed_name: discord.app_commands.Choice[int]):
            if not isOfficer(interaction=interaction):
                await interaction.response.send_message("Invalid permissions", ephemeral=True)
                return
            target_channel_id = int(get_channel_by_name(
                client=self.client, target_name=channel.name).id)

            if embed_name.name == "clubinfo":
                await self.client.get_channel().send(embed=clubinfo.clubinfo)
                await interaction.response.send_message("Done", ephemeral=True)
                await log(client=self.client, content=f"<@{interaction.user.id}> sent the {embed_name} embed in <#{target_channel_id}>.")
                return
            elif embed_name.name == "roles":
                await self.client.get_channel(target_channel_id).send(embed=roles.roles)
                await interaction.response.send_message("Done", ephemeral=True)
                await log(client=self.client, content=f"<@{interaction.user.id}> sent the {embed_name} embed in <#{target_channel_id}>.")
                return
            elif embed_name.name == "rules":
                await self.client.get_channel(target_channel_id).send(embed=rules.rules)
                await interaction.response.send_message("Done", ephemeral=True)
                await log(client=self.client, content=f"<@{interaction.user.id}> sent the {embed_name} embed in <#{target_channel_id}>.")
                return
            await interaction.response.send_message("Not a valid embed", ephemeral=True)

        @self.tree.command(name="send", description="Send a message on behalf of BlueBot")
        @discord.app_commands.choices(channel=self.all_channels)
        async def send(interaction: discord.Interaction, channel: discord.app_commands.Choice[int], target_message_id: str):
            if not isOfficer(interaction=interaction):
                await interaction.response.send_message("Invalid permissions", ephemeral=True)
                return
            target_channel_id = int(get_channel_by_name(
                client=self.client, target_name=channel.name).id)
            message_content = await self.client.get_guild(int(interaction.guild_id)).get_channel(int(interaction.channel_id)).fetch_message(int(target_message_id))
            await self.client.get_channel(target_channel_id).send(content=message_content.content)
            await log(client=self.client, content=f"<@{interaction.user.id}> sent https://discord.com/channels/{interaction.guild_id}/{interaction.channel_id}/{target_message_id} in <#{target_channel_id}>.")
            await interaction.response.send_message("Done", ephemeral=True)

        @self.tree.command(name="edit", description="Replace one of BlueBot's messages with another")
        @discord.app_commands.choices(channel=self.all_channels)
        async def edit(interaction: discord.Interaction, channel: discord.app_commands.Choice[int], original_message_id: str, new_message_id: str):
            if not isOfficer(interaction=interaction):
                await interaction.response.send_message("Invalid permissions", ephemeral=True)
                return
            target_channel_id = int(get_channel_by_name(
                client=self.client, target_name=channel.name).id)
            old_message = await self.client.get_channel(target_channel_id).fetch_message(int(original_message_id))
            if old_message.author.name != self.client.user:
                await interaction.response.send_message(content=f"The author of the target message is not {self.client.user}!", ephemeral=True)
                return
            new_message = await self.client.get_channel(interaction.channel_id).fetch_message(int(new_message_id))
            await old_message.edit(content=new_message.content)
            await log(client=self.client, content=f"<@{interaction.user.id}> edited BlueBot's https://discord.com/channels/{interaction.guild_id}/{target_channel_id}/{original_message_id} with https://discord.com/channels/{interaction.guild_id}/{interaction.channel_id}/{new_message_id}")
            await interaction.response.send_message("Done", ephemeral=True)
            return

        @self.tree.command(name="purge", description="Delete all messages in a channel")
        async def purge(interaction: discord.Interaction):
            interaction.channel.purge()
            interaction.response.send_message("Done", ephemeral=True)
            await log(client=self.client, content=f"<@{interaction.user.id}> purged all messages in <#{interaction.channel.id}>")
