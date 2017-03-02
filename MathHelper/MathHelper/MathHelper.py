import sys

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
    
def main(input):
    if len(input) == 1:
        return welcome_messedge + help_messedge
        
    elif len(input) > 2:
        parameter = input[1]
        list = input[2:]
        
        for i in input[2:]:
            if not(i.isdigit()):
                return error_messedge + help_messedge        
        
        if parameter == '-am':
            return arithmetic_mean( list )
            
        elif parameter == '-gm':
            return geometric_mean( list )
            
        else:
            return error_messedge + help_messedge    
    
    else:
        
        return error_messedge + help_messedge
        

welcome_messedge = 'Здравствуйте, данная программа вычисляет среднее арифметическое и среднее геометрическое для списка чисел\n'
help_messedge = '''Вызовите программу с одним из следующих аргументов:\n
           -am <список чисел> - вычисляет среднее арифметическое для списка чисел.
            Разрешаются только положительные числа. Например, -am 1 2 3 4 5\n
           -gm <список чисел> - вычисляет среднее геометрическое для списка чисел.
            Разрешаются только положительные числа. Например, -gm 3 3 3'''
error_messedge = 'Вы ввели неправильные аргументы\n'
            
inp = sys.argv
print(main(inp))      
#print(sys.argv[1:])