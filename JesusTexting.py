#!/usr/bin/env python3
#
import sys
from random import randint

try:
    import boto3
except ImportError:
    sys.stderr.write("ERROR: Please install boto3 from https://github.com/boto/boto3\n")

###############################################################################
# MAIN FUNCTION
# 1. Generates a message.
# 2. Sends the message.
###############################################################################

def main(args):

    if not args:
        err("No CLI arguments specified.")

    # Start putting together the message with a greeting.
    message = getGreeting()

    # Get main body of the message.
    message += getBody(args[0])
    print(message)

    # Send the message
    client = boto3.client('sns')
    response = client.publish (
        PhoneNumber = "+xxxxxxxxxxx",
        Message = message
    )
    print(response)
    

###############################################################################
# GET MESSAGE FUNCTIONS
###############################################################################

def getGreeting():
    greetings = (
        "Good morning! ",
        "Wake up! ",
        "Sup. ",
        "Buenos Dias. ",
        "",
    )

    rand = randint(0, len(greetings)-1)
    return greetings[rand]

def getBody(arg):
    try:
        arg = int(arg)
    except:
        err("CLI argument needs to be int 0-6.")

    if arg == 0 or arg == 1:
        body = getReading()

    elif arg == 2 or arg == 3:
        body = getPrayer()

    elif arg == 4:
        body = getMedia()

    elif arg == 5:
        body = getDeed()

    elif arg == 6:
        body = getSabbath()

    else:
        err("Bad CLI argument. Needs to be 0-6.")

    return body

def getReading():
    # Beginning:
    messages = (
        "You will be reading",
        "You get to read",
        "Please read",
        "Do yourself a favor and read",
    )

    rand = randint(0, len(messages)-1)
    ret = messages[rand]

    # Middle:
    (name, chapter) = getChapter()

    # Chapter is the number of chapters in the book, so we need to convert it
    # to a random chapter to read.
    chapter = str(randint(1, chapter))

    ret += " " + name + " " + chapter + " "

    # End:
    messages = (
        "today",
        "this fine morning",
    )

    rand = randint(0, len(messages)-1)
    ret += messages[rand] + "."

    return ret

def getPrayer():
    messages = (
        "You will be praying for",
        "You get to pray for",
        "Please pray for",
    )

    rand = randint(0, len(messages)-1)
    ret = messages[rand] + " "

    messages = (
        "your family",
        "your friends",
        "america",
        "the world",
        "your coworkers",
        "your wife",
        "your spiritual well-being",
        "your church",
    )

    rand = randint(0, len(messages)-1)
    ret += messages[rand] + " "

    messages = (
        "today",
        "this fine morning",
    )

    rand = randint(0, len(messages)-1)
    ret += messages[rand] + "."

    return ret

def getMedia():
    messages = (
        "Media day!",
        "It's media day!",
        "Happy media day!",
    )

    rand = randint(0, len(messages)-1)
    ret = messages[rand] + " "

    messages = (
        "Please ",
        "",
    )

    rand = randint(0, len(messages)-1)
    ret += messages[rand]

    messages = (
        "Pick",
        "Choose",
        "Select",
    )

    rand = randint(0, len(messages)-1)
    ret += messages[rand] + " "

    ret += "a good podcast/video/song and listen to/watch it.";

    return ret

def getDeed():
    messages = (
        "Do something nice for",
        "Do a good deed for",
    )

    rand = randint(0, len(messages)-1)
    ret = messages[rand] + " "

    messages = (
        "your wife",
        "a coworker",
        "a stranger",
    )

    rand = randint(0, len(messages)-1)
    ret += messages[rand] + " "

    ret += "today."

    return ret

def getSabbath():
    messages = (
        "Sabbath day!",
        "Today is your sabbath!",
        "Today is your sabbath day!",
        "Day of rest!",
    )

    rand = randint(0, len(messages)-1)
    ret = messages[rand] + " "

    messages = (
        "Sleep in",
        "Go play pokemon",
        "Make a special breakfast",
    )

    rand = randint(0, len(messages)-1)
    ret += messages[rand] + " "

    ret += "or something."

    return ret

# Helper method to getReading. It's at the bottom intentionally.
def getChapter():
    bible = (
        ("Genesis", 50),
        ("Exodus", 40),
        ("Leviticus", 27),
        ("Numbers", 36),
        ("Deuteronomy", 34),
        ("Joshua", 24),
        ("Judges", 21),
        ("Ruth", 4),
        ("1 Samuel", 31),
        ("2 Samuel", 24),
        ("1 Kings", 22),
        ("2 Kings", 25),
        ("1 Chronicles", 29),
        ("2 Chronicles", 36),
        ("Ezra", 10),
        ("Nehemiah", 13),
        ("Esther", 10),
        ("Job", 42),
        ("Psalms", 150),
        ("Proverbs", 31),
        ("Ecclesiastes", 12),
        ("Song of Songs", 8),
        ("Isaiah", 66),
        ("Jeremiah", 52),
        ("Lamentations", 5),
        ("Ezekiel", 48),
        ("Daniel", 12),
        ("Hosea", 14),
        ("Joel", 3),
        ("Amos", 9),
        ("Obadiah", 1),
        ("Jonah", 4),
        ("Micah", 7),
        ("Nahum", 3),
        ("Habakkuk", 3),
        ("Zephaniah", 3),
        ("Haggai", 2),
        ("Zechariah", 14),
        ("Malachi", 4),
        ("Matthew", 28),
        ("Mark", 16),
        ("Luke", 24),
        ("John", 28),
        ("Acts", 28),
        ("Romans", 16),
        ("1 Corinthians", 16),
        ("2 Corinthians", 13),
        ("Galatians", 6),
        ("Ephesians", 6),
        ("Philippians", 4),
        ("Colossians", 4),
        ("1 Thessalonians", 5),
        ("2 Thessalonians", 3),
        ("1 Timothy", 6),
        ("2 Timothy", 4),
        ("Titus", 3),
        ("Philemon", 1),
        ("Hebrews", 13),
        ("James", 5),
        ("1 Peter", 5),
        ("2 Peter", 3),
        ("1 John", 5),
        ("2 John", 1),
        ("3 John", 1),
        ("Jude", 1),
        ("Revelation", 22),
    )

    rand = randint(0, len(bible)-1)
    return bible[rand]

###############################################################################
# HELPER FUNCTIONS
###############################################################################

def err(msg):
    sys.stderr.write("ERROR: " + msg + "\n")
    sys.exit(1)

main(sys.argv[1:])
