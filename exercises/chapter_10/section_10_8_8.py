"""Problem 8 in Chapter 10.8, Field Bet Results"""
import random

def win(dice, num, pays=1):
    """Returns payout for dice value relative to a bet of num"""
    if(dice != num):
        return 0
    else:
        return pays

def field(dice):
    payout = 0
    payout += win(dice, 2, 2)
    payout += win(dice, 3)
    payout += win(dice, 4)
    payout += win(dice, 9)
    payout += win(dice, 10)
    payout += win(dice, 11)
    payout += win(dice, 12, 2)
    assert(payout <= 2)
#    print(str(dice) + "," + str(payout))
    if(payout == 0): payout = -1
    return payout

def roll():
    die1, die2 = random.randrange(1,7), random.randrange(1,7)
    total = die1 + die2
#    print(str(die1) + "," + str(die2) + "=" + str(total))
    assert(total >= 2 and total <= 12)
    return die1 + die2


total_payout = 0
num_rolls = 1000000
for x in range(num_rolls):
    total_payout += field(roll())

print("Payout of " + str(total_payout) + " in " + str(num_rolls) + " gives an \
average of " + str(total_payout/num_rolls))

