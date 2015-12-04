import pickle, sys, os

# функция для ввода команды/данных 	
def in_out(text):
	inp=input('{0}: '.format(text))
	return inp

# функция ввода марки автомобиля проверки того, что она состоит только из букв латинского или русского алфавитов. Мощность только из цифр.
def alpha():  

	car=in_out('Введите марку автомобиля')
	if car.isalpha()==True:
		return True, car
	else:
		return None, None

# функция ввода можности автомобиля и проверки того, что она состоит только из цифр.
def digit(): 
	temp=in_out('Введите мощность автомобиля')
	if temp.isdigit()==True:
		power=int(temp)
		return True, power
	else:
		return None, None

def pickle_load(flnm):
	try:
		f = open(flnm, 'rb')
		allcars = pickle.load(f)
		return allcars
	except FileNotFoundError:
		print ('Файла cars.pickle пока не существет')
		allcars = {}
		return allcars
	else:
		print ('Какая-то непонятно как здесь оказавшаяся ошибка')
