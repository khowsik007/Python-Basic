def fibo(n):
    a,b = 0,1
    fibonacci_number = []
    for i in range(n):
        fibonacci_number.append(a)
        a,b = b,b+a
    return fibonacci_number
number = 10
print(fibo(number))