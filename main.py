import random
garnir_obed = ["Тефтели с рисом", "Котлеты", "Индейка"]
obed_plus = ["Плов из индейки", "Плов из говядины"]

garnir_ujin = ["Цыплята отварные", "Минтай", "Фрикадельки", "Печень", "Горбуша"]

osnova = ["Гречка", "Картофель отварной", "Макароны", "Картофельное пюре", "Рис"]

dni_nedeli = ["Понедельник", "Вторник", "Среда", "Чутверг", "Пятница", "Суббота", "Воскресенье"]

obed = []
i = 1
while len(obed) < 7:
    osnova_el = random.choice(osnova)
    garnir_el = random.choice(garnir_obed)
    if len(obed)!=0:
        if osnova_el != obed[i-1][0] and garnir_el != obed[i-1][1]:
            obed.append([osnova_el, garnir_el])
            # osnova.remove(osnova_el)
            i = i+1
    else:
        obed.append([osnova_el, garnir_el])
    
print(obed)
print(len(obed))


