"""Problem 4 in Chapter 15.9, Recursive Binary Search"""
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def binarySearch(seq, target, lo=0, hi=-1):
    """binarySearch(sequence, number, number, number) -> number

    Returns the index of target in sequence between elements lo and hi
    If the target is not present, returns -1"""
    if(hi == -1): hi=len(seq)-1

    logger.debug("Initial sequence is " + str(seq) + " and looking for " +
                 str(target) + " between %i and %i." % (lo,hi))

    if(lo>hi): return -1
    middle = (lo+hi)//2
    if(seq[middle] == target): return middle
    if(seq[middle] > target): return binarySearch(seq, target, lo, middle-1)
    if(seq[middle] < target): return binarySearch(seq, target, middle+1, hi)

print(binarySearch([1], 1))
print(binarySearch([1, 3, 4, 5, 10, 16], 1))
print(binarySearch([1, 3, 4, 5, 10, 16], 16))
print(binarySearch([1, 3, 4, 5, 10, 16], 5))
print(binarySearch([1, 4, 5, 10, 16], 5))
print(binarySearch([1, 3, 4, 5, 10, 16], 6))
