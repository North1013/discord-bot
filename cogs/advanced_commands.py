import discord
from discord.ext import commands
import json

class AdvancedCommands:
    def __init__(self, bot):
        self.bot = bot
        self.path = "/root/discord-bot/"
        self.json = self.path + "data/commands.json"

    @commands.command()
    async def ping(self, ctx):
        author = ctx.message.author.id
        await ctx.send("<@{}> Pong!".format(author))

    @commands.command()
    async def join(self, ctx, *, args):
        args_list = args.split()
        separator = " " + args_list[0] + " "
        string = args_list[1:1000]
        await ctx.send(separator.join(string))

    async def on_message(self, message):
        with open(self.json) as f:
            j = json.load(f)
        if message.content in j.keys():
            await message.channel.send(j[message.content])

def setup(bot):
    bot.add_cog(AdvancedCommands(bot))
