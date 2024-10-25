import random
garnir_obed = ["Тефтели с рисом", "Котлеты", "Индейка"]
obed_plus = ["Плов из индейки", "Плов из говядины"]

garnir_ujin = ["Цыплята отварные", "Минтай", "Фрикадельки", "Печень", "Горбуша"]

osnova = ["Гречка", "Картофель отварной", "Макароны", "Картофельное пюре", "Рис"]

dni_nedeli = ["Понедельник", "Вторник", "Среда", "Чутверг", "Пятница", "Суббота", "Воскресенье"]

obed = []
#i = 1
for i in garnir_obed:
    for x in osnova:
        obed.append([i, x])


print(obed)

# full_obed = obed+obed_plus
# print(full_obed)
# print(len(full_obed))


