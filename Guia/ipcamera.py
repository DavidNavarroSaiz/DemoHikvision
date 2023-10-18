# https://www.it-swarm-es.com/es/python/acceso-la-camara-ip-en-python-opencv/838815069/

# Dada una cámara IP:

# Encuentra tu cámara IP dirección
# Encuentre la port donde se accede a la dirección IP
# Encuentre el protocolHTTP/RTSP, etc.) especificado por el proveedor de la cámara
# Entonces, si su cámara está protegida, adelante, averigüe:

# tu username
# tu password

# Luego usa tus datos para ejecutar el siguiente script:

"""Access IP Camera in Python OpenCV""" 
import cv2 
# stream = cv2.VideoCapture('protocol://IP:port/1') 
# Use the next line if your camera has a username and password # 
# stream = cv2.VideoCapture('rtsp://root:root@192.168.0.42/axis-media/media.amp')
# stream = cv2.VideoCapture('rtsp://root:SDSline397@192.168.0.112/axis-media/media.amp')

stream = cv2.VideoCapture('rtsp://root:SDSline397@192.168.0.112/axis-media/media.amp')#Muelles 3 y 4

while True: 
    r, f = stream.read() 
    resized = cv2.resize(f,(1024,600))
    cv2.imshow('IP Camera resized',resized) 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break 
        cv2.destroyAllWindows()


# Se puede acceder a una cámara IP en modo abierto proporcionando la URL de transmisión }
# de la cámara en el constructor de cv2.VideoCapture.

# Por lo general, la cámara utiliza el protocolo RTSP o HTTP para transmitir video. 
# Un ejemplo de URL de transmisión de cámara IP es el siguiente:

# capture = cv2.VideoCapture('rtsp://username:password@192.168.1.64/1')
# cap = cv2.VideoCapture("http://192.168.18.37:8090/test.mjpeg")



# Para obtener el enlace de video de la cámara IP:

# Abra la cámara IP con IP y PORT en el navegador
# Haz clic derecho en el video y selecciona "copiar la dirección de la imagen"
# Usa esa dirección para capturar video






# Para acceder a una cámara IP, primero, le recomiendo que la instale como la va a
# usar para la aplicación estándar, sin ningún código, utilizando el software normal.

# Después de esto, debes saber que para diferentes cámaras tenemos diferentes códigos. 
# Hay un sitio web donde puede ver qué código puede usar para acceder a ellos:

# https://www.ispyconnect.com/sources.aspx

# Pero tenga cuidado, para mi cámara (Intelbras S3020) no funciona. La forma correcta 
# es preguntar a la compañía de su cámara, y si son una buena compañía, la proporcionarán.

# Cuando sepas tu código solo agrégalo como:

# cap = cv2.VideoCapture("http://LOGIN:PASSWORD@IP/cgi-bin/mjpg/video.cgi?&subtype=1")
# En vez de INICIAR SESIÓN, ingresará su nombre de usuario y, en cambio, CONTRASEÑA, 
# ingresará su contraseña.

# Para averiguar la dirección IP de la cámara, hay muchos programas que puede descargar 
# y proporcionarle la dirección IP. Utilizo el software de Intelbras, pero también 
# recomiendo EseeCloud porque funcionan para casi todas las cámaras que compré:

# https://eseecloud.software.informer.com/1.2/

# En este ejemplo, muestra el protocolo http para acceder a la cámara IP, 
# pero también puede usar rstp, depende de la cámara, como dije.

# Si tienes más preguntas solo házmelo saber.