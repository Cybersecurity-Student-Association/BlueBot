import discord
import os

from variables.variables import SERVER, JOIN_MESSAGES_CHANNEL, CAMPUSGROUPS_MESSAGE_LINK
from events.EventThreads import EventThreads

class Events:
    def __init__(self, client: discord.Client):
        self.client = client

        self.register_events()
        EventThreads(client=client)

    def register_events(self):
        @self.client.event
        async def on_message(message: discord.Message):
            if message.author == self.client.user:
                return

            return
            if message.mentions.__contains__(self.client.user):
                await message.reply("Don\'t @ me.")

            if message.content.lower() == "inertia":
                await message.reply("Inertia is a property of matter")

        @self.client.event
        async def on_member_join(member: discord.Member):
            channel = self.client.get_guild(
                int(SERVER)).get_channel(int(JOIN_MESSAGES_CHANNEL))
            await channel.send(file=discord.File("assets/CS2A.png"),
                               content=f"""Welcome <@{member.id}>!\nPlease change your nickname to include your real first name and last initial or full last name.\nMake sure to join the club on Campus Groups (link found at {CAMPUSGROUPS_MESSAGE_LINK}).""",
                               suppress_embeds=True)
