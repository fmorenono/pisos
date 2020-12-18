
#-*-coding:utf-8-*-_
import urllib.request,unicodedata,time,_thread
from bs4 import BeautifulSoup
from datetime import datetime,date,timedelta
import sys

dia='2020-07-11'
casas=['B3','SK','LD','WH','EE','FB','VC','PP','UN','CE','FR','WA','SA','BY','VT','OE','SE','GN','PE','SX','BF','BD','MK']

def calcular_cuota(cuota):
	n=cuota.find("/")
	#print(str(n)+"xxxxxxxxxxxxxxxxxxx"+cuota)
	#time.sleep(5)
	if(n<1):
		return cuota	
	else:
		deci=1000.0
		n1=cuota[0:n]
		n2=cuota[n+1:]
		deci=float(n1)/float(n2)
		#print(str(n)+"yyyyy"+cuota)
		return str('%.2f'%deci)
		
					
	
def conectando(web):
	try:
		print('>>>set..')
		ur=urllib.request.urlopen(web,timeout=3)
		print('>>>set2..')
		return ur 
		#conector1=urllib.request.urlopen(url1,timeout=30)#timeoutde10segundos
	except:
		print('>>>Exceptcion')
		time.sleep(1)
		return conectando(web)

def conectandoRead(url,cone):
	try:
		print('>>>set')
		html=cone.read()
		print('>>>set2')
		return html
		#conector1=urllib.request.urlopen(url1,timeout=30)#timeoutde10segundos
	except:
		print('>>>Exceptcion2')
		print(url)
		time.sleep(1)
		t=conectando(url)
		return conectandoRead(url,t)

def leyendo(fich):
	try:
		#leedeunficherolaprimeralineaquetieneunacuota
		#Enprimerlugardebemosdeabrirelficheroquevamosaleer.
		#Usa'rb'envezde'r'sisetratadeunficherobinario.
		#print('>>>Lecturadeunalíneadelfichero\n')
		infile=open(fich,'r')
		#Mostramosporpantallaloqueleemosdesdeelfichero
		#print('>>>Lecturadeunalíneadelfichero\n')
		
		s=infile.readline()
		#print(s)
		#Cerramoselfichero.
		infile.close()
		return '0'

	except:
		print("noexiste")
		return'-1'

def guardando(fich,valor):
	try:
		outfile=open(fich,'w')#Indicamoselvalor'w'.
		outfile.write(valor)
		outfile.close()

	except:
		print("Excepcionguardando")

def guardando_a(fich,valor):
	try:
		print("guardando... "+fich)
		outfile=open(fich,'a')#Indicamoselvalor'w'.
		outfile.write(valor)
		outfile.close()

	except:
		print("Excepcionguardando")

def buscarForecast(s):
			print("buscarForecast Ini:"+s)
			texto= ' '+s[17:]+','
			listaCaballos = {}
			#print(texto[index+34:])		
			while (texto.find(','))>0:
						finTexto=texto.find(',')
						textoAux=texto[:finTexto]
						textoAux=textoAux.replace(",","")
						indicePar=textoAux.find(' ')
						#caballo=textoAux[:indicePar]
						indicePar=textoAux.find(',')
						clicks=textoAux[indicePar+1:]
						#print("x"+caballo+"x")
						indiceCab=clicks.rfind(' ')
						caballo=clicks[1:indiceCab]
						fore=clicks[indiceCab+1:]
						#print('x'+caballo+"x x" + fore+'x')
						texto=texto[finTexto+1:]
						#duo=[]
						#duo.append(caballo)
						#duo.append(clicks)
						#listaCaballos.append(duo)
						listaCaballos.update( {caballo : fore} )
						#clicks=
			print("buscarForecast Fin")
			return listaCaballos	
	
		
def buscarClicks(s):
			listaCaballos = {}
			_tr=s.findAll("script")
			#print(_tr)
			for _tr_ in _tr:
				#_tr=_tr_.findAll("script")
				texto=_tr_.text
				index=texto.find('"container": "my_chart", "data": ')
				if(index>0):
					#print(texto[index+34:])		
					while (texto.find('['))>0:
						finTexto=texto.find(']')
						textoAux=texto[texto.find('['):finTexto]
						textoAux=textoAux.replace("[","").replace('"',"")
						indicePar=textoAux.find('(')
						caballo=textoAux[:indicePar-1]
						indicePar=textoAux.find(',')
						clicks=textoAux[indicePar+1:]
						#print("x"+caballo+"x")
						#print(clicks)
						texto=texto[finTexto+1:]
						#duo=[]
						#duo.append(caballo)
						#duo.append(clicks)
						#listaCaballos.append(duo)
						listaCaballos.update( {caballo : clicks} )
						#clicks=
			print("buscarClicks Fin")
			return listaCaballos	


def tratar_cuota(_home,web,caballo,listaClicks,listaForecast,web2):
					#print(_home_)
					dd=0
					#['a','div']
					for _home_ in _home:
						#print("....xx7xx")
						#print("....xx55555xx"+web2)
						#print("unooo")
						#print("zzzzzzZ"+_home_)
						_home2=_home_.findAll("p") 
						#print("uno1")
						cuo='NA'
						try:
							#print("uno2")
							for _home2_ in _home2:
								cuo=calcular_cuota(_home2_.text.strip())
								#print("uno3"+cuo)
								
						except:
							print("error")
						guardando_a('_'+web2,cuo+';')
						#print("uno4")
						#print("zzzzzzZ"+_home2)
						#print("XXXX"+str(cuo))
						
						#print("uno5")
					#print("cuota Fin")
				#if (leyendo('_'+web3)=='-1'):
				#	print('Guardando forecast')
				#	guardando_a('_'+web3,time.strftime("%c",now)+';'+infoForecast+'\n')
				
			
#métododeanálisisdeunadirecciónweb
def analisisDescargaDetalle(web,i):

#web='http://www.oddschecker.com/horse-racing/2016-09-19-leicester/14:30/winner'
		#print("..................	intento------")
		#print(web)
		try:
			try:
				#conexion5=urllib.request.urlopen(web,timeout=10000)#timeoutde10segundos
				conexion5=conectando(web)
				#print("..................	")
			except:
							#print(e.code)
							try:
								print("Segundointento------")
								time.sleep(3)
								conexion5=urllib.request.urlopen(web,timeout=10000)#timeoutde10segundos
							except:
								print("Tercerintento------")
								time.sleep(10)
								conexion5=urllib.request.urlopen(web,timeout=10000)#timeoutde10segundos
			#print("AD"+str(i)+""+str(zz)+""+web)
			html=conexion5.read()
			web2=web.replace("http://www.oddschecker.com/horse-racing/","")
			web2=web2.replace(".html","")
			web2=web2.replace(dia+"-","")
			web2=web2.replace("/","_")
			web2=web2.replace(":","_")
			web3=dia+'_'+web2+'_info.csv'
			web2=dia+'_'+web2+'.csv'
	
			print(str(i)+"readD")
			soup2=BeautifulSoup(html)
			_tr=soup2.findAll("div",{"class":"race-extra-info"}) 
			for _tr_ in _tr:
				#print('eii'+_tr_.text)
				listaForecast=buscarForecast(_tr_.text)
				_tr=_tr

			listaClicks=buscarClicks(soup2)
			
			_tr=soup2.findAll("tr",{"class":"diff-row evTabRow bc"}) 
			
			for _tr_ in _tr:
				#print(_tr)
					caballo=_tr_['data-bname']
				#_home=_tr_.findAll("p") 
					#print("uno")
				#_home=_tr_.findAll("td",{"class":["bc bs o",""]})
				#_home=_tr_.findAll(["td",{"class":"bc bs o"},"td",{"class":"bc bs"}])
				#_home=_tr_.findAll("td",{"class":"bc bs o"})
					guardando_a('_'+web2,time.strftime("%c",now)+';'+caballo+';')
				#for x in range(0,len(casas)):
				#	t=casas[x]
				#	tt='"td",{"data-bk":"'+t+'"}'
					#tt="td",{"data-bk":"B3"}'
				#	print(tt)
					#_home=_tr_.findAll(str(tt))
					
				
					dd=1
					if (listaClicks.get(caballo)!=None):
								guardando_a('_'+web2,listaClicks.get(caballo)+';')
					else:
								guardando_a('_'+web2,'0'+';')
					#print("cuota Fin")
					if (listaForecast.get(caballo)!=None):
								guardando_a('_'+web2,listaForecast.get(caballo)+';')
					else:
								guardando_a('_'+web2,'NA'+';')
					#print("cuota Fin")
					guardando_a('_'+web2,';')
					#print("cuota Fin2")	

					z=1
					_home=_tr_.findAll("td",{"data-bk":"B3"})
					z=z+1
					#print(str(z))
					tratar_cuota(_home,web,caballo,listaClicks,listaForecast,web2)
					_home=_tr_.findAll("td",{"data-bk":"SK"})
					z=z+1
					#print(str(z))
					tratar_cuota(_home,web,caballo,listaClicks,listaForecast,web2)
					_home=_tr_.findAll("td",{"data-bk":"LD"})
					z=z+1
					#print(str(z))
					tratar_cuota(_home,web,caballo,listaClicks,listaForecast,web2)
					_home=_tr_.findAll("td",{"data-bk":"WH"})
					z=z+1
					#print(str(z))
					tratar_cuota(_home,web,caballo,listaClicks,listaForecast,web2)
					_home=_tr_.findAll("td",{"data-bk":"EE"})
					z=z+1
					#print(str(z))
					tratar_cuota(_home,web,caballo,listaClicks,listaForecast,web2)
					_home=_tr_.findAll("td",{"data-bk":"FB"})
					z=z+1
					#print(str(z))
					tratar_cuota(_home,web,caballo,listaClicks,listaForecast,web2)
					_home=_tr_.findAll("td",{"data-bk":"VC"})
					z=z+1
					#print(str(z))
					tratar_cuota(_home,web,caballo,listaClicks,listaForecast,web2)
					_home=_tr_.findAll("td",{"data-bk":"PP"})
					z=z+1
					#print(str(z))
					tratar_cuota(_home,web,caballo,listaClicks,listaForecast,web2)
					_home=_tr_.findAll("td",{"data-bk":"UN"})
					z=z+1
					#print(str(z))
					tratar_cuota(_home,web,caballo,listaClicks,listaForecast,web2)
					_home=_tr_.findAll("td",{"data-bk":"CE"})
					z=z+1
					#print(str(z))
					tratar_cuota(_home,web,caballo,listaClicks,listaForecast,web2)
					_home=_tr_.findAll("td",{"data-bk":"FR"})
					z=z+1
					#print(str(z))
					tratar_cuota(_home,web,caballo,listaClicks,listaForecast,web2)
					_home=_tr_.findAll("td",{"data-bk":"WA"})
					z=z+1
					#print(str(z))
					tratar_cuota(_home,web,caballo,listaClicks,listaForecast,web2)
					_home=_tr_.findAll("td",{"data-bk":"SA"})
					z=z+1
					#print(str(z))
					tratar_cuota(_home,web,caballo,listaClicks,listaForecast,web2)
					_home=_tr_.findAll("td",{"data-bk":"BY"})
					z=z+1
					#print(str(z))
					tratar_cuota(_home,web,caballo,listaClicks,listaForecast,web2)	
					_home=_tr_.findAll("td",{"data-bk":"VT"})
					z=z+1
					#print(str(z))
					tratar_cuota(_home,web,caballo,listaClicks,listaForecast,web2)
					_home=_tr_.findAll("td",{"data-bk":"OE"})
					z=z+1
					#print(str(z))
					tratar_cuota(_home,web,caballo,listaClicks,listaForecast,web2)
					_home=_tr_.findAll("td",{"data-bk":"SE"})
					z=200
					#print(str(z))
					tratar_cuota(_home,web,caballo,listaClicks,listaForecast,web2)
					_home=_tr_.findAll("td",{"data-bk":"GN"})
					z=z+1
					#print(str(z))
					tratar_cuota(_home,web,caballo,listaClicks,listaForecast,web2)
					_home=_tr_.findAll("td",{"data-bk":"PE"})
					z=z+1
					#print(str(z))
					tratar_cuota(_home,web,caballo,listaClicks,listaForecast,web2)
					_home=_tr_.findAll("td",{"data-bk":"SX"})
					z=z+1
					#print(str(z))
					tratar_cuota(_home,web,caballo,listaClicks,listaForecast,web2)
					_home=_tr_.findAll("td",{"data-bk":"BF"})
					z=z+1
					#print(str(z))
					tratar_cuota(_home,web,caballo,listaClicks,listaForecast,web2)
					_home=_tr_.findAll("td",{"data-bk":"BD"})
					z=z+1
					#print(str(z))
					tratar_cuota(_home,web,caballo,listaClicks,listaForecast,web2)
					_home=_tr_.findAll("td",{"data-bk":"MK"})
					z=z+1
					#print(str(z))
					tratar_cuota(_home,web,caballo,listaClicks,listaForecast,web2)						
					guardando_a('_'+web2,'\n')
					
			
			print("finalizando Carrera")
			#time.sleep(10)
			#time.sleep(50)
			#conexion6=urllib.request.urlopen(web,timeout=30)
			#seevitarecursividad
			#analisisDescargaDetalle(web,dato,i,zz)
		except:
			print(str(i)+"exceptcion.Esperamos5minutos...")
			time.sleep(100)
			print("Reintentando")
			analisisDescargaDetalle(web,i)

