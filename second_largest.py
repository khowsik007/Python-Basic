def second_largest(numbers):
    if len(numbers) < 2:
        return "---To find second 2nd largest need atleast 2 numbers is a list---"
    largest = second_l = numbers[1]
    for i in numbers: # starts from 2nd element
        if i > largest:
            second_l = largest
            largest = i
        elif i > second_l and i != largest:
            second_l = i
        if largest == second_l:
            return "--- No distinct second largest found ---"

    return second_l

list_no = [97,56,82,40,78,82]
list_empty = []
print(f"The second largest number is : {second_largest(list_no)}")


