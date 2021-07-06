import discord
import time
import asyncio
import random
import pymongo
from pymongo import MongoClient
from discord.ext import tasks

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
toktoo = "ODQxMjAxNjU1NzE3OTUzNTU3.YJjUFw.yDtJ3Y_sH3wGrT2jhexr9Yoz_R8"


cluster = MongoClient("mongodb+srv://bot:1234@cluster0.5bkqm.mongodb.net/discord?retryWrites=true&w=majority")
db = cluster["discord"]
collection = db["bot"]

global logined
logined = 0

@client.event
async def on_ready():
    logined = 1
    game = discord.Game("Asteroid Support Server, hmm...")
        # await client.change_presence(status=discord.Status.idle, activity=game)
        # await client.change_presence(status=discord.Status.online, activity=game)
        # await client.change_presence(status=discord.Status.invisible, activity=game)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{game}", status=discord.Status.idle))
    print("Helper Bot = {} is Ready Boss!!".format(client.user))

@client.event
async def on_member_join(member):
    print(1)
    chan = client.get_channel(834639567687647262)
    print(11)
    await chan.send(embed=discord.Embed(title=f"Welcome To Asteroid Support {member}", description=f"Hope you enjoy your stay here {member.mention} \n** Check these out!** \n __Our website:__ https://asteroidbot.xyz \n__Invite:__ https://asteroidbot.xyz/invite \n __Support Mail:__ support@asteroidbot.xyz"))
    print(111)
    
@client.event
async def on_member_leave(member):
    print(2)
    chan = client.get_channel(835080036205199370)
    print(22)
    await chan.send(embed=discord.Embed(title=f"{member} Left our server :( "))
    print(222)


@tasks.loop(minutes=1)
async def update_server():
    if logined == 1:
        print("in 1")
        time.sleep(30)
        print("in 2")
        channel = client.get_channel(784697044236763176)
        print("in 3")
        await channel.send("debugserverct asteroid")
        print("in 4")
        time.sleep(5)
        await channel.send("debugserverct asteroidmusic")
        print("out 1")


