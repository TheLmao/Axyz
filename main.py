import discord
from discord.ext import commands
import random, os
import config
from discord.ext.commands.cooldowns import BucketType
import json
class main():
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(1, 20, BucketType.server)
    @commands.command(pass_context=True)
    async def contact(self, ctx, msg=""):
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
            em = discord.Embed(color=0x7289DA, description="**Welcome**\nwelcome  Setup Welcome channel\nautorole  Setup Autorole!\n**Misc**\nhelp  yea....\ncontact  Need help?")
            em.set_author(name='Axyz Commands', icon_url=author.avatar_url)
        if cmd == "help":
            em = discord.Embed(color=0x7289DA, description="**Welcome**\nwelcome  Setup Welcome channel\nautorole  Setup Autorole!\n**Misc**\nhelp  yea....\ncontact  Need help?")
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
        with open('data/welcome/{}.json'.format(server.id), 'w') as outfile:
            json.dump(data, outfile)
            channel = self.bot.get_channel(chan.id)
            await self.bot.send_message(channel, "Welcome Messages here!")
            await self.bot.say("Done!")

    @commands.command(pass_context=True)
    async def autorole(self, ctx):
        """"""
        await self.bot.say("Usage: `a!autoroleset role`")

    @commands.command(pass_context=True)
    async def autoroleset(self, ctx, role="Member"):
        """"""
        server = ctx.message.server
        data = {}
        data['Autorole'] = []
        data['Autorole'].append({
            'Role': '{}'.format(role)
            })
        with open('data/autorole/{}.json'.format(server.id), 'w') as outfile:
            json.dump(data, outfile)
            await self.bot.say("Done!")

        
def setup(bot):
    bot.add_cog(main(bot))
