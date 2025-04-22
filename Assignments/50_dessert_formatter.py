desserts_in_process = ["Strawberry Cheese Cake", "Cherry Cheese Cake", "Strawberry Ice Cream", "Vanilla Ice Cream", "Cookie Dough Ice Cream"]

test_string = ["gus", "mike", "walter", "skyler", "walt jr"]

completed_desserts = []


def foo(list_of_string):
    bar = []
    for x in range(len(list_of_string)): #get string len in list leng
        current_dessert = list_of_string.pop(0) #Pop it 
        current_dessert = current_dessert.upper() #Make it upper
        bar.append(current_dessert) #Append to completed
    return bar


completed_desserts = foo(desserts_in_process)



print(completed_desserts)

#Append bar to completed_desserts?

#1/1 - Formatting
#1/1 - Comments
#3/3 - Content