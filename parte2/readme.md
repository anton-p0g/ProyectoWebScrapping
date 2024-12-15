# Directorio Correlaciones

Este directorio contiene el fichero `Correlaciones.ipynb` y el directorio `Figuras`.

## Correlaciones.ipynb

Correlaciones.ipynb es un Jupyter notebook que documenta el análisis de los datos extraídos del archivo original restaurants_definitivo.csv. En este notebook, se realizaron diversas manipulaciones y transformaciones de los datos para preparar un análisis más profundo. Esto incluyó la creación de nuevas variables numéricas a partir de los datos originales, así como la conversión de variables categóricas en valores numéricos para facilitar los análisis.

### Entre las nuevas variables creadas se encuentran:

- **Horas totales trabajadas por semana.**
- **Número total de días abiertos.**
- **Horas promedio trabajadas por día.**
- **Número total de redes sociales disponibles** (Website, Instagram, Facebook).
- **Indicador binario de si tiene al menos una red social.**
- **Métrica de popularidad**, que combina ponderaciones de diferentes características (número de ratings, marcadores, presencia en redes sociales, entre otros).

### El análisis incluyó:

1. **Visualización de la Popularidad**:
   Se generó un histograma para interpretar la distribución de la métrica de popularidad, identificando tendencias y posibles conclusiones. Para ello primero se han normalizado las variables usadas en el cálculo usando la librería sklearn usando el método de MinMaxScaler que transforma los datos en valores entre 0 y 1. 

2. **Matriz de Correlaciones**:
   Se construyó una matriz de correlaciones para identificar relaciones significativas entre las variables numéricas. Esto permitió detectar relaciones interesantes, como la clara correlación entre el número de ratings y el número de marcadores.

3. **Gráficos de Dispersión**:
   - Se creó un scatter plot para visualizar la correlación entre el número de ratings y el número de marcadores.
   - Otro scatter plot analizó la relación entre las horas trabajadas por semana y la métrica de popularidad.


El notebook incluye tanto las transformaciones realizadas como la documentación en celdas de markdown y comentarios dentro del código, asegurando que los pasos están claramente explicados.

## Directorio Figuras

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
