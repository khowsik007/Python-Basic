def smallest_no(n):
    if not n:
        return "!!! Need atleast 1 elements or invaild !!"
    smallest_number = n[0]
    for i in n:
        if i < smallest_number:
            smallest_number = i
    return smallest_number

number = eval(input("Enter the list of Numbers :"))
print(f"Smallest number is: {smallest_no(number)}")