#Лесникова Екатерина, 21ИС21, 14.11.22
#Задание 3. If3. Дано целое число. Если оно является положительным, то вычесть из него 8; если отрицательным, то прибавить к нему 6; если нулевым, то заменить его на 10. 
a=int(input())
if a > 0:
    print (a-8)
elif a == 0:
    print(10)
else:
    print(a+6)
