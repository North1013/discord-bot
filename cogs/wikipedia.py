import discord
from discord.ext import commands

try:
    import wikipediaapi
    reqs_avail = True
except:
    reqs_avail = False

class Wikipedia:
    def __init__(self, bot):
        self.bot = bot
        self.lang = "en"

    @commands.command(aliases=["wiki"])
    async def wikipedia(self, ctx, *, args):
        async with ctx.typing():
            wiki = wikipediaapi.Wikipedia(self.lang)
            page = wiki.page(args)
            if page.exists():
                embed = discord.Embed(
                        colour = discord.Colour.blue()
                        )
                embed.set_author(name=page.title)
                embed.add_field(name="Summary", value=page.summary[0:900] + "...")
                embed.add_field(name="Link", value=page.fullurl)
                await ctx.send(embed=embed)
            else:
                await ctx.send("The wiki page: {}, does not exist".format(args))

    @commands.command(aliases=["wikilang", "wl"])
    async def wiki_lang(self, ctx, args):
        avail_lang = [
                "en", "sv"
                ]
        if args in avail_lang:
            self.lang = args
        else:
            await ctx.send("Not a valid language")

def setup(bot):
    if reqs_avail:
        bot.add_cog(Wikipedia(bot))
    else:
        raise RuntimeError("You are missing the requirement: wikipediaapi")

