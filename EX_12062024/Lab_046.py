# Write a program  that calculate and dispplay the letter
# given numberical  score (eg A, b. C D)
# based on the follwing scale
# Mutiple condition:

marks = int(input("Enter the user score : "))
if marks >= 90 and marks <=100:
    print("Your garde is A")
elif marks >=80 and marks<=90:
    print("Your garde is B")
elif marks >= 70 and marks <= 80:
    print("Your garde is C")
elif marks >= 60 and marks <= 70:
    print("Your garde is D")
elif marks >= 50 and marks <= 60:
    print("Your garde is E")
elif marks >= 40 and marks <= 50:
    print("Your garde is F")
else:
    print("Invalid score")


