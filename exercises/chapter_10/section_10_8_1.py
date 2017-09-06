"""Problem 1 of Section 10.8, Fast exponentiation of integers"""

def fastexp(number, power):
    if(power==0): return 1.0
    elif (power%2==1): return number * fastexp(number, power-1)
    else :
        t = fastexp(number, power/2)
        return t*t

print("4**3 = " + str(fastexp(4,3)))
print("2**11 = " + str(fastexp(2, 11)))
