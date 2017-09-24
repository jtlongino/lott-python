"""Problem 2 in Chapter 19.8, The Generator Version of range"""
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def genrange(start, end=None, step=1):
    if(end == None):
        start, end = 0, start

    current = start
    while(current != end):
        yield current
        current += step


myrange = [ num for num in genrange(9, 13, 2)]
print(myrange)
