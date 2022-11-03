duration = int(input('duration = '))
if duration < 60: # Если число меньше 60, печатаем сообщение с данной информацией
    print(F"{duration} сек")
elif duration < 3600: # elif позволяет нам проверять несколько выражений
    m = duration // 60
    print(F"{m} мин {duration - m * 60} сек")
elif duration < 8640: # Если число меньше 8640, печатаем сообщение с данной информацией
    m = duration // 60; h = duration // 3600; m = m - h * 60; s = duration - h * 3600 - m * 60
    print(F"{h} час {m} мин {s} сек")
else: # иначе
    d = duration // 86400; t = duration % 86400; h = duration // 3600; duration = duration % 3600; m = duration // 60; s = duration % 60
    print(f"{d} д {h} час {m} мин {s} сек")
