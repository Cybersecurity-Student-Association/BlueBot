import discord
from variables.variables import debug
from variables.channels import event_threads_channel

class EventThreads:
    def __init__(self, client: discord.Client):
        self.client = client

        self.register_EventThreads()

    def register_EventThreads(self):
        @self.client.event
        async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
            if debug: print(f'{payload.user_id} added a reaction')
            return  # cant add users from the event "interested". If they react, then they will not be interested in the event
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
            if debug: print(f'{payload.user_id} removed a reaction')
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
            if debug: print(f'{event.name} created')

            channel = self.client.get_channel(event_threads_channel)
            message = await channel.send(event.name + " (scheduled)")
            thread = await message.create_thread(name=event.name + " (scheduled)")
            await thread.add_user(event.creator)

        @self.client.event
        async def on_scheduled_event_update(event_before: discord.ScheduledEvent, event_after: discord.ScheduledEvent):
            channel = self.client.get_channel(event_threads_channel)
            threads = channel.threads
            if event_after.status == discord.EventStatus.completed or event_after.status == discord.EventStatus.ended:
                for thread in threads:
                    if event_before.name in thread.name:
                        await thread.edit(name=event_before.name + " (finished)", archived=True, locked=True)
                        message = await channel.fetch_message(thread.id)
                        await message.edit(content=event_before.name + " (finished)")
                        thread.send(f"@everyone {event_after.name} is over.")
                        return
            elif event_after.status == discord.EventStatus.active:
                for thread in threads:
                    if event_before.name in thread.name:
                        await thread.edit(name=event_after.name + " (right now)")
                        message = await channel.fetch_message(thread.id)
                        await message.edit(content=event_after.name + " (right now)")
                        await thread.send(f"@everyone {event_after.name} has started.")
                        return
            elif event_before.name != event_after.name:
                for thread in threads:
                    if event_before.name in thread.name:
                        await thread.edit(name=event_after.name)
                        message = await channel.fetch_message(thread.id)
                        await message.edit(content=event_after.name)
                        return

        @self.client.event
        async def on_scheduled_event_delete(event: discord.ScheduledEvent):
            if debug: print(f'{event.name} deleted')
            channel = self.client.get_channel(event_threads_channel)
            threads = channel.threads
            for thread in threads:
                if event.name in thread.name:
                    message = await channel.fetch_message(thread.id)
                    await message.edit(content=event.name + " (canceled)")
                    await thread.send(f"@everyone {event.name} has been canceled.")
                    await thread.edit(name=event.name + " (canceled)", archived=True, locked=True)
                    return

        @self.client.event
        async def on_scheduled_event_user_add(event: discord.ScheduledEvent, username: str):
            print(f'{username} joined {event.name}')
            threads = self.client.get_channel(event_threads_channel).threads
            for thread in threads:
                if event.name in thread.name:
                    await thread.add_user(username)
                    return

        @self.client.event
        async def on_scheduled_event_user_remove(event: discord.ScheduledEvent, username: str):
            print(f'{username} left {event.name}')
            threads = self.client.get_channel(event_threads_channel).threads
            for thread in threads:
                if event.name in thread.name:
                    await thread.remove_user(username)
                    return
