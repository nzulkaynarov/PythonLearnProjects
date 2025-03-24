total_book = int(input("Сколько книг выдал библиотекарь? "))
count_damaged_books = 0

while count_damaged_books != 5:
  books_viewed = int(input("Сколько книг просмотрел? "))
  total_book -= books_viewed

  damaged_books = int(input("Сколько из них было испорчено? "))
  count_damaged_books += damaged_books

  if total_book <= 0:
    print("Библиотекарь: На сегодня всё. Благодарю за помощь!")
    break

  if count_damaged_books < 5:
    print("Цель практики ещё не достигнута — встретимся завтра.")
  else:
    print("Ура! Практика завершена!")





