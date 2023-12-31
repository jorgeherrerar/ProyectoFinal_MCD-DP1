# Análisis de productos vendidos por medio de e-commerce: Caso de Amazon

### Scraping
Lo primero que se tiene que realizar es el scraping de los productos, para lo cual se está considerando contar con un csv con los ASIN que se van a buscar, además que el lenguaje de programación utilizado será python. Para ello tomamos el csv que cuenta con 26 ASIN correspondientes a televisores de diferentes marcas y para los cuales vamos a buscar los datos que se mencionan en la tabla. 

|ASIN|star_rating|title|review_text|
|---|---|---|---|
|B0CJNQBKX9|5.0 de 5 estrellas|EXCELENTE NITIDEZ Y CALIDAD DE IMAGEN|"Me fascino por la versatilidad"|

Una vez realizado el scraping desde la página oficial de Amazon México, considerando los 25 ASIN que contenía el csv, se obtuvieron un total de 380 registros, los cuales se van a utilizar para los análisis posteriores. 

### NLP

Utilizamos Spacy, una biblioteca de procesamiento de lenguaje natural (NLP, por sus siglas en inglés) usada para realizar tareas relacionadas con el procesamiento y análisis del lenguaje humano.

![image](https://github.com/jorgeherrerar/ProyectoFinal_MCD-DP1/assets/109696745/9f0a8f71-e599-452c-8b1c-06768e4509d5)

Y creamos nubes de palabras con Sustantivos y Adjetivos Representativos por ASIN

![image](https://github.com/jorgeherrerar/ProyectoFinal_MCD-DP1/assets/109696745/44f88a79-75ff-4386-826a-6376b3186f62)


### Análisis de Sentimientos
En el análisis de sentimientos, la polaridad y la subjetividad son dos dimensiones importantes para entender la opinión expresada en un texto. Estos valores son calculados mediante algoritmos de procesamiento de lenguaje natural (NLP) y análisis de sentimientos. Aquí explicamos cómo interpretar estos valores:

Polaridad:

Definición: La polaridad indica la dirección o el tono de la opinión expresada en el texto. Puede ser positiva, negativa o neutra.
Interpretación:
Positiva: Indica que el texto expresa una opinión favorable o positiva hacia el tema.
Negativa: Muestra una opinión desfavorable o negativa hacia el tema.
Neutra: No hay una inclinación clara hacia lo positivo o lo negativo. La opinión es neutral.

![image](https://github.com/jorgeherrerar/ProyectoFinal_MCD-DP1/assets/109696745/44953097-a614-4762-b780-e066aa3f5c3a)



Subjetividad:

Definición: La subjetividad mide el grado de subjetividad u objetividad en el texto. Un valor alto indica subjetividad, mientras que un valor bajo sugiere objetividad.
Interpretación:
Alta subjetividad: El texto está influenciado por las opiniones personales, emociones o juicios subjetivos del autor.
Baja subjetividad: El texto tiende a ser objetivo y basado en hechos más que en opiniones personales.

![image](https://github.com/jorgeherrerar/ProyectoFinal_MCD-DP1/assets/109696745/627b4cdf-a758-4db7-b734-fd74059739ee)


![image](https://github.com/jorgeherrerar/ProyectoFinal_MCD-DP1/assets/109696745/cd0346a0-7297-41c2-b300-51226a27b3dc)



## Conclusión

En este proyecto se realizaron las actividades de: Web Scraping, NPL, Análisis de Sentimientos y  un breve análisis exploratorio de datos con el uso de las librerías: BeautifulSoup, Spacy, TextBlob y Altair respectivamente donde comprobamos que el análisis de sentimiento coincide que los comentarios son mayormente positivos, esto concuerda con que la mayoría de las calificaciones dadas son de 4 y 5 estrellas y que las palabras más representativas de cada ASIN también son positivas. 

![image](https://github.com/jorgeherrerar/ProyectoFinal_MCD-DP1/assets/109696745/e7d3507c-b9ec-4b73-9f49-d4a586f1d862)


## Referencias 
[Numeralia de Amazon](https://vender.amazon.com.mx/sellerblog/amazon-conecta#:~:text=Ciudad%20de%20M%C3%A9xico%2C%2027%20de%20abril%20de%202023.&text=Actualmente%2C%20Amazon%20M%C3%A9xico%20cuenta%20con,57%2C000%20empleos%20directos%20e%20indirectos.)

[PCMI](https://paymentscmi.com/our-services/latin-america-e-commerce-digital-payments-data/?utm_source=Website&utm_medium=AMI+site)

[Americas Market Inteligence](https://americasmi.com/insights/lo-que-mas-compran-los-mexicanos-por-internet/)



# Estructura de repositorio


    ├── LICENSE           <- MIT License.  
    |  
    ├── README.md         <- Main Readme file with the description of the project.  
    |  
    ├── CONTRIBUTING.md   <- Steps yo contribute to the project.  
    |  
    ├── CITATION.md       <- Way to cite the project.  
    |  
    ├── data              <- Original data bases.  
    |  
    ├── doc               <- Archivos de texto.  
    |  
    ├── results           <- Clean and analyzes data bases.  
    |  
    └── src               <- Coding files.  
