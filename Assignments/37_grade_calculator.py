#Set gpa
GPA = input()

if GPA < str(4) and GPA > str(3.67):
    print("You average is an A")
elif GPA < str(3.67) and GPA > str(3.33):
    print("You average is an A-")
elif GPA < str(3.33) and GPA > str(3.00):
    print("You average is an B+")
elif GPA < str(3.00) and GPA > str(2.67):
    print("You average is an B")
elif GPA < str(2.67) and GPA > str(2.33):
    print("You average is an C+")
elif GPA < str(2.33) and GPA > str(2.00):
    print("You average is an C")
elif GPA < str(2.00) and GPA > str(1.67):
    print("You average is an C-")
elif GPA < str(1.67) and GPA > str(1.33):
    print("You average is an D+")
elif GPA < str(1.33) and GPA > str(1.00):
    print("You average is an D")
elif GPA < str(1.00) and GPA > str(0.67):
    print("You average is an D-")
elif GPA < str(0.67) and GPA > str(0.00):
    print("You average is an F")
else:
    ("Error with GPA Input")

#1/1 - Formatting
#1/1 - Comments
#3/3 - Content