# Instrucciones para correr el scrapper

## inputs

El scrapper contempla que tienes un archivo csv con lo números de ASIN (Amazon Standard Identification Number) de los productos que quieres consultar. De no saberlos puedes obtenerlos de la página del producto, ya sea en la información adicional de este

<img src="https://github.com/jorgeherrerar/ProyectoFinal_MCD-DP1/blob/main/doc/images/asin_info.png" alt="asin_info" width="500"/>

O desde la URL

<img src="https://github.com/jorgeherrerar/ProyectoFinal_MCD-DP1/blob/main/doc/images/asin_url.png" alt="asin_url" width="500"/>

Estos ASIN deben guardarse dentro de la carpeta data en un archivo csv llamado "ASINS.csv" con la siguiente estructura:

|ASIN|
|---|
|B0CJNQBKX9|
|B0C47PZ6HR|
|B08TVSM195|

*Se recomienda que los productos a consultar sean vendidos por amazon méxico, ya que si los vende Amazon Estados Unidos este scrapper no obtiene los ratings ni el texto del review

Para correr el scrapper se debe ejecutar el archivo 'src/resenas/scrapper_resenas.py', este archivo esta confiogurado para obtener un máximo de 5 páginas de reseñas por producto, basta con cambiar el valor de la variable *max_pages_per_asin* para omitir esta limitante, al ejecutar este archivo se guardarán los resultados en un archivo csv '/results/all_amazon_reviews.csv' con la siguiente estructura:

|asin|star_rating|title|review_text|
|---|---|---|---|
|B0CJNQBKX9|5.0 de 5 estrellas|EXCELENTE NITIDEZ Y CALIDAD DE IMAGEN|"Me fascino por la versatilidad"|
