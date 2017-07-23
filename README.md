# Mini-Ttwitt-Django #                   

![alt-text](https://github.com/DGun17/MTwitt/blob/master/static/img/logo.png)

Aplicacion web que tiene las bases en twitter como modelo, con fines practicos para aprender del framework, realizado con 
**Python 3.5**

# Requisitos #

+ **Mysqlcliente**

  - Instalación  
    - `$ pip install mysqlclient`
 
  - Aveces se produce un error al instalar el paquete ya que depende de la libreria **libmysqlclient-dev**, y su solucion es instalando dicha libreria
    - `$ sudo apt-get install libmysqlclient-dev` \
    **Fuente: https://stackoverflow.com/questions/5178292/pip-install-mysql-python-fails-with-environmenterror-mysql-config-not-found#5178698**
  
+ **Django 1.11.3**

  - Instalación
    - `$ pip install django`

+ **Django-Registration-Redux**

  - Instalación
    - `$ pip install django-registration-redux`
    
  - Documentación
    - https://django-registration-redux.readthedocs.io/en/latest/
    
+ **Django-Crispy-Forms**

  - Instalación
    - `$ pip install --upgrade django-crispy-forms`
    
   - Documentación
      - http://django-crispy-forms.readthedocs.io/en/latest/index.html 
   

Nota: se encontraran en el archivo de requeriments.txt

# Ejemplo #

![alt-text](https://github.com/DGun17/MTwitt/blob/master/static/img/pagination.png)


# Instalacion o ejecucion #

**Nota: Se debe aclarar que ademas de los modulos requeridos en este, se debe tener una 
base de datos MySQL instalada, ya que se explicara aqui si seleccionan otra de su 
preferencia podrian averiguar un poco de esta, ya que no difiere mucho, ademas de saber
si es compatible con Django, ademas se asumira que cuentan con un entorno virtualizado con python 3.5**
https://virtualenv.pypa.io/en/stable/
 
 ## 1. Creando archivo settings.py ##
 
 Dentro del directorio **twitter** se encontrara el archivo **settings_copy.py**
 se procede a reenombrarlo a **settings.py**
 
 ## 2. Registrando base de datos ##
 
 Con el archivo settings preparado se procede a "registrar" la base de datos
 en la aplicacion rellenando lo siguiente
  
 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': ' el nombre de tu Base de Datos ',
        'USER': ' tu usuario ',
        'PASSWORD': ' tu contraseña ',
        'HOST': ' IP ',
        'PORT':' Puerto ',
    }
}
```

Para alguna diferente a MySQL se puede consultar en: https://docs.djangoproject.com/en/1.11/ref/settings/#databases


## 3. Instalando modulos requeridos ##

Para esto ejecutaremos el siguiente comando

`$ pip install -r requirements.txt`

## 4. Configurando correo electronico ##

En mi caso utilice el servicio smtp de gmail llene los siguientes datos en el
archivo settings.py

```
EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=25
EMAIL_HOST_USER=' Tu Correo Electronico de Gmail'
EMAIL_HOST_PASSWORD=' Tu contraseña '
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
```

Para que su cuenta de gmail pueda enviar mensajes desde el aplicativo, pueden
desactivar lo siguiente https://myaccount.google.com/lesssecureapps?pli=1 (Solucion propuesta),
recomiendo que se creen una cuenta diferente a la personal.
 

## 5. Generando migraciones ##

Este paso es para estar seguro que al momento de migrar los modelos, del
aplicativo estos se hallan realizado correctamente, se ejecuta el siguiente
comando

`$ python manage.py makemigrations`

Lo anterior creara un archivo de migracion que sera usado para registrar los modelos en la
base de datos configurada, por ultimo se realiza la migracion si no ha sucedido nada malo

`$ python manage.py migrate`

## 6. Ejecutando la aplicacion ##

El comando habla por si solo :D

`$ python manage.py runserver`


