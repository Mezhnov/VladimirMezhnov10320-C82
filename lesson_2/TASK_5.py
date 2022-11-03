a = int(input('Введите год: '))
if a % 4 == 0:
    print(str(a)+' високосный год')
elif a % 100 == 0:
    if a % 400 == 0:
        print('str(a)+ не високосный год')
    else:
        print('Год  високосный')
else:
    print(str(a) +' не високосный год')

