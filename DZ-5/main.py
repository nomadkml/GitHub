import db
flnm = 'cars.pickle'
allcars = db.pickle_load(flnm)

values_list=[] # этот кусок кода - для фильтрации и поиска
keys_list=[]
if len(allcars) != 0:
	try:		
		for keys,values in allcars.items():
			values_list.append(values)
			keys_list.append(keys)
	except:
		print ('Что-то пошло не так')


if __name__ == "__main__":
	import db, debug
	import pickle, sys, os



	while True:
		wtd=db.in_out('Поиск или Работа с данным?:')
		if wtd == 'Работа' or wtd == 'работа' or wtd == 'Работа с данными' or wtd == 'работа с данными':
			data = debug.proverka(debug.cycle)
			break
		elif wtd == 'Поиск' or wtd == 'поиск':
			debug.s_earch()
		else:
			print ('Ошибка, попробуйте еще раз')
	 
	if len(allcars) == 0:
		allcars = data
	else:
		for i in range(len(allcars)):
			allcars.update(data)

	debug.pickle_safe(allcars,flnm)