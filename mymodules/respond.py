def message_respond(author_id, message):
    if str.lower(message) == "!aniki":
        return("ANIKI <:HandsUp:510384211346063360>")
    elif str.lower(message) == "!music":
        return("qwe")
    elif str.lower(message) == "!f":
        return("<:PepeHands:517047131329003530> BILLY <:PepeHands:517047131329003530> BILLY https://youtu.be/ISJlNRRvT3g")
    elif str.lower(message) == "!pajlada":
        return("https://youtu.be/UFu4kUEA310")
    elif str.lower(message) == "!whiteknight":
        return("https://youtu.be/85CSrFksKxg")
    elif str.lower(message) == "!dota":
        return("https://clips.twitch.tv/CleanStylishSoybeanTheTarFu")
    elif str.lower(message) == "!ping":
        return("<@%s> Pong!" % author_id)
    else:
        return("Not a valid command!!!")
