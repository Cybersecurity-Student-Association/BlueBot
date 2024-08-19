import feedparser
from datetime import datetime, timedelta
from discord.ext import tasks
import discord
from variables.variables import debug
from variables.channels import rss_channel

URL = "https://feeds.feedburner.com/TheHackersNews"
# URL = "http://lorem-rss.herokuapp.com/feed"


class RSS:
    # Constructor
    def __init__(self, client: discord.Client):
        self.client = client
        self.url = URL
        self.old_feed = feedparser.parse(self.url)

        self.rssSendMessage.start()

    # send RSS updates
    @tasks.loop(minutes=30)
    async def rssSendMessage(self):
        await self.client.wait_until_ready()
        channel = self.client.get_channel(rss_channel)
        if debug:
            await channel.send("Checking for RSS")
        feed = feedparser.parse(self.url)

        for entry in feed.entries:
            is_entry_found = False
            for old_entry in self.old_feed.entries:
                if entry.link == old_entry.link:
                    is_entry_found = True
                    break
            if not is_entry_found:
                message = f'# {entry.title}\n{entry.summary}\n{entry.link}'
                await channel.send(content=message)
        self.old_feed = feed