@client.event
async def on_message(message):
    global messages
    if message.content.startswith("id=") and str(message.channel.id) == "840984366149926922":
        try:
            voted_user = await client.fetch_user(int(message.content.split("=")[-1]))
            print(voted_user)
            await message.delete()
            vtmsg = await message.channel.send(f"{voted_user.mention}, Voted for <@780472070072696852>! Thank you so much!")
            await vtmsg.add_reaction("💗")
            fio = collection.find_one({"_id":3222 })
            votedic = fio["voters"]
            if str(voted_user.id) in votedic:
                vts = int(votedic[str(voted_user.id)])
                vts += 1
                (votedic[str(voted_user.id)]) = vts
            else:
                votedic[str(voted_user.id)] = 1
            collection.update_one({"_id":3222},{"$set":{"voters":votedic}})
        except Exception as e:
            print(e)
            await message.channel.send(f"an error occured: {e}")
    if message.content.startswith("id2=") and str(message.channel.id) == "840984366149926922":
        try:
            voted_user = await client.fetch_user(int(message.content.split("=")[-1]))
            print(voted_user)
            await message.delete()
            vtmsg2 = await message.channel.send(f"{voted_user.mention}, Voted for Our Server! Thank you so much!")
            await vtmsg2.add_reaction("💗")
            fio = collection.find_one({"_id": 3222})
            votedic = fio["voters"]
            if str(voted_user.id) in votedic:
                vts = int(votedic[str(voted_user.id)])
                vts += 1
                (votedic[str(voted_user.id)]) = vts
            else:
                votedic[str(voted_user.id)] = 1
            collection.update_one({"_id":3222},{"$set":{"voters":votedic}})
        except Exception as e:
            print(e)
            await message.channel.send(f"an error occured: {e}")

    if message.content.startswith("id3=") and str(message.channel.id) == "840984366149926922":
        try:
            voted_user = await client.fetch_user(int(message.content.split("=")[-1]))
            print(voted_user)
            await message.delete()
            vtmsg2 = await message.channel.send(f"{voted_user.mention}, Voted for <@836830093644791809>! Thank you so much!")
            await vtmsg2.add_reaction("💗")
        except Exception as e:
            print(e)
            await message.channel.send(f"an error occured: {e}")

    if message.content.startswith("ah/addbot help") or message.content.startswith("ah/help addbot") or message.content.startswith("ah/help") or message.content.startswith("ah/ help"):
        await message.add_reaction("<a:ag_gglmod:781410678446489600>")
        await message.channel.send(embed=discord.Embed(title="Asteroid Helper", description="The only command for now:\n__AddBot__: You can add any bot to this server with permissions Defined by the Admins.\n By default You get 1 bot to add but you can purchase more by using `a/ redeem`.\n\n**Rules:** \nNEVER Exploit bugs, Report it!\nStrictly NO NSFW Commands.\nNO Malicous or advertising bots\nNO spam bots or free nitro bots.\n__Warnings__ :warning:: The bot will be removed when you leave the Server.\nThe add bot request will be denied if it tends to violate rules\nThe bot if violates rules or performs malicous activities will be removed and added to ban list(you cant add it again) and also your bot space will not be given back.\nIf you wish to remove a bot or report a bot Create a ticket Using `a/ ticket new`.\n Admins and Moderators have full rights to kick and ban these bots but you will be given a valid reason.\nYour bot wont be added instantly, it will take time.\nA rule not listed here does not mean you can break it, use common sense.\n\n**Syntax:** `ah/addbot botid reason and features`"))

    if message.content.startswith("ah/ addbot"):
        await message.add_reaction("<a:ag_gglmod:781410678446489600>")
        await message.channel.send("Use `ah/addbot` without space between command and prefix")

    if message.content.startswith("ah/addbot"):
        await message.add_reaction("<a:ag_gglmod:781410678446489600>")
        boc = collection.find_one({"_id":3444 })
        boc = boc["botspace"]
        try:
            goin = 0
            addbotinfo = ""
            try:
                for i in range(1, len(list(message.content))):
                    cooltemp = message.content.split(" ")[i]
                    addbotinfo += f"{cooltemp} "
                    goin = 1
            except:
                pass
            if addbotinfo == "":
                await message.channel.send("Enter bot id and descreption.\n Example: `ah/addbot botid descreption`")
        except Exception as e:
            await message.channel.send(f"Please report this\nError occured: {e}")

        if goin == 1:
            if str(message.author.id) in boc:
                if int(boc[str(message.author.id)]) <= 0:
                    await message.channel.send(embed=discord.Embed(title="Not Enough Space", description="Sorry You dont have used your space to add bot to this server\nYou can redeem more space using `a/ redeem`"))
                elif int(boc[str(message.author.id)]) > 0:
                    boc[str(message.author.id)] = int(boc[str(message.author.id)]) - 1
                    chanel = client.get_channel(842649371179089940)
                    await chanel.send(f"Bot Add Request\n\nUser: {message.author.mention}\ninfo: {addbotinfo}")
                    await message.channel.send("Your Request has been sent Succesfully. Make sure you have addded your bot id. IF no then create a ticket using `a/ ticket new`")
            else:
                boc[str(message.author.id)] = 0
                chanel = client.get_channel(842649371179089940)
                await chanel.send(f"Bot Add Request\n\nUser: {message.author.mention}\ninfo: {addbotinfo}")
                await message.channel.send("Your Request has been sent. Make sure you have addded ur bot id in the descreption or create a new requet. When Spammed your bot won't be added")
            collection.update_one({"_id":3444},{"$set":{"botspace":boc}})
    


            
        


update_server.start()
client.run(toktoo)
