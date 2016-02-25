#!/usr/bin/env python
# coding=utf-8

import sys
import math

#Importamos pygame
import pygame
from pygame.locals import *
#
#tablero 8x8

#constantes
#tablero_ruta = "img/tablero-ajedrez.png"
ancho = 600
alto = 600
negro = (128, 70, 50)
blanco = (176, 104, 56)
tam_ficha = [75, 75]
lims = [0, tam_ficha[0]*8]
#

#función principal

class Chess:
    def __init__(self):
        self.piezas_blancas = [[1, "peon", 0, 75, "img/peonb.png"], 
                               [2, "peon", 75, 75, "img/peonb.png"],
                               [3, "peon", 150, 75, "img/peonb.png"],
                               [4, "peon", 225, 75, "img/peonb.png"],
                               [5, "peon", 300, 75, "img/peonb.png"],
                               [6, "peon", 375, 75, "img/peonb.png"],
                               [7, "peon", 450, 75, "img/peonb.png"],
                               [8, "peon", 525, 75, "img/peonb.png"],
                               [1, "torre", 0, 0, "img/torreb.png"],
                               [1, "caballo", 75, 0, "img/caballob.png"],
                               [1, "alfil", 150, 0, "img/alfilb.png"],
                               [1, "reina", 225, 0, "img/reinab.png"],
                               [1, "rey", 300, 0, "img/reyb.png"],
                               [2, "alfil", 375, 0, "img/alfilb.png"],
                               [2, "caballo", 450, 0, "img/caballob.png"],
                               [2, "torre", 525, 0, "img/torreb.png"]
                              ]
        self.piezas_negras = [[1, "peon", 0, 450, "img/peonn.png"], 
                               [2, "peon", 75, 450, "img/peonn.png"],
                               [3, "peon", 150, 450, "img/peonn.png"],
                               [4, "peon", 225, 450, "img/peonn.png"],
                               [5, "peon", 300, 450, "img/peonn.png"],
                               [6, "peon", 375, 450, "img/peonn.png"],
                               [7, "peon", 450, 450, "img/peonn.png"],
                               [8, "peon", 525, 450, "img/peonn.png"],
                               [1, "torre", 0, 525, "img/torren.png"],
                               [1, "caballo", 75, 525, "img/caballon.png"],
                               [1, "alfil", 150, 525, "img/alfiln.png"],
                               [1, "reina", 225, 525, "img/reinan.png"],
                               [1, "rey", 300, 525, "img/reyn.png"],
                               [2, "alfil", 375, 525, "img/alfiln.png"],
                               [2, "caballo", 450, 525, "img/caballon.png"],
                               [2, "torre", 525, 525, "img/torren.png"]]
        self.piezas_blancas_comidas = [] #comidas por las negras :)
        self.piezas_negras_comidas = []
        pygame.init() #iniciamos pygame
    
        self.pantalla = pygame.display.set_mode((ancho, alto)) #creamos la ventana con propiedades
        
        self.cursor_x = 0
        self.cursor_y = 0
        self.lista_cuadros = []
        self.pieza_seleccionada = None
        self.pieza_seleccionada_pasada = None
        self.cuadrado = False
        self.turno = "negras"
        
        self.reloj_blancas = None
        self.reloj_negras = None
        
        
        self.actualizar()
        
        #actualizar para ver cambios
        pygame.display.flip()
        
        #bucle principal
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.cuadrado = True
                    self.cursor_x = 0
                    self.cursor_y = 0

                    self.actualizar()
                    pygame.display.flip()
                    #print "You pressed the left mouse button at (%d, %d)" % event.pos

                    for x, y in self.lista_cuadros:
                        if x <= event.pos[0] and x + 75 >= event.pos[0] and y <= event.pos[1] and y+75 >= event.pos[1]:
                            #print self.pieza_en_bloque([x, y])
                            print x, y
                            

                            
                            for piezab in self.piezas_blancas:
                                if piezab[2] == x and piezab[3] == y:
                                    #print "%d %s blanco/a" % (piezab[0], piezab[1])
                                    self.pieza_seleccionada = piezab
                            
                            for piezan in self.piezas_negras:
                                if piezan[2] == x and piezan[3] == y:
                                    #self.obtener_obstaculos(piezan, 2)
                                    #print "%d %s negroo/a" % (piezan[0], piezan[1])
                                    self.pieza_seleccionada = piezan
                            
                            if self.pieza_seleccionada is not None and self.obtener_color_pieza(self.pieza_seleccionada) == self.turno:

                                if self.obtener_color_pieza(self.pieza_en_bloque([x, y])) == self.obtener_color_inverso(self.turno):
                                    print "L118: %s" % self.pieza_en_bloque([x, y])
                                    self.comer_pieza(self.pieza_en_bloque([x, y]))
                                    mp = self.mover_pieza(self.pieza_seleccionada, [x, y])
                                    self.actualizar()
                                    self.pieza_seleccionada = None
                                    self.cambiar_turno()
                                    self.cuadrado = False

                                else:
                                    mp = self.mover_pieza(self.pieza_seleccionada, [x, y])
                                    if mp[0]:
                                        self.actualizar()
                                        self.pieza_seleccionada = None
                                        self.cambiar_turno()
                                        self.cuadrado = False
                            
                            if self.cuadrado:
                                self.actualizar()
                                cuadrado = pygame.Surface((tam_ficha[0], tam_ficha[1]), pygame.SRCALPHA)
                                cuadrado.fill((0,0,255, 50))
                                self.pantalla.blit(cuadrado, (x, y))
                                pygame.display.flip()
                            
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    pass
                    #print "You released the left mouse button at (%d, %d)" % event.pos

    def dibujar_tablero(self):
        
        color_actual = negro
        while self.cursor_x != 600:
            for i in range(0, 8):
                pygame.draw.rect(self.pantalla, color_actual, (self.cursor_x, self.cursor_y,tam_ficha[0],tam_ficha[1]))
                
                self.lista_cuadros.append((self.cursor_x, self.cursor_y))
                
                pygame.display.flip()
                
                if color_actual == blanco:
                    color_actual = negro
                else:
                    color_actual = blanco
                
                self.cursor_y += 75

            if color_actual == blanco:
                color_actual = negro
            else:
                color_actual = blanco

            self.cursor_y = 0
            self.cursor_x += 75

    def dibujar_piezas(self):
        for pieza in self.piezas_blancas:
            piezaDib = pygame.image.load(pieza[4]).convert_alpha()
            piezaDib = pygame.transform.scale(piezaDib, (75, 75))
            self.pantalla.blit(piezaDib, (pieza[2], pieza[3]))

        for pieza in self.piezas_negras:
            piezaDib = pygame.image.load(pieza[4]).convert_alpha()
            piezaDib = pygame.transform.scale(piezaDib, (75, 75))
            self.pantalla.blit(piezaDib, (pieza[2], pieza[3]))
    
    def actualizar(self):
        self.dibujar_tablero()
        pygame.display.flip()
        self.dibujar_piezas()
        pygame.display.flip()
