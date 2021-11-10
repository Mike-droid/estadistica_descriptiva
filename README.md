# Curso de Matemáticas para Data Science: Estadística Descriptiva

## ¿Para qué sirve la estadística descriptiva?

### Estadístiva descriptiva vs inferencial

La estadística tiene 2 ramas pricipales:

- Descriptiva
- Inferencial

Supongamos las estadísticas de un jugador de fútbol.

- Descriptiva -> Resumir historial deportivo
- Inferencial -> Predecir desempeño futuro del jugador

> Con frecuencia construimos un caso estadístico con datos imperfectos, como resultado hay numerosas razones por las culaes individuos intelectuales respetables pueden no estar de acuerdo sobre los resultados estadísticos. - Chales Wheelan en su libro Naked Statistics

¿Por qué aprender estadística?

- Resumir grandes cantidades de información
- Tomar mejores decisiones (¿o peores?)
- Responder preguntas con relevancia social
- Reconocer patrones en los datos
- Descubrir a quienes usan estas herramientas con fines nefastos

### Flujo de trabajo en data science

1. Ingesta de datos
2. Validación
3. Preparación
4. Entrenamiento del modelo
5. Evaluación del modelo
6. Modelo en producción
7. Interacción con el usuario final

### Plan del curso

## Estadística descriptiva para analítica

### ¿Cómo usar Deepnote?

[Deepnote](https://deepnote.com/) y su [documentación](https://docs.deepnote.com/)

[¿Qué es Deepnote y cómo utilizarlo en Data Science](https://platzi.com/blog/deepnote/)

### Tipos de datos

Tenemos 2 tipos de datos:

1. Categóricos (género, categoría de película, método de pago) -> ordinal y nominal
2. Numéricos (edad, altura, temperatura) -> discretos y continuos

A la librería Pandas se le conoce también como "El excel de Python"

### Medidas de tendencia central

Las medidas de tendencia central son una manera de resumir información.

- [Media](https://es.wikipedia.org/wiki/Media_(matem%C3%A1ticas))
- [Mediana](https://es.wikipedia.org/wiki/Mediana_(estad%C3%ADstica))
- [Moda o dato que más se repite](https://es.wikipedia.org/wiki/Moda_(estad%C3%ADstica))

También existen:

- [Media ponderada](https://es.wikipedia.org/wiki/Media_ponderada)
- [Media armónica](https://es.wikipedia.org/wiki/Media_arm%C3%B3nica)
- [Media geométrica](https://es.wikipedia.org/wiki/Media_geom%C3%A9trica)

¿Cuándo usar cual?

- La media es susceptible a valores atípicos ⚠️
- La moda no aplica para datos numéricos continuos

### Metáfora de Bill Gates en un bar

Es importante tomar en cuenta los datos que tenemos, un valor muy diferente podría hacer que, por ejemplo, si usaramos la media, no refleje la realidad de la situación.

### Medidas de tendencia central en Python

En esta clase usamos un [histograma](https://es.wikipedia.org/wiki/Histograma)

[Documentación oficial de Pandas](https://pandas.pydata.org/docs/)

Existe una librería de  Python para visualización de datos con enfoque estadístico, su nombre es [Seaborn](https://seaborn.pydata.org/)

### Medidas de dispersión

Las medidas de dispersión son un excelente complemento para las medidas de tendencia central.

- Rango
- Rango intercuartil
- Desviación estándar

[Cómo calcular el Rango Intercuartil- Khan Academy](https://www.youtube.com/watch?v=0tyFxmfQMU8)

### Desviación estándar

- [Artículo de Wikipedia sobre Desviación Estándar](https://es.wikipedia.org/wiki/Desviaci%C3%B3n_t%C3%ADpica)
- [Estadística - Desviación estándar | Khan Academy](https://www.youtube.com/watch?v=7VvdazICUlo)
- [Rango, varianza y desviación estándar como medidas de dispersión | Khan Academy](https://www.youtube.com/watch?v=JjZM6Yq5-n0)
- [Función Gaussiana](https://es.wikipedia.org/wiki/Funci%C3%B3n_gaussiana)
- [Distribución Normal](https://es.wikipedia.org/wiki/Distribuci%C3%B3n_normal)
- [Introducción a la distribución normal](https://www.youtube.com/watch?v=EmU0ZOiO_do)

### Medidas de dispersión en Python

Otra de las librerías de visualización de datos en Python es [matplotlib](https://matplotlib.org/).

Un diagrama que se usa muchísimo con los cuartiles son los [diagramas de caja](https://en.wikipedia.org/wiki/Box_plot) o en inglés Box Plot.

[Vídeo sobre Diagrama de cajas y bigotes | Boxplot](https://www.youtube.com/watch?v=24Uz1mBksL4)

### Exploración visual de los datos

Por un lado tenemos el **bloque analítico**, con ellas están las:

- Medidas de tendencia central
- Medidas de disperción

Y por otro lado tenemos la parte visual, la **estadística descriptiva**, tenemos por ejemplo:

- Histograma
- Diagrama de caja

> Una imagen vale más que 1000 palabras.

[Dataviz project](https://datavizproject.com/) es una página con muchos gráficos visuales explicando para qué tipo de situación usar cada uno.

[from Data to Viz](https://www.data-to-viz.com/) es una página donde encontramos no solo los gráficos y cuándo usarlos, pero también su cógido de implementación en Python y R.

### Diagramas de dispersión en el análisis de datos

El diagrama de dispersión o scatterplot nos muestra la visualización entre 2 variables, para saber si estas están positivamente o negativamente correlacioandas, o puede que no lo estén.
