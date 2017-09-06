"""Problem 2 in Chapter 10.8, Greatest Common Divisor"""

def GCD(p, q):
    """Returns the greatest common divisor of p and q"""
    if(p==q): return p
    elif(p<q): return GCD(q,p)
    else: return GCD(p-q,q)

print("GCD of 5 and 10 is " + str(GCD(5, 10)))
print("GCD of 13 and 2 is " + str(GCD(13, 2)))
