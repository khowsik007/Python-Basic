def odd_even(n):
    if n%2 == 0:
        print(f"Given number {n} is a even number")
    else:
        print(f"Given number {n} is a odd number")

number = int(input("Enter the Number: "))
odd_even(number)