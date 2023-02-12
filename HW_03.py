quantity = int(input("Уважаемые посетители,\nсообщаем Вам,что при покупке от 3 билетов действиует скидка в 10% на полную "
                     "стоимость заказа!\nУкажите количество билетов: "))
age = list(int(input("Укажите возраст посетителя: ")) for i in range(quantity))
price = []
for t in age:
    if t in range(1,18):
        price.append(0)
    elif t in range(18,25):
        price.append(990)
    else:
        price.append(1390)
if quantity > 3:
    print("Сумма к оплате с учетом скидки: ", sum(price)-((sum(price)/100)*10))
else:
    print("Сумма к оплате: ", sum(price))









