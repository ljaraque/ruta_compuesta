# Ejemplo Django 
### Tema: Rutas Compuestas `urls.py proyecto` + `urls.py apps`  

#### Descripción

Este proyecto `Django` describe la configuración de URLS para un proyecto compuesto por múltiples `apps` sobre un proyecto principal llamado `ruta_compuesta`.  

#### Applicaciones  

1. `app_ex` --> Ubicada en ruta `""` del proyecto principal `ruta_compuesta`.  
2. `dashboard` --> Ubicada en la ruta `dash` del proyecto principal `ruta_compuesta`.  

#### URLs  

URLs montadas sobre ruta raíz `""`del proyecto base:  
1. URL: **localhost:8000** 
	Correspondiente a la función `inicio` del archivo `views.py` de la aplicación `app_ex`.  
2. URL: **localhost:8000/empresa**  
	Corresponde a la funcion `empresa` del archivo `views.py` de la aplicación `app_ex`. 
3. URL: **localhost:8000/contacto**  

URLs montadas sobre ruta `dash/` del proyecto base:  
1. URL: **localhost:8000/dash/grafico**  
	Correspondiente a la función `grafico_principal` del archivo `views.py`de la aplicación `dashboard`.  
2. URL: **localhost:8000/buscador**  
	Correspondiente a la función `google` del archivo `views.py` de la aplicación `dashboard`. Esta función efectúa un redireccionamiento a `http://www.google.com`  

#### Acerca de funciones en `views.py`  

En aplicación `app_ex`:  
- `inicio`: Renderiza template `elefante.html` con `context={'texto':'Texto de Ejercicio 1'}`.  
- `empresa`: Renderiza template `empresa.html` con `context={'texto':'Texto de Ejercicio 1'}`.  
- `contacto`: No implementada.  

En aplicación `dashboard`:  
- `grafico_principal`: Renderiza template `grafico.html`, sin `context`.  
- `google`: Redirecciona a `https://www.google.com`.  




