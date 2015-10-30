#coding: utf-8
lst=['Виталий Жирков','Илья Жирадков','Ирина Манторова','Дмитрий Родин','Андрей Андреев','Дмитрий Журба','Алексей Филиппов','Константин Элсо','Алёна Соколова','Игорь Лавров','Дмитрий Синицкий','Евгений Харченко','Алексей Доброхотов','Катерина Фомина','Роман Делес','Дарья Шкурко','Элеонора Аквитанская','Макс Степанов','Максим Аласкаров']
lst.sort()

print ('\n\nЗадание 1 (Вывод имени одного студента)\n')
n=len(lst)
a=int(input('Всего в списке {} имен. Введите номер от 1 до {}:'.format(n,n)))
a=a-1
if (a <= n):
    print (lst[a])
else:
    print ('Неверное число')\

print ('\nЗадание 2 (Вывод на экран имен студентов из среза)\n')
b=int(input('Введите начало среза: '))
if (b <= n):
    b=b-1
    c=int(input('Введите конец среза: '))
    if (c <= n):
        for i in range(b,c):
            print(lst[i])
    else:
        print ('Неверное число')
else:
    print ('Неверное число')


print ('\nЗадание 3 (Поиск количества студентов, в именах которых есть буква "р")\n')
x=0
for ln in lst:
    if 'р' in ln:
        x=x+1 
    else:
        continue
print (x)


print ('\nЗадание 4 (Поиск студентов с одинаковыми именами, создание списков таких студентов)\n')

names = []
names1=[]
students = []
for i in lst:
    name = i.split()[0]
    names1.append(name)
    if name not in students:
        names.append(name)
        students.append([i])
    else:
        students[ names.index(name) ].append(i)

print (students)

names_set=sorted(set(names))






