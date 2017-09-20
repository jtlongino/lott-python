"""Problem 5 in Chapter 15.9, Sieve of Eratosthenes"""
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def sieve(endNum):
    """sieve(number) -> list

    Returns a list of all prime numbers between 2 and endNum"""

    logger.debug("EndNum is %i" % endNum)
    prime = [True] * (endNum+1)
    primesList = []
    for candidate in range(2, endNum):
        #If number is prime, remove multiples
        if(prime[candidate]):
            primesList.append(candidate)
            for removeNum in range(candidate*2, endNum, candidate):
                prime[removeNum] = False
        else:
            pass
    return primesList


print("Primes < 13: " + (",".join(str(x) for x in sieve(13))))
print("Primes < 5000: " + (",".join(str(x) for x in sieve(5000))))
