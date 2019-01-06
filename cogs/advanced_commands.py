import discord
from discord.ext import commands

class AdvancedCommands:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        author = ctx.message.author.id
        await ctx.send("<@{}> Pong!".format(author))

def setup(bot):
    bot.add_cog(AdvancedCommands(bot))
