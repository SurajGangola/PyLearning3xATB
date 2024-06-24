def find_odd_even(num):
    if num % 2==0:
        print("Its is even no")
    else:
        print("it is a odd no")
find_odd_even(4)


check =lambda num : "Even" if num %2 == 0 else "Odd"
print(check(3))