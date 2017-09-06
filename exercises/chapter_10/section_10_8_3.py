"""Problem 3 in Chapter 10.8, Factorial Function"""

def factorial(number):
    if(number == 0): return 1
    if(number > 0): return number * factorial(number-1)
    raise InvalidNumberException("Factorial doesn't accept negative numbers!")


print("4! = " + str(factorial(4)))
print("10! = " + str(factorial(10)))
