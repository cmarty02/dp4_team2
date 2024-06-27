
# Data Project: Modelo Predictivo para Clasificar Radiografías

## Descripción del Proyecto

El objetivo de este Data Project es entrenar un modelo predictivo capaz de determinar qué parte del cuerpo ha sido radiografiada. Clasificar una parte del cuerpo a partir de una imagen de rayos X puede parecer algo trivial, pero tenerlo automatizado puede ser clave para todo el sector del aprendizaje profundo en imágenes médicas.

En muchos hospitales, cuando un médico solicita múltiples adquisiciones de imágenes, se crea un número de acceso para cada parte del cuerpo (p. ej., rodilla, tobillo y pierna), pero el registro de las imágenes correspondientes suele ser incorrecto dentro de cada número de acceso.

## Importancia del Proyecto

El registro incorrecto de partes del cuerpo en radiografías es un problema relevante. Si, por ejemplo, se desea extraer un dataset de rodilla utilizando el filtrado de PACS (base de datos donde se almacenan las imágenes médicas en un hospital) mediante la descripción del estudio, a menudo se extraerán imágenes con varias partes del cuerpo. Además, si se crea un modelo para clasificar enfermedades en alguna parte del cuerpo específica, la implementación del modelo en la práctica clínica será casi imposible.

Imagina que se crea un modelo para detectar neumonía en radiografías de tórax. Para implementar ese modelo, debemos asegurarnos de obtener solo radiografías de tórax. De lo contrario, podríamos terminar tratando de diagnosticar una neumonía a partir de una radiografía de cráneo, lo que no tiene ningún sentido.

## Beneficios del Proyecto

- **Automatización:** Ayuda a automatizar la clasificación de radiografías, mejorando la eficiencia en hospitales y centros médicos.
- **Precisión:** Asegura que las imágenes estén correctamente registradas y clasificadas, evitando errores en el diagnóstico y tratamiento.
- **Optimización de Modelos:** Facilita la implementación de modelos específicos de detección de enfermedades al asegurar la correcta clasificación de las imágenes.


# Equipo

Cristian Marty, Andrés Cervera, Eloy Martinez y Lucía Esteve



## Descripción del conjunto de datos

### ¿Qué archivos necesito?

Necesitarás descargar una copia de las imágenes. Encontrarás dos directorios (train y test) que contienen archivos DICOM anonimizados.

También necesitarás las etiquetas de entrenamiento de train.csv y los nombres de los archivos del conjunto de test de sample_submission.csv.

### ¿Cuál es el formato de los datos?

Los datos de entrenamiento se proporcionan como un conjunto de SOPInstanceUIDs y sus etiquetas en csv. Las etiquetas se definen como una columna Target que contiene enteros que se asignan a diferentes partes del cuerpo.

#### Imágenes DICOM

Todas las imágenes proporcionadas están en formato DICOM.

### ¿Qué estoy prediciendo?

En este desafío, los competidores deben predecir la parte del cuerpo a partir de una radiografía.

Debe haber una columna de predicción por imagen, y las etiquetas se representan como números enteros que corresponden cada uno a una parte del cuerpo contenida en el conjunto de datos:

* Abdomen = 0
* Tobillo = 1
* Columna cervical = 2
* Tórax = 3
* Clavículas = 4
* Codo = 5
* Pies = 6
* Dedos = 7
* Antebrazo = 8
* Mano = 9
* Cadera = 10
* Rodilla = 11
* Pierna = 12
* Columna lumbar = 13
* Otros = 14
* Pelvis = 15
* Hombro = 16
* Senos paranasales = 17
* Cráneo = 18
* Muslo = 19
* Columna torácica = 20
* Muñeca = 21

*Nota*: Otros indica si la muestra contiene imágenes no radiográficas que a veces se colocan erróneamente en el sistema PACS como radiografías (por ejemplo, esofagograma, densitometría).

### Archivos

* train.csv - el conjunto de entrenamiento. Contiene el SOPInstanceUID y la información del objetivo.
* sample_submission.csv - un archivo de presentación de muestras en el formato correcto. Contiene SOPInstanceUID para el conjunto de test.

### Columnas

* SOPInstanceUID- Cada SOPInstanceUID corresponde a una imagen única.
* Target - La etiqueta asignada a cada muestra.
