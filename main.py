import cv2

# Muestra la lista de cámaras disponibles
print("Cámaras disponibles:")
for i in range(0, 10):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print("Cámara encontrada en el índice:", i)
        cap.release()

# Solicita al usuario que seleccione una cámara
index = int(input("Por favor, introduce el índice de la cámara que quieres usar: "))

# Inicializa la cámara seleccionada
cap = cv2.VideoCapture(index)

# Create a window in normal size
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

while(True):
    # Captura cuadro por cuadro
    ret, frame = cap.read()

    # Muestra el cuadro resultante
    cv2.imshow('frame', frame)
    
    # Set the window to full screen
    cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # Si presionas 'q' en el teclado, se cierra la ventana
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cuando todo esté hecho, libera la captura y cierra las ventanas
cap.release()
cv2.destroyAllWindows()
