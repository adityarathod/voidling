from typing import List

from discord import Message

from voidling_discord.message_processor.response_builder import build_message_responses
from voidling_discord.message_processor.sender import send_receive_messages
from voidling_discord.message_processor.types import MessageOrEmbed, RasaMessage

__all__ = ["RasaMessage", "MessageOrEmbed"]


def message_handler(message: Message) -> List[MessageOrEmbed]:
    if hasattr(message.author, "id"):
        sender = str(message.author.id)
    else:
        sender = message.author.name
    messages = send_receive_messages(message.content, sender)
    return build_message_responses(messages)
