import pickle, sys
import os



# функция загрузки данных из cars.pickle:
def pickle_load(flnm):
	
	if os.path.exists(flnm):
		f = open(flnm, 'rb')
		allcars = pickle.load(f)
		return allcars
	else:
		allcars={}
		return allcars

flnm = 'cars.pickle'
allcars = pickle_load(flnm)
values_list=[] # этот кусок кода - для фильтрации и поиска
keys_list=[]
for keys,values in allcars.items():
	values_list.append(values)
	keys_list.append(keys)

# функция сохранения в cars.pickle:
def pickle_safe(allcars,flnm): 

	f=open(flnm, 'wb')
	pickle.dump(allcars,f)
	f.close()
	exit()

# функция для ввода команды/данных 	
def in_out(text):
	inp=input('{0}: '.format(text))
	return inp

# общая функция проверки правильности данных, введенных пользователем
def proverka(func):  
	ToF,var=func()
	while ToF is not True:
		print ('Ошибка, попробуйте еще раз')
		ToF,var=func()
	else:
		return var

# функция проверки того, что марка состоит только из букв латинского или русского алфавитов. Мощность только из цифр.
def alpha():  

	car=in_out('Введите марку автомобиля')
	if car.isalpha()==True:
		return True, car
	else:
		return None, None

# функция проверки того, что можность состоит только из цифр.
def digit(): 
	temp=in_out('Введите мощность автомобиля')
	power=int(temp)
	if temp.isdigit()==True:
		return True, power
	else:
		return None, None

# функция вывода
def vivseti(flnm): 
	if os.path.exists(flnm):
		q = open(flnm, 'rb')
		allcars = pickle.load(q)
		allcars_s_c=sorted(allcars)


		print ('Все данные:')
		for i in allcars:
			value = allcars[i]
			print (i, '-', value)

		print ('Данные, сортированные по имени:')
		for i in sorted(allcars):
			value = allcars[i]
			print (i, '-', value)
		sorted_list = [(k,v) for v,k in sorted([(v,k) for k,v in allcars.items()])]
		
		print ('Данные, сортированные по мощности:')
		for i in sorted_list:
			print(i)
		sys.exit(0)
		
	else:
		print ('База пуста. Сначала введите хотя бы одно значение')

# запускающая функция
def cycle(): 
	while True:
		wtd_inp=in_out('Ввести или вывести?')
		if wtd_inp == 'Ввести' or wtd_inp == 'ввести':
			data = {proverka(alpha):proverka(digit)}
			return True, data
			break
		elif wtd_inp == 'Вывести' or wtd_inp == 'вывести':
			vivseti(flnm)
		else:
			return None, None

# функция поиска по названию
def search_name():
	car_search = in_out ('Введите модель автомобиля или слово для поиска: ')
	for i in range(len(keys_list)):
		if car_search in keys_list[i]:
			print (keys_list[i])
			sys.exit(0)

#функция поиска по мощности:
def search_power(values_list):
	while True:
		P1=input('Введите первое значение из промежутка: ')
		P2=input('Введите второе значение из промежутка (большее): ')

		if P1.isdigit()==True and P2.isdigit()==True:

			print ('Модели автомобилей с мощностью больше, чем', P1,':')
			for i in range(len(values_list)):
				if int(P1)<int(values_list[i]):
					print (keys_list[i])


			print ('Модели автомобилей с мощностью меньше, чем', P1,':')
			for j in range(len(values_list)):
				if int(P1)>int(values_list[j]):
					print (keys_list[j])

			print ('Модели автомобилей с мощностью в промежутке между', P1,'и', P2)
			for j in range(len(values_list)):
				if int(P1) < int(values_list[j]) < int(P2):
					print (keys_list[j])
			sys.exit(0)

		else:
			print ('Должны быть только цифры')	

def s_earch():
	while True:
		wtd1=in_out('Внимание! Регистр учитывается!\nПоиск по мощности (введите P) или по марке(введите М)? ')
		if (wtd1 == 'P' or wtd1 == 'Р' or wtd1 == 'M' or wtd1 == 'М')==True:
			if wtd1 == 'P' or wtd1 == 'Р':
				search_power(values_list)
				break
			elif wtd1 == 'M' or wtd1 == 'М':
				search_name()
				break
			else:
				print ('Ошибка, попробуйте еще раз')



while True:
	wtd=in_out('Поиск или Работа с данным?:')
	if wtd == 'Работа' or wtd == 'работа' or wtd == 'Работа с данными' or wtd == 'работа с данными':
		allcars = pickle_load(flnm)
		data = proverka(cycle)
		break
	elif wtd == 'Поиск' or wtd == 'поиск':
		s_earch()
	else:
		print ('Ошибка, попробуйте еще раз')
 





if len(allcars) == 0:
	allcars = data
else:
	for i in range(len(allcars)):
		allcars.update(data)

pickle_safe(allcars,flnm)
