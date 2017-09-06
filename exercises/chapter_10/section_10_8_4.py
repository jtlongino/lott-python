"""Problem 4 in Chapter 10.8, Fibonacci Sequence"""

def fibo(number):
    if(number == 0): return 0
    elif(number == 1): return 1
    elif(number > 1): return fibo(number-1) + fibo(number-2)
    raise InvalidNumberException("Factorial doesn't accept negative numbers!")


print("fibo(4) = " + str(fibo(4)))
print("fibo(10) = " + str(fibo(10)))
