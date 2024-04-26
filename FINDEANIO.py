import time
from datetime import datetime
import pygame

# Inicializar pygame
pygame.init()

# Establecer la ruta de los archivos MP3
archivo1 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\7-15.mp3"
archivo2 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\7-30.mp3"
archivo3 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\7-45.mp3"
archivo4 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\8.mp3"
archivo5 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\8-15.mp3"
archivo6 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\8-30.mp3"
archivo7 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\8-45.mp3"
archivo8 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\9.mp3"
archivo9 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\9-15.mp3"
archivo10 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\9-30.mp3"
archivo11 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\9-45.mp3"
archivo12 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\10.mp3"
archivo13 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\10-15.mp3"
archivo14 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\10-30.mp3"
archivo15 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\10-45.mp3"
archivo16 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\11.mp3"
archivo17 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\11-15.mp3"
archivo18 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\11-30.mp3"
archivo19 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\11-35.mp3"
archivo20 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\11-45.mp3"
archivo21 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\11-50.mp3"
archivo22 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\11-55.mp3"
archivo23 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\11-56.mp3"
archivo24 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\11-57.mp3"
archivo25 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\11-58.mp3"
archivo26 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\11-59.mp3"
archivo27 = "C:\\Users\\Xps\\Downloads\\placas\\findeano\\HORA\\12.mp3"

hora_programada1 = "19:15"
hora_programada2 = "19:30"
hora_programada3 = "19:45"
hora_programada4 = "20:00"
hora_programada5 = "20:15"
hora_programada6 = "20:30"
hora_programada7 = "20:45"
hora_programada8 = "21:00"
hora_programada9 = "21:15"
hora_programada10 = "21:30"
hora_programada11 = "21:45"
hora_programada12 = "22:00"
hora_programada13 = "22:15"
hora_programada14 = "22:30"
hora_programada15 = "22:45"
hora_programada16 = "23:00"
hora_programada17 = "23:15"
hora_programada18 = "23:30"
hora_programada19 = "23:35"
hora_programada20 = "23:45"
hora_programada21 = "23:50"
hora_programada22 = "23:55"
hora_programada23 = "23:56"
hora_programada24 = "23:57"
hora_programada25 = "23:58"
hora_programada26 = "23:59"
hora_programada27 = "00:00"

ultima_reproduccion = None

def reproducir_mp3(ruta):
    global ultima_reproduccion
    print(f"Reproduciendo: {ruta}")
    pygame.mixer.music.load(ruta)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        ultima_reproduccion = datetime.now().strftime("%H:%M")

print("El script está en ejecución...")

while True:
    hora_actual = datetime.now().strftime("%H:%M")

    if hora_actual in [hora_programada1, hora_programada2, hora_programada3, hora_programada4, hora_programada5,
                       hora_programada6, hora_programada7, hora_programada8, hora_programada9, hora_programada10,
                       hora_programada11, hora_programada12, hora_programada13, hora_programada14, hora_programada15,
                       hora_programada16, hora_programada17, hora_programada18, hora_programada19, hora_programada10,
                       hora_programada21, hora_programada22, hora_programada23, hora_programada24, hora_programada25,
                       hora_programada26, hora_programada27]:
      if hora_actual != ultima_reproduccion:  # Evitar la reproducción en el mismo minuto
        if hora_actual == hora_programada1:
            reproducir_mp3(archivo1)
        elif hora_actual == hora_programada2:
            reproducir_mp3(archivo2)
        elif hora_actual == hora_programada3:
            reproducir_mp3(archivo3)
        elif hora_actual == hora_programada4:
            reproducir_mp3(archivo4)
        elif hora_actual == hora_programada5:
            reproducir_mp3(archivo5)
        elif hora_actual == hora_programada6:
            reproducir_mp3(archivo6)
        elif hora_actual == hora_programada7:
            reproducir_mp3(archivo7)
        elif hora_actual == hora_programada8:
            reproducir_mp3(archivo8)
        elif hora_actual == hora_programada9:
            reproducir_mp3(archivo9)
        elif hora_actual == hora_programada10:
            reproducir_mp3(archivo10)
        elif hora_actual == hora_programada11:
            reproducir_mp3(archivo11)
        elif hora_actual == hora_programada12:
            reproducir_mp3(archivo12)
        elif hora_actual == hora_programada13:
            reproducir_mp3(archivo13)
        elif hora_actual == hora_programada14:
            reproducir_mp3(archivo14)
        elif hora_actual == hora_programada15:
            reproducir_mp3(archivo15)
        elif hora_actual == hora_programada16:
            reproducir_mp3(archivo16)
        elif hora_actual == hora_programada17:
            reproducir_mp3(archivo17)
        elif hora_actual == hora_programada18:
            reproducir_mp3(archivo18)
        elif hora_actual == hora_programada19:
            reproducir_mp3(archivo19)
        elif hora_actual == hora_programada20:
            reproducir_mp3(archivo20)
        elif hora_actual == hora_programada21:
            reproducir_mp3(archivo21)
        elif hora_actual == hora_programada22:
            reproducir_mp3(archivo22)
        elif hora_actual == hora_programada23:
            reproducir_mp3(archivo23)
        elif hora_actual == hora_programada24:
            reproducir_mp3(archivo24)
        elif hora_actual == hora_programada25:
            reproducir_mp3(archivo25)
        elif hora_actual == hora_programada26:
            reproducir_mp3(archivo26)
        elif hora_actual == hora_programada27:
            reproducir_mp3(archivo27)

    time.sleep(5)  # Espera 40 segundos antes de volver a verificar la hora