#num, tipo, x, y, imgsrc
    
    def mover_pieza(self, pieza, nuevaPos):
        movido = False
        comido = False
        if self.obtener_color_pieza(pieza) == "negras":
            if pieza[1] == "peon" and not self.pieza_en_bloque([nuevaPos[0], nuevaPos[1]]):
                if pieza[3] == 450 and pieza[3] - nuevaPos[1] <= tam_ficha[0]*2 and pieza[2] == nuevaPos[0]:
                    #print pieza[3] - nuevaPos[1]
                    pieza[2] = nuevaPos[0]
                    pieza[3] = nuevaPos[1]
                    movido = True

                elif pieza[3] - nuevaPos[1] == tam_ficha[0] and pieza[2] == nuevaPos[0]:
                    print "ultim"
                    #print 2
                    pieza[2] = nuevaPos[0]
                    pieza[3] = nuevaPos[1]
                    movido = True

            elif pieza[1] == "torre" and not self.pieza_en_bloque([nuevaPos[0], nuevaPos[1]]):
                #adelante
                distancia = abs(self.pixeles_a_distancia(abs(nuevaPos[1] - pieza[3])))
                print "distancia %d" % distancia
                print "obs: %s" % self.obtener_obstaculos(pieza, distancia, "adelante")
                if nuevaPos[1] - pieza[3] <= 0 and len(self.obtener_obstaculos(pieza, distancia, "adelante")) == 0:
                #   pass
                    pieza[2] = nuevaPos[0]
                    pieza[3] = nuevaPos[1]
                    movido = True
                    
        elif self.obtener_color_pieza(pieza) == "blancas":
            if pieza[1] == "peon" and not self.pieza_en_bloque([nuevaPos[0], nuevaPos[1]]):
                if pieza[3] == 75 and pieza[3] - nuevaPos[1] <= tam_ficha[0]*2 and pieza[2] == nuevaPos[0]:
                    #print pieza[3] - nuevaPos[1]
                    pieza[2] = nuevaPos[0]
                    pieza[3] = nuevaPos[1]
                    movido = True
                elif pieza[3] - nuevaPos[1] == tam_ficha[0] and pieza[2] == nuevaPos[0]:
                    #print 2
                    pieza[2] = nuevaPos[0]
                    pieza[3] = nuevaPos[1]
                    movido = True
            
            elif pieza[1] == "torre" and not self.pieza_en_bloque([nuevaPos[0], nuevaPos[1]]):
                #adelante
                distancia = abs(self.pixeles_a_distancia(abs(nuevaPos[1] - pieza[3])))
                print nuevaPos[1] - pieza[3]
                print distancia
                print self.obtener_obstaculos(pieza, distancia, "adelante")
                if pieza[3] - nuevaPos[1] <= 0 and len(self.obtener_obstaculos(pieza, distancia, "adelante")) == 0:
                    pieza[2] = nuevaPos[0]
                    pieza[3] = nuevaPos[1]
                    movido = True



        self.actualizar()
        return [movido, comido]
