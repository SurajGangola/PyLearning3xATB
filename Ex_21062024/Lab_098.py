def dec1(f1):
    def wp():
        f1()
        print("Decorator1")
    return wp
def dec2(f1):
    def wp():
        f1()
        print("Decorator2")

    return wp

@dec1
@dec2

def say_hello():
    print("hello")

say_hello()