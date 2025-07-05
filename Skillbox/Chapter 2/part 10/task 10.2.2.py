age = open('ages.txt', 'r')
age_file = age.read()
result = {}
index = 0
names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'k', 'l']
for item in age_file.split():
    result[names[index]] = item
    index += 1
print(result)

result_file = open('result.txt', 'w')

for name, age in result.items():
    result_file.write(name + '-' + age + '\n')