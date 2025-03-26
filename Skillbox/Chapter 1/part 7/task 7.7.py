cards = int(input('Введите количество карточек: '))
cards_summ = 0
lost_summ = 0
for card in range (1, cards+1):
	cards_summ += card
print('Сумма всех карточек: ', cards_summ)
for lost_card in range (cards-1):
		cards_number = int(input('Введите номер оставшейся карточки: '))
		lost_summ += cards_number
print('Сумма оставшихся карточек: ', lost_summ)
print('Номер потерянной карточки: ', cards_summ - lost_summ)
		