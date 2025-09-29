def sum_elements(n):
    if not n:
        return " Invalid Elements !!"
    sum = 0
    for i in n:
        sum += i
    return sum
numbers = eval(input("Enter the Numbers :"))
print(sum_elements(numbers))