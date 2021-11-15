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

## Estadística de la ingesta de datos

### Pipelines de procesamiento para variables numéricas

Escalamiento lineal

[PDF de La técnica de escalamiento lineal por intervalos: una propuesta de estandarización aplicada a la medición de niveles de bienestar social](https://www.upo.es/revistas/index.php/RevMetCuant/article/view/2691/2147)

¿Por qué usarlo? -> Porque los modelos de machine learning son eficientes en el rango [-1, 1].

¿Hay diferentes tipos? -> maxmin, Clipping, Z-score, Winsorizing, más información en la [Documentación de Normalization de Google Developers](https://developers.google.com/machine-learning/data-prep/transform/normalization?hl=id)

¿Cuándo usarlos? -> cuando tenemos data simétrica o uniformemente distribuida

Fórmula usando el escalamiento de min-max -> Tenemos X y debemos llegar a Xs, entonces: Xs = (2X - min - max) / (max- min)

> Un escalamiento lineal es una función lineal que simplemente transforma unos números en otros

### Transformación no lineal

Para recordar, los métodos de *escalamientos lineales* se suelen usar con datós que están distribuidos de forma simétrica.

¿Qué hacer si los datos no están distribudos de forma simétrica?

1. Tomo un problema que no sé cómo resolver (datos sesgados no uniformes)
2. Lo transformo en un problema que ya sé cómo resolver (les aplico la función lineal para uniformarlos)

Transformación no lineal

¿Por qué usarlos? -> Datos fuertemente sesgados, no simétricos

¿Hay diferentes tipos? -> Logarítmicos, sigmoides, polinomiales (grado 2 para arriba), etc

¿Cuándo usarlos? -> ¡Antes de escalamientos lineales!

Esto al final del día viene muy de la mano con la [Geometría Análítica](https://www.youtube.com/playlist?list=PL9SnRnlzoyX2ksvCQ2e3_uIB5SxhnpbyF) y también estamos hablando del [Escalado](https://es.wikipedia.org/wiki/Escalado_(geometr%C3%ADa))

### Procesamiento de datos numéricos en Python

Para recordar:

- [Numpy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [Seaborn](https://seaborn.pydata.org/)

### Pipelines de procesamiento para variables categóricas

Cuando se tiene variables categóricas se hace un mapeo numérico. Para eso hay 2 métodos, de manera que sean fácilmente interpretables en modelos de machine learning:

- Dummy
	- Representación compacta
	- Mejor inputs linealmente independientes
- One-hot
	- Permite describir categorías no incluidas inicialmente

Ambos siguen la cateroría de que tienes que mapear numéricamente las categorías.

### Procesamiento para variables categóricas con Python

¿Podemos tratar a las variables numéricas como categóricas? Claro que sí. Todo depende del contexto y del proyecto.

En el mundo de ciencia de datos, es muy común usar el modo 'one-hot', puesto que 'dummy' ni siquiera existe en las librerías de Python.

La desventaja del one-hot es que cada elemento de los vectores que resultan es como si fueran nuevas variables. Esto aumenta demasiado la dimensionalidad de nuestro dataset y se vea afectado en el rendimiento.

[One Hot Encoding](https://interactivechaos.com/es/manual/tutorial-de-machine-learning/one-hot-encoding)

### Correlaciones

[Coeficiente de correlación en Youtube](https://www.youtube.com/watch?v=aKsjilxc5ww)

[Desigualdad de Cauchy-Bunyakovsky-Schwarz](https://es.wikipedia.org/wiki/Desigualdad_de_Cauchy-Bunyakovsky-Schwarz)

### Matriz de covarianza

La matriz de covarianza es muy importante para hacer un análisis exploratorio de datos y ver qué tan correlacionadas están las distintas variables que tenemos (porque seguramente no van a ser solamente 2).

## Proyecto de aplicación

### Cálculo de valores propios de una matriz

[Artículo en Platzi](https://platzi.com/clases/2353-estadistica-descriptiva/39056-calculo-de-valores-propios-de-una-matriz/)

### PCA: análisis de componentes principales

[StatQuest: Principal Component Analysis (PCA), Step by step](https://www.youtube.com/watch?v=FgakZw6K1QQ)

### Reducción de dimensionalidad con PCA

[Link para el proyecto en DeepNote](https://deepnote.com/project/curso-estadistica-descriptiva-2021-Duplicate-S8kixU3FS0ydDgs7SH6ZZg/%2Fplatzi-curso-estadistica-descriptiva-2021%2F%5Bclase-22%5DPCA.ipynb)

[Apuntes del curso desde DeepNote](https://deepnote.com/@anthonymanotoa/Apuntes-de-Estadistica-Descriptiva-z6iCtsB_Q_6ZARwuRxzhIA)
