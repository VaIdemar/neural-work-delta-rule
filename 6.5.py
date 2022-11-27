import fun
import numpy as np

def f(z):

    sp = {'*': [0, 0, 0, 0, 1, 0, 0, 0, 0],
          ':': [0, 1, 0, 0, 0, 0, 0, 1, 0],
          '-': [0, 0, 0, 1, 1, 1, 0, 0, 0],
          '+': [0, 1, 0, 1, 1, 1, 0, 1, 0],
          '=': [1, 1, 1, 0, 0, 0, 1, 1, 1]}
    for i in ['*', ':', '-', '+', '=']:
        if i!=z:
            sp[i]+=[0]
        else:
            sp[i]+=[1]

    w = {'*': np.random.random(10) - 1,
         ':': np.random.random(10) - 1,
         '-': np.random.random(10) - 1,
         '+': np.random.random(10) - 1,
         '=': np.random.random(10) - 1}

    for i in ['*', ':', '-', '+', '=']:
        d = 10
        y = fun.proceed(fun.dot(sp[i], w[i]), d)
        e = sp[i][-1] - y
        for m in range(10):
            if e > 0:
                for j in range(9):
                    if sp[z][j] == 1:
                        w[i][j] =  w[i][j] + sp[i][j]*e
                if e < 0:
                    for j in range(9):
                        if sp[i][j] == 1 and sp[z][j] == 0:
                            w[i][j] = w[i][j] - sp[i][j]*e
                else:
                    continue

    for i in ['*', ':', '-', '+', '=']:
        print ( 'Знак', i,' :s=',fun.dot(sp[i], w[i]), 'y=', fun.proceed(fun.dot(sp[i], w[i]), d))

z = input('Какой знак вы хотите распознать? ')
print(f(z))

'''inf=input('Данная программа реализует нейросеть, которая распознает введённый вами знак. Хотите ли вы продолжить работу?').lower()
if inf=='да' or 'yes' or '+':
    z = input('Какой знак вы хотите распознать? ')
    print(f(z))
else:
    print('Досвидания! Хорошего вам дня')'''


"""def dot(f,z):
    s=0
    for i in range (len(f)):
        s=s+z[i]*f[i]
    return s

def proceed(summ,porog):
    if summ>=porog:
        return 1
    else:
        return 0"""