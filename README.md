# Web Scraping de Restaurantes Veganos

Grupo 06

Pablo Tsang Chang 

Anton Pogromskyy 

Eduardo Vicente García 

José Ma

Este proyecto realiza la extracción automatizada de datos del sitio web [Happy Cow](https://www.happycow.net/) usando principalmente la librería Selenium. El objetivo principal es recopilar información clave sobre los restaurantes, como su nombre, dirección, precio, horario, y otros datos relevantes, para luego almacenarlos en un archivo CSV.



## 1. Introducción

En este proyecto hemos diseñado y desarrollado un sistema de web scraping para navegar por un conjunto de URLs de restaurantes, extraer los datos importantes y organizarlos en un formato estructurado. 

La funcionalidad general del sistema incluye: 



* Una navegación automática a través de Selenium
* Aceptación automática de cookies: Incluye manejo de ventanas emergentes de cookies, con verificación de diferentes tipos de pop-ups.
* Extracción de datos relevantes
* Manejo de errores: Control de errores para sitios web inaccesibles o elementos faltantes en las páginas.
* Almacenamiento de los datos: Los datos recolectados se guardan en un archivo CSV para análisis posterior.

## 2. Retos y Soluciones


### Búsqueda de Sitio Web 

Inicialmente, elegimos Tripadvisor como nuestro sitio web preferido para hacer web scraping, ya que es una de las plataformas más grandes con una cantidad significativa de datos interesantes sobre restaurantes. Sin embargo, nos encontramos rápidamente con un obstáculo: fuimos detectados como bots, lo que resultó en el bloqueo de nuestra IP y la aparición constante de captchas, haciendo imposible continuar el scraping. Intentamos explorar otras alternativas como Yelp y The Fork, pero obtuvimos resultados similares, enfrentándonos nuevamente a sistemas anti-scraping.

Probamos varias técnicas para evadir estos bloqueos, incluyendo la modificación de User-Agents, la implementación de esperas dinámicas en el código para simular un comportamiento más humano, y el uso de proxies para evitar el bloqueo de IPs. Sin embargo, ninguna de estas soluciones resultó efectiva a largo plazo. Además, los proxies gratuitos que encontramos online no funcionaban adecuadamente, y no tuvimos acceso a servicios premium como Bright Data, que ofrecen soluciones profesionales pero son de pago.

La razón principal detrás de estos obstáculos es que muchas de estas grandes plataformas, como Tripadvisor, implementan sistemas robustos contra bots, y esto se refleja claramente en sus políticas de robots.txt, que prohíben la extracción automatizada de datos.

Finalmente, encontramos un sitio web alternativo: Happy Cow, una plataforma centrada en restaurantes y cafeterías veganas y vegetarianas, cuya estructura era muy similar a la de Tripadvisor. Afortunadamente, Happy Cow tiene una política menos restrictiva hacia los bots, lo que lo convirtió en la opción ideal para nuestro proyecto.


### Aceptación de cookies

Otro reto importante que enfrentamos fue la gestión de las cookies en Happy Cow. Descubrimos que el sitio tenía tres tipos diferentes de pop-ups de cookies, lo que complicó el proceso de scraping. El primer tipo de pop-up fue fácil de identificar y no tuvimos problemas en encontrar y hacer clic en el botón de aceptación. Sin embargo, el segundo tipo de pop-up fue más problemático y causaba que el programa se detuviera sin motivo aparente.

Después de investigar, descubrimos que este segundo pop-up tenía una estructura muy similar al primero, pero con ligeras diferencias en su diseño, lo que dificultaba su detección. Además, este pop-up aparecía de forma aleatoria y no con mucha frecuencia, lo que complicaba su captura e inspección en tiempo real. Sospechamos que esta irregularidad en la aparición del pop-up estaba diseñada intencionalmente para dificultar los intentos de scraping automático en la página.

El tercer tipo de pop-up correspondía a la página principal de Happy Cow, mientras que el primer tipo de pop-up aparecía en las páginas de los restaurantes individuales. La solución final en el código fue la creación de tres bloques anidados de try except que prueba los tres tipos de cookies. 

### Banner publicitario

También nos encontramos con la siguiente dificultad a la hora de extraer los datos: en la página web de cada restaurante aparece un banner publicitario en la parte inferior de la página que podía interferir con la acción del driver de hacer clic en el desplegable del horario, al estar el anuncio encima del botón del desplegable, especialmente cuando se ejecuta el código en un ordenador portátil, cuya pantalla es pequeña y hace que la ventana del navegador también lo sea. 

Lo primero que se nos ocurrió para solucionar esto es cerrar el anuncio, ya que el banner dispone de un botón para ello, pero vimos que para acceder al anuncio era necesario cambiar el driver al iframe en el cual el anuncio se encontraba, y aun así, la acción de hacer clic en el botón de cerrar el anuncio no funcionaba correctamente. Y no solo eso, sino que también, mientras hacíamos pruebas al código, vimos que ocasionalmente el proveedor de publicidad que mostraba el anuncio no era siempre el mismo, de forma que conseguimos identificar 3 iframes distintos pertenecientes a diferentes servicios de publicidad con estructuras distintas que podían aparecer de manera aleatoria al cargar la página web. 

Con lo cual, debido a la complejidad que podría suponer el código para cerrar el anuncio, decidimos optar por una solución más sencilla pero igual de efectiva, que era, antes de hacer clic al desplegable del horario, incluir una línea de código que ejecuta una línea de JavaScript que hace que un pequeño scroll (de 70 píxeles) en la ventana, de forma que el anuncio no tapa el botón de desplegar el horario y así, el driver podía hacer clic a éste correctamente y recopilar la información del horario.


### Modo headless

Selenium ofrece una opción llamada –headless que permite ejecutar el navegador Chrome sin abrir la ventana visible, lo que puede acelerar la ejecución del código al reducir el consumo de recursos. Esta opción es útil en muchas aplicaciones de web scraping, especialmente para automatizaciones en segundo plano o en servidores sin interfaz gráfica.

Sin embargo, en nuestro caso no funcionó de forma óptima. Dado que nuestro proceso incluía múltiples interacciones dinámicas con elementos de la página, observamos que Selenium no siempre ejecutaba el código correctamente en este modo. Esto podría deberse a problemas con la carga y visualización de ciertos elementos cuando no hay una ventana visible.

Por este motivo, decidimos no usar el modo headless y optamos por monitorear visualmente la ejecución, lo cual nos permitió identificar y solucionar posibles errores en tiempo real.


### XPath Absoluto vs Relativo

Al principio, usamos XPaths absolutos para seleccionar elementos, ya que era la forma más directa y rápida de acceder a ellos. No obstante, nos dimos cuenta de que esta estrategia no era óptima a largo plazo. En algunos sitios web de restaurantes, la estructura de la página variaba ligeramente, lo que causaba que el código fallara al no encontrar los elementos esperados.

Para resolver este problema, convertimos la mayoría de nuestros XPaths a rutas relativas. Este cambio permitió que el código fuera más flexible, encontrando los elementos de forma dinámica y adaptándose mejor a posibles cambios estructurales en las páginas. Aunque requirió tiempo y ajustes, esta experiencia nos ayudó a mejorar nuestras habilidades en la creación de XPaths y a hacer el código más robusto.

### Añadido dinámico al CSV

El último problema que nos surgió fue relacionado con la obtención del resultado final. Cuando ejecutábamos “main.py”, el CSV se escribía cuando se habían obtenido todos los datos de todos los restaurantes en el fichero de URLs. Esto causaba que, en caso de fallo del script, perdíamos todo el progreso realizado. Para ello, modificamos la función que escribe los datos de los restaurantes en el archivo CSV, de forma que, una vez obtenido los datos de un restaurante, los escribe en el CSV antes de empezar a recolectar los datos del siguiente restaurante. De esta forma, en caso de fallo, podemos retomar la ejecución del script en el punto donde ocurrió el fallo.



## 3. Estructura

main.py: Este es el archivo principal que ejecuta el proceso de extracción de datos de los restaurantes. Optamos por realizar el scraping en batches (bloques) debido a la gran cantidad de URLs, lo cual hacía que el proceso fuera largo si se realizaba de una sola vez. Trabajar por batches también permitió distribuir el trabajo entre los cuatro miembros del equipo, lo que aceleró considerablemente la recolección de datos y evitó sobrecargar el sistema.

restaurant_class.py: Este archivo implementa la clase Restaurant, que encapsula todas las funciones necesarias para extraer información de la página web de cada restaurante. Dentro de main.py, una vez se instancia la clase Restaurant, se puede llamar al método fetch_restaurant_data(), que obtiene toda la información deseada del restaurante y devuelve un diccionario con los datos extraídos, listo para ser procesado o guardado.

get_urls.py: este archivo usa las funciones de “get_urls_functions.py” para obtener las URLs de los restaurantes cuyos datos queremos recolectar. Para ello, el driver se inicia en la página principal de HappyCow, acepta las cookies (puede tardar un poco), introduce “Madrid, Spain” en la barra de búsqueda y hace clic para buscar. Luego, se aplican ciertos filtros para seleccionar los restaurantes que nos interesan, se reduce el mapa

get_urls_functions.py

fichero_url.txt: este fichero es obtenido con “get_urls.py” y contiene las URLs de las páginas de los restaurantes en HappyCow. Luego este fichero será usado por “main.py” para obtener los datos de los restaurantes contenidos en el fichero.



## 4. Requisitos

Es necesario tener instalado la librería de selenium:

pip install selenium

pip install webdriver_manager



## 5. Configuración

Clonar el repositorio o descargar los archivos.

Instalar las dependencias.

Asegurarse de tener el navegador compatible instalado.



## 6. Instrucciones de Uso

Para el correcto funcionamiento de los scripts, deberemos tener en el mismo directorio los ficheros “get_urls.py”, “get_urls_functions.py”, “restaurant_class.py” y “main.py”. También es muy importante **dejar en primer plano la ventana del navegador** que se abre al ejecutar los scripts, ya que en el caso de que esta ventana esté detrás de otra, minimizada o en segundo plano puede generar problemas a la hora de extraer los datos.



* Paso 1:

    Lo primero de todo, necesitamos generar el fichero .txt con las URLs de los restaurantes cuyos datos vamos a extraer, así que primero de todo ejecutaremos “get_urls.py”. Este fichero, que usa las funciones definidas en “get_urls_functions.py ”, extraerá todos los enlaces de los restaurantes en Madrid que tiene la página web (la ciudad que viene definida en el script). Una vez terminado, se habrá creado en nuestro directorio el fichero “fichero_url.txt” con todas las URLs que vamos a explorar.

* Paso 2:

    Una vez obtenido el fichero con las URLs, ejecutaremos “main.py”. Este script es el encargado de extraer los datos de todas las páginas web que se encuentran en “fichero_url.txt”. Una vez acabada la ejecución del script, obtendremos un fichero llamado “restaurants.csv” con toda la información recopilada de todos los restaurantes.

## 7. Output

El output final para este proyecto es el fichero csv restaurants.csv con la información de todos los restaurantes. Está compuesto por los siguientes campos:



* id: número identificativo del restaurante en el .csv.
* Name: nombre del restaurante.
* Address: dirección de restaurante.
* Lat: latitud en la que se encuentra el restaurante.
* Long: longitud en la que se encuentra el restaurante
* Number of ratings: número de reseñas que tiene el restaurante.
* Restaurant rating: número de estrellas (de 0 a 5) que tiene el restaurante, basado en las reseñas.
* Type of restaurant: lista con la(s) nacionalidad(es) del restaurante.
* Number of bookmarks: número de personas que han guardado la página del restaurante.
* Price range: rango de precio del restaurante.
* Phone number: número de teléfono del restaurante.
* Website: página web del restaurante.
* Instagram: enlace a la página de instagram del restaurante.
* Facebook: enlace a la página de facebook del restaurante.
* Timetable: diccionario con el horario del restaurante. Las claves son los días de la semana y los valores las horas a las que el restaurante está abierto ese día.
* Url: URL que dirige a la página del restaurante en HappyCow.
