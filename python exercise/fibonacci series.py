def fib(n):
    print("FIBONACCI SERIES :")
    a, b = 0, 1
    c = 0

    while c < n:
        print(a, end=" ")
        a, b = b, a + b
        c += 1


n = 10
fib(n)