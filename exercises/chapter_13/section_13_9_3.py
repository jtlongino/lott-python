"""Problem 3 in Chapter 13.9, Word Lengths"""
import math
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def constructLengths(text):
    """constrctLenths(string) -> string

    Constructs a string where each digit is the length of a word in text"""

    sequence = ""
    words = text.split()
    logger.debug(words)
    for word in words:
        length = 0
        #If alphanumeric, just get the length
        if(word.isalnum()):
            logger.debug("Function length is %d", len(word))
            length = len(word)
            sequence = sequence + calcLength(length)
        #Return count of alphanumerics
        else:
            length = 0
            for index in range(len(word)):
                if(word[index].isalnum()):
                    length+=1
                elif(word[index] == '-'):
                    logger.debug("Calculated length is %d", length)
                    sequence = sequence + calcLength(length)
                    length = 0
            logger.debug("Calculated length is %d", length)
            sequence = sequence + calcLength(length)
        logger.debug("Sequence value is %s", sequence)
    return sequence

def calcLength(length):
    """calcLength(number) -> string

    Converts a word length number to a length string. 1-9 just take string
    valuevalues, = 0 returns null string, and 10 returns '0'"""

    if(length == 0): return ""
    elif(1 <= length <= 9): return str(length)
    elif(length == 10): return '0'
    else: raise ValueError("length expected to be between 0 and 10")

cadenza = """Poe, E.
Near a Raven
Midnights so dreary, tired and weary,
Silently pondering volumes extolling all by-now obsolete lore.
During my rather long nap - the weirdest tap!
An ominous vibrating sound disturbing my chamber's antedoor.
"This", I whispered quietly, "I ignore"."""

print(constructLengths(cadenza))
print("314159265358979323846264338327950288419716")
