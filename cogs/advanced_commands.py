import discord
from discord.ext import commands

class advancedCommands:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ddg(self, ctx, *, args):
        await ctx.send("https://duckduckgo.com/?q={}".format(args.replace(" ", "+")))

    @commands.command()
    async def ping(self, ctx):
        author = ctx.message.author.id
        await ctx.send("<@{}> Pong!".format(author))

    @commands.command()
    async def help(self, ctx):
        """Prints embedded message for a help message"""
        # "normal" commands
        embed = discord.Embed(
                colour = discord.Colour.orange()
                )
        embed.set_author(name="Help")
        embed.add_field(name="!ddg", value="DDG search", inline=False)
        embed.add_field(name="!ping", value="Returns Pong!", inline=False)
        embed.add_field(name="!aniki", value="Very important command", inline=False)
        embed.add_field(name="!dota", value="Very important command", inline=False)
        embed.add_field(name="!whiteknight", value="Very important command", inline=False)
        embed.add_field(name="!pajlada", value="Very important command", inline=False)
        await ctx.send(embed=embed)

        # music commands
        embed = discord.Embed(
                colour = discord.Colour.blue()
                )
        embed.set_author(name="Music Help")
        embed.add_field(name="!join", value="Joins the current voice channel you're in", inline=False)
        embed.add_field(name="!leave", value="Leaves the current voice channel you're in", inline=False)
        embed.add_field(name="!play", value="Plays a youtube song, use queue if already playing", inline=False)
        embed.add_field(name="!queue", value="Queues a youtube song to the", inline=False)
        embed.add_field(name="!pause", value="Pauses the currently playing music", inline=False)
        embed.add_field(name="!stop", value="Stops the currently playing music", inline=False)
        embed.add_field(name="!resume", value="Resumes the currently playing music", inline=False)
        embed.add_field(name="!search", value="Returns the 3 highest youtube clips", inline=False)
        embed.add_field(name="!searchplay", value="Plays the highest youtube clip", inline=False)
        await ctx.send(embed=embed)

    # @commands.command()
    # async def help(self, ctx):
    # author = ctx.message.author

def setup(bot):
    bot.remove_command("help")
    bot.add_cog(advancedCommands(bot))
