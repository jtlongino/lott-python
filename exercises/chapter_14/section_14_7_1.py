"""Problem 1 in Chapter 14.7, Blocks of Stock"""
import logging
import locale
locale.setlocale(locale.LC_ALL, '')
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

portfolio= [ ( "25-Jan-2001", 43.50, 25, 'CAT', 92.45 ),
( "25-Jan-2001", 42.80, 50, 'DD', 51.19 ),
( "25-Jan-2001", 42.10, 75, 'EK', 34.87 ),
( "25-Jan-2001", 37.58, 100, 'GM', 37.58 )
]


def calculatePurchasePrice(portfolio):
    """calculatePurchasePrice(tuple) -> number

    Returns total purchase price for all stock blocks in a portfolio"""

    price = 0
    for stock in portfolio:
        price += stock[1] * stock[2]
    return price

def calculateGain(portfolio):
    """calculateGain(tuple) -> number

    Returns total amount gained or lost in a portfolio"""

    gained = 0
    for stock in portfolio:
        #Calculate (current price - purchase price) * total shared
        gained += (stock[4]-stock[1])*stock[2]

    return gained

print("Purchase price is $%d" % calculatePurchasePrice(portfolio))
print("Purchase price is %s" % str(locale.currency(calculateGain(portfolio))))
