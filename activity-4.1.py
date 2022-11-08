# Problem 1: Write a lambda function to sort a list of tuples in ascending order according to the number in the second position of each tuple.
grades = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_grades = sorted(grades, key = lambda x: x[1])
print(sorted_grades)

cubed = lambda x: [i**3 for i in x]
print(cubed([3,6,9,2]))
# Original list: [3,6,9,2] List after lambda function: [27,216,729,8]

# Write a lambda function to determine whether a number is even or odd (the function should return True or False), and then use the function and a list comprehension to create a new list of booleans, where even numbers are True and odd numbers are False.
# Input list: [3,6,9,2] List after lambda function and list comprehension: [False, True, False, True]
even_odd = lambda x: True if x%2 == 0 else False
print([even_odd(x) for x in [3,6,9,2]])

# Use a list comprehension to create a list of the numbers from 1 to 100 (including 100).
nums = [i for i in range(1,101)]
print(nums)

# Use a dictionary comprehension to count the length of each word in a sentence.
# Input: "The quick brown fox jumped over the fence." otuput: {'The': 3, 'quick': 5, 'brown': 5, 'fox': 3, 'jumped': 6, 'over': 4, 'the': 3, 'fence.': 6}
sent = "The quick brown fox jumped over the fence."
print({word:len(word) for word in sent.split()})