baddata = True
while baddata == True:
    try:
        a= int(input('Введите a: '))
        b= int(input('Введите b: '))
        c= int(input('Введите c: '))
        baddata = False
    except:
        print('Не удалось получить данные!')

D= (b*b)-(4*a*c)

if D>0:
    print('Два корня')
elif D==0:
    print('Один корень')
else:
    print('Нет корней')