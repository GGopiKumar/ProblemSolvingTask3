"""
Author : G Gopi Kumar
Date : 16/10/2024

Program 1 : You have been given a Python List [10, 501, 22, 37, 100, 999, 87, 351] your task is to
create two List one which have all the Even Numbers and another List which will have all
the ODD numbers in it ?

"""
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Even:", even_numbers)
print("Odd:", odd_numbers)


"""
Author : G Gopi Kumar
Date : 16/10/2024

Program 2 : Given a Python List [10, 501, 22, 37, 100, 999, 87, 351] your task is to Count all the
Prime Numbers and create a new Python List which will contain all the Prime Numbers
in it ?

"""
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = [num for num in [10, 501, 22, 37, 100, 999, 87, 351] if is_prime(num)]
print("Prime Numbers:", prime_numbers)


"""
Author : G Gopi Kumar
Date : 16/10/2024

Program 3 : Given a Python List [10, 501, 22, 37, 100, 999, 87, 351] Find out how many numbers are
there in the given Python List which are Happy Numbers ?

"""
def is_happy_number(n):
    visited = set()
    while n != 1 and n not in visited:
        visited.add(n)
        n = sum(int(i) ** 2 for i in str(n))
    return n == 1

numbers = [10, 501, 22, 37, 100, 999, 87, 351]
happy_numbers = [num for num in numbers if is_happy_number(num)]
print("Happy Numbers:", happy_numbers)


"""
Author : G Gopi Kumar
Date : 16/10/2024

Program 4 : Write a python program to find the sum of the first and last digit of an integer ?

"""

def sum_first_last_digit(n):
    n_str = str(n)
    return int(n_str[0]) + int(n_str[-1])

n = 35462
print("Sum of first and last digit:", sum_first_last_digit(n))



"""
Author : G Gopi Kumar
Date : 16/10/2024

Program 5 : You have been given a list of N integers which represents the number of
Mangoes in a bag. Each bag has a variable number of Mangoes. There are M
students in a Guvi class, your task is to distribute the Mangoes in such a way that
each student gets one Bag. The difference between the number of Mangoes in a
bag with maximum Mangoes and Bag with minimum Mangoes given to the
student is minimum ?

"""

def distribute_mangoes(bags, students):
    bags.sort()
    min_difference = min(bags[i + students - 1] - bags[i] for i in range(len(bags) - students + 1))
    return min_difference

bags = [10, 501, 22, 37, 100, 999, 87, 351]
students = 3
print("Minimum difference in mangoes:", distribute_mangoes(bags, students))

"""
Author : G Gopi Kumar
Date : 16/10/2024

Program 6 : You have been given three lists. Your task is to find the duplicates in the three
lists. Write a python program for the same. You can use your own python lists ?

"""

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

duplicates = list(set(list1) & set(list2) & set(list3))
print("Duplicates:", duplicates)


"""
Author : G Gopi Kumar
Date : 16/10/2024

Program 7 : Write a python program to find the first non - repeating elements in a given list of
integers ?

"""

def first_non_repeating(lst):
    for num in lst:
        if lst.count(num) == 1:
            return num
    return None

lst = [4, 5, 1, 2, 0, 4, 5]
print("First non-repeating element:", first_non_repeating(lst))


"""
Author : G Gopi Kumar
Date : 16/10/2024

Program 8 : Write a python program to find the minimum element in a rated and sorted list ?

"""

def find_min_in_rotated(arr):
    return min(arr)

arr = [4, 5, 6, 7, 0, 1, 2]
print("Minimum element:", find_min_in_rotated(arr))


"""
Author : G Gopi Kumar
Date : 16/10/2024

Program 9 : You have been given a Python list [10,20,30,9] and a value of 59. Write a python
program to find the triplet in the list whose sum is equal to the given value ?

"""

def find_triplet_with_sum(lst, target_sum):
    n = len(lst)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if lst[i] + lst[j] + lst[k] == target_sum:
                    return (lst[i], lst[j], lst[k])
    return None

lst = [10, 20, 30, 9]
target_sum = 59
print("Triplet with sum:", find_triplet_with_sum(lst, target_sum))


"""
Author : G Gopi Kumar
Date : 16/10/2024

Program 10 : Given a list [4,2,-3,1,6] Write a python program to find if there is a sub-list with
sum equal to Zero ?

"""

def has_zero_sum_sublist(lst):
    # Create a set to store the cumulative sums
    sums_set = set()
    current_sum = 0

    for num in lst:
        current_sum += num
        if current_sum == 0 or current_sum in sums_set:
            return True
        sums_set.add(current_sum)

    return False

# Given list
lst = [4, 2, -3, 1, 6]
result = has_zero_sum_sublist(lst)
print("Is there a sublist with sum 0?", result)

