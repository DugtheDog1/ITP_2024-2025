
from datetime import datetime



def purchaseTicket(currentBuyer):
    dt = datetime.now() #DEF VARS
    dayOfWeek = dt.isoweekday()
    childrenTicketPrice = 8
    adultTicketPrice = 12
    seniorTicketPrice = 10
    babyPrice = 0


    if dayOfWeek == 2: #IS IT TUESDAY
        childrenTicketPrice = childrenTicketPrice - 2
        adultTicketPrice = adultTicketPrice - 2
        seniorTicketPrice = seniorTicketPrice - 2

    if currentBuyer < 3 and currentBuyer > 0:
        return babyPrice
    elif currentBuyer < 13 and currentBuyer > 3: #AGE OF PERSON
        return childrenTicketPrice
    elif currentBuyer > 13 and currentBuyer < 65:
        return adultTicketPrice
    else:
        return seniorTicketPrice






movieViewers = [13, 34, 88, 7, 45]
for age in movieViewers:
    print("You age is " + str(age) + " and your ticket costs $" + str(purchaseTicket(age)))

#1/1 - Formatting
#1/1 - Comments
#3/3 - Content