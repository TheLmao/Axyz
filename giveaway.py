import discord
from discord.ext import commands
import random, os
import config
from discord.ext.commands.cooldowns import BucketType
import json
import asyncio

class main():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def giveaway(self, ctx, time=60, *, prize="Nothing..."):
        """"""
        server = ctx.message.server
        author = ctx.message.author
        if ctx.message.author.server_permissions.administrator:
            total_time = time
            mins, secs = divmod(total_time, 60)
            hours, mins = divmod(mins, 60)
            em = discord.Embed(color=author.color, description="**Prize:** {}\n".format(prize) + "**Time:** %d Hours %d Minutes %d Seconds\n" % (hours, mins, secs))
            em.set_author(name="Giveaway")
            await self.bot.say(embed=em)
            await asyncio.sleep(time)
            await self.bot.say("YAY! {} won the {} :tada: ".format(random.choice(list(server.members)), prize))
        else:
            await self.bot.say("Nope! No Permission!")


def setup(bot):
    bot.add_cog(main(bot))
