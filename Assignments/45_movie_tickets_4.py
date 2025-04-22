
from datetime import datetime

dt = datetime.now()
dayOfWeek = dt.isoweekday()


def purchaseTicket(currentBuyer):
    childrenTicketPrice = 8
    adultTicketPrice = 12
    seniorTicketPrice = 10
    if dayOfWeek == 2:
        childrenTicketPrice = childrenTicketPrice - 2
        adultTicketPrice = adultTicketPrice - 2
        seniorTicketPrice = seniorTicketPrice - 2
    else:
        childrenTicketPrice = 8
        adultTicketPrice = 12
        seniorTicketPrice = 10
    if currentBuyer < 13:
        print("Your ticket costs",childrenTicketPrice)
    elif currentBuyer > 13 and currentBuyer < 65:
        print("Your ticket costs",adultTicketPrice)
    else:
        print("Your ticket costs",seniorTicketPrice)

movieViewers = [45, 46, 14, 75, 3, 65]
for age in movieViewers:
    purchaseTicket(age)

#1/1 - Formatting
#1/1 - Comments
#3/3 - Content