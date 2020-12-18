
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
		print("guardando... "+fich)
		outfile=open(fich,'a')#Indicamoselvalor'w'.
		outfile.write(valor)
		outfile.close()

	except:
		print("Excepcionguardando")

	
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
	guardando_a(fichero_aux,line.rstrip()+'\n')
										
print("Acabado")
#time.sleep(9000)
