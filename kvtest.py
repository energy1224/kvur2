baddata = True
while baddata == True:
    try:
        a= int(input('Введите a: '))
        b= int(input('Введите b: '))
        c= int(input('Введите c: '))
        baddata = False
    except:
        print('Не удалось получить данные!')

