#Ограничение времени	2 секунды
#Ограничение памяти	512Mb
#Ввод	стандартный ввод или input.txt
#Вывод	стандартный вывод или output.txt
import string


for i in range(int(input())):
    l = input().split(',')
    num1 = len(set(''.join(l[0:3])))
    num2 = sum([int(z) for z in list((str(l[3]) + str(l[4])))]) * 64
    num3 = (string.ascii_lowercase.index(l[0][0].lower()) + 1) * 256
    result = (hex(num1 + num2 + num3).upper()[-3:]).ljust(3, '0')
    print(result)