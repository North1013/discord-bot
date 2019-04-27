import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import discord
import feedparser


        # channel = self.get_channel(232917647250030592)

class Crisis:
    """Parses krisinformationen.se for new crisis in Sweden"""
    def __init__(self, bot):
        self.bot = bot
        self.scheduler = AsyncIOScheduler()
        self.scheduler.add_job(self.at_time, 'cron', minute=40)
        self.scheduler.start()
        self.path = "/root/discord-bot/"
        self.id_log = self.path + "data/crisis.log"

    def check_log(self, entry):
        """Checks if string exists in the log file"""
        with open(self.id_log, "r+") as file:
            for line in file:
                if entry in line.split():
                    return True
            return False

    def string_to_log(self, entry):
        """Adds the string to the log file"""
        with open(self.id_log, "a") as file:
            file.write(entry + "\n")

    async def at_time(self):
        """Parses krisinformationen and sends the informationen to the discord channel"""
        channel = self.bot.get_channel(232917647250030592)
        feed = feedparser.parse("http://api.krisinformation.se/v1/feed?format=xml")
        suffix = "en?format=xml"
        for entry in feed.entries:
            if entry.id.endswith(suffix):
                break
            else:
                if not self.check_log(entry.id):
                    text = entry.title + "\n" + entry.summary # + "\n" + entry.link
                    self.string_to_log(entry.id)
                    await channel.send("```" + text + "```")

def setup(bot):
    bot.add_cog(Crisis(bot))
