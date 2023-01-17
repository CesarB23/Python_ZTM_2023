def outer():
    x = "loca"
    def inner():
        nonlocal x
        x = "Nonlocal"
        print("inner:",x)
    inner()
    print("outer:",x)

outer()