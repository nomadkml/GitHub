#coding: UTF-8
import sys, time, os, argparse

parser = argparse.ArgumentParser()
parser.add_argument('typ',type=str, help='Расширение файла')
parser.add_argument('stroka',type=str,help='Что ищем')
args = parser.parse_args()

def find(rash): # создаем функцию find
	for filename in os.listdir('.'): # перечисляем все имена файлов в текущей директории
		if filename.endswith(rash): # проверяем окончание
			for i, line in enumerate(open(filename).readlines()): # читаем построчно, в i - порядковый номер строки, в line - строчки из файла - !!можно без readlines!! - хз почему
				yield filename, i, line #возвращает имя файла, номер строки и строку

def grep(gen,substr): #создаем функцию grep с атрибутами gen и substr
	for name, i, s in gen: # 
		if substr not in s:
			yield name, i, s

for name, i, s in grep(gen=find(args.typ) ,substr=args.stroka):
	print (name, i, s)

print (" Расширение:",args.typ)
print (" Строка поиска:",args.stroka)