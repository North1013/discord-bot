import urllib.request
import discord
from discord.ext import commands
from bs4 import BeautifulSoup as bs

class Music:
    def __init__(self, bot):
        self.bot = bot
        self.responses = ["You have chose one.", "You have chosen two", "You have chosen three"]
        self.players = {}
        self.queues = {}
        self.links = {"link1": "", "link2": "", "link3": ""}

    def check_queue(self, player_id):
        if self.queues[player_id] != []:
            player = self.queues[player_id].pop(0)
            self.players[player_id] = player
            player.start()

    @commands.command()
    async def join(self, ctx):
        channel = ctx.message.author.voice.voice_channel
        await self.bot.join_voice_channel(channel)

    @commands.command()
    async def leave(self, ctx):
        server = ctx.message.server
        voice_bot = self.bot.voice_bot_in(server)
        if voice_bot:
            await voice_bot.disconnect()
            print("Bot disconnected from voice channel")
        else:
            print("Bot not in voice channel")

    @commands.command()
    async def play(self, ctx, url):
        # TODO merge queue and play, by checking for already playing
        server = ctx.message.server
        voice_bot = self.bot.voice_bot_in(server)
        player = await voice_bot.create_ytdl_player(url, after=lambda: self.check_queue(server.id))
        self.players[server.id] = player
        player.start()
        await ctx.send("Music playing")

    @commands.command()
    async def queue(self, ctx, url):
        server = ctx.message.server
        voice_bot = self.bot.voice_bot_in(server)
        player = await voice_bot.create_ytdl_player(url, after=lambda: self.check_queue(server.id))

        if server.id in self.queues:
            self.queues[server.id].append(player)
        else:
            self.queues[server.id] = [player]
        print(self.queues)
        await ctx.send("Music queued")

    @commands.command()
    async def pause(self, ctx):
        server = ctx.message.server
        self.players[server.id].pause()
        await ctx.send("Music paused")
 
    @commands.command()
    async def stop(self, ctx):
        server = ctx.message.server
        self.players[server.id].stop()
        await ctx.send("Music stopped")

    @commands.command()
    async def resume(self, ctx):
        server = ctx.message.server
        self.players[server.id].resume()
        await ctx.send("Music resumed")

    @commands.command()
    async def search(self, ctx, *, args):
        link = "https://www.youtube.com/results?search_query={}".format(args.replace(" ", "+"))
        response = urllib.request.urlopen(link)
        html = response.read()
        soup = bs(html, features="html.parser")
        counter = 0
        for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
            if ("list" not in vid['href']) and ("user" not in vid['href']) and ("googlead" not in vid['href']):
                counter += 1
                self.links["link{}".format(counter)] = 'https://www.youtube.com' + vid['href']
                if counter == 3:
                    await ctx.send("1. {}\n2. {}\n3. {}".format(self.links["link1"], self.links["link2"], self.links["link3"]))
                    break

    @commands.command()
    async def searchplay(self, ctx, *, args):
        link = "https://www.youtube.com/results?search_query={}".format(args.replace(" ", "+"))
        response = urllib.request.urlopen(link)
        html = response.read()
        soup = bs(html, features="html.parser")
        counter = 0
        for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
            if ("list" not in vid['href']) and ("user" not in vid['href']) and ("googlead" not in vid['href']):
                video = "https://www.youtube.com" + vid['href']
                server = ctx.message.server
                voice_bot = self.bot.voice_bot_in(server)
                player = await voice_bot.create_ytdl_player(video, after=lambda: self.check_queue(server.id))
                self.players[server.id] = player
                player.start()
                await ctx.send("Now playing {}".format(video))
                break

def setup(bot):
    bot.add_cog(Music(bot))
