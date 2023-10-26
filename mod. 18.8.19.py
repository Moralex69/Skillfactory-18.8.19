sum_tickets = 0
tickets = int(input("Введите количество билетов: "))
for age in range(tickets):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        sum_tickets += 0
    elif age >= 18 and age <= 25:
        sum_tickets += 990
    elif age > 25:
        sum_tickets += 1390
if tickets > 3:
    discount = sum_tickets / 100 * 10
    print("К оплате с учетом скидки:", sum_tickets - discount, "руб.")
