## Trabajando colaborativamente en git

1. Hacer un `git pull`, esto copiará los cambios de nube a local
2. Escribir sus cambios
3. Hacer un `git add .` para agregar los cambios en local
3. Hacer un `git commit -m 'comentario'` para generar un commit con los cambios
4. Hacer un `git push` para enviar el commit de local a la nube

# Estructura de repositorio

El objetivo de este repositorio es implementar las buenas prácticas de acuerdo al paper ["Good Enough Practices in Scientific Computing"](https://arxiv.org/abs/1609.00037) por Greg Wilson, Jennifer Bryan, Karen Cranston, Justin Kitzes, Lex Nederbragt, Tracy K. Teal.

La estructura que queremos que tenga este repositorio es la siguiente:

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
