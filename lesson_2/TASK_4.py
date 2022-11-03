a = int(input('Введите первое число '))
c = input('Введите операцию +, -, /, * ')
b = int(input('Введите второе число '))
if c == "+":
     print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
     print(a * b)
elif c == '/':
   if b != 0:
       print(a / b)
   else:
        print('Ошибка! На 0 делить нельзя')










