#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# @author     Raúl Caro Pastorino
# @copyright  Copyright © 2018 Raúl Caro Pastorino
# @license    https://wwww.gnu.org/licenses/gpl.txt
# @email      tecnico@fryntiz.es
# @web        www.fryntiz.es
# @github     https://github.com/fryntiz
# @gitlab     https://gitlab.com/fryntiz
# @twitter    https://twitter.com/fryntiz

# Guía de estilos aplicada: PEP8

#######################################
# #           Descripción           # #
#######################################

#######################################
# #       Importar Librerías        # #
#######################################
import time  # Importamos la libreria time --> time.sleep
import os  # Importamos la libreria para comandos de la consola/shell
import random  # Genera números aleatorios --> random.randrange(1,100)
# import nombre_libreria as nuevo_nombre_libreria
import serial
import base64

#######################################
# #             Variables           # #
#######################################
sleep = time.sleep

#######################################
# #             Funciones           # #
#######################################

class LCDUart:
    orientation = 'vertical'
    width = 128
    height = 64

    # Variable que almacena la conexión UART con la pantalla
    ser = None

    # Variables para los colores.
    colors = {
        'black': 0,
        'red': 1,
        'green': 2,
        'blue': 3,
        'yellow': 4,
        'lightblue': 5,
        'purple': 6,
        'gray': 7,
        'lightgray': 8,
        'brown': 9,
        'darkgreen': 10,
        'navyblue': 11,
        'darkyello': 12,
        'orange': 13,
        'lightred': 14,
        'white': 15
    }


    def __init__(self, port='/dev/ttyUSB0', baudrate=115200, timeout=1, orientation='vertical'):
        ## Abre el puerto
        self.ser = serial.Serial(port, baudrate, timeout=timeout)

        print('Serial Open? → ' + str(self.ser.is_open))

        self.ser.write(b"RESET;\r\n") 

        time.sleep(0.1)
        self.ser.write(b"BPS(115200);\r\n") 

        time.sleep(0.1)
        self.setOrientation = orientation


        print('color: ' + str(self.colors.get('yellow')))


    def stop(self):
        """
        Detiene la comunicación con la pantalla
        """
        self.ser.close()

    def write(self, command):
        """
        Envía un comando en bruto a la pantalla
        """
        self.ser.write(bytes(command)) 
        time.sleep(0.1)

    def getScreenSize(self):
        """
        Devuelve el tamaño de la pantalla
        """
        return {
            'width': self.width,
            'height': self.height
        }


    def getScreenOrientation(self):
        """
        Devuelve la orientación actual de la pantalla
        """
        return self.orientation


    def setScreenOrientation(self, orientation):
        """
        Establece un nuevo modo para la orientación de la pantalla
        """
        if (orientation == 'vertical') or (orientation == 'horizontal'):
            self.orientation = orientation    
            return true

        return false    

    def showImage(self, path):
        """
        Muestra por la pantalla la imagen recibida por su ruta conviertiéndola primero
        a binario.
        """
        output = base64.b64encode(path)
        bin = "".join(format(ord(x), "b") for x in base64.decodestring(output))

        lcd.write(bytes("FSIMG(" + bin + ",0,0,176,220,0);\r\n"))
        time.sleep(0.1)

        
