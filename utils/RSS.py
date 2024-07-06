import feedparser
from datetime import datetime, timedelta
from discord.ext import tasks
import discord
from variables.variables import rss_channel


URL = "https://feeds.feedburner.com/TheHackersNews"
# URL = "http://lorem-rss.herokuapp.com/feed"


class RSS:
    # Constructor
    def __init__(self, client: discord.Client):
        self.client = client
        self.url = URL
        self.rssSendMessage.start()
        self.first_run = True
        self.old_feed = feedparser.parse(self.url)

    # send RSS updates
    @tasks.loop(minutes=1)
    async def rssSendMessage(self):
        await self.client.wait_until_ready()
        channel = self.client.get_channel(rss_channel)
        # await channel.send("Checking for RSS")
        feed = feedparser.parse(self.url)

        if self.first_run:
            return

        for entry in feed.entries:
            if entry not in self.old_feed.entries:
                message = f'Title: {entry.title}\nPublication Date: {entry.published}\nSummary: {entry.summary}\nLink: {entry.link}'
                await channel.send(message)
        self.old_feed = feed

        if self.first_run:
            self.first_run = False
