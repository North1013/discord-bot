import aiohttp
import discord
from discord.ext import commands
import json

class Duckduckgo:
    def __init__(self, bot):
        self.bot = bot

    async def fetch(self, session, url):
        async with session.get(url) as response:
            return await response.text()

    @commands.command(aliases=['duckduckgo', 'search'])
    async def ddg(self, ctx, *, args):
        async with ctx.typing():
            url = "https://api.duckduckgo.com/?q={}&format=json&atb=v142-1__".format(args.replace(" ", "+"))
            async with aiohttp.ClientSession() as session:
                html = await self.fetch(session, url)
            # print(html)
            x = json.loads(html)
            ddg_link = "https://duckduckgo.com/?q={}".format(args.replace(" ", "+"))
            # ddg_abstract_url = x["AbstractURL"]
            ddg_abstract_text = x["AbstractText"]
            ddg_answer_type = x["AnswerType"]

            if ddg_abstract_text:
                embed = discord.Embed(
                        colour = discord.Colour.blue()
                        )
                embed.set_author(name=ddg_answer_type)
                embed.add_field(name="Text", value=ddg_abstract_text)
                embed.add_field(name="Link", value=ddg_link)
                await ctx.send(embed=embed)
            else:
                await ctx.send("https://duckduckgo.com/?q={}".format(args.replace(" ", "+")))

def setup(bot):
    bot.add_cog(Duckduckgo(bot))
