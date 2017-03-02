import sys


parameter = sys.argv[1]
list = sys.argv[2:]


def arithmetic_mean(list):
    sum = 0
    for i in list:
        sum += int(i)    
    return sum / len(list)


def geometric_mean(list):
    multiplication = 1
    for i in list:
        multiplication *= int(i)
    return multiplication ** (1/len(list))
    
if parameter == '-am':
    print(  arithmetic_mean( list )  ) 

elif parameter == '-gm':
    print(  geometric_mean( list )  )
    
    

else:
    print('Здравствуйте, Вас приветсвует программа вычисления среднего арифметического и геометрического списка чисел')
    print('''Вызовите программу с одним из следующих аргументов:\n
           -am <список чисел> - вычисляет среднее арифметическое для списка чисел.\n
            Разрешаются только положительные числа. Например, -am 1 2 3 4 5\n
           -gm <список чисел> - вычисляет среднее геометрическое для списка чисел.\n
            Разрешаются только положительные числа. Например, -gm 3 3 3''')


print(sys.argv[1:])