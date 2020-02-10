# serial-lcd-uart-jc22-v05

Librería para interactuar con la pantalla tft de 2,2 pulgadas JC22-v05 que trabaja únicamente comunicándose por Serial

## Descripción

Al encontrarme con poca información o errónea me dedico a preparar esta librería con los usos que le voy dando a esta pantalla.

![Imagen de la pantalla TFT UART JC22-v05](images/doc/img1.jpg)

## Modo de uso de la librería

El archivo **main.py** puede ser utilizado a modo de ejemplo para la librería.

La clase principal se encuentra en el archivo **LCDUart.py** y es la única necesaria
para llevar a cabo un proyecto.

Bastará con importar y utilizar sus métodos, en el interior de la clase dejo descrito
cada método con su funcionalidad.

## Colores

![Imagen de la pantalla TFT UART JC22-v05](images/doc/img2.jpg)

|     Color   |      Nº      |
|  :-------:  |  :--------:  |
|  0          |  black       |
|  1          |  red         |
|  2          |  green       |
|  3     |  blue          |
|  4     |  yellow          |
|  5     |  cyan-blue          |
|  6     |  purple          |
|  7     |  gray          |
|  8     |  Light gray          |
|  9     |  brown          |
|  10     |  Dark green          |
|  11     |  Navy blue          |
|  12     |  Dark yellow          |
|  13     |  Orange          |
|  14     |  Light red          |
|  15     |  white          |


## Comandos Probados

![Imagen de la pantalla TFT UART JC22-v05](images/doc/img3.jpg)


## Comandos por probar, información de internet



### Reset

RESET;


This command allows the module to enter the software reset, receive this command, the module's peripheral components and system parameters will be restored to the power value.

### Get the version information instructions for the module
VER;


Through the VER; you can get the firmware version of this module information, and displayed on the screen

Set the baud rate command
BPS(bps);
The default baud rate is 115200 when the system is powered on.



Clear command
CLR(c);
Note that the range of c is 0 to 15, and if the value of c exceeds 15, the system will not respond to the CMD, and the range of c values will look at the following color list.

CLR for the script, c for the clear use of the background color, the specific code see the following color list. If you want to fill the screen with black, then CLR (0);

LCD control CMD
LCDON（on_off）;
On_off parameters only 0 or 1, the system ignores other parameters.

LCDON for the script, on_off, respectively, that start or turn off the LCD. Such as LCDON (1); that start LCD, LCDON (0); turn off the LCD.

Display the LCD
FSIMG(addr,x，y，w,h,mode);
When Mode is 1, the white background of the picture will not be displayed. This mode is used to overlay the icon and the background image. Addr is the flash start address for storing pictures, starting at 2097152

FSIMG for the script, addr for the picture stored in the flash address, x, y for the picture to be displayed on the screen above the starting position, w for the picture width, h for the picture height, mode for the picture display: 1 for the transparent display , 0 is normal display. Such as FSIMG (2097152,0,0,240,400,1); that from the 2097152 FLASH address removed 240 * 400 pictures and 0,0 position transparent display.

Image download to FLASH command
FS_DLOAD(SIZE);
Picture will be downloaded to the FLASH 2M high storage space, so from 2M (2097152 position to start storing pictures) a total of 2M
This command supports the merger of the picture programming, does not support a single picture file programming.

FS_DLOAD is the script, and SIZE is the total size of the picture to be downloaded. Such as FS_DLOAD (192000); that 192000 bytes of pictures downloaded to the flash, the total size of the picture can not exceed 2097152 bytes, if the SIZE assignment greater than 2097152 bytes, the system only to identify 2097152 bytes.


SDIMG for the script, x, y for the picture to be displayed at the beginning of the screen position, w, h were the width and height of the picture, 'name' for the file name, currently only supports English name. SDIMG (0,0,240,400, '6.bin'); that is, the SD card stored 6.bin file in the module 0,0 position display

Vertical and horizontal screen switch CMD
DIR(H_V);
The LCD is displayed by default for DIR (0); for vertical screen

Such as DIR (0); for vertical screen. DIR (1); for horizontal screen

Set the brightness of the backlight
BL (p); 
After the system is powered on, the brightness of the backlight is 20

where BL is the instruction code, p is the brightness value of the backlight, the adjustment range is: 0 ~ 255, where 0 is full display, 255 is off display.

Draw points
PS (x, y, c); 
This instruction does not apply to large areas of speculation, if there is a need to recommend built-in internal modules

where PS is the instruction code, x, y is the starting position of the display, c is the color of the point

Draw lines
PL (x1, y1, x2, y2, c) 
Note that the range of c is 0 to 15, and if the value of c exceeds 15, the system will ignore this operation.

where PL is the instruction code, x1, y1 is the starting point, x2, y2 is the position of the end point, c is the color of the line

Draw box
BOX (x1, y1, x2, y2, c) 


where BOX is the instruction code, x1, y1, the position of the starting point, x2, y2 is the position of the end point, c is the color of the box

Draw box with Filled color
BOXF (x1, y1, x2, y2, c);


 where BOXF is the instruction code, x1, y1, the position of the starting point, x2, y2 is the position of the end point, c is the color of the box

Draw a circle
CIR (x, y, r, c); 


where CIR is the instruction code, x, y is the center of the circle, r is the radius of the circle, c is the circle color

Draw a circle with Filled color
CIRF (x, y, r, c); 


where CIRF is the instruction code, x, y is the center of the circle, r is the radius of the circle, c is the color of the circle

Set background color
SBC (c); 


where SBC is the instruction code, c is the background color value, and c ranges from 0 to 63.

Display 16 high character With background color instruction
DCV16 (x, y, * str, c); 


where DCV16 is the instruction code, x, y is the starting position of the character, * str is the pointer of the character, c is the color of the character

Display 24 high character With background color instruction
DCV24 (x, y, * str, c); 


where DCV24 is the instruction code, x, y is the starting position of the character, * str is the pointer of the character, c is the color of the character

Display 32 high character With background color instruction
DCV32 (x, y, * str, c); 


where DCV32 is the instruction code, x, y is the starting position of the character, * str is the pointer of the character, c is the color of the character

