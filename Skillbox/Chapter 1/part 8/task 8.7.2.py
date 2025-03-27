boys = int(input('Введите кол-во мальчиков: '))
girls = int(input('Введите кол-во девочек: '))
answer = ''
if (boys > 2 * girls) or (girls > 2 * boys):
    answer = 'Нет решения'
else:
    pair_count = abs(boys - girls)
    if boys >= girls:
        alone_boys_count = girls - pair_count
        answer += 'BGB' * pair_count
        answer += 'BG' * alone_boys_count
    else:
        alone_girls_count = boys - pair_count
        answer += 'GBG' * pair_count
        answer += 'GB' * alone_girls_count

print(answer)