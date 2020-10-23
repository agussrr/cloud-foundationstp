# Diplomatura en Cloud Data Engineering - Módulo Foundations - Trabajo Practico Final

## Objetivo del trabajo

El objetivo de este trabajo fue elegir un dataset y responder algunas preguntas de negocios dado una determinada base de datos. 
Se utilizo un dataset publico obtenido de la plataforma on-line de Kaggle: https://www.kaggle.com/rtatman/lego-database. 
Este contiene las piezas,conjuntos, colores e inventarios LEGO de cada set oficial de la base de datos de Rebrickable. Los archivos están actualizados a julio de 2017. Originalmente se genero este dataset para ayudar a coleccionistas que ya tenian unos sets de LEGO a investigar que piezas se podrian reutilizar para hacer otros sets.

Este dataset ofrece mucho espacio para explorar y responde muchas preguntas que los coleccionistas le interesa saber. Para ellos no es solamente un hobby sino tambien un negocio que puede ser muy rentable. Más adelante explayaremos en algunas preguntas que le pueden ser de mucho interés como por ejemplo: ¿ Si existen algunos colores asociados alguna tematica especifica? o ¿Que tematica tiene mayor sets de LEGO?.

## Contenido del Repositorio

En este repositorio se encuentran todos los archivos necesarios para crear las imagenes de Docker desde la lectura del dataset para luego realizar el ETL (Extract, Transform and Load) a una base de datos Postgres creada. Ademas, se incluyen consultas que pueden agregar valor a los colleccionistas de LEGO.

## Instalacion Previa

Antes de iniciar es necesario tener instalado lo siguiente:

- Token de auntenticacion de la API de Kaggle: https://www.kaggle.com/docs/api. Para facilitar la evaluación del trabajo, hemos incluido un token en este    repositorio. Dicho archivo se llama kaggle.json.
- Docker Engine: https://docs.docker.com/engine/install/
- Docker Compose: https://docs.docker.com/compose/install/

## Instrucciones

Luego de realizar un git clone del repositorio (Para mayor informacion: https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository) ingrese a la carpeta cloud-foundationstp de la siguiente manera:

```
cd cloud-foundationstp
```
A continuacion procederemos a a construir la imagen de Docker que contiene tres contenedores:

1. Base de datos Postgres: Se levanta la imagen oficial de Postgres (https://hub.docker.com/_/postgres). La base de datos se expone con el puerto estandar (5432)   hacia el puerto 5432 del localhost. Ademas, se inicializa con los valores por default:
- Nombre: postgres
- Usuario: postgres
- Password: postgres 

2. Proceso de ETL: Este contenedor realiza el paso de ETL (extract-transform-load) que dejará los data lista para ser consultada. Popula la base de datos con el dataset a elección. Para esto se creo un script de Python para que lea el archivo con los datos crudos, los procese y luego los cargue en la base. 

3. Consultas de negocio: Este contenedor trae consultas del negocio en formato de reporte .csv que se guardan en el directorio del proyecto. Esto se realiza mediante un script de python. 
  
 Dichas consultas agregan valor a los coleccionistas de LEGO de la siguiente manera:
  
### color_theme_rel:
Ayuda a identificar que colores están más asociados a ciertas tematicas. Esto permite a los coleccionistas en enfocarse en terminar sus sets temáticos buscando los colores más relevantes en piezas a reutilizar\
### parentchildrenthem:
Permite a los coleccionistas buscar cuales son las tematicas más grande de LEGO acorde a la relacion tematica padre e hijo (Por ejemplo tematica padre Star Wars, tematica hijo el set del Halcon Milenario). Esto ayuda a los coleccionistas a verificar si tienen todos los LEGOS de una tematica en particular (por ejemplo si tienen todos los LEGOS relacionados a Star Wars\
### themesets:
Facilita a los coleccionistas a buscar cuales son las tematicas que tiene muchos sets de LEGO para armar. Esto posibilita en llevar un conteo al coleccionista si tiene todos los sets de una tematica\ 
### yearsets:
Muestra en que epoca se producieron mayores sets de LEGO. Esto ayuda al coleccionista a valuar los sets que uno tiene dado a los años y la dificultad de conseguir un set de un año especifico.\ 
### Parts_cat:
Ayuda a averiguar cuantas piezas tiene una categoria de piezas. Esto permite saber al coleccionista cuales son las piezas mas dificiles/faciles de reemplazar si se las quiere reutilizar.

Los tres contenedores explicados anteriormente se corren de la siguiente manera:

1. Buildeamos la imagen de los contenedores
```
docker-compose -f docker-compose1.yml build
```
2. Ejecutamos la imagen
```
docker-compose -f docker-compose1.yml up -d
```
## Mejoras
Para las proximas iteraciones considero que se podrian hacer las siguientes mejoras:
* Normalizacion de tablas: Considero que se podria haber hecho mayores normalizaciones a las tablas dadas por el data set para obtener otro tipo de consultas que tambien serian relevantes para el negocio.
* Dado a las dificultades que me genero en realizar el build de la imagen, considero que debo tener una mejor estrategia de logging para poder identificar los problemas mas rapidos.
