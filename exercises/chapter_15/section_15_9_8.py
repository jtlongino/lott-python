"""Problem 8 in Chapter 15.9, Dutch National Flag"""
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def flagSort(seq, midVal):
    """flagSort(sequence, number) -> sequence

    Returns a sorted list of three values in O(n) time"""

    logger.debug("Start seq is " + str(seq) + " with midval of " + str(midVal))

    #Set start points for the bottom of high value and top of low and mid
    high = len(seq)-1
    bottom = 0
    mid = 0
    while(mid <= high):
        logger.debug("Seq[%i] = %i" % (mid, seq[mid]))
        if(seq[mid] == midVal):
            mid += 1
        elif(seq[mid] < midVal):
            seq[bottom], seq[mid] = seq[mid], seq[bottom]
            mid += 1
            bottom += 1
        else:
            seq[high], seq[mid] = seq[mid], seq[high]
            high -= 1
        logger.debug("Seq is now " + str(seq) + " lo %i, mid %i, hi %i"
                     %(bottom, mid, high))
    return seq

print(str(flagSort([0, 1, 2, 1, 2, 0], 1)))
print(str(flagSort([0, 0, 1, 1, 2, 2], 1)))
print(str(flagSort([2, 1, 2, 1, 2, 2], 1)))
print(str(flagSort([0, 0, 0, 0, 0, 0], 1)))
print(str(flagSort([2, 1, 0, 2, 0, 1], 1)))
