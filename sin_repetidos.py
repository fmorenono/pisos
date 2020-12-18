
#-*-coding:utf-8-*-_
import urllib.request,unicodedata,time,_thread
from bs4 import BeautifulSoup
from datetime import datetime,date,timedelta
import sys

def buscar_id(url3)	:	
	finTexto=url3.find(".htm")
	textoAux=url3[:finTexto]
	print(textoAux)
	inicioTexto=textoAux.rfind("i")
	textoo=textoAux[inicioTexto:]
	print(textoo)
	return textoo


def guardando_a(fich,valor):
	try:
		#print("guardando... "+fich)
		outfile=open(fich,'a')#Indicamoselvalor'w'.
		outfile.write(valor)
		outfile.close()

	except:
		print("Excepcionguardando")

def existe(fich,valor):
	encontrado=False
	try:
		infile=open(fich,'r')
		for line in list(infile):
				if (line.find(valor)>-1):
					encontrado=True
					
		infile.close()
		return encontrado
	except:
		print("no existe el fichero")


	
#Programaprincipal
now=time.localtime(time.time())
print('Comienza elprograma'+time.strftime("%c",now))
time.sleep(1)
fichero_inicial=sys.argv[1]
fichero_aux=fichero_inicial+'.aux'
#fichero='datos'+str(fecha_inicio)+'.csv'
#fichero=fichero.replace('/','_')
#time.sleep(1)
z=1
#while z<1000:
for line in reversed(list(open(fichero_inicial))):
	bloques=line.split(sep=';')
	bloc=bloques[1]
	#print("Xxx"+bloc)
	if not existe(fichero_aux,bloc):
		guardando_a(fichero_aux,line.rstrip()+'\n')
	else:
		print('existe '+bloc)
										
print("Acabado")
#time.sleep(9000)
