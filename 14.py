# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.
# 10 -> 1 2 4 8

n=int(input("Введите N: "))
k=0
count_i=0
while count_i<n:
    count_i=2**k
    if count_i>n:
        break
    else:
        k+=1
    print(count_i,end=" ")