def analisisDescarga(conexion,web,dato,i):
		html=conexion.read()
		soup=BeautifulSoup(html)
		#obtenemosunalistadeStringconlacondicióndeatributosclassconvaloresdetailsyprice
		_tr=soup.findAll("tr",{"itemtype":"http://schema.org/SportsEvent"})
		#print(len(_tr))
		zz=0
		dd=0
		for _tr_ in _tr:
			#print("....")
			_home=_tr_.findAll("a")
			
			for _home_elemento in _home:
					url2='http://uk.wettportal.com'+_home_elemento['href']
					zz=zz+1
					print("IMPORTANTE"+str(i)+""+str(zz)+""+url2)
					print("------")
					print("------")
					print("------")
					print("lanzandothread")
					#nossaltamoslosparesporquevienerepetido
					if(dd==0):
						_thread.start_new_thread(analisisDescargaDetalle,('http://uk.wettportal.com'+_home_elemento['href'],0,i,zz))
						dd=1
					else:
						#thread.start_new_thread(analisisDescargaDetalle,('http://uk.wettportal.com'+_home_elemento['href'],0,i,zz))FM
						dd=dd
						#dd=0
					print("lanzadothread")
					#analisisDescargaDetalle(conexion3,'http://uk.wettportal.com'+_home_elemento['href'],0,i)
			
	
			
