# mutant_detector_parcial
Instrucciones para ejecutar el programa Mutantdetector:

Paso 1
Instala las dependencias necesarias ejecutando este comando en la terminal:

pip install -r requirements.txt

Ejecuta el programa iniciando el archivo principal con el siguiente comando:

python3 app.py

Paso 2
Abre Postman y carga el archivo ubicado en la carpeta collection.

Paso 3
En Postman, selecciona la solicitud POST para enviar una secuencia de ADN y verificar si es mutante. Introduce una secuencia de ADN en el cuerpo de la solicitud y envíala.

Paso 4
Para consultar estadísticas, selecciona la solicitud GET en Postman para ver el número de mutantes y no mutantes registrados en la base de datos.

Postman funcionará en esta URL local:
http://127.0.0.1:5000/

Si el programa está dockerizado y alojado en Render, solo abre Postman y utiliza las siguientes URL:

    Para la solicitud POST:
    https://parcialdise-o-1.onrender.com/mutant

    Para la solicitud GET de estadísticas:
    https://mutant-detector-parcial.onrender.com/stats
