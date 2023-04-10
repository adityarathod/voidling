import discord
from typing import List
from voidling_discord.message_processor import MessageOrEmbed, RasaMessage


def build_message_responses(messages: List[RasaMessage]) -> List[MessageOrEmbed]:
    responses: List[MessageOrEmbed] = []
    for message in messages:
        if message.image:
            embed = discord.Embed()
            embed.set_image(url=message.image)
            if message.text:
                embed.description = message.text
            responses.append(embed)
        elif message.text:
            responses.append(message.text)
    return responses
