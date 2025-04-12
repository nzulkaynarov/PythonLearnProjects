def is_prime(num):
		if num % 2 == 0:
				print("четное")
		else:
				print("нечетное")

while True:
	num = int(input("Введите число: "))
	is_prime(num)