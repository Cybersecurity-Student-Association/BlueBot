import discord
from variables.variables import debug, SERVER
from variables.channels import event_threads_channel
from discord.ext import tasks
from datetime import datetime, timedelta
from pytz import utc

class EventThreads:
    def __init__(self, client: discord.Client):
        self.client = client

        self.register_EventThreads()
        self.send_reminder_message.start()

    def register_EventThreads(self):
        @self.client.event
        async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
            if debug:
                print(f'{payload.user_id} added a reaction')
            return  # cant add users to the event "interested". If they react, then they will not be interested in the event
            message = await self.client.get_channel(event_threads_channel).fetch_message(payload.message_id)
            event_name = message.content
            threads = self.client.get_channel(event_threads_channel).threads
            for thread in threads:
                if thread.name in event_name:
                    await thread.add_user(discord.Object(id=payload.user_id))
                    return
            events = self.client

        @self.client.event
        async def on_raw_reaction_remove(payload: discord.RawReactionActionEvent):
            if debug:
                print(f'{payload.user_id} removed a reaction')
            return  # cant remove users from the event "interested". If they unreact, then they will still be interested in the event
            message = await self.client.get_channel(event_threads_channel).fetch_message(payload.message_id)
            event_name = message.content
            threads = self.client.get_channel(event_threads_channel).threads
            for thread in threads:
                if event_name in thread.name:
                    await thread.remove_user(discord.Object(id=payload.user_id))
                    return

        @self.client.event
        async def on_scheduled_event_create(event: discord.ScheduledEvent):
            if debug:
                print(f'{event.name} created')

            channel = self.client.get_channel(event_threads_channel)
            # message = await channel.send(event.name + " (scheduled)")
            thread = await channel.create_thread(name=event.name + " (scheduled)", invitable=False)
            await thread.add_user(event.creator)
            epoch = str(event.start_time.timestamp()).split(".")[0]
            await thread.send(content=f"{event.name} is starting on <t:{epoch}>")

        @self.client.event
        async def on_scheduled_event_update(event_before: discord.ScheduledEvent, event_after: discord.ScheduledEvent):
            channel = self.client.get_channel(event_threads_channel)
            threads = channel.threads
            if event_before.name != event_after.name:
                for thread in threads:
                    if event_before.name in thread.name:
                        await thread.edit(name=event_after.name + " (" + thread.name.split("(")[-1])
                        return
            elif event_before.status == discord.EventStatus.active and (event_after.status == discord.EventStatus.completed or event_after.status == discord.EventStatus.ended):
                for thread in threads:
                    if event_before.name in thread.name:
                        await thread.edit(name=event_before.name + " (finished)", archived=True, locked=True)
                        await thread.send(f"{event_after.name} is over.")
                        return
            elif event_before.status == discord.EventStatus.scheduled and event_after.status == discord.EventStatus.active:
                for thread in threads:
                    if event_before.name in thread.name:
                        await thread.edit(name=event_after.name + " (right now)")
                        await thread.send(f"@everyone {event_after.name} has started.")
                        return
            elif event_before.status == discord.EventStatus.active and event_after.status == discord.EventStatus.scheduled:
                for thread in threads:
                    if event_before.name in thread.name:
                        await thread.edit(name=event_after.name + " (scheduled)")
                        epoch = str(event_after.start_time.timestamp()).split(".")[0]
                        await thread.send(f"@everyone {event_after.name} has ended. It will occur again on <t:{epoch}>")
                        return
            elif event_before.start_time != event_after.start_time:
                for thread in threads:
                    if event_before.name in thread.name:
                        epoch = str(event_after.start_time.timestamp()).split(".")[0]
                        await thread.send(content=f'{event_before.name} will start at <t:{epoch}>')
                        return

        @self.client.event
        async def on_scheduled_event_delete(event: discord.ScheduledEvent):
            if debug:
                print(f'{event.name} deleted')
            channel = self.client.get_channel(event_threads_channel)
            threads = channel.threads
            for thread in threads:
                if event.name in thread.name:
                    # message = await channel.fetch_message(thread.id)
                    # await message.edit(content=event.name + " (canceled)")
                    await thread.send(f"{event.name} has been canceled.")
                    await thread.edit(name=event.name + " (canceled)", archived=True, locked=True)
                    return

        @self.client.event
        async def on_scheduled_event_user_add(event: discord.ScheduledEvent, username: str):
            if debug:
                print(f'{username} joined {event.name}')
            threads = self.client.get_channel(event_threads_channel).threads
            for thread in threads:
                if event.name in thread.name:
                    await thread.add_user(username)
                    return

        @self.client.event
        async def on_scheduled_event_user_remove(event: discord.ScheduledEvent, username: str):
            if debug:
                print(f'{username} left {event.name}')
            threads = self.client.get_channel(event_threads_channel).threads
            for thread in threads:
                if event.name in thread.name:
                    await thread.remove_user(username)
                    return

        @self.client.event
        async def on_raw_thread_member_remove(thread: discord.RawThreadMembersUpdate):
            removed_member_id = int(thread.data["removed_member_ids"][0])
            event_thread = self.client.get_guild(SERVER).get_channel(
                event_threads_channel).get_thread(thread.thread_id)
            events = await self.client.get_guild(SERVER).fetch_scheduled_events()
            for event in events:
                if event.name in event_thread.name:
                    async for user in event.users():
                        if user.id == removed_member_id:
                            await event_thread.send(content=f'<@{removed_member_id}> please remove yourself from the "Interested" in the event details to leave this channel. {event.url}')
                            return

    @tasks.loop(hours=1)
    async def send_reminder_message(self):
        events = await self.client.get_guild(SERVER).fetch_scheduled_events()
        threads = self.client.get_channel(event_threads_channel).threads
        for event in events:
            time_difference = event.start_time - datetime.now().astimezone(tz=utc)
            if timedelta(days=1) <= time_difference and time_difference < timedelta(days=1, hours=1):
                for thread in threads:
                    if event.name in thread.name:
                        epoch = str(event.start_time.timestamp()).split(".")[0]
                        await thread.send(f'@everyone {event.name} is starting **TOMORROW** (<t:{epoch})! If you do not wish to be part of this event, go to the "Events" in the top left and click "Interested." Thank you.')
                        break
            elif timedelta(days=3) <= time_difference and time_difference < timedelta(days=3, hours=1):
                for thread in threads:
                    if event.name in thread.name:
                        epoch = str(event.start_time.timestamp()).split(".")[0]
                        await thread.send(f'@everyone {event.name} is starting in **3 days** (<t:{epoch})! If you do not wish to be part of this event, go to the "Events" in the top left and click "Interested." Thank you.')
                        break
            elif timedelta(days=7) <= time_difference and time_difference < timedelta(days=7, hours=1):
                for thread in threads:
                    if event.name in thread.name:
                        epoch = str(event.start_time.timestamp()).split(".")[0]
                        await thread.send(f'@everyone {event.name} is starting in 7 days (<t:{epoch})! If you do not wish to be part of this event, go to the "Events" in the top left and click "Interested." Thank you.')
                        break
            elif timedelta(days=14) <= time_difference and time_difference < timedelta(days=14, hours=1):
                for thread in threads:
                    if event.name in thread.name:
                        epoch = str(event.start_time.timestamp()).split(".")[0]
                        await thread.send(f'@everyone {event.name} is starting in two weeks (<t:{epoch})! If you do not wish to be part of this event, go to the "Events" in the top left and click "Interested." Thank you.')
                        break
            elif timedelta(days=28) <= time_difference and time_difference < timedelta(days=28, hours=1):
                for thread in threads:
                    if event.name in thread.name:
                        epoch = str(event.start_time.timestamp()).split(".")[0]
                        await thread.send(f'@everyone {event.name} is starting in four weeks (<t:{epoch})! If you do not wish to be part of this event, go to the "Events" in the top left and click "Interested." Thank you.')
                        break
