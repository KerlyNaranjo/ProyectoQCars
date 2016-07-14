import pygame
import sys
from pygame.locals import*

#Constante para la pantalla.
width=900
height=500
#Constante para el movimiento
x=100
y=304
x1=700
y1=304

#Declarando la posicion del Sprite
xixf={}
Rxixf={}

contador=6
direccion=True
i=0

#========== IMAGEN ========

def cargar_imagen(filename, transparent=False):
	try: image = pygame.image.load(filename)
	except pygame.error. message:
		raise SystemExit. message
	image = image.convert()
	if transparent:
		color = image.get_at((0,0))
		image.set_colorkey(color, RLEACCEL)
	return image

#==================================================
#Iiniciamos PyGame
pygame.init()
#Dimensiones y etiquetas de la pantalla
pantalla=pygame.display.set_mode((width,height))
pygame.display.set_caption("QUITS CARS")
#==================================================

carro=cargar_imagen("imagenes/carro.png",True)
#cargando carro enemigo
enemigo=cargar_imagen("imagenes/enemigo.png",True)
#cargando imagen de fondo
carretera=cargar_imagen("imagenes/camino.png",True)
#carro_inv=pygame.transform.flip(carro,True,False)
reloj=pygame.time.Clock()
pantalla.blit(carro,(100,304))
#posicion del enemigo
pantalla.blit(enemigo,(x1,y1))
#posicion del carretero
pantalla.blit(carretera,(90,250))
pygame.display.flip()

while True:
	for eventos in pygame.event.get(): #Controla los eventos de la pantalla
		if eventos.type== QUIT:
			sys.exit(0)
	x1-=5
	x+=5

    #Ubicacion del srite en la imagen
	xixf[0]=(0,0,33,50)
	xixf[1]=(35,0,73,50)
	xixf[2]=(75,0,115,50)
	xixf[3]=(117,0,168,50)
	xixf[4]=(172,0,215,50)
	xixf[5]=(217,0,265,50)
	xixf[6]=(267,0,365,50)

	Rxixf[6]=(0,0,33,50)
	Rxixf[5]=(35,0,73,50)
	Rxixf[4]=(75,0,115,50)
	Rxixf[3]=(117,0,168,50)
	Rxixf[2]=(172,0,215,50)
	Rxixf[1]=(217,0,265,50)
	Rxixf[0]=(267,0,365,50)

	p=7

	if contador==p:
		i=0
	if contador==p*2:
		i=1
	if contador==p*3:
		i=2
	if contador==p*4:
		i=3
	if contador==p*5:
		i=4
	if contador==p*6:
		i=5
	if contador==p*7:
		i=6
    #Controlando los movimeintos del carro
	teclado=pygame.key.get_pressed()
	if teclado [K_w]:
		y-=5
	if teclado [K_s]:
		y+=5
		

	reloj.tick(25)
	pantalla.fill((0,0,0))
	#if direccion==True:
		#pantalla.blit(carro(x,y),(xixf[i]))
	#if direccion==False:
		#pantalla.blit(carro_inv(x,y),(Rxixf[i]))
	pantalla.blit(carretera,(50,250))
	pantalla.blit(carro,(x,y))
	pantalla.blit(enemigo,(x1,y1))
	pygame.display.flip()

      