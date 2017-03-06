#!/usr/bin/env python3
#
import sys
from random import randint

try:
    import boto3
except ImportError:
    msg = "ERROR: Please install boto3 from: https://github.com/boto/boto3"
    sys.stderr.write(msg + "\n")

# Global variables:
msg    = 'message'
weight = 'weight'

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

    # Send the message to one of the following:
    # 1. PhoneNumber (make sure to use the correct format, E.164)
    # 2. TopicArn
    # 3. TargetArn
    #
    # Note that these are all mutually exclusive, so you'll have to uncomment
    # one at the most.
    #
    client = boto3.client("sns")
    response = client.publish (
        #PhoneNumber = "+xxxxxxxxxxx",
        #TopicArn = "",
        #TargetArn = "",
        Message = message
    )

    print(message)
    print(response)

###############################################################################
# GET MESSAGE FUNCTIONS
###############################################################################

def getGreeting():
    return getRandMessage((
        { msg : "Good morning! ", weight : 1 },
        { msg : "Wake up! "     , weight : 1 },
        { msg : "Sup. "         , weight : 1 },
        { msg : "Buenos Dias. " , weight : 1 },
        { msg : ""              , weight : 1 },
    ))

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
    ret = getRandMessage((
        { msg : "You will be reading"         , weight : 3 },
        { msg : "You get to read"             , weight : 3 },
        { msg : "Please read"                 , weight : 3 },
        { msg : "Do yourself a favor and read", weight : 1 },
    ))

    # Middle:
    (name, chapter) = getChapter()

    # Chapter is the number of chapters in the book, so we need to convert it
    # to a random chapter to read.
    chapter = str(randint(1, chapter))

    ret += " " + name + " " + chapter + " "

    # End:
    ret += getRandMessage((
        { msg : "today"            , weight : 4 },
        { msg : "this fine morning", weight : 1 },
    ))

    return ret + "."

def getPrayer():
    ret = getRandMessage((
        { msg : "You will be praying for", weight : 1 },
        { msg : "You get to pray for"    , weight : 1 },
        { msg : "Please pray for"        , weight : 1 },
    ))

    ret += " "

    ret += getRandMessage((
        { msg : "your family"              , weight : 1 },
        { msg : "your friends"             , weight : 1 },
        { msg : "America"                  , weight : 1 },
        { msg : "the world"                , weight : 1 },
        { msg : "your coworkers"           , weight : 1 },
        { msg : "your spouse"              , weight : 1 },
        { msg : "your spiritual well-being", weight : 1 },
        { msg : "your church"              , weight : 1 },
    ))

    ret += " "

    ret += getRandMessage((
        { msg : "today"            , weight : 4 },
        { msg : "this fine morning", weight : 1 },
    ))

    return ret + "."

def getMedia():
    ret = getRandMessage((
        { msg : "Media day!"      , weight : 1 },
        { msg : "It's media day!" , weight : 1 },
        { msg : "Happy media day!", weight : 1 },
    ))

    ret += " "

    tmp = getRandMessage((
        { msg : "Please ", weight : 1 },
        { msg : ""       , weight : 1 },
    ))

    needslc = True if tmp == "Please " else False
    ret += tmp

    tmp = getRandMessage((
        { msg : "Pick"  , weight : 1 },
        { msg : "Choose", weight : 1 },
        { msg : "Select", weight : 1 },
    ))

    if needslc: tmp = tmp.lower()
    ret += tmp + " "

    ret += "a good podcast/video/song and listen to/watch it.";

    return ret

def getDeed():
    ret = getRandMessage((
        { msg : "Do something nice for", weight : 1 },
        { msg : "Do a good deed for"   , weight : 1 },
    ))

    ret += " "

    ret += getRandMessage((
        { msg : "your spouse"    , weight : 2 },
        { msg : "a coworker"     , weight : 2 },
        { msg : "a stranger"     , weight : 1 },
        { msg : "a friend"       , weight : 2 },
        { msg : "a family member", weight : 1 },
    ))

    return ret + " today."

def getSabbath():
    ret = getRandMessage((
        { msg : "Sabbath day!"              , weight : 1 },
        { msg : "Today is your sabbath!"    , weight : 1 },
        { msg : "Today is your sabbath day!", weight : 1 },
        { msg : "Day of rest!"              , weight : 1 },
    ))

    ret += " "

    ret += getRandMessage((
        { msg : "Sleep in"                , weight : 1 },
        { msg : "Go play pokemon"         , weight : 1 },
        { msg : "Make a special breakfast", weight : 1 },
        { msg : "Make coffee"             , weight : 1 },
    ))

    return ret + " or something."

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

#
# This could have used lists/tuples instead of dictionaries but dictionaries
# make it easier to change I think.
#
# Example testing of this function:
#
# import JesusTexting
# tod = ({'message': 0, 'weight': 1}, {'message': 1, 'weight': 1})
# res=[0,0]
# for i in range(0,1000):
#     res[JesusTexting.getRandMessage(tod)] += 1
# print(res)
#
def getRandMessage(messages):
    # Get the sum of all weights.
    total_weight = 0

    for message in messages:
        total_weight += message[weight]

    # Pick a random weight.
    rand_weight = randint(1, total_weight)

    # Go through the tuple again and figure out which message to return.
    for message in messages:
        rand_weight -= message[weight]
        if rand_weight <= 0: return message[msg]

###############################################################################
if __name__ == "__main__":
    main(sys.argv[1:])
