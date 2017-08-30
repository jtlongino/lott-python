""" Exercise 4 from Section 5.5.2 """
print("SACR at medium dive", (33*(3000-500)) / (60*(60+33)))
print("SACR at deeper dive", (33*(3000-500)) / (15*(100+33)))
print("SACR at shallow dive", (33*(3000-1500)) / (60*(30+33)))
print("Can dive at 60 feet for ", (33*(2500-500))/(15.2 * (60+33)), " minutes", sep="")
print("Can dive at 70 feet for ", (33*(2500-500))/(15.2 * (70+33)), " minutes", sep="")
