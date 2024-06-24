def outer():
    var1=30
    def inner():
        print(var1)
    inner()
outer()