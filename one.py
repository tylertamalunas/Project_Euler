# Problem 1
# Multiples of 3 and 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

five = 5
three = 3
top = 1000

number = 1
sum_of_numbers = 0
number = 1
list_of_nums = []

while number < top:
    if number % 3 == 0:
        sum_of_numbers += number
        list_of_nums.append(number)
        number += 1
    elif number % 5 == 0:
        sum_of_numbers += number
        list_of_nums.append(number)
        number += 1
    else:
        number += 1


#print(list_of_nums)
print(sum_of_numbers)