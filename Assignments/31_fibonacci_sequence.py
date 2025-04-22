# solveTo = 100

# previousNumber = 0
# nextNumber = 1

# endNumber = previousNumber + nextNumber 

# print(endNumber)

# test = nextNumber + endNumber

# print(test)

# test2 = test + endNumber

# print(test2)

# test3 = test2 + test

# print(test3)
# # for x in solveTo:
# #     print(endNumber + nextNumber)

# solveTo = 2
# fibA = 0
# fibB = 1

# for x in range(solveTo):
#     test = fibA + fibB
#     print(test)

#     fibA = fibA + 1
#     fibB = test + 0

#     print(fibA)
#     print(fibB)




# prevNum = 0
# nextNum = 1
# totalNum = 0

# for x in range(2):
#     totalNum = prevNum + nextNum

#     print(totalNum)

#     nextNum = nextNum + 1
#     xVar = totalNum + nextNum
#     print(xVar)


#How to quit programming?

# f1 = -1
# f2 = 0
# for z in range(5):
#     f1 = f1 + 1
#     f2 = f2 + 1
#     f3 = f2 + f1
#     print(f3)
#     f1 = f3 + f2
#     print(f1)




# n = 0

# for x in range(1):

#     f1 = n - 1
#     f2 = n - 2

#     f3 = f2 + f1

#     print(f3)
#     n = n + 1



#FIX

# for x in range(2):
#     list = [0, 1]

#     num1 = list.pop(x)
#     list.insert(x,num1)
#     num2 = list.pop(x)
#     list.insert(x,num2)

#     print("Num 1 is",num1)
#     print("Num 2 is",num2)

    # print(num1 + num2)
    # list.append(num1 + num2)

    # print(list)





x = 0
y = 1
fib = [0, 1]

fibInput = input("Enter the specified length: ")
fibInput = int(fibInput)

for x in range(fibInput):    
    num1 = fib.pop(x)
    fib.insert(x,num1)
    num2 = fib.pop(y)
    fib.insert(y,num2)

    total = num1 + num2
    fib.append(total)
    
    x = x + 1
    y = y + 1

print(fib)

#1/1 - Formatting
#1/1 - Comments
#3/3 - Content