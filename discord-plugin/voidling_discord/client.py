import os

import discord

from voidling_discord.message_processor import message_handler

DEFAULT_INTENTS = discord.Intents.default()
DEFAULT_INTENTS.message_content = True

BOT_PREFIX = os.getenv("BOT_PREFIX")


def create_client(intents=DEFAULT_INTENTS):
    return VoidlingClient(intents=intents)


class VoidlingClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user} with prefix `{BOT_PREFIX}`")

    async def on_message(self, message: discord.Message):
        print(f"Message from {message.author}: {message.content}")
        # check if we can send a message to the channel
        can_send_messages = message.channel.permissions_for(
            message.guild.me
        ).send_messages
        if not can_send_messages:
            print("Cannot send message to channel.")
            return
        # check if the message is from us
        if message.author == self.user:
            return
        # check message content for prefix
        if not message.content.startswith(BOT_PREFIX):
            return
        message.content = message.content[len(BOT_PREFIX) :]
        # mark as typing
        async with message.channel.typing():
            await self._communicate_with_server(message)

    async def _communicate_with_server(self, message: discord.Message):
        # get all responses from the server
        server_responses = message_handler(message)
        # send all responses given
        for idx, response in enumerate(server_responses):
            is_first_response = idx == 0
            is_embed = not isinstance(response, str)
            await message.channel.send(
                content=response if not is_embed else None,
                embed=response if is_embed else None,
                reference=message if is_first_response else None,
            )
