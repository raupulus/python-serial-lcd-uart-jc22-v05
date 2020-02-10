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

## Importo la pantalla
from LCDUart import LCDUart

#######################################
# #             Variables           # #
#######################################
sleep = time.sleep
lcd = LCDUart()

#######################################
# #             Funciones           # #
#######################################

# https://www.amazon.es/M%C3%B3dulo-Pantalla-Pulgadas-%C3%A1ngulo-Colorida/dp/B0832FP3FQ
# https://articulo.mercadolibre.com.mx/MLM-709874849-22-pulgadas-uart-lcd-tft-modulo-de-pantalla-con-pl2303-puer-_JM







#ser.write(b'BPS(115200)') 
#ser.write(b'VIEW;') 
#ser.write(b'VER') 
#ser.write(b'BL(0);') 
#ser.write(b'CLR(12);') 

#ser.write(b'SBC(1);') 


#ser.write(b'DCV32(0,0 ,spotpear,0);') 



lcd.write(b"RESET;\r\n") 
time.sleep(1)
lcd.write(b"BPS(115200);\r\n") 
time.sleep(1)
lcd.write(b"CLR(0);\r\n") 
time.sleep(1)
lcd.write(b'DCV32(0,0 ,spotpear,0);') 
time.sleep(1)
lcd.showImage('images/debian.png')
lcd.stop()


"""
printf("serial test start ...\n");
        delay(800);
        serialPrintf(fd,"RESET;\r\n");//reset the LCD
        delay(100);
        serialPrintf(fd,"BPS(115200);\r\n");//Set Baud rate
        delay(100);
        serialPrintf(fd,"CLR(0);\r\n");//Clean LCD with black color
        delay(100);
        serialPrintf(fd,"CLR(1);\r\n");//Clean LCD with red color
        delay(100);
        serialPrintf(fd,"CLR(15);\r\n");//Clean LCD with white color
        delay(100);
        serialPrintf(fd,"DIR(0);\r\n");//Vertical display 
        delay(100);
        serialPrintf(fd,"DCV24(0,0,spotpear,0);\r\n");
//display "spotpear" at coordinate（0.0），Font color ：0-black；background color ：default black
        delay(100);
        serialPrintf(fd,"SBC(1);\r\n");//set  background color red
        delay(100);
        serialPrintf(fd,"DCV24(0,24,spotpear,0);\r\n");
//display "spotpear" at coordinate（X-0.Y-24）
        delay(500);
        serialPrintf(fd,"DCV24(0,24,spotpear,3);\r\n");//，Font color ：3-;
        delay(500);
        serialPrintf(fd,"CLR(0);\r\n");//Clean LCD with black color
        delay(500);
        serialPrintf(fd,"DIR(1);\r\n");//Horizontal display
        delay(500);
        serialPrintf(fd,"DCV16(0,24,spotpear,0);\r\n");
        delay(500);
        serialPrintf(fd,"DCV32(0,0,spotpear,0);\r\n");
        delay(500);
        serialPrintf(fd,"CIRF(40,80,20,3);\r\n");//filling circle coordinate（X-40.Y-80,r-20,color-3）
        delay(100);
        serialPrintf(fd,"CIR(70,150,20,1);\r\n");//circle coordinate（X-70.Y-150,r-20,color-1）
        delay(500);
        serialPrintf(fd,"BOXF(70,150,90,170,3);\r\n");//rectangle  coordinate
        delay(500);
        serialPrintf(fd,"BOX(40,80,70,110,3);\r\n");//rectangle  coordinate
        delay(500);
        serialPrintf(fd,"PL(0,0,220,176,6);\r\n");//line: color-6,
        delay(500);
        serialPrintf(fd,"PS(110,110,4);\r\n");//line: color-6,
        delay(1000);
        serialPrintf(fd,"DIR(0);\r\n");//Vertical display
        delay(100);
        serialPrintf(fd,"FSIMG(2097152,0,0,176,220,0);\r\n");
//load picture-1 from LCD（picture loaded by computer UART software in advance）
        delay(500);
        serialPrintf(fd,"FSIMG(2174592,0,0,176,220,0);\r\n");//load picture-2 from LCD
        delay(500);
        serialPrintf(fd,"FSIMG(2252032,0,0,176,220,0);\r\n");
        delay(500);
        serialPrintf(fd,"BL(1023);\r\n");////Backlight ightness:1024-open display
        delay(1000);
        serialPrintf(fd,"BL(0);\r\n");//Backlight ightness:0-stop display
        delay(300);
//        serialPrintf(fd,"RESET;\r\n");//reset*/
//        delay(300);
        serialPrintf(fd,"DCV24(0,0,spotpear,0);\r\n");
        delay(300);

"""






