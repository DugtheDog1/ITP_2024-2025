age = 15

#Age divided by days in year plus days since last birthday
ageMonth = age * 365 + 215
exactAgeMath = ageMonth / 365

print("Today I am exactly " + str(exactAgeMath) + ' years old')
print("Today I am " + aboutAge)

#1/1 - Formatting
#1/1 - Comments
#1/3 - Content
#This is not what was requested. You were supposed to display the float as an integer using int()
print("Today I am exactly",exactAgeMath,'years old')
print("Today I am " + int(age) + " years old")
