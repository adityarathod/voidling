from typing import Optional, Union

from discord import Embed
from pydantic import BaseModel


class RasaMessage(BaseModel):
    recipient_id: str
    text: Optional[str]
    image: Optional[str]


MessageOrEmbed = Union[str, Embed]
