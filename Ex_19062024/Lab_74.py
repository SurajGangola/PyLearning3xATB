#list
number=[1, 2, 3]

def do_something(number):
    number.append(4)
    number[0]=200
    return number

l = do_something(number)
print(l)