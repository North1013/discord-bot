# -*- coding: utf-8 -*-

def crisis_information():
    """Parses krisinformationen for new VMA"""
    feed = feedparser.parse("http://api.krisinformation.se/v1/feed?format=xml")

    for entry in feed.entries:
        with open("/root/discord-bot/mymodules/crisis/log_id.txt", "r") as id_file:
            for line in id_file:
                if entry.id in line.split():
                    print()
                    break
            else:
                string_to_return = entry.title + "\n" + entry.summary # + "\n" + entry.link
                with open("/root/discord-bot/mymodules/crisis/log_id.txt", "a") as new_file:
                    new_file.write(entry.id + "\n")
                return(string_to_return)

import feedparser
