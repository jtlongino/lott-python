"""Problem 1 in Chapter 15.9, Accumulating Distinct Values"""
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def findDistinct(seq):
    """findDistinct(sequence) -> sequence

    Returns all distinct items in an sequence, removing duplicates"""
    logger.debug("Initial sequence is " + str(seq))
    dv = list()
    for v in seq:
        i=0
        dv.append(v)
        logger.debug(dv)
        while(dv[i] != v):
            logger.debug("Compare %s to %s" % (str(dv[i]), str(v)))
            i += 1
        logger.debug("i is %i, len is %i" % (i, len(dv)))
        if(i != len(dv) - 1):
            dv.pop()
        logger.debug(dv)
    return dv

def findDistinctIndex(seq):
    """findDistinctIndex(sequence) -> sequence

    Returns all distinct items in an sequence, removing duplicates"""
    logger.debug("Initial sequence is " + str(seq))
    dv = list()
    for v in seq:
        i=0
        dv.append(v)
        logger.debug(dv)
        i = dv.index(v)
        logger.debug("i is %i, len is %i" % (i, len(dv)))
        if(i != len(dv) - 1):
            dv.pop()
        logger.debug(dv)
    return dv


print(findDistinct([1, 2, 3, 4]))
print(findDistinct([1, 2, 1, 4]))
print(findDistinct([1, 1, 1, 1]))
print(findDistinct([5, 2, 1, 1]))
print()
print(findDistinctIndex([1, 2, 3, 4]))
print(findDistinctIndex([1, 2, 1, 4]))
print(findDistinctIndex([1, 1, 1, 1]))
print(findDistinctIndex([5, 2, 1, 1]))
