""" Exercise 3 from Section 5.5.2 """
print("Mortgate payment due is $", round(110000 * ((.0725/12)/(1 - ((1+(.0725/12))**(-(30*12))))), 2), sep="")
