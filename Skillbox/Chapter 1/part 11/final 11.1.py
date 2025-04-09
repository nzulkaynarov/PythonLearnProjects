eur_prices = float(input("Стоимость покупки в евро: "))
usd_prices = eur_prices * 1.25
rub_prices = usd_prices * 60.87
print("Стоимость в рублях: ", rub_prices)