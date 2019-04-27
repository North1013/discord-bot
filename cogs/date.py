from datetime import date
import discord
from discord.ext import commands

class Date:
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=["week", "today"])
    async def date(self, ctx):
        async with ctx.typing():
            d = date.today()
            week = d.isocalendar()[1]
            d1 = d.strftime("%A") +  " " + d.strftime("%d")
            d2 = d.strftime("%B") +  " " + d.strftime("%Y")
            await ctx.send("Today is {0} of {1}, week {2}".format(d1, d2, week))

def setup(bot):
    bot.add_cog(Date(bot))
