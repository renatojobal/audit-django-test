# Backend de __introducir_nombre_genial_aquí_

## Requirements

Para poder trabajar sobre el mismo entorno y con las mismas librerías, crea un entorno virtual con el siguiente nombre '.env', usando el comando 'python -m venv .env'

Luego, activa el entorno yendo a '.env\Scripts\activate'.

Una vez que tengas el entorno activado, regresa a la carpeta raiz d
el repositorio y escribe 'pip install -r requirements.txt'. Aquí pip instalar todas las librerías que estén escritas en requirements.txt.

Ahora si puedes continuar...

## Levantar el servidor en tu máquina local

### Paso 1
Abre una terminal en la carpeta del proyecto y dirígete justo donde esta el archivo manage.py

### Paso 2
Asegúrate de haber realizado las migraciones en la base de datos con los comandos:

~~~
python manage.py makemigrations
~~~
~~~
python manage.py migrate
~~~
Si ya tienes un super usuario puedes saltarte al siguiente paso, si no, aquí te recordamos como hacerlo:

Escribe:
~~~
python manage.py createsuperuser
~~~
Se te abrirá un shell interactivo donde te pedirán tus credenciales.

Nota: El superusuario no es necesario para levantar el servidor pero si para poder visualizar los datos de mejor manera a traves del admin de django

### Paso 3
Escribe:
~~~
python manage.py runserver
~~~
Y listo! Si quieres detener el servicio pulsa Ctrl + C.

Nota: Los pasos 1 y 2 solo se deben hacer la primera vez, ya que aun no tienes la base de datos. Despues, solo necesitar el paso 3 cada vez que quieras levantar el servicio.


## Levantar el servidor en tu máquina local con Docker (RECOMENDADO)

Obviamente debes tener instalado docker y docker-compose en tu máquina, puedes buscar en los sitios oficiales como hacerlo.

### Paso 1 (Solo una vez)
Abre una terminal en la carpeta raiz del proyecto.
Aquí escribe:
~~~
docker-compose build
~~~
Esto demorará algunos minutos dependiendo de tu conexión a internet.

### Paso 2 (Solo una vez)
Asegúrate de haber realizado las migraciones en la base de datos con los comandos:

~~~
docker-compose run web python backend/manage.py makemigrations
~~~
~~~
docker-compose run web python backend/manage.py migrate
~~~
Si ya tienes un super usuario puedes saltarte al siguiente paso, si no, aquí te recordamos como hacerlo:

Escribe:
~~~
docker-compose run web python backend/manage.py createsuperuser
~~~
Se te abrirá un shell interactivo donde te pedirán tus credenciales.

Nota: El superusuario no es necesario para levantar el servidor pero si para poder visualizar los datos de mejor manera a traves del admin de django

Nota: Docker y docker-compose funciona mejor en Linux o en Mac. Si tienes Windows Pro, también lo puedes hacer pero tendrás que modificar un poco los comandos

### Paso 3 
Escribe:
~~~
docker-compose up
~~~
Y listo! Si quieres detener el servicio pulsa Ctrl + C.

Nota: Los pasos 1 y 2 solo se deben hacer la primera vez, ya que aun no tienes la base de datos. Despues, solo necesitar el paso 3 cada vez que quieras levantar el servicio.
