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
 
if len(db.allcars) == 0:
	db.allcars = data
else:
	for i in range(len(db.allcars)):
		db.allcars.update(data)

debug.pickle_safe(db.allcars,db.flnm)