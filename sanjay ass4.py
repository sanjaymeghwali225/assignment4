marks = int(input("Enter your marks: "))
if marks < 25:
    print("Your grade for " + str(marks) + " marks is F")
elif 45 > marks >= 25:
    print("Your grade for " + str(marks) + " marks is E")
elif 50 > marks >= 45:
    print("Your grade for " + str(marks) + " marks is D")
elif 60 > marks >= 50:
    print("Your grade for " + str(marks) + " marks is C")
elif 80 > marks >= 60:
    print("Your grade for " + str(marks) + " marks is B")
elif marks > 80:
    print("Your grade for " + str(marks) + " marks is A")
    year = int(input("Enter a year: "))
if year % 400 == 0:
    is_leap_year = True
elif year % 100 == 0:
    is_leap_year = False
elif year % 4 == 0:
    is_leap_year = True
else:
    is_leap_year = False
if is_leap_year:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
 13
Q3.py
@@ -0,0 +1,13 @@
import random
num_questions = 10
points = 0
for i in range(num_questions):
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    answer = int(input("What is {} x {}? ".format(num1, num2)))
    if answer == num1 * num2:
        points += 1
        print("Correct!")
    else:
        print("Incorrect. The correct answer is {}.".format(num1 * num2))
print("You scored {} points.".format(points))
for i in range(1, 200):
    num = True
    if i % 5 != 2:
        num = False
    if i % 6 != 3:
        num = False
    if i % 7 != 2:
        num = False
    if num == True:
        print(i)