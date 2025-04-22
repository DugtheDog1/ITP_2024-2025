#Def ticket prices
childrenTicketPrice = ("$8")
adultTicketPrice= ("$12")
seniorTicketPrice = ("$10")
#Def buyer name
currentBuyer = 68

if currentBuyer < 13:
    print("Your ticket costs ",childrenTicketPrice)
elif currentBuyer > 13 and currentBuyer < 65:
    print("Your ticket costs",adultTicketPrice)
else:
    print("Your ticket costs",seniorTicketPrice)

#1/1 - Formatting
#1/1 - Comments
#3/3 - Content