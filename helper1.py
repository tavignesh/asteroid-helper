import discord
import time
import asyncio
import random

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
token = "ODQxMjAxNjU1NzE3OTUzNTU3.YJjUFw.yDtJ3Y_sH3wGrT2jhexr9Yoz_R8"


@client.event
async def on_ready():
    print("Helper Bot = {} is Ready Boss!!".format(client.user))


@client.event
async def on_message(message):
    global messages
    if message.content.startswith("id=") and str(message.channel.id) == "840984366149926922":
        try:
            voted_user = await client.fetch_user(int(message.content.split("=")[-1]))
            print(voted_user)
            await message.delete()
            await message.channel.send(f"{voted_user.mention}, Voted for <@780472070072696852>! Thank you so much!")
        except Exception as e:
            print(e)
            await message.channel.send(f"an error occured: {e}")
    if message.content.startswith("id2=") and str(message.channel.id) == "840984366149926922":
        try:
            voted_user = await client.fetch_user(int(message.content.split("=")[-1]))
            print(voted_user)
            await message.delete()
            await message.channel.send(f"{voted_user.mention}, Voted for Our Server! Thank you so much!")
        except Exception as e:
            print(e)
            await message.channel.send(f"an error occured: {e}")
            
        



client.run(token)