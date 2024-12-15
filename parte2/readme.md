# Directorio Correlaciones

Este directorio contiene el fichero `Correlaciones.ipynb` y el directorio `Figuras`.

## Correlaciones.ipynb

`Correlaciones.ipynb` es un Jupyter notebook que documenta el análisis de los datos extraídos del archivo original `restaurants_definitivo.csv`. En este notebook, se realizaron diversas manipulaciones y transformaciones de los datos para preparar un análisis más profundo. Esto incluyó la creación de nuevas variables numéricas a partir de los datos originales, así como la conversión de variables categóricas en valores numéricos para facilitar los análisis.

### Entre las nuevas variables creadas se encuentran:

- **Horas totales trabajadas por semana.**
- **Número total de días abiertos.**
- **Horas promedio trabajadas por día.**
- **Número total de redes sociales disponibles** (Website, Instagram, Facebook).
- **Indicador binario de si tiene al menos una red social.**
- **Métrica de popularidad**, que combina ponderaciones de diferentes características (número de ratings, marcadores, presencia en redes sociales, entre otros).

### El análisis incluyó:

1. **Visualización de la Popularidad**:
   Se generó un histograma para interpretar la distribución de la métrica de popularidad, identificando tendencias y posibles conclusiones. Para ello primero se han normalizado las variables usadas en el cálculo usando la librería `sklearn` usando el método de `MinMaxScaler` que transforma los datos en valores entre 0 y 1. 

2. **Matriz de Correlaciones**:
   Se construyó una matriz de correlaciones para identificar relaciones significativas entre las variables numéricas. Esto permitió detectar relaciones interesantes, como la clara correlación entre el número de ratings y el número de marcadores.

3. **Gráficos de Dispersión**:
   - Se creó un scatter plot para visualizar la correlación entre el número de ratings y el número de marcadores.
   - Otro scatter plot analizó la relación entre las horas trabajadas por semana y la métrica de popularidad.


El notebook incluye tanto las transformaciones realizadas como la documentación en celdas de markdown y comentarios dentro del código, asegurando que los pasos están claramente explicados.

### Directorio Figuras

El directorio Figuras contiene las gráficas generadas durante el análisis, que fueron utilizadas en nuestra presentación. Estas incluyen:

- El **histograma de la popularidad**.
- La **matriz de correlaciones**.
- El **gráfico de dispersión** que destaca las relaciones clave entre ratings y marcadores.

Este análisis nos ha permitido obtener una visión más clara de los factores que influyen en los datos de los restaurantes y generar conclusiones importantes basadas en las correlaciones identificadas.

---
# Directorio ficheros_csv
Este directorio contiene los ficheros .csv que se van a emplear para el tratamiento y visualización de datos. Esos ficheros son:

- `restaurants_definitivo.csv`: fichero que contiene todos los datos de los restaurantes obtenidos mediante scraping.
- `restaurantes_con_distrito_barrio.csv`: fichero obtenido del notebook `mapas.ipynb` que contiene, además de todos los datos contenidos en `restaurants_definitivo.csv`, dos columnas extra con el distrito y barrio en el que se localiza cada restaurante.
- `transformaciones.csv`: contiene las transformaciones y manipulaciones de datos que hemos realizado sobre el dataset original. 
---

# Directorio Mapas distribución y afluencia
Este directorio contiene los siguientes ficheros:

## mapas.ipynb 
Se trata de un notebook que realiza todas las transformaciones de datos necesarias para responder dos preguntas: 
- ¿Cuál es la distribución de los restaurantes veganos por distritos en la ciudad de Madrid? 
- ¿Qué distritos tienen los restaurantes más populares?. 

Para ello se manipulan los ficheros `restaurants_definitivo.csv`, `Distritos.shp` y `Barrios.shp`. Una vez realizadas las transformaciones oportunas (descritas en el notebook con anotaciones markdown) se generan dos gráficas: la primera contiene los mapas por distrito y barrio de la cantidad de restaurantes que hay en cada distrito o barrio y la segunda contiene un mapa que muestra qué distritos tienen de media más reseñas por restaurante, lo que puede ser un indicador de popularidad.

## Ficheros auxiliares
- `Distritos.shp`: fichero que describe los polígonos que forman los distritos de la ciudad de Madrid. Depende del fichero Distritos.shx.
- `Distritos.shx`: fichero que contiene los índices de los polígonos del fichero anterior.
- `Barrios.shp`: fichero que describe los polígonos que forman los distritos de la ciudad de Madrid. Depende del fichero Barrios.shx.
- `Barrios.shx`: fichero que contiene los índices de los polígonos del fichero anterior.

---
# Directorio Top tipos de restaurantes 

En el directorio mencionado se encuentra el Jupyter notebook top_tipos_restaurantes.ipynb, que utiliza como base el archivo CSV `restaurantes_con_distrito_barrio`. A partir de este, realiza diversas operaciones para generar el CSV `df_tipos`. El resultado es un dataframe cuyo índice representa los tipos de gastronomía, mientras que sus columnas contienen diferentes factores relacionados.

El propósito de este apartado es responder preguntas como:

- ¿Cuáles son los tipos de restaurantes más abundantes, los que tienen más reseñas y los mejor valorados?
- ¿Cuáles son los tipos menos comunes, con menos reseñas y peor valorados?

Además, se proporciona información útil, como un rango aproximado de precios y los barrios y distritos donde cada tipo de restaurante se encuentra con mayor frecuencia.

Para complementar, se incluyen diagramas de tarta que ilustran la proporción de cada tipo de restaurante según distintas características, así como diagramas de cajas que permiten analizar la distribución de los restaurantes en función de diferentes variables.

---
# Directorio Análisis_areas

### Tratamiento de datos
Imaginemos el caso de un empresario que desea abrir un restaurante pero no sabe dónde ubicarlo. Con este escenario en mente, hemos decidido realizar un análisis geográfico para identificar las ubicaciones de los restaurantes más exitosos en función del barrio o de ciertos subgrupos de distritos de Madrid.  
Para llevar a cabo este análisis, hemos desarrollado una métrica que cuantifica el éxito de los restaurantes:  

**Success Ratio = "Number of Ratings" * "Restaurant Rating" + "Number of Bookmarks"**

Además, realizamos una hipótesis inicial que se basa en la teoría de Hotelling. Esta teoría sostiene que los negocios competidores tienden a agruparse en lugar de dispersarse, lo que les permite obtener ventajas económicas y atraer a un mayor número de clientes.


### Importación y limpieza de datos y creación de columnas
---

Este análisis se encuentra en el **jupyter notebook** `análisis_areas.ipynb` donde emplearemos las columnas:  
**Lat, Long, Number of Ratings, Restaurant Rating, Number of Bookmarks, NOMBRE_DISTRITO, NOMBRE_BARRIO.**  

Para dibujar el sector en la gráfica importamos los archivos **Distritos.shp** y **Barrios.shx** y transformamos las coordenadas que aparecen al formato **EPSG:4326 (el nuestro).**


### Visualización de los datos
---
Posteriormente, dividimos la gráfica en 12 subplots correspondientes a las 12 zonas que tenemos. Calculamos los vectores singulares de la matriz de longitud y latitud de los restaurantes con más éxito en una determinada zona correspondiente para crear después dos rectas que representarán las direcciones principales de los restaurantes con éxito.  

Pintamos en cada gráfica los puntos de los restaurantes y les damos un color respecto a la distancia con los demás restaurantes.

Además, para poder ver los restaurantes con éxito y los que no tenemos certeza de que lo tienen, dibujamos alrededor de cada restaurante una figura geométrica: un pentágono para los que tienen éxito y un rectángulo para los que no sabemos.  

Por último, dibujamos el sector con las coordenadas que importamos de **Distritos.shp** y **Barrios.shx.**  
Esta gráfica se añade al directorio `figuras`.

---

## Ejecución del código
Todo nuestro código está organizado en cuatro Jupyter Notebooks, cada uno especializado en las distintas partes del análisis descritas anteriormente. La ejecución es sencilla: basta con ejecutar cada celda secuencialmente para reproducir los resultados.

Además, cada notebook incluye celdas de Markdown con explicaciones claras y detalladas que describen el propósito y funcionamiento de cada sección del código, facilitando su comprensión y seguimiento.

## Módulos y librerías utilizadas
- **NumPy**: Se utilizó para cálculos numéricos eficientes, como operaciones en la regresión lineal.
  Instalación: `pip install numpy`
- **Pandas**: Se usó para la manipulación y transformación de datos en formato tabular.   
  Instalación: `pip install pandas`
- **Scikit-learn (Sklearn)**: Se empleó para normalizar los datos utilizando MinMaxScaler. 
  Instalación: `pip install scikit-learn`
- **Matplotlib**: Para crear gráficos como histogramas y gráficos de dispersión.  
  Instalación: `pip install matplotlib`
- **Seaborn**: Para generar gráficos estadísticos avanzados, como el heatmap de correlaciones.  
  Instalación: `pip install seaborn`
- **GeoPandas**: Nos sirvió para trabajar con objetos geoespaciales como puntos y polígonos.  
  Instalación: `pip install geopandas`

## Bibliografía
Hemos usado estos artículos de `Wikipedia` para consultar el orden en el que están los distritos y barrios de Madrid para incluir una columna en cada `GeoDataFrame` con los polígonos de cada distrito y barrio que les etiquetara.

- [Distritos de Madrid](https://es.wikipedia.org/wiki/Anexo:Distritos_de_Madrid)  
- [Barrios administrativos de Madrid](https://es.wikipedia.org/wiki/Anexo:Barrios_administrativos_de_Madrid)

## Fuentes de los archivos .shp
Hemos obtenido los archivos `.shp` que describen los polígonos que describen el contorno de los distritos y barrios de Madrid de las siguientes fuentes:
- **Distritos**:  
  [Datos Madrid - Distritos](https://datos.madrid.es/sites/v/index.jsp?vgnextoid=7d6e5eb0d73a7710VgnVCM2000001f4a900aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD)
- **Barrios**:  
  [Datos Madrid - Barrios](https://datos.madrid.es/sites/v/index.jsp?vgnextoid=760e5eb0d73a7710VgnVCM2000001f4a900aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD)
