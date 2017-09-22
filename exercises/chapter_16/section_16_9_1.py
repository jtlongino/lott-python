"""Problem 1 in Chapter 16.9, Word Frequencies"""
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def findDistinct(seq):
    """findDistinct(sequence) -> sequence

    Returns all distinct items in an sequence, removing duplicates"""
    logger.debug("Initial sequence is " + str(seq))
    dv = {}
    for v in seq:
        if(dv.get(v, None) == None):
            dv[v] = 1
        else:
            dv[v] += 1
        logger.debug(dv)
    return dv



print(findDistinct([1, 2, 3, 4]))
print(findDistinct([1, 2, 1, 4]))
print(findDistinct([1, 1, 1, 1]))
print(findDistinct([5, 2, 1, 1]))
