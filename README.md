# Análisis de productos vendidos por medio de e-commerce: Caso de Amazon

## Introducción

En los últimos años el comercio electrónico se ha vuelto el canal de compra preferido por millones de personas, desde comprar el super hasta automóviles, tal es el caso que en México para el año 2022 el valor de este tipo de comercio superaba los 33.000 millones de dólares, siendo el segundo más importante a nivel mundial solo por encima de Brasil. 

Según datos de Amazon, en abril del 2023 contaba con casi 18 mil vendedores independientes, de los cuales 99 % eran PyMes, las que tienen un estimado de 3 millones de productos en venta en esta plataforma. Por ello este análisis se centra en la manera en que una empresa o PyMe, puede revisar el título, calificación y comentarios de sus productos por medio de web scraping, y análisis de lenguaje natural. 

## Desarrollo

Para poder comenzar con  el análisis de los productos, primero hay que identificar el ASIN (Amazon Standard Identification Number) de este, por lo general cada empresa ya cuenta con su listado de ASIN proporcionado por Amazón para cada producto que se encuentra en  venta en su plataforma, de no contar con él, puede ser consultado en la página de cada uno de los productos en el apartado de descripción del mismo (como se muestra en la imagen). 

![image](https://github.com/jorgeherrerar/ProyectoFinal_MCD-DP1/assets/109696745/847e6b86-211e-490b-aaae-0e01fa9db911)


Lo primero que se tiene que realizar es el scraping de los productos, para lo cual se está considerando contar con un csv con los ASIN que se van a buscar, además que el lenguaje de programación utilizado será python. Para ello tomamos el csv que cuenta con 26 ASIN correspondientes a televisores de diferentes marcas y para los cuales vamos a buscar los datos que se mencionan en la tabla. 

|asin|star_rating|title|review_text|
|---|---|---|---|
|B0CJNQBKX9|5.0 de 5 estrellas|EXCELENTE NITIDEZ Y CALIDAD DE IMAGEN|"Me fascino por la versatilidad"|




### Análisis de Dentimientos
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


#



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