#estemétodoseconectaráconlawebyestableceuntimeoutqueobligaareintentarelfallo
def preparar(web,x):
	try:
		print("PPPPPPPPPPPPPPPPP"+web)
		conector=urllib.request.urlopen(web,timeout=30)#timeoutde10segundos
		#print("P2")
		analisisDescarga(conector,web,0,x)
	except:
		time.sleep(30)
		print("Tiempodeesperaagotado,volviendoaintentar")
		preparar(web,x)

def buscar_id(url3)	:	
	finTexto=url3.find(".htm")
	textoAux=url3[:finTexto]
	print(textoAux)
	inicioTexto=textoAux.rfind("i")
	textoo=textoAux[inicioTexto:]
	print(textoo)
	return textoo

		
#Programaprincipal
now=time.localtime(time.time())
print('Comienza elprograma'+time.strftime("%c",now))
time.sleep(1)
limit=sys.argv[1]
print(limit)
limit2=sys.argv[2]
print(limit2)
fecha_inicio=sys.argv[3]
fichero='datos'+str(fecha_inicio)+'.csv'
fichero=fichero.replace('/','_')
time.sleep(1)
url1='http://uk.wettportal.com/Tennis/ITF_Men/'
url1='http://www.oddschecker.com/horse-racing/'
url1='http://www.idealista.com/venta-viviendas/barcelona-barcelona/pagina-2.htm'
url1='https://www.fotocasa.es/es/comprar/viviendas/barcelona-capital/todas-las-zonas/l?latitude=41.3854&longitude=2.1775&combinedLocationIds=724,9,8,232,376,8019,0,0,0'
url1='https://www.habitaclia.com/viviendas-barcelona.htm'
url1='https://www.habitaclia.com/viviendas-barcelona-'
url2='.htm'
z=1
z=int(limit)
#while z<1000:
while z<int(limit2):
	try:
		#url11=url1+str(z)+url2+'?filtro_periodo=3&ordenar=mas_antiguos'
		url11=url1+str(z)+url2+'?ordenar=mas_antiguos'
		print(url11)
		print('--------------------------------------------------------')
		#time.sleep(1)
		z=z+1
		#conector1=urllib.request.urlopen(url11,timeout=50)#timeoutde10segundos
		conector1=conectando(url11)
		#html=conector1.read()
		html=conectandoRead(url11,conector1)
		soup=BeautifulSoup(html)
		#print("Log...."+html.decode('utf-8'))
		#divprincipal
		_1_div=soup.findAll("h3",{"class":"list-item-title"})
		#_1_div=soup.findAll("a",{"data-time":"2016-09-21"})
		#_1_div=soup.findAll("a",{"data-time":"2016-09-21"})
		xx=0
		#print("Log....1")
		for a_elemento in _1_div:
					try:
							print("Log....1")
							#print(a_elemento)
							_2_div=a_elemento.findAll("a")
							for a_elemento2 in _2_div:
								url3=a_elemento2.get('href')
								print(url3)
								#cone=urllib.request.urlopen(url3,timeout=500)#timeoutde10segundos
								cone=conectando(url3)
								print("Log....1111")
								try:
									#html=cone.read()
									html=conectandoRead(url3,cone)
								except:
									print("repitiendo.....")
									time.sleep(5)
									try:
										html=conectandoRead(url3,cone)
									except:
										print("repitiendo.....")
										guardando_a('errores2.txt',url3+'\n')
										#time.sleep(5)
										#html=cone.read()
								print("Log....12")
								soup2=BeautifulSoup(html)
								print("Log....13")
								#guardando_a('kk.txt',url3+'\n')
								print("Log....3")
								div10=soup2.findAll("article",{"class":"has-aside"})
								#fecha modificaion...
								for element in div10:
									#print(element)
									div2=element.findAll("p",{"class":"time-tag"})
									for el in div2:
										##print(el)
										el=el
										div3=el.findAll("time")
										for l in div3:
											fec=l.text
											#print("#"+li.text.replace('\n', '').replace('\r', '')+"#")
								fecha_inicio_formateada=datetime.strptime(fecha_inicio,'%d/%m/%Y')
								fecha_formateada=datetime.strptime(fec,'%d/%m/%Y')
								print(str(fecha_formateada))
								saltar= (str(fecha_inicio_formateada)>str(fecha_formateada))
								if (not saltar):	
								
									t_url=buscar_id(url3)
									t_url=t_url+';'
									div_=soup2.findAll("div",{"class":"price"})
									for _element in div_:
											x=_element.findAll("span",{"class":"font-2"})
											#print(x)
											for li__ in x:
												#print(li__.text)
												precio=li__.text+';'
												
									rebaja="0€"
									num_rebajas=0
									datos_rebajas=";;;;;;;;;;"
									for _element in div_:
											x=_element.findAll("strong")
											#print(x)
											for li__ in x:
												#print(li__.text)
												rebaja=li__.text
												num_rebajas=num_rebajas+1
												datos_rebajas=rebaja+";X;;;;;;;;;"
									rebaja=rebaja+';'
									num_rebajas_string=str(num_rebajas)+';'
									
									
									
									div_=soup2.findAll("article",{"class":"location"})
									loc="Sin barrio"
									for _element in div_:
											x=_element.findAll("a",{"id":"js-ver-mapa-zona"})
											#print(x)
											for li__ in x:
												#print(li__.text)
												loc=li__.text.replace('\n', '').replace('\r', '').lstrip().rstrip()
									
											
									if not 'Sin barrio' in loc:
										fec2=str(datetime.now().day)+'/'+ str(datetime.now().month)+ '/'+str(datetime.now().year)
										guardando_a(fichero,fec+';'+fec2+';0;'+num_rebajas_string+t_url+precio+rebaja+loc+';')
									
									
									div_=soup2.findAll("article",{"id":"js-feature-container"})
									print("Log....2")
									for _element in div_:
										#div2_=_element.findAll("h4",{"class":"hidden"})
										#print(div2_)
										#for el_ in div2_:
											#print(_element)
											x=_element.findAll("ul",{"class":"feature-container"})
											#print(x)
											for li__ in x:
												#print(li__)
												dd_=li__.findAll('li')
												for li_ in dd_:
													#Quitamos la indicacion de tambien alquiler
													if not 'alquiler' in li_.text:
														t_=li_.text.replace('\n', '').replace('\r', '').lstrip().rstrip()
														if not "Sin barrio" in loc:
															guardando_a(fichero,t_+';')
									
												
									
									
									
									
									for element in div10:
										#print(element)
										div2=element.findAll("h3",{"class":"f-left"})
										for el in div2:
											##print(el)
											el=el
										dd=element.findAll('li')
										for li in dd:
											if not 'Certificado' in li.text:
												t="#"+li.text.replace('\n', '').replace('\r', '').lstrip().rstrip()+"#"
												if not "Sin barrio" in loc:
													guardando_a(fichero,t)
												#print("#"+li.text.replace('\n', '').replace('\r', '')+"#")

									#guardando_a(fichero,'\n')		
									if not "Sin barrio" in loc:
										guardando_a(fichero,';'+url3+';'+datos_rebajas+'\n')
									#guardando_a('fichero','__________________________'+'\n')		
									print("Log....4")		
									#time.sleep(1)
								#time.sleep(2)
										#preparar(url2,xx)
					except Exception as e:
						print("error..."+str(e))

	except Exception as e:
		print("erro..."+str(e))
		guardando_a('errores1.txt',url11+'\n')
print("Acabado")
#time.sleep(9000)
