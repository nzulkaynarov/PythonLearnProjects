cheese = 60
ice_cream = 20
cash = int(input('Сколько дали денег? '))

if cash >= cheese:
  print('На сыр денег хватило')
  cash -= cheese
  if cash >= ice_cream:
    print('И на мороженое тоже!')
    cash -= ice_cream
  else:
    print('Денег маловато')

else:
  print('Денег не хватило даже на сыр!')
print('У тебя всего денег: ', cash)