

money = int(input("Сумма вклада: "))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
rate = list(per_cent.values())
incomeTKB = (round(rate[0]/100*money))
incomeSKB = (round(rate[1]/100*money))
incomeVTB = (round(rate[2]/100*money))
incomeSBER = (round(rate[3]/100*money))
deposit = [incomeTKB, incomeSKB, incomeVTB, incomeSBER]
max(deposit)
print('Максимальная сумма, которую Вы можете заработать - ', max(deposit))
