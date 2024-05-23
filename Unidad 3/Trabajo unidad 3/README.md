# Sistema de Gestión de Imágenes DICOM en Python


 Bienvenido al tutorial del sistema de Gestión de Imágenes DICOM en Python, donde se abarcará la optimizanción de la gestión de datos, protegiendo la privacidad del paciente y facilitando el análisis de imágenes médicas.
 

------------


 
###### Instrucciones: 
 El tutorial consiste en una serie de pasos para realizar la gestión avanzada de imágenes DICOM, incluyendo la anonimización, organización y conversión a formato NIfTI
 

------------


 
####  Paso 0. Definición del problema.

En el ámbito de la investigación clínica, la gestión de imágenes médicas y su correspondiente metadata es fundamental para garantizar tanto la integridad del proceso investigativo como la privacidad de los pacientes. Las imágenes DICOM, que contienen datos detallados tanto clínicos como personales, requieren un manejo cuidadoso para evitar la divulgación de información identificable.



![image](https://github.com/Mejia2003/InfoII/assets/159477450/ac479e12-f04b-4059-8304-f42df2cf1361)




------------

 
#### Paso 1. Desarrollar el diagrama de clase. 

Para el desarrollo del diagrama de Clases para el Sistema de Gestión de Imágenes DICOM, nos enfocamos en 3 clases diferentes usando la programación orientada a objetos para diseñar clases que encapsulen las funcionalidades necesarias, promoviendo la reutilización del código y la fácil mantenibilidad.

-  Clase Estudio

##### Métodos:
• Cargar estudio DICOM

• Anonimizar estudio

• Convertir a formato NIfTI

• Obtener información del estudio



-  Clase Paciente:

##### Métodos:

• Consultar estudios


• Obtener información del paciente


- Clase SistemaGestion:
##### Atributos 
• Lista paciente
##### Métodos:

• Agregar paciente

• Consultar paciente

• Eliminar paciente

• Buscar estudio por ID de paciente y ID de estudio

• Obtener lista de pacientes

• Agregar estudio 

• Visualizar Imagen 

• Eliminar estudio

Todos los métodos tienen encapsulamiento público.

Para ver el diagrama de clase completo  con sus respectivas relaciones entre las 3 diferentes clases, por favor de click sobre  Diagrama de clase



[![Diagrama de clase]("C:\Users\nidam\OneDrive\Imágenes\Capturas de pantalla\Captura de pantalla 2024-05-21 135154.png" "Diagrama de clase")](https://www.canva.com/design/DAGFo10vH6s/j3GNMKWpQhlk7iqYXqdw8w/edit "Diagrama de clase")


------------



#### Paso 2. Configurar el entorno de trabajo
Prepararemos el entorno de trabajo para garantizar que todas las dependencias estén instaladas y listas para su uso.

Las librerías utilizadas son:




##### Dicom2nifti
Diseñada específicamente para convertir archivos DICOM al formato NIfTI (Neuroimaging Informatics Technology Initiative). NIfTI es otro formato común para almacenar y compartir imágenes médicas, particularmente en la investigación de neuroimagen.

dicom2nifti simplifica el proceso de conversión al:
Manejar adecuadamente los datos de imagen y metadatos DICOM.
Asegurar la orientación y el espaciado de vóxeles correctos en la salida NIfTI.
Ofrecer potencialmente opciones de conversión adicionales (según la versión de la biblioteca).

##### Numpy
Es una librería fundamental para la computación científica en Python. Proporciona soporte para arreglos multidimensionales, junto con una gran colección de funciones matemáticas de alto nivel para operar en estos arreglos. NumPy es eficiente en términos de memoria y computación, y es ampliamente utilizado en el procesamiento de imágenes, el análisis de señales, el álgebra lineal, la simulación y otros campos.

##### Os
Proporciona funciones para interactuar con el sistema operativo. Es un módulo de propósito general que puede ser útil para diversas tareas en un script de procesamiento de imágenes médicas, como:

-Listar archivos y directorios en una ruta específica.
-Crear nuevos directorios.
-Eliminar archivos o directorios.
-Verificar permisos de archivos.
-Acceder a variables de entorno.


##### Pydicom:

Librería para el manejo de archivos DICOM:
Carga y lee archivos DICOM, que son el formato estándar para almacenar imágenes médicas.
Extrae información relevante de los archivos DICOM, como datos del paciente, fecha de adquisición, modalidad de imagen, etc.
Permite manipular y procesar datos de imagen DICOM.


##### Nilearn:

Librería especializada en neuroimagen:
Ofrece herramientas para cargar, preprocesar, analizar y visualizar datos de neuroimagen.
Incluye algoritmos para el análisis de resonancia magnética funcional (fMRI), tomografía por emisión de positrones (PET), etc.
Permite realizar estudios de conectividad cerebral, mapeo de funciones cerebrales y otras tareas de neurociencia.


##### Nilearn.plotting:

Submódulo de nilearn para visualización de neuroimagen:
Proporciona funciones para mostrar imágenes cerebrales 3D o 4D.
Permite personalizar la visualización, como la orientación de la imagen, el rango de valores y la paleta de colores.
Facilita la creación de figuras y gráficos para comunicar resultados de estudios neurocientíficos.

Puedes instalar los requerimientos así:
**python -m pip install pydicom**

------------

#### Paso 3. Inicio del código.

El código se divide en 3 clases, cada una con sus respectivos atributos y métodos.

Para dar inicio al código se empezó por la clase Estudio, la cuál encapsula la información y funcionalidad relacionada con cada estudio médico en el sistema.

La clase Estudio tiene como objetivo gestionar y manipular estudios DICOM. Su constructor inicializa los atributos relacionados con la información del paciente, fecha, modalidad, descripción del estudio, imágenes DICOM y dimensiones de las imágenes.
El método anonimizarEstudio permite anonimizar los estudios, reemplazando o enmascarando la información sensible del paciente en los archivos DICOM de una carpeta específica.

El método visualizarImagenes visualiza las imágenes NIfTI de un estudio, permitiendo elegir diferentes modos de visualización (por ejemplo, ortogonal, en un solo plano, o en mosaico).

El método obtenerInfoEstudio extrae y muestra información relevante de un estudio DICOM, como la fecha de adquisición, modalidad, descripción y dimensiones de la imagen, a partir de los archivos DICOM de una carpeta específica.


------------

#### Paso 4. Punto medio del código.

En este paso es esencial usar la clase paciente, ya que, es el punto medio de nuestro código y en el sistema de gestión de imágenes médicas es responsable de representar a cada paciente y almacenar los estudios asociados a él. 

La clase Paciente tiene como objetivo gestionar la información de los pacientes, incluyendo su ID y nombre. El método obtener_nombres_pacientes recibe una carpeta como argumento y busca archivos dentro de ella para extraer nombres de pacientes a partir de los nombres de archivo. Los nombres se separan por un guión bajo ('_') y se añaden a una lista llamada listaPacientes, mientras que los IDs se añaden a una lista llamada IDpacientes. Si la carpeta está vacía, se muestra un mensaje de error indicando que no hay carpetas de pacientes.

------------

#### Paso 5. Final del código.

Para este paso nos enfocamos en la clase SistemaGestion, esta clase es el núcleo del sistema de gestión de imágenes médicas, encargada de administrar todos los pacientes y sus respectivos estudios.

La clase sistemaGestion se encarga de gestionar el sistema de gestión de pacientes y estudios. Algunos de los métodos importantes incluyen:

•	agregarEstudio: Agrega un estudio DICOM a un paciente existente o crea un nuevo paciente si no existe. Convierte las imágenes DICOM a formato NIfTI y las guarda en las carpetas correspondientes.

•	agregarPacientes: Agrega un nuevo paciente al sistema.

•	consultarPacientes: Consulta si un paciente existe en el sistema.

•	eliminarPaciente: Elimina un paciente del sistema, incluidos sus estudios.

•	buscarEstudio: Busca un estudio de un paciente y muestra la ruta de acceso al estudio DICOM y NIfTI.

•	eliminarEstudio: Elimina un estudio de un paciente.

•	infoEstudio: Obtiene información de un estudio DICOM.

•	visualizar: Permite visualizar estudios NIfTI en diferentes modos (ortogonal, un solo plano, mosaico).

•	anonimizarEstudio: Anonimiza un estudio DICOM, eliminando o enmascarando la información sensible del paciente.

•	listaPacientes: Obtiene una lista de los nombres de los pacientes en el sistema.

La clase utiliza asociación con la clase Estudio y Paciente para acceder a métodos específicos de esas clases. También incluye la definición de atributos como la carpeta de pacientes, nombre, ID del paciente, y las carpetas para los estudios DICOM y NIfTI.


------------

#### Paso 6. Pruebas de funcionalidad.

Realizar pruebas para cada funcionalidad implementada, para asegurar que el sistema funcione correctamente bajo diferentes escenarios.

Para realizar dichas pruebas es indispensable hacer uso de un menú que contenga todas las opcciones de los métodos que se plantearón en cada una de las 3 clase.

###### El menú es el siguiente: 

sistema=sistemaGestion()
while True:

    menu=input('Ingrese la opción a la que desea ingresar:\n1. Agregar paciente\n2. Consultar paciente\n3. Eliminar paciente\n4. Cargar estudio\n5. Buscar estudio\n6. Eliminar estudio\n7. Obtener información del estudio\n8. Visualizar imagen\n9. Obtener lista de pacientes\n10. Anonimizar estudio\n11. Salir')
    
    menu=validar(menu,int)
    
    if menu=='1':
    
        nombre=input('Ingrese el nombre del paciente\n')
        
        nombre=validar(nombre,str)
        
        ID=input('Ingrese el ID del paciente\n')
        
        sistema.agregarPacientes(nombre,ID)
        
    elif menu=='2':
    
        nombre=input('Ingrese el nombre del paciente\n')
        
        nombre=validar(nombre,str)
        
        ID=input('Ingrese el ID del paciente\n')
        
        sistema.consultarPacientes(nombre,ID)
        
    elif menu=='3':
    
        nombre=input('Ingrese el nombre del paciente\n')
        
        nombre=validar(nombre,str)
        
        ID=input('Ingrese el ID del paciente\n')
        
        sistema.eliminarPaciente(nombre,ID)
        
    elif menu=='4':
        carpetaDICOM=input('Ingrese la ruta de la carpeta DICOM que desea cargar\n')
        
        sistema.agregarEstudio(carpetaDICOM)
        
    elif menu=='5':
    
        nombre=input('Ingrese el nombre del paciente\n')
        
        nombre=validar(nombre,str)
        
        ID=input('Ingrese el ID del paciente\n')
        
        sistema.buscarEstudio(nombre,ID)
        
    elif menu=='6':
    
        nombre=input('Ingrese el nombre del paciente\n')
        
        nombre=validar(nombre,str)
        
        ID=input('Ingrese el ID del paciente\n')
        
        sistema.eliminarEstudio(nombre,ID)
        
    elif menu=='7':
    
        carpetaDICOM=input('Ingrese la ruta de la carpeta DICOM que desea cargar\n')

       
        sistema.infoEstudio(carpetaDICOM)
        
    elif menu=='8':
    
        carpetaNifti=input('Ingrese la dirección del estudio NIFTI')
        
        sistema.visualizar(carpetaNifti)
        
    elif menu=='9':
    
        sistema.listaPacientes()
        
    elif menu=='10':
    
        carpetaDICOM=input('Ingrese la ruta de la carpeta DICOM que desea anonimizar\n')
        
        sistema.anonimizarEstudio(carpetaDICOM)
        
    elif menu=='11':
    
        break
        
    else:
    
        print('Opción no válida')
    print('Gracias por utilizar nuestro sistema de gestión.')



Es un menú interactivo para gestionar pacientes y estudios médicos a través de la instancia sistema de la clase sistemaGestion. Ya con dicho menú se hizo mas fácil realizar la prueba para verificar que el código funcionará. El ciclo While donde por teclado se ingresa las opcciones que sean requqeridas, y por medio del llamado de las funciones, las relaciones entre las clases y a los archivos proporcionados previamente permiten que se ejecuten las diversas opcciones del menú.

Es indispensable validar que los valores ingresados por los usuarios.

Para realizar las pruebas de funcionalidad se le brindó al código pedir directamete la dirección de los archivos tanto Dicom como nifti, ya que se consideró que era más simple hacerlo de dicha manera. 

-----------------------------
###### Este sistema de gestión de ímagenes Dicom en PYthon fue realizado por:
Pablo Andres Aristizabal

Alma Olea

Nicole Dayanne Mejia

Laura Alzate 





