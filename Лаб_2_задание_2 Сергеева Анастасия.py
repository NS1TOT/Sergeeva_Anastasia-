# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0
count_months = 0
while count_months < months:
    money_capital += spend - salary
    spend += spend * increase
    count_months += 1
print(f"Подушка безопасности, чтобы протянуть {count_months} месяцев без долгов:", round(money_capital))
