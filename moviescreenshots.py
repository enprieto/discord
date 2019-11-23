import discord
from imgurpython import ImgurClient
import asyncio

imgur_client = ImgurClient('imgur_id', 'imgur_secret')
screenshots = imgur_client.get_album_images('imgur_album_id')

discord_client = discord.Client()


@discord_client.event
async def play_movie():
    await discord_client.wait_until_ready()
    while True:
        i = 0
        channel = discord_client.get_channel(channel_id)
        for i in range(0, 300):
            await channel.send(screenshots[i].link)
            await asyncio.sleep(20)

discord_client.loop.create_task(play_movie())
discord_client.run('client_id')
