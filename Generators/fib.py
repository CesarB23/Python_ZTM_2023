def fibonacci(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        print(f"{a} value")
        temp = a
        a = b
        b = temp + b



for i in fibonacci(5):
    print(i)

