import discord
from discord.ext import commands
import yaml

try:
    import wolframalpha
    reqs_avail = True
except:
    reqs_avail = False

class WolframAlpha:
    def __init__(self, bot):
        self.bot = bot
        self.path = "/root/discord-bot/"
        self.settings = self.path + "data/settings.yaml"
        data = yaml.safe_load(open(self.settings))
        self.wolfram = wolframalpha.Client(data['wolframalpha'])

    @commands.command(aliases=["math", "wolfram"])
    async def wolframalpaha(self, ctx, *, args):
        async with ctx.typing():
            results = self.wolfram.query(args)
            author = ctx.message.author.id
            try:
                await ctx.send("<@{}>\n".format(author) + next(results.results).text)
            except:
                await ctx.send("<@{}>\nNot a valid query!".format(author))

def setup(bot):
    if reqs_avail:
        bot.add_cog(WolframAlpha(bot))
    else:
        raise RuntimeError("You are missing the requirement: wolframalpha")
