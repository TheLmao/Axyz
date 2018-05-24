import discord
from discord.ext.commands import Bot
import logging
import config
import random
import sys, os, time
import checks
import json

def fcount(path):
    #Counts the number of files in a directory
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    return count

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

logging.basicConfig(level=logging.INFO) # Configurates the logger
logger = logging.getLogger('discord')
bot = Bot(command_prefix=config.prefix) # Sets the client and sets the prefix
startup_extensions = ["main"]
bot.remove_command("help")

@bot.event
async def on_server_join(server):
    users = len(set(bot.get_all_members()))
    servers = len(bot.servers)
    channels = len([c for c in bot.get_all_channels()])
    game = "a!help | {} Servers".format(servers)
    await bot.change_presence(game=discord.Game(name=game))

@bot.event
async def on_member_join(member):
    if os.path.isfile('data/welcome/{}.json'.format(member.server.id)):
        with open('data/welcome/{}.json'.format(member.server.id)) as json_file:  
            data = json.load(json_file)
            for p in data['Welcome']:
                channel = bot.get_channel(p['channel'])
                em = discord.Embed(color=0x000000, description=p['msg'])
                em.set_author(name=member, icon_url=member.avatar_url)
                await bot.send_message(channel, embed=em)
    if os.path.isfile('data/autorole/{}.json'.format(member.server.id)):
        with open('data/autorole/{}.json'.format(member.server.id)) as json_file:  
            data = json.load(json_file)
            for p in data['Autorole']:
                role = discord.utils.get(member.server.roles, name=p['Role'])
                await bot.add_roles(member, role)

@bot.event
async def on_ready():
    users = len(set(bot.get_all_members()))
    servers = len(bot.servers)
    channels = len([c for c in bot.get_all_channels()])
    shards = ["1", "2", "3", "4"]
    game = "a!help | {} Servers".format(servers)
    await bot.change_presence(game=discord.Game(name=game))
    clear_screen()
    if __name__ == "__main__":
        for extension in startup_extensions:
            try:
                bot.load_extension(extension)
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                print('Failed to load extension {}\n{}'.format(extension, exc))
    print("-=-=-=-=-=-=-=-\n"
          " Axyz\n"
          "-=-=-=-=-=-=-=-\n")
    print("Servers  {}\n"
          "Channels {}\n"
          "Users    {}\n".format(servers, channels, users))
    print("\n"
          "URL : https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=-1".format(bot.user.id))


@checks.is_owner()
@bot.command(pass_context=True)
async def reload(ctx, *, cog):
    """"""
    try:
        bot.unload_extension(cog)
        bot.load_extension(cog)
        await bot.say(":ok_hand: ")
        print("The cog '{}' was reloaded".format(cog))
    except Exception as e:
        exc = ':x: {}: {}'.format(type(e).__name__, e)
        await bot.say(exc)

@checks.is_owner()
@bot.command(pass_context=True)
async def load(ctx, *, cog):
    """"""
    author = ctx.message.author
    print("[Command] {} (=load)".format(author))
    try:
        bot.load_extension(cog)
        await bot.say(":ok_hand: ")
        print("The cog '{}' was loaded".format(cog))
    except Exception as e:
        exc = ':x: {}: {}'.format(type(e).__name__, e)
        await bot.say(exc)

bot.run(config.token)
