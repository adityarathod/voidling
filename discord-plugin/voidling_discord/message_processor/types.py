from typing import Optional, Union
from pydantic import BaseModel
from discord import Embed


class RasaMessage(BaseModel):
    recipient_id: str
    text: Optional[str]
    image: Optional[str]


MessageOrEmbed = Union[str, Embed]
