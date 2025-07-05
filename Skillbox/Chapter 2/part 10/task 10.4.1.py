names_file = open('people.txt', 'r')
count = 0

for item in names_file:
    name_len = len(item.rstrip())
    count += name_len
    if len(item.strip('\n')) <  3:
        raise Exception
print(count)
