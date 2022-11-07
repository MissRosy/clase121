import cv2
import time
import numpy as np

#Para guardar el output en un archivo output.avi.
#fourcc comprime como el .zip
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

#Iniciar la cámara web.
cap = cv2.VideoCapture(0)

#Permitir a la cámara web iniciar. haciendo al código "dormir" o esperar por 2 segundos.
time.sleep(2)
bg = 0

#Capturar el fondo por 60 cuadros.
for i in range(60):
    ret, bg = cap.read()
#Voltear el fondo.
bg = np.flip(bg, axis=1)

#Leer el cuadro capturado hasta que la cámara esté abierta.
#ret: devuelve verdadero si el cuadro está disponible
#img: tiene la matriz de la imagen
while (cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    #Voltear la imagen para que haya concordancia.
    img = np.flip(img, axis=1)

    #Convertir el color de BGR a HSV (Tono,Saturación,Brillo).
    #para detectar el color rojo de manera más eficiente
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #Generar la máscara para detectar el color rojo.
    #Color rojo
    lower_red = np.array([0, 120, 50])
    upper_red = np.array([10, 255,255])
    mask_1 = cv2.inRange(hsv, lower_red, upper_red)
    #Tono rojo
    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask_2 = cv2.inRange(hsv, lower_red, upper_red)
    
    mask_1 = mask_1 + mask_2

    cv2.imshow("mask_1", mask_1)

    cv2.waitKey(1)


cap.release()
cv2.destroyAllWindows()

