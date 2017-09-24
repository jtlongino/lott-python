"""Problem 1 in Chapter 19.8, Sieve of Eratosthenes"""
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def sieve(endNum):
    """sieve(number) -> list

    Returns an iterator of all prime numbers between 2 and endNum"""

    logger.debug("EndNum is %i" % endNum)
    prime = [True] * (endNum+1)
    for candidate in range(2, endNum):
        #If number is prime, remove multiples
        if(prime[candidate]):
            yield candidate
            for removeNum in range(candidate*2, endNum, candidate):
                prime[removeNum] = False
        else:
            pass
    return

primes = [ prime for prime in sieve(15) ]
print(primes)
