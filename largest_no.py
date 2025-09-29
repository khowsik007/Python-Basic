def largest_no(numbers):
    if numbers is None:
        return "It is an empty list"
    largest_number =numbers[0]
    for i in numbers:
        if i > largest_number:
            largest_number = i
    return largest_number
list_no = [12,52,1,22]
list_2 = [8,32,45,2,23,89,3]
print(f"The largest number is : {largest_no(list_2)}")