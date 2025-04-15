def maximum_of_two(first, second):
	if first > second:
		return first
	else:
		return second
		
def maximum_of_three(first, second, third):
	max_two = maximum_of_two(first, second)
	return maximum_of_two(max_two, third)

first_number = int(input("Введите число: "))
second_number = int(input("Введите число: "))
third_number = int(input("Введите число: "))
result = maximum_of_three(first_number, second_number, third_number)
print("Самое большое число:", result)