import math
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
    d = math.sqrt(D)
    X1= ((-b)+d)/(2*a)
    X2 = ((-b) - d) / (2 * a)
elif D==0:
    print('Один корень')
    X1 = (-b) / (2 * a)
else:
    print('Нет корней')