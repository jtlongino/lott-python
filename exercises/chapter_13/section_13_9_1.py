"""Problem 1 in Chapter 13.9, Check Amount Writing"""
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def checkAmount(number):
    """checkAmount(number) -> string

    Translates a number into an english phrase."""

    result = ""
    tens_count = 0
    digit = -1
    group_result = ""

    while(number > 0):
        tens_count_add = 0
        number_div = 1
        logger.debug("STEP 1: Result = %s, group_result = %s, tens_count = %i, number = %i" %
              (result, group_result, tens_count, number))
        if(tens_count%3 == 0): group_result = ""
        if(tens_count%3 == 0 and number%100 < 20):
            group_result += constructTeens(number%100)
            tens_count_add = 2
            number_div = 100
        else:
            digit = number%10
            if(tens_count%3 == 0):
                group_result = constructOnes(digit) + group_result
            elif(tens_count%3 == 1):
                group_result = constructTens(digit) + group_result
            elif(tens_count%3 == 2):
                group_result = constructHundreds(digit) + group_result
            tens_count_add = 1
            number_div = 10
        logger.debug("STEP 2: Result = %s, group_result = %s, tens_count = %i, number = %i" %
              (result, group_result, tens_count, number))
        if(tens_count%3 == 2 and group_result):
            group_result = group_result + getMultiple(tens_count)
            result = group_result.lstrip() + " " + result.lstrip()
            group_result = ""
        tens_count += tens_count_add
        number = number//number_div

    if(tens_count%3 !=0):
        group_result = group_result + getMultiple(tens_count)
        result = group_result.lstrip() + " " + result.lstrip()

    return result.lstrip()

def getMultiple(tens_count):
    """getMultiple(number) -> string

    Returns separator multiple based on a tens count"""

    grouping = tens_count // 3
    logger.debug("Grouping - group is %d" % (grouping))
    if(grouping == 0): return ""
    elif(grouping == 1): return " thousand"
    elif(grouping == 2): return " million"
    else: raise (ArgumentError, "Argument too big!")

def constructOnes(number):
    """constructOnes(number) -> string

    Returns a string value for a number < 10"""
    if(number == 9): return " nine"
    elif(number == 8): return " eight"
    elif(number == 7): return " seven"
    elif(number == 6): return " six"
    elif(number == 5): return " five"
    elif(number == 4): return " four"
    elif(number == 3): return " three"
    elif(number == 2): return " two"
    elif(number == 1): return " one"
    else: return ""

def constructTeens(number):
    """constructTeens(number) -> string

    Returns a string value for a number < 20"""

    if(number == 19): return " nineteen"
    elif(number == 18): return " eighteen"
    elif(number == 17): return " seventeen"
    elif(number == 16): return " sixteen"
    elif(number == 15): return " fifteen"
    elif(number == 14): return " fourteen"
    elif(number == 13): return " thirteen"
    elif(number == 12): return " twelve"
    elif(number == 11): return " eleven"
    elif(number == 10): return " ten"
    else: return constructOnes(number)

def constructTens(number):
    """constructTens(number) -> string

    Returns a string value for a tens digit number between 90 and 20"""

    assert(number >= 2)
    if(number == 9): return " ninety"
    elif(number == 8): return " eighty"
    elif(number == 7): return " seventy"
    elif(number == 6): return " sixty"
    elif(number == 5): return " fifty"
    elif(number == 4): return " forty"
    elif(number == 3): return " thirty"
    else: return " twenty"

def constructHundreds(number):
    """constructHundreds(number) -> string

    Returns hundreds value as a string"""

    assert(number <= 9)
    if(number != 0): return " " + constructOnes(number) + " hundred"
    else: return ""


print(checkAmount(1))
print(checkAmount(8))
print(checkAmount(13))
print(checkAmount(20))
print(checkAmount(54))
print(checkAmount(99))
print(checkAmount(100))
print(checkAmount(116))
print(checkAmount(126))
print(checkAmount(256))
print(checkAmount(401))
print(checkAmount(1216))
print(checkAmount(1268))
print(checkAmount(13578))
print(checkAmount(22349))
print(checkAmount(578939))
print(checkAmount(913273))
print(checkAmount(913000))
print(checkAmount(1000000))
print(checkAmount(1000124))
print(checkAmount(900143000))
