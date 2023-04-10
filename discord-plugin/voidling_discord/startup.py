import os

from voidling_discord.client import create_client


def launch_bot():
    token = os.getenv("DISCORD_TOKEN")
    client = create_client()
    client.run(token)
