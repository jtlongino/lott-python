"""Problem 2 in Chapter 13.9, Roman Numerals"""
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def romanNumeral(number):
    """romanNumeral(number) -> string

    Translates a number into Roman Numerals.
    Number must be less than 4000"""

    if(number>=4000):
        raise ValueError("Number is greater than 4000")
    result = constructOnes(number%10)
    logger.debug("After Construct Ones %s", result)
    number = number//10
    result = constructTens(number%10) + result
    logger.debug("After Construct Tens %s", result)
    number = number//10
    result = constructHundreds(number%10) + result
    number = number//10
    result = constructThousands(number%10) + result
    return result


def constructOnes(number):
    """constructOnes(number) -> string

    Returns a Roman Numeral string value for 10^0 digit"""

    return constructDigit(number, "X", "V", "I")

def constructTens(number):
    """constructTens(number) -> string

    Returns a Roman Numeral string value for 10^1 digit"""

    return constructDigit(number, "C", "L", "X")

def constructHundreds(number):
    """constructHundreds(number) -> string

    Returns a Roman Numeral string value for 10^2 digit"""

    return constructDigit(number, "M", "D", "X")

def constructDigit(number, ten, five, one):
    """constructDigit(number, char, char, char)

    Constructs a Roman Numeral string given maximum (e.g., X), medium (e.g., V)
    and minimum (e.g., I) for a given position."""

    if(number == 9): return one + ten
    elif(5 <= number <= 8): return five + (one*(number-5))
    elif(number == 4): return one + five
    elif(0 <= number <= 3): return one*number
    else: raise ValueError("Number must be between 0 and 9")


def constructThousands(number):
    """constructThousands(number) -> string

    Returns a Roman Numeral string value for 10^3 digit"""

    if(0 <= number <= 3): return "M"*number
    else: raise ValueError("Number must be between 0 and 3")


print(romanNumeral(1))
print(romanNumeral(8))
print(romanNumeral(13))
print(romanNumeral(20))
print(romanNumeral(54))
print(romanNumeral(99))
print(romanNumeral(100))
print(romanNumeral(116))
print(romanNumeral(126))
print(romanNumeral(256))
print(romanNumeral(401))
print(romanNumeral(1216))
print(romanNumeral(1268))
print(romanNumeral(1956))
print(romanNumeral(1994))
print(romanNumeral(3888))
print(romanNumeral(4888))
