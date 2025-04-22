
def fizbuzzFunction(num_rounds):
    for x in range(num_rounds):
        if x % 5 == 0 and x % 3 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)


# fizbuzzFunction(25)

#1/1 - Formatting
#1/1 - Comments
#3/3 - Content
fizbuzzFunction(int(input()))
