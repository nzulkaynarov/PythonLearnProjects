import random

first_tuple = tuple(random.randint(0, 5) for number in range(10))
second_tuple = tuple(random.randint(-5, 0) for number in range(10))
third_tuple = first_tuple + second_tuple
zero_count = third_tuple.count(0)
print("First tuple:", first_tuple)
print("Second tuple:", second_tuple)
print('Third tuple: ', third_tuple)
print('Count of Zero in Third tuple: ', zero_count)