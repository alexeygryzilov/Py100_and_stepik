
money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month = 1

balance = money_capital + salary - spend

while balance >= 0:
    balance += salary
    balance -= spend * (1 + increase) ** month
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month - 1)
