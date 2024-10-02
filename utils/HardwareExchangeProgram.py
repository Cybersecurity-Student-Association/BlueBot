import discord
from discord.ext import tasks
import pandas as pd
from datetime import datetime, timedelta
from pytz import utc
from variables.variables import SERVER, SERVER_OBJ, hardware_exchange_program_gsheetid
from variables.channels import hardware_exchange_program_channel
from utils.user import get_user_by_name
from utils.isOfficer import isOfficer
from utils.log import log

sheet_name = "Responses"
gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(
    hardware_exchange_program_gsheetid, sheet_name)


class HardwareExchangeProgram:
    def __init__(self, client: discord.Client, tree: discord.app_commands.CommandTree):
        self.client = client
        self.tree = tree

        self.register_commands()
        self.read_sheet.start()

    @tasks.loop(minutes=1)
    async def read_sheet(self):
        df = pd.read_csv(gsheet_url)
        for row in range(0, len(df["Timestamp"])):
            now = datetime.now().astimezone(tz=utc)
            time = datetime.strptime(
                df["Timestamp"][row], "%m/%d/%Y %H:%M:%S").astimezone(tz=utc)
            if now > time and now - time <= timedelta(minutes=1):
                product = df["Equipment type (PC, switch, server, etc.)"][row] + \
                    ": " + df["Manufacturer and Model"][row]
                channel = self.client.get_guild(SERVER).get_channel(
                    hardware_exchange_program_channel)

                name = df["Enter your name"][row]
                equipment = df["Equipment type (PC, switch, server, etc.)"][row]
                model = df["Manufacturer and Model"][row]
                quantity = df["Quantity"][row]
                images = df["Upload images"][row]
                notes = df["Aditional Device notes"][row]
                first_message = f"Name: {name}\nEquipment type: {equipment}\nManufacturer and Model: {model}\nQuantity: {quantity}\nImages: {images}\nAdditional notes: {notes}"

                for tag_id in channel._available_tags:
                    if channel._available_tags[tag_id].name == "open":
                        forum = await channel.create_thread(name=product, content=first_message, applied_tags=[channel._available_tags[tag_id]], suppress_embeds=True)
                        user = get_user_by_name(
                            client=self.client, username=df["Enter your Discord (no nicknames or @)"][row])
                        await forum.thread.send(content=f'<@{user.id}>')
                        break

    def register_commands(self):
        @self.tree.command(name="done", description="End this thread in the hardware exchange program", guild=SERVER_OBJ)
        async def done(interaction: discord.Interaction):
            if interaction.guild_id != SERVER:
                return
            isFound = False
            channel = self.client.get_guild(SERVER).get_channel(
                hardware_exchange_program_channel)
            for forum in channel.threads:
                if interaction.channel.id == forum.id:
                    isFound = True
                    break

            if not isFound:
                await interaction.response.send_message("Used in incorrect channel!", ephemeral=True)
                return

            forum = channel.get_thread(interaction.channel.id)
            async for message in forum.history(limit=2, oldest_first=True):
                for tag_id in channel._available_tags:
                    if channel._available_tags[tag_id].name == "fullfilled" and str(interaction.user.id) in message.content:
                        await interaction.response.send_message("Done", ephemeral=True)
                        await forum.send("This hardware exchange has been fullfilled.")
                        await forum.edit(applied_tags=[channel._available_tags[tag_id]], archived=True)
                        return
                    elif isOfficer(interaction=interaction):
                        await interaction.response.send_message("Done", ephemeral=True)
                        await forum.send("This hardware exchange has been ended by an officer.")
                        await forum.edit(applied_tags=[channel._available_tags[tag_id]], archived=True)
                        log(client=self.client,
                            content=f'<@{interaction.user.id}> has ended the hardware exchange <#{forum.id}>.')
                        return

            await interaction.response.send_message("You are not the owner of this post in the hardware exchange program", ephemeral=True)
