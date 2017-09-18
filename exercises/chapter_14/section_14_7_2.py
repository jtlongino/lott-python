"""Problem 3 in Chapter 14.7, Standard Deviation"""
import logging
import math
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def calculateStandardDeviation(sequence):
    """calculateStandardDeviation(sequence) -> number

    Returns the standard deviation of a sequence"""

    if(len(sequence)<=1): raise ValueError("Standard Deviation only valid for \
sequences of at least two items.")
    mean = calculateMean(sequence)
    sum_ = 0

    for item in sequence:
        difference = item-mean
        sum_ += difference**2
    variance = sum_/(len(sequence) - 1)
    return math.sqrt(variance)



def calculateMean(sequence):
    """calculateMean(sequence) -> number

    Calculates the mean of a sequence. Assumes addition is defined for sequence
    items"""

    return sum(sequence)/len(sequence)

print("SD of (1, 2, 3) is %f" % calculateStandardDeviation((1, 2, 3)))
print("SD of (3,3) is %f" % calculateStandardDeviation((3,3)))
print("SD of (-1, 2, 3) is %f" % calculateStandardDeviation((-1, 2, 3)))
