# Tercera_preentrega_Lobos

Tercera preentrega curso Python: WEB Django con patrón MVT.

Bienvenidx.

Esta es una página web creada utilizando Django. Es una página de recetas de cocina.

He creado cuatro modelos que encontrarás en "\Tercera_preentrega_Lobos\proyecto_uno\App1\models.py". Tres des estos modelos consisten en bases de datos de recetas y el modelo restante es una base de datos de contactos de visitantes de la página.

Cada modelo tiene asociado un formulario, que se encuentra en "\Tercera_preentrega_Lobos\proyecto_uno\App1\forms.py", a partir de los cuales se realiza la carga de datos a cada base de datos.

Así mismo, en el módulo "\Tercera_preentrega_Lobos\proyecto_uno\App1\views.py" se encuentran las vistas tanto de los modelos, como de los formularios de carga de datos como de búsqueda de datos en las bases de datos.

En el módulo "Tercera_preentrega_Lobos\proyecto_uno\App1\urls.py" se encuentran las urls de cada vista, asi como de los formularios de búsqueda y de resultados de las búsquedas.

Para correr la página es necesario ejecutar en la consola: 1- pyhton manage.py makemigrations 2- python manage.py migrate 3- python manage.py runserver Luego,desde un explorador de internet, debes ingresar a la siguente dirección: http://127.0.0.1:8000/App1/

Cualquier duda oconsulta, escribime al siguiente correo: mariana.lobos88@gmail.com
