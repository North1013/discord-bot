import discord
from discord.ext import commands

class Commands:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ddg(self, *, args):
        await self.client.say("https://duckduckgo.com/?q={}".format(args.replace(" ", "+")))

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        author = ctx.message.author.id
        await self.client.say("<@{}> Pong!".format(author))

    @commands.command()
    async def aniki(self):
        await self.client.say("ANIKI <:HandsUp:510384211346063360> https://www.youtube.com/watch?v=XXwPRmT41Bs")

    @commands.command()
    async def pajlada(self):
        await self.client.say("https://youtu.be/UFu4kUEA310")

    @commands.command()
    async def whiteknight(self):
        await self.client.say("https://youtu.be/85CSrFksKxg")

    @commands.command()
    async def dota(self):
        await self.client.say("https://clips.twitch.tv/CleanStylishSoybeanTheTarFu")

    @commands.command()
    async def help(self):
        # Prints embedded help message for normal commands
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
        await self.client.say(embed=embed)
        # Prints embedded help message for music commands
        embed = discord.Embed(
                colour = discord.Colour.blue()
                )
        embed.set_author(name="Music Help")
        embed.add_field(name="!join", value="Joins the current voice channel you're in", inline=False)
        embed.add_field(name="!leave", value="Leaves the current voice channel you're in", inline=False)
        embed.add_field(name="!pause", value="Pauses the currently playing music", inline=False)
        embed.add_field(name="!stop", value="Stops the currently playing music", inline=False)
        embed.add_field(name="!resume", value="Resumes the currently playing music", inline=False)
        embed.add_field(name="!search", value="Returns the 3 highest youtube clips", inline=False)
        embed.add_field(name="!searchplay", value="Plays the highest youtube clip", inline=False)
        await self.client.say(embed=embed)

    # @commands.command(pass_context=True)
    # async def help(self, ctx):
    # author = ctx.message.author

def setup(client):
    client.remove_command("help")
    client.add_cog(Commands(client))
