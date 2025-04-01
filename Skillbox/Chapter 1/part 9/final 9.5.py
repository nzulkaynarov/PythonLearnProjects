cow_place = input('Введите 10 стойл в одну строку. a — свободное стойло, b — занятое:\n')
milk = 0
stall_number = 1

for place in cow_place:
    if place == 'b':
        milk += stall_number * 2 
    stall_number += 1 

print('Произведено молока за день:', milk)