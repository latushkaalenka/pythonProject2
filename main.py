f name =='main':
    a1 = int(input('Введите номер стлбца:'))
    b1 = int(input('Введите номер строки:'))
    a2 = int(input('Введите номер стлбца:'))
    b2 = int(input('Введите номер строки:'))
    var = int()
    if a1 - a2 == b1 - b2 :
        print('Yes')
    elif a1 + b1 == a2 + b2:
        print('Yes')
    else:
        print('No')
