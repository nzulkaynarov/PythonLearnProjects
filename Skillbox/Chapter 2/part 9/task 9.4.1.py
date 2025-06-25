file = open('numbers.txt', 'r')
summ = 0
for elem in file:
    summ += int(elem)

new_file = open('answer.txt', 'w')
new_file.write(str(summ))