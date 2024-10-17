# LINKS

FRONTEND: https://github.com/https-www-uax-com/Frontend_React_Node_.git

BACKEND: https://github.com/https-www-uax-com/Backend_Springboot.git

SCRIPT: https://github.com/https-www-uax-com/Limpieza-de-datos-Python-.git

# PARTICIPANTES

Jaime López Díaz

Juan Manuel Rodriguez

Gwendal Saget

Marcos García Benito Bilbao

# Limpieza de Datos y Envío a API REST

Este proyecto tiene como objetivo limpiar un conjunto de datos CSV y enviarlos a un backend mediante una API REST. La limpieza incluye la eliminación de valores nulos, duplicados, y normalización de datos. Los datos se envían posteriormente a un servidor REST a través de solicitudes HTTP POST.

## Descripción del Proyecto

El script realiza las siguientes tareas:

1. **Carga de Datos**: Carga un archivo CSV que contiene la información de clasificación de medicamentos (USP drug classification).
2. **Limpieza de Datos**: Realiza un proceso de limpieza de datos, incluyendo la eliminación de columnas innecesarias, manejo de valores nulos, normalización de tipos de datos, y eliminación de duplicados.
3. **Exportación de Datos**: Exporta el dataset limpio a un nuevo archivo CSV.
4. **Envío de Datos**: Envía los datos procesados a un servidor backend (implementado en Spring Boot) a través de una API REST.

## Funcionalidades Principales

### 1. Inicialización de la clase `LimpiezaDatos`

El constructor de la clase carga el dataset desde el archivo CSV proporcionado. Muestra el número de filas y columnas del dataset.

### 2. Métodos de Limpieza

- **mostrar_informacion_inicial()**: Muestra la información básica del dataset y la cantidad de valores nulos.
- **eliminar_columnas_inutiles(umbral=0.5)**: Elimina las columnas que tienen un porcentaje de valores nulos mayor que el umbral proporcionado (50% por defecto).
- **eliminar_filas_incompletas()**: Elimina todas las filas que contienen valores nulos.
- **manejar_valores_duplicados()**: Elimina las filas duplicadas en el dataset.
- **normalizar_tipos_datos()**: Intenta convertir todas las columnas de tipo texto que contienen datos numéricos a un tipo numérico.
- **rellenar_valores_faltantes(metodo="media")**: Rellena los valores faltantes en las columnas numéricas usando la media, mediana o moda según lo especificado.
- **renombrar_columnas()**: Renombra las columnas eliminando espacios y convirtiéndolas a minúsculas.

### 3. Exportación de Datos

- **exportar_datos(ruta_salida)**: Exporta el dataset limpio a un archivo CSV en la ruta especificada.

### 4. Envío de Datos a una API REST

- **enviar_datos(url)**: Envía los datos procesados a una API REST en formato JSON. Utiliza la librería `requests` para hacer solicitudes HTTP POST al backend. El script muestra si cada solicitud es exitosa o si ha ocurrido algún error.

### 5. Ejecución General

- **limpiar(umbral_columnas=0.5, metodo_relleno="media")**: Ejecuta todo el proceso de limpieza, eliminando columnas inútiles, filas incompletas, duplicados, normalizando tipos de datos, rellenando valores nulos, y renombrando columnas.

## Requisitos

Para ejecutar el proyecto, asegúrate de tener las siguientes dependencias instaladas:

- Python 3.x
- Pandas
- Requests

Puedes instalar las dependencias usando:

```bash
pip install pandas requests
```
