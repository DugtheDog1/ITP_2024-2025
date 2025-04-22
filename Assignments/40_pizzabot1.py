#The toppings that available to go on a pizza
toppings = ["Grilled Chicken", "Pepperoni", "Beef", "Spicy Italian Sausage", "Bacon", "Sausage", "Canadian Bacon", "Mushrooms", "Green Olives", "Roma Tomatoes", "Pineapple", "Onions", "Black Olives", "Jalapeno Peppers", "Banana Peppers", "Green Peppers"]

#The pizza requests
first_pizza = ["Sausage", "Pepperoni", "Onions", "Green Peppers"]
second_pizza = ["Spicy Italian Sausage", "Skittles", "Pork Chops", "Mushrooms", "Brownies"]
third_pizza = ["Canadian Bacon", "Jalapeño Peppers, but not the gross pickled kind, because those give me a stomachache", "Grilled Onions","Pineapple"]

current_pizza = []

def order(z, name):
    print("Order recieved:", name)
    for x in toppings:
        if x in z:
            current_pizza.append(x)
    print("Your pizza is baking")
    print("The toppings on your pizza are:",current_pizza)
    current_pizza.clear()


order(first_pizza, "First Pizza")
order(second_pizza, "Second Pizza")
order(third_pizza, "Third Pizza") 

#1/1 - Formatting
#1/1 - Comments
#3/3 - Content