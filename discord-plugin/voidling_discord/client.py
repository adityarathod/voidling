import discord

DEFAULT_INTENTS = discord.Intents.default()
DEFAULT_INTENTS.message_content = True


def create_client(intents=DEFAULT_INTENTS):
    return VoidlingClient(intents=intents)


class VoidlingClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")
        # check if we can send a message to the channel
        can_send_messages = message.channel.permissions_for(
            message.guild.me
        ).send_messages
        # check if the message is from us
        is_not_me = message.author != self.user
        if can_send_messages and is_not_me:
            await message.channel.send("nice!", reference=message)
        elif not can_send_messages:
            print("Cannot send message to channel.")
        else:
            print("Message is from me.")