#num, tipo, x, y, imgsrc
    def comer_pieza(self, pieza):
        #self.obtener_color_pieza(pieza)
        #comida = self.pieza_en_bloque([nuevaPos[0], nuevaPos[1]])
        #self.piezas_blancas_comidas.append(comida)
        #self.piezas_blancas.remove(comida)
        if self.obtener_color_pieza(pieza) == "blancas":
            self.piezas_blancas_comidas.append(pieza)
            self.piezas_blancas.remove(pieza)
        else:
            self.piezas_negras_comidas.append(pieza)
            self.piezas_negras.remove(pieza)

    
    def pieza_en_bloque(self, pos):
        toreturn = None
        for piezab in self.piezas_blancas:
            for piezan in self.piezas_negras:
                if piezab[2] == pos[0] and piezab[3] == pos[1]:
                    toreturn = piezab
                elif piezan[2] == pos[0] and piezan[3] == pos[1]:
                    toreturn = piezan
        return toreturn

    def obtener_obstaculos(self, pieza, distancia, direccion):
        posiciones = []
        fichas = []
        self.cursor_x = pieza[2]
        self.cursor_y = pieza[3]
        
        if direccion == "adelante":
            for i in range(0, distancia):
                posiciones.append([self.cursor_x, self.cursor_y - 75])
                self.cursor_y -= 75
        elif direccion == "atras":
            for i in range(0, distancia):
                posiciones.append([self.cursor_x, self.cursor_y + 75])
                self.cursor_y += 75
        elif direccion == "izquierda":
            for i in range(0, distancia):
                posiciones.append([self.cursor_x - 75, self.cursor_y])
                self.cursor_x -= 75
        elif direccion == "derecha":
            for i in range(0, distancia):
                posiciones.append([self.cursor_x + 75, self.cursor_y ])
                self.cursor_x += 75
        
        for bloque in posiciones:
            if self.pieza_en_bloque(bloque) is not None:
                fichas.append(self.pieza_en_bloque(bloque))

        return fichas

    def obtener_posibilidades(self, pieza):
        pass
    
    def obtener_color_pieza(self, pieza):
        if pieza in self.piezas_blancas:
            return "blancas"
        else:
            return "negras"
    
    def cambiar_turno(self):
        if self.turno == "blancas":
            self.turno = "negras"
        else:
            self.turno = "blancas"

    def pixeles_a_distancia(self, pixeles):
        return pixeles / 75

    def obtener_color_inverso(self, color):
        if color == "blancas":
            return "negras"
        else:
            return "blancas"
        
if __name__ == "__main__":
    Chess()
