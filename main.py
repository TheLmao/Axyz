import discord
from discord.ext import commands
import random, os
import config
from discord.ext.commands.cooldowns import BucketType
from pyfiglet import Figlet
import json
import aiohttp
import asyncio
import time
import checks

class main():
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()
        self.f = Figlet(font='slant')

    @commands.cooldown(1, 20, BucketType.server)
    @commands.command(pass_context=True)
    async def contact(self, ctx, *, msg=""):
        """"""
        author = ctx.message.author
        cha = ctx.message.channel
        channel = self.bot.get_channel("449108055812997120")
        ms = "<@{}> {}\n{}\n{}".format(author.id, author, msg, await self.bot.create_invite(cha))
        mst = "<@{}> {}\n{}".format(author.id, author, msg)
        try:
            await self.bot.send_message(channel, ms)
            await self.bot.say("Contact Sent!\nContact again in 20 seconds!")
        except:
            await self.bot.send_message(channel, mst)
            await self.bot.say("Contact Sent! But we were unable to get an invite to your server!")

    @commands.command(pass_context=True)
    async def help(self, ctx, cmd=""):
        """"""
        author = ctx.message.author
        if cmd == "":
            em = discord.Embed(color=0x36393E, description="`a!help <command>`\n**Economy**\n    daily,  Get your daily credits!\n    bank,  See bank commands!\n**Statistics**\n    discordstats,  Check Discords Stats!\n    webstats,  See the status of a website!\n**Giveaway**\n    giveaway,  Giveaway something...\n**Moderation**\n    kick,  Kick a member!\n    ban,  Ban a member!\n    softban,  Ban someone for a sertain period of time!\n**Welcome**\n    welcome,  Setup Welcome channel\n    autorole,  Setup Autorole!\n**Misc**\n    help,  yea....\n    stats,  Axyz's Statistics!\n    invite,  Invite me to your server!\n    contact,  Need help?")
            em.set_author(name='Axyz Commands', icon_url=author.avatar_url)
        if cmd == "welcome":
            await self.bot.say("**a!welcome**\n"
                               "\n"
                               "Setup welcome channel!")
        if cmd == "autorole":
            await self.bot.say("**a!autorole**\n"
                               "\n"
                               "Setup On-join role!")
        if cmd == "contact":
            await self.bot.say("**a!contact**\n"
                               "\n"
                               "need some help?")
        if cmd == "kick":
            await self.bot.say("**a!kick**\n"
                               "\n"
                               "Kick a member")
        if cmd == "ban":
            await self.bot.say("**a!ban**\n"
                               "\n"
                               "Ban a Member")
        if cmd == "giveaway":
            await self.bot.say("**a!giveaway**\n"
                               "\n"
                               "YAY i won something! :tada: ")
        await self.bot.say(embed=em)

    @commands.command(pass_context=True)
    async def welcome(self, ctx):
        """"""
        await self.bot.say("Usage: `a!welcomeset #channel msg`")

    @commands.command(pass_context=True)
    async def welcomeset(self, ctx, chan: discord.Channel, *, msg=""):
        """"""
        server = ctx.message.server
        data = {}
        data['Welcome'] = []
        data['Welcome'].append({
            'channel': '{}'.format(chan.id),
            'msg': '{}'.format(msg)
            })
        if ctx.message.author.server_permissions.administrator:
            with open('data/welcome/{}.json'.format(server.id), 'w') as outfile:
                json.dump(data, outfile)
                channel = self.bot.get_channel(chan.id)
                await self.bot.send_message(channel, "Welcome Messages here!")
                await self.bot.say("Done!")
        else:
            await self.bot.say("You do not have permission to use this command!")

    @commands.command(pass_context=True)
    async def autorole(self, ctx):
        """"""
        await self.bot.say("Usage: `a!autoroleset role`")

    @commands.command(pass_context=True)
    async def autoroleset(self, ctx, *, role="Member"):
        """"""
        server = ctx.message.server
        data = {}
        data['Autorole'] = []
        data['Autorole'].append({
            'Role': '{}'.format(role)
            })
        if ctx.message.author.server_permissions.administrator:
            with open('data/autorole/{}.json'.format(server.id), 'w') as outfile:
                json.dump(data, outfile)
                await self.bot.say("Done!")
        else:
            await self.bot.say("You do not have permission to use this command!")

    @commands.command(pass_context=True)
    async def ban(self, ctx, user: discord.User):
        """"""
        server = ctx.message.server
        if ctx.message.author.server_permissions.ban_members:
            try:
                await self.bot.ban(user)
                await self.bot.say("Banned {}!".format(user))
            except:
                await self.bot.say("Oops! Looks like i dont have permission to ban this user!")

    @commands.command(pass_context=True)
    async def kick(self, ctx, user: discord.User):
        """"""
        server = ctx.message.server
        if ctx.message.author.server_permissions.kick_members:
            try:
                await self.bot.kick(user)
                await self.bot.say("Kicked {}!".format(user))
            except:
                await self.bot.say("Oops! Looks like i dont have permission to kick this user!")

#    @commands.command(pass_context=True)
#    async def permban(self, ctx, user: discord.User):
#        """"""
#        server = ctx.message.server
#        channel = ctx.message.channel
#        if ctx.message.author.server_permissions.ban_members:
#            try:
#                await self.bot.kick(user)
#                try:
#                    os.mkdir(os.path.expanduser("~/data/serverdata/permban/{}".format(server.id)))
#                except:
#                    pass
#                await self.bot.say("Perm Banned {}!".format(user))
#                try:
#                    await self.bot.send_message(user, "You have been perm banned from {}!\nYou will be unbanned soon?".format(server, time))
#                except:
#                    pass
#            except Exception as e:
#                await self.bot.say("Oops! Looks like i dont have permission to perm ban this user!")
#                exc = ':x: {}: {}'.format(type(e).__name__, e)
#                await self.bot.say(exc)

    @commands.command(pass_context=True)
    async def invite(self, ctx):
        """"""
        await self.bot.whisper("https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=-1\nhttps://discord.gg/r5jTgPy".format(self.bot.user.id))


    @commands.command(pass_context=True)
    async def module(self, ctx, module="", status="on"):
        """"""
        server = ctx.message.server
        if os.path.isfile('data/lockdown/{}.json'.format(server.id)):
            lockstat = "Enabled"
        else:
            lockstat = "Disabled"
        if ctx.message.author.server_permissions.administrator:
            if module == "":
                em = discord.Embed(color=0x000000, description="Lockdown `({})`".format(lockstat))
                em.set_author(name="Modules List")
                await self.bot.say(embed=em)
            if module == "Lockdown":
                if status == "on":
                    data = {}
                    data['Lock'] = []
                    data['Lock'].append({
                         'Mod': 'on'
                         })
                    with open('data/lockdown/{}.json'.format(server.id), 'w') as outfile:
                        json.dump(data, outfile)
                        await self.bot.send_message(ctx.message.author, "Module Enabled!\nTo disable use `a!module Lockdown off`")
                if status == "off":
                    try:
                        os.remove("data/lockdown/{}.json".format(server.id))
                    except:
                        pass
                    await self.bot.say("Module Disabled!")
        else:
            await self.bot.say("You do not have permission to use this command!")

    @commands.command(pass_context=True)
    async def discordstats(self, ctx):
        """"""
        import urllib.request
        t1 = time.perf_counter()
        await self.bot.send_typing(ctx.message.channel)
        t2 = time.perf_counter()
        em = discord.Embed(color=0x000000, description="**Status**,  {}\n**Discord API Ping**,  {}".format(urllib.request.urlopen("https://stackoverflow.com/").getcode(), str(round((t2-t1)*1000))))
        em.set_author(name="Discord Statistics")
        await self.bot.say(embed=em)

    @commands.command(pass_context=True)
    async def webstats(self, ctx, website="https://google.com"):
        """"""
        import urllib.request
        try:
            await self.bot.say("Status for <{}>!\n"
                           "\n"
                           "Status: {}\n"
                           "\n"
                           "Status Codes: <https://en.wikipedia.org/wiki/List_of_HTTP_status_codes>".format(website, urllib.request.urlopen(website).getcode()))
        except:
            await self.bot.say("Status for <{}>!\n"
                           "\n"
                           "Status: 403\n"
                           "\n"
                           "Status Codes: <https://en.wikipedia.org/wiki/List_of_HTTP_status_codes>".format(website))

    @commands.cooldown(1, 86400, BucketType.user)
    @commands.command(pass_context=True)
    async def daily(self, ctx):
        """"""
        author = ctx.message.author
        server = ctx.message.server
        if os.path.isfile('data/coins/{}.json'.format(author.id)):
            with open('data/coins/{}.json'.format(author.id)) as json_file:  
                data = json.load(json_file)
                for p in data['Money']:
                    summ = float(100) + float(p['Coins'])
                    bsumm = float(1) + float(p['Bits'])
                    data = {}
                    data['Money'] = []
                    data['Money'].append({
                        'Coins': summ,
                        'Bits': bsumm
                        })
                    with open('data/coins/{}.json'.format(author.id), 'w') as outfile:
                        json.dump(data, outfile)
                        await self.bot.say("You collected your 100 daily Credits & 1 bit!")
        else:
            await self.bot.say("Please use `a!bank setup`")
            ctx.command.reset_cooldown(ctx)

    @checks.is_owner()
    @commands.command(pass_context=True)
    async def setmoney(self, ctx, user, amount):
        """"""
        data = {}
        data['Money'] = []
        data['Money'].append({
            'Coins': amount
            })
        with open('data/coins/{}.json'.format(user), 'w') as outfile:
            json.dump(data, outfile)

    @checks.is_owner()
    @commands.command(pass_context=True)
    async def changelogset(self, ctx, version, *, changelog=""):
        """"""
        data = {}
        data['CL'] = []
        data['CL'].append({
            'Version': version,
            'Changelog': '{}'.format(changelog),
            'Time': time.ctime()
            })
        with open('data/changelog.json', 'w') as outfile:
            json.dump(data, outfile)

    @commands.command(pass_context=True)
    async def changelog(self, ctx):
        """"""
        with open('data/changelog.json') as json_file:  
            data = json.load(json_file)
            for p in data['CL']:
                await self.bot.say("```diff\n"
                                   "! ==== v{} ==== !\n"
                                   "\n"
                                   "{}\n"
                                   "\n"
                                   "- {} -```".format(p['Version'], p['Changelog'], p['Time']))


    @commands.command(pass_context=True)
    async def cat(self, ctx):
        """"""
        resp = await self.session.get("http://random.cat/meow")
        image_url = await resp.json()
        resp.close()
        image_url = image_url["file"]

        await self.bot.say(image_url)
        
    @commands.command(pass_context=True)
    async def dog(self, ctx):
        """"""
        resp = await self.session.get("https://random.dog/woof.json")
        image_url = await resp.json()
        resp.close()
        image_url = image_url["url"]

        await self.bot.say(image_url)

    @commands.command(pass_context=True)
    async def ascii(self, ctx, *, text : str):
        """"""
        future = self.bot.loop.run_in_executor(None, self.f.renderText, text)
        result = await future

        await self.bot.say("```"+result+"```")
    
    @commands.command(pass_context=True)
    async def bank(self, ctx, btype="", b=""):
        """"""
        author = ctx.message.author
        if btype == "":
            await self.bot.say("__**:moneybag: Bank :moneybag:**__\n"
                               "\n"
                               "setup,  Setup your bank account!\n"
                               "total,  How many credits?\n"
                               "info,   See your bank account info!\n"
                               "\n"
                               "**Buy/Sell**\n"
                               "\n"
                               "items,  See our store items!\n"
                               "buy,    Buy an item!\n")
        if btype == "setup":
            if os.path.isfile('data/coins/{}.json'.format(author.id)):
                await self.bot.say("You already have a bank account!")
            else:
                data = {}
                data['Money'] = []
                data['Money'].append({
                    'Coins': 0,
                    'Bits': 0
                    })
                with open('data/coins/{}.json'.format(author.id), 'w') as outfile:
                    json.dump(data, outfile)
                    await self.bot.say("Welcome to the Economy!")
        if btype == "total":
            if os.path.isfile('data/coins/{}.json'.format(author.id)):
                with open('data/coins/{}.json'.format(author.id)) as json_file:  
                    data = json.load(json_file)
                    for p in data['Money']:
                        await self.bot.say("Total Credits: {}".format(p['Coins']))
        if btype == "info":
            if os.path.isfile('data/coins/{}.json'.format(author.id)):
                with open('data/coins/{}.json'.format(author.id)) as json_file:  
                    data = json.load(json_file)
                    for p in data['Money']:
                        em = discord.Embed(color=0x000000)
                        em.set_author(name="Bank Account for {}".format(author), icon_url=author.avatar_url)
                        em.add_field(name="Name", value=(author))
                        em.add_field(name="Credits", value=(p['Coins']))
                        em.add_field(name="Bits", value=(p['Bits']))
                        em.set_thumbnail(url=author.avatar_url)
                        await self.bot.say(embed=em)
            else:
                await self.bot.say("You dont have a bank account yet!")
        if btype == "items":
            await self.bot.say("```diff\n"
                               "\n"
                               "Usage: a!bank buy <itemNumber>\n"
                               "\n"
                               "1. 500 Credits  (10 bits)\n```")
        if btype == "buy":
            if b == "1":
                if os.path.isfile('data/coins/{}.json'.format(author.id)):
                    with open('data/coins/{}.json'.format(author.id)) as json_file:  
                        data = json.load(json_file)
                        for p in data['Money']:
                            summ = float(500) + float(p['Coins'])
                            bsumm = float(p['Bits']) - float(10)
                            if bsumm < 0.0:
                                await self.bot.say("Not enough money!")
                            else:
                                data = {}
                                data['Money'] = []
                                data['Money'].append({
                                    'Coins': summ,
                                    'Bits': bsumm
                                    })
                                with open('data/coins/{}.json'.format(author.id), 'w') as outfile:
                                    json.dump(data, outfile)
                                    await self.bot.say("Bought 500 Credits!")
                else:
                    await self.bot.say("Register a bank account first!")

    
        
def setup(bot):
    bot.add_cog(main(bot))
