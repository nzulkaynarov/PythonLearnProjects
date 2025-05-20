def nice_view(text):
    text = ", ".join(text.split(';'))
    return text.title()
site_menu = input('Введите доступное меню: ')
print('Доступное меню:', site_menu)
print('На данный момент в меню есть:', nice_view(site_menu))
