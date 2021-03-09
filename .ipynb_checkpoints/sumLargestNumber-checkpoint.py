def sumLargestNumbers(lst_numbers):
    #Sum the two largest numbers in the list given
    if not lst_numbers:
        return 'Error: empty list'
    elif len(lst_numbers) < 2:
        return 'Error: need at least two numbers in a list'
    try:
        largest_num = max(lst_numbers)
        lst_numbers.remove(largest_num)
        second_largest_num = max(lst_numbers) 
        sum_2nums = largest_num + second_largest_num
    except AssertionError as error:
        print(error)
    return sum_2nums

print(sumLargestNumbers([1, 10]))
print(sumLargestNumbers([1, 2, 3]))
print(sumLargestNumbers([10, 4, 34, 6, 92, 2]))