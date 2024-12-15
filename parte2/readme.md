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
