# decorators

# what is deccoraters
# Decoraters is essentially a function that takes other function as argument and  returns a new fucntion
def my_decorater(func):
    def wrapper():
        print("Starting........")
        print("**************************")
        func()
        print("Ending__________")
    return wrapper()

@my_decorater
def sy_hello():
    print("Sy hello")
#sy_hello()
