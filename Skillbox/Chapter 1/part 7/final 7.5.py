for i in range(10, 100):
    first_item = i // 10
    second_item = i % 10
    if first_item * second_item * 3 == i:
        print(i)