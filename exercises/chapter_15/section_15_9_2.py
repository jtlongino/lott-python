"""Problem 2 in Chapter 15.9, Binary Search"""
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def binarySearch(seq, target):
    """binarySearch(sequence, number) -> number

    Returns the index of target in sequence.
    If the target is not present, returns -1"""

    logger.debug("Initial sequence is " + str(seq) + " and looking for " +
                 str(target))
    l,h = (0,len(seq))
    m = (l+h)//2
    logger.debug("After initialization, l = %i, h = %i, m = %i" % (l,h,m))
    while(l+1 < h and seq[m] != target):
        if(target < seq[m]): h = m
        if(target > seq[m]): l = m+1
        m = (l+h)//2
        logger.debug("After loop, l = %i, h = %i, m = %i" % (l,h,m))
    if(target == seq[m]): return m
    return -1

print(binarySearch([1], 1))
print(binarySearch([1, 3, 4, 5, 10, 16], 1))
print(binarySearch([1, 3, 4, 5, 10, 16], 16))
print(binarySearch([1, 3, 4, 5, 10, 16], 5))
print(binarySearch([1, 4, 5, 10, 16], 5))
print(binarySearch([1, 3, 4, 5, 10, 16], 6))
