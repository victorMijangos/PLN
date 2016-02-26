# PLN
#-*-encoding:utf8-*-
from collections import Counter,defaultdict

#Genera un diccionario que despues se llena con datos del corpus
def voc():
	dict = defaultdict()
	dict.default_factory = lambda: len(dict)
	return dict

#Llena el diccionario con datos del corpus	
def get_ids(C,dict):
	yield [dict[w] for w in C]
	
#Uso de las funciones
	# dict = voc()
	# lista = list(get_ids(file,dict))
#dict va a ser un diccionario con las referencias númericas de las palabras y
#lista es la sustitución en el archivo original file de las palabras por números.
