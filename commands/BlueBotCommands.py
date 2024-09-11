import discord
from embeds import clubinfo, roles, rules
from utils.isOfficer import isOfficer
from utils.log import log
from utils.get_channel_by_name import get_channel_by_name
from variables.channels import *
from variables.variables import SERVER


class BlueBotCommands:
    def __init__(self, client: discord.Client, tree: discord.app_commands.CommandTree):
        self.client = client
        self.tree = tree

        self.valid_embeds = []
        self.valid_embeds.append(
            discord.app_commands.Choice(name="clubinfo", value=1))
        self.valid_embeds.append(
            discord.app_commands.Choice(name="roles", value=2))
        self.valid_embeds.append(
            discord.app_commands.Choice(name="rules", value=3))

        self.register_BlueBotCommands()

    def register_BlueBotCommands(self):
        @self.tree.command(name="send-embed", description="Send an embed in a channel")
        @discord.app_commands.choices(embed=self.valid_embeds)
        async def send_embed(interaction: discord.Interaction, channel: str, embed: discord.app_commands.Choice[int]):
            if interaction.guild_id != SERVER:
                return
            if not isOfficer(interaction=interaction):
                await interaction.response.send_message("Invalid permissions", ephemeral=True)
                return
            try:
                target_channel_id = int(channel)
            except ValueError:
                target_channel_id = get_channel_by_name(
                    client=self.client, target_name=channel)
                if target_channel_id == None:
                    await interaction.response.send_message(content="Invalid channel name!", ephemeral=True)
                    return
                target_channel_id = int(target_channel_id.id)

            if embed.name == "clubinfo":
                await self.client.get_channel().send(embed=clubinfo.clubinfo)
                await interaction.response.send_message("Done", ephemeral=True)
                await log(client=self.client, content=f"<@{interaction.user.id}> sent the {embed.name} embed in <#{target_channel_id}>.")
                return
            elif embed.name == "roles":
                await self.client.get_channel(target_channel_id).send(embed=roles.roles)
                await interaction.response.send_message("Done", ephemeral=True)
                await log(client=self.client, content=f"<@{interaction.user.id}> sent the {embed.name} embed in <#{target_channel_id}>.")
                return
            elif embed.name == "rules":
                await self.client.get_channel(target_channel_id).send(embed=rules.rules)
                await interaction.response.send_message("Done", ephemeral=True)
                await log(client=self.client, content=f"<@{interaction.user.id}> sent the {embed.name} embed in <#{target_channel_id}>.")
                return
            await interaction.response.send_message("Not a valid embed", ephemeral=True)

        @self.tree.command(name="send", description="Send a message on behalf of BlueBot")
        async def send(interaction: discord.Interaction, channel: str, target_message_id: str):
            if interaction.guild_id != SERVER:
                return
            if not isOfficer(interaction=interaction):
                await interaction.response.send_message("Invalid permissions", ephemeral=True)
                return
            try:
                target_channel_id = int(channel)
            except ValueError:
                target_channel_id = get_channel_by_name(
                    client=self.client, target_name=channel)
                if target_channel_id == None:
                    await interaction.response.send_message(content="Invalid channel name!", ephemeral=True)
                    return
                target_channel_id = int(target_channel_id.id)
            
            try:
                target_message = await self.client.get_guild(int(interaction.guild_id)).get_channel(int(interaction.channel_id)).fetch_message(int(target_message_id))
            except discord.errors.NotFound:
                    await interaction.response.send_message(content="Invalid message ID!", ephemeral=True)
                    return
            new_message = await self.client.get_channel(target_channel_id).send(content=target_message.content.replace("@.", "@"), allowed_mentions=discord.AllowedMentions.all())
            await log(client=self.client, content=f"<@{interaction.user.id}> sent {target_message.jump_url} at {new_message.jump_url}.")
            await interaction.response.send_message("Done", ephemeral=True)

        @self.tree.command(name="edit", description="Replace one of BlueBot's messages with another")
        async def edit(interaction: discord.Interaction, channel: str, original_message_id: str, new_message_id: str):
            if interaction.guild_id != SERVER:
                return
            if not isOfficer(interaction=interaction):
                await interaction.response.send_message("Invalid permissions", ephemeral=True)
                return
            try:
                target_channel_id = int(channel)
            except ValueError:
                target_channel_id = get_channel_by_name(
                    client=self.client, target_name=channel)
                if target_channel_id == None:
                    await interaction.response.send_message(content="Invalid channel name!", ephemeral=True)
                    return
                target_channel_id = int(target_channel_id.id)
                
            try:
                old_message = await self.client.get_guild(int(interaction.guild_id)).get_channel(int(interaction.channel_id)).fetch_message(int(original_message_id))
            except discord.errors.NotFound:
                    await interaction.response.send_message(content="Invalid original message ID!", ephemeral=True)
                    return

            if old_message.author.name != self.client.user:
                await interaction.response.send_message(content=f"The author of the target message is not {self.client.user}!", ephemeral=True)
                return
            
            try:
                new_message = await self.client.get_channel(interaction.channel_id).fetch_message(int(new_message_id))
            except discord.errors.NotFound:
                    await interaction.response.send_message(content="Invalid new message ID!", ephemeral=True)
                    return
            
            await old_message.edit(content=new_message.content.replace("@.", "@"), allowed_mentions=discord.AllowedMentions.all())
            await log(client=self.client, content=f"<@{interaction.user.id}> edited BlueBot's {old_message.jump_url} with {new_message.jump_url}")
            await interaction.response.send_message("Done", ephemeral=True)
            return

        @self.tree.command(name="purge", description="Delete an X amount of messages in a channel")
        async def purge(interaction: discord.Interaction, count: int):
            if interaction.guild_id != SERVER:
                return
            if not isOfficer(interaction=interaction):
                await interaction.response.send_message("Invalid permissions", ephemeral=True)
                return
            await interaction.response.send_message("Done", ephemeral=True)
            await interaction.channel.purge(limit=count)
            await log(client=self.client, content=f"<@{interaction.user.id}> purged all messages in <#{interaction.channel.id}>")

        @self.tree.context_menu(name="Send to #rules", guild=discord.Object(id=SERVER))
        async def send_to_rules(interaction: discord.Interaction, message: discord.Message):
            if not isOfficer(interaction=interaction):
                await interaction.response.send_message("Invalid permissions", ephemeral=True)
                return
            target_channel_id = rules_channel
            new_message = await self.client.get_channel(target_channel_id).send(content=message.content.replace("@.", "@"), allowed_mentions=discord.AllowedMentions.all())
            await interaction.response.send_message("Done", ephemeral=True)
            await log(client=self.client, content=f"<@{interaction.user.id}> sent {message.jump_url} at {new_message.jump_url}.")

        @self.tree.context_menu(name="Send to #club-information", guild=discord.Object(id=SERVER))
        async def send_to_club_information(interaction: discord.Interaction, message: discord.Message):
            if interaction.guild_id != SERVER:
                return
            if not isOfficer(interaction=interaction):
                await interaction.response.send_message("Invalid permissions", ephemeral=True)
                return
            target_channel_id = club_information_channel
            new_message = await self.client.get_channel(target_channel_id).send(content=message.content.replace("@.", "@"), allowed_mentions=discord.AllowedMentions.all())
            await log(client=self.client, content=f"<@{interaction.user.id}> sent {message.jump_url} at {new_message.jump_url}.")
            await interaction.response.send_message("Done", ephemeral=True)

        @self.tree.context_menu(name="Send to #resources", guild=discord.Object(id=SERVER))
        async def send_to_resources(interaction: discord.Interaction, message: discord.Message):
            if interaction.guild_id != SERVER:
                return
            if not isOfficer(interaction=interaction):
                await interaction.response.send_message("Invalid permissions", ephemeral=True)
                return
            target_channel_id = resources_channel
            new_message = await self.client.get_channel(target_channel_id).send(content=message.content.replace("@.", "@"), allowed_mentions=discord.AllowedMentions.all())
            await log(client=self.client, content=f"<@{interaction.user.id}> sent {message.jump_url} at {new_message.jump_url}.")
            await interaction.response.send_message("Done", ephemeral=True)

        @self.tree.context_menu(name="Send to #stuff-to-check-out", guild=discord.Object(id=SERVER))
        async def send_to_stuff_to_check_out(interaction: discord.Interaction, message: discord.Message):
            if interaction.guild_id != SERVER:
                return
            if not isOfficer(interaction=interaction):
                await interaction.response.send_message("Invalid permissions", ephemeral=True)
                return
            target_channel_id = stuff_to_check_out_channel
            new_message = await self.client.get_channel(target_channel_id).send(content=message.content.replace("@.", "@"), allowed_mentions=discord.AllowedMentions.all())
            await log(client=self.client, content=f"<@{interaction.user.id}> sent {message.jump_url} at {new_message.jump_url}.")
            await interaction.response.send_message("Done", ephemeral=True)

        @self.tree.context_menu(name="Send to #announcements", guild=discord.Object(id=SERVER))
        async def send_to_announcements(interaction: discord.Interaction, message: discord.Message):
            if interaction.guild_id != SERVER:
                return
            if not isOfficer(interaction=interaction):
                await interaction.response.send_message("Invalid permissions", ephemeral=True)
                return
            target_channel_id = announcements_channel
            new_message = await self.client.get_channel(target_channel_id).send(content=message.content.replace("@.", "@"), allowed_mentions=discord.AllowedMentions.all())
            await log(client=self.client, content=f"<@{interaction.user.id}> sent {message.jump_url} at {new_message.jump_url}.")
            await interaction.response.send_message("Done", ephemeral=True)
