"""Problem 3 in Chapter 15.9, QuickSort"""
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def quickSort(seq, lo=0, hi=-1):
    """quickSort(sequence, number, number) -> sequence

    Returns a sorted sequence using the quick sort algorithm"""

    if(hi == -1): hi = len(seq)-1

    logger.debug("Initial sequence is " + str(seq) + " lo is " + str(lo) +
                 " and hi is " + str(hi))
    if(lo >= hi): return
    ls,hs = lo,hi
    middle = (ls+hs)//2

    while(ls < hs):
        logger.debug("Sequence is " + str(seq) + " ls is " + str(ls) +
                 " and hs is " + str(hs) + " and middle is " + str(middle))
        if(seq[ls] <= seq[middle]): ls+=1
        elif(seq[ls] > seq[middle]): seq[ls],seq[middle] = seq[middle],seq[ls]
        if(seq[hs] >= seq[middle]): hs-=1
        elif(seq[hs] < seq[middle]): seq[hs],seq[middle] = seq[middle],seq[hs]

    quickSort(seq, lo, middle)
    quickSort(seq, middle+1, hi)

    return seq




print(quickSort([4, 1]))
print(quickSort([1, 35, 14, 500, 140, 1]))
print(quickSort([1000, 33, 421, 5, -10, 316]))
print(quickSort([1, 3, 4, 5, 10, 16]))
print(quickSort([1, 4, 5, 10, 16]))
print(quickSort([1, 3, 4, 5, 10, 16]))
print(quickSort([1, 3, 1, 5, 10, 2]))
