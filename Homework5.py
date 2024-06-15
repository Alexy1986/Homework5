immutable_var=1,2,3, True, "a","b" #В кортеже коллекция неизменяема. Числа, строки нельзя изменить.
immutable_var1=([1,2,3], True, "a","b") #Если в кортеж помещаем список [] то его можно изменить.
print(immutable_var)
immutable_var1[0][0] = 2
print(immutable_var1)

mutable_list=[1,2,3,'a','b','Modified']
print(mutable_list)

mutable_list[0]=6# замена 1 на 6
print(mutable_list)

mutable_list[5]='minecraft'#замена слова Modidied на Minecraft
print(mutable_list)

mutable_list.append(True)# добавляем в конец списка True
print(mutable_list)

mutable_list.insert(0,9)# добавляем в начало списка число 9
print(mutable_list)

print([99]+mutable_list)# добавляем в начало списка число 9

mutable_list.extend(['alex',4])# добавляет в конец списка Alex и 4, если убрать [] то alex добавит по буквам
print(mutable_list)

print("a" in mutable_list)# имеется "а" в переменной mutable_list
print("a" not in mutable_list)# "a" не содержится в переменной mutable_list
print("z" in mutable_list)# имеется "z" в списке  нет поэтому False
print("x" not in mutable_list)# "z" нет в списке поэтому True