# Meli-Challenge
Esta aplicación cumple con el challenge propuesto Caso - Keyword en Gmail.
La misma consiste en un script que se conecta automaticamente a la cuenta de gmail, busca por todos los correos que contengan la palabra **DevOps** y los almacena en una base de datos.

## Requisitos
Para que la aplicación funcione correctamente, es necesario tener instalado:
 - Docker-compose
 - Python3 y pip3
 - google-api-python-client
 - google-auth-httplib2
 - google-auth-oauthlib

## Utilizar la aplicación
Para el uso de la aplicación, es necesario:
 - Clonar el repositorio
 - Generar el archivo **credentials.json** y guardarlo dentro del repositorio clonado.

Una vez realizado lo anterior, vamos a ejecutar el siguiente comando:
`python3 start.py`

El cual nos abrira una sesión del navegador en donde nos tendremos que loguear utilizando la cuenta de prueba y tendremos que aceptar los permisos que requiere la aplicación.

Luego de esto y si no hubo ningun inconveniente veremos un mensaje satisfactorio en la consola y podremos correr el contenedor de Docker
`docker-compose up -d --build`

## Visualizar la Base de Datos
Para poder ver la base de datos, el aplicativo cuenta con una instacia de **Adminer** a la cual podremos ingresar mediante la URL http://localhost:8080 en donde tanto el usuario como la contraseña son "root"
