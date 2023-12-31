numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers)
# 1.Change the first element of numbers to "ten" (the string, not the number 10)
# 2.Change the last element of numbers to 1
# 3.Print all the elements from numbers except the first two (slice)
# 4.Print whether 9 is an element of numbers
"""
numbers[0] = 3
numbers[-1] = 2
numbers[3] = 1
numbers[:-1] = 3, 1, 4, 1, 5, 9 X
numbers[:-1] = [3, 1, 4, 1, 5, 9]
numbers[3:4] = 1 X
numbers[3:4] = [1]
5 in numbers = True
7 in numbers = False
"3" in numbers = False
numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""

"""
1. Change the first element of numbers to "ten" (the string, not the number 10)
"""
numbers[0] = "ten"
print(numbers)

"""
2. Change the last element of numbers to 1
"""
numbers[-1] = 1
print(numbers)

"""
3. Print all the elements from numbers except the first two (slice)
"""

print(numbers[2:])
"""
4. Print whether 9 is an element of numbers
"""

if 9 in numbers:
    print("9 is an element of numbers")
else:
    print("9 is not an element of numbers")
