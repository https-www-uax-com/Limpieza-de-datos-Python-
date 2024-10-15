import pandas as pd
import requests
import json


class LimpiezaDatos:
    def __init__(self, ruta_archivo):
        """
        Inicializa el objeto de limpieza con el archivo de datos.
        """
        self.ruta_archivo = ruta_archivo
        self.df = pd.read_csv(ruta_archivo)
        print(f"Dataset cargado correctamente con: {self.df.shape[0]} filas y {self.df.shape[1]} columnas.")

    def mostrar_informacion_inicial(self):
        """
        Muestra un resumen general del dataset.
        """
        print("\nInformación inicial del dataset:")
        print(self.df.info())
        print("\nValores nulos por columna:")
        print(self.df.isnull().sum())

    def eliminar_columnas_inutiles(self, umbral=0.5):
        """
        Elimina columnas con más del umbral % de valores nulos.
        """
        limite = len(self.df) * umbral
        self.df = self.df.dropna(thresh=limite, axis=1)
        print(f"\nColumnas con más del {umbral * 100}% de valores nulos eliminadas.")

    def eliminar_filas_incompletas(self):
        """
        Elimina filas con valores nulos.
        """
        self.df = self.df.dropna()
        print("\nFilas con valores nulos eliminadas.")

    def manejar_valores_duplicados(self):
        """
        Elimina las filas duplicadas del dataset.
        """
        self.df = self.df.drop_duplicates()
        print("\nFilas duplicadas eliminadas.")

    def normalizar_tipos_datos(self):
        """
        Convierte tipos de datos inconsistentes en columnas.
        """
        for col in self.df.columns:
            if self.df[col].dtype == 'object':
                try:
                    self.df[col] = pd.to_numeric(self.df[col])
                    print(f"Columna '{col}' convertida a numérica.")
                except ValueError:
                    pass

    def rellenar_valores_faltantes(self, metodo="media"):
        """
        Rellena los valores nulos de las columnas numéricas según el metodo seleccionado.
        - "media": Rellena con la media.
        - "mediana": Rellena con la mediana.
        - "moda": Rellena con el valor más frecuente (moda).
        """
        metodos_validos = ["media", "mediana", "moda"]
        if metodo not in metodos_validos:
            raise ValueError(f"El método de rellenado '{metodo}' no es válido. Usa uno de {metodos_validos}.")

        for col in self.df.columns:
            if self.df[col].isnull().sum() > 0:
                if metodo == "media" and pd.api.types.is_numeric_dtype(self.df[col]):
                    self.df[col].fillna(self.df[col].mean(), inplace=True)
                    print(f"Valores nulos en '{col}' rellenados con la media.")
                elif metodo == "mediana" and pd.api.types.is_numeric_dtype(self.df[col]):
                    self.df[col].fillna(self.df[col].median(), inplace=True)
                    print(f"Valores nulos en '{col}' rellenados con la mediana.")
                elif metodo == "moda":
                    self.df[col].fillna(self.df[col].mode()[0], inplace=True)
                    print(f"Valores nulos en '{col}' rellenados con la moda.")

    def renombrar_columnas(self):
        """
        Normaliza los nombres de las columnas, eliminando espacios y convirtiendo a minúsculas.
        """
        self.df.columns = [col.strip().lower().replace(" ", "_") for col in self.df.columns]
        print("\nNombres de columnas normalizados.")

    def exportar_datos(self, ruta_salida):
        """
        Exporta el dataset limpio a un nuevo archivo CSV.
        """
        self.df.to_csv(ruta_salida, index=False)
        print(f"\nDataset limpio exportado a: {ruta_salida}")

    def enviar_datos(self, url):
        """
        Envía los datos a través de la API REST en formato JSON.
        """
        for _, fila in self.df.iterrows():
            # Preparar los datos a enviar
            data = {
                "uspCategory": fila['usp_category'],
                "uspClass": fila['usp_class'],
                "uspDrug": fila['usp_drug'],
                "keggIdDrug": fila['kegg_id_drug'],
                "drugExample": fila['drug_example'],
                "nomenclature": fila['nomenclature']
            }
            headers = {'Content-Type': 'application/json'}

            # Enviar la solicitud POST al backend
            response = requests.post(url, data=json.dumps(data), headers=headers)

            # Verificar el estado de la solicitud
            if response.status_code == 201:
                print(f"Datos enviados exitosamente: {data}")
            else:
                print(f"Error al enviar los datos: {response.status_code} - {response.text}")

    def limpiar(self, umbral_columnas=0.5, metodo_relleno="media"):
        """
        Realiza todo el proceso de limpieza en el dataset.
        """
        self.mostrar_informacion_inicial()
        self.eliminar_columnas_inutiles(umbral_columnas)
        self.eliminar_filas_incompletas()
        self.manejar_valores_duplicados()
        self.normalizar_tipos_datos()
        self.rellenar_valores_faltantes(metodo_relleno)
        self.renombrar_columnas()
        print("\nProceso de limpieza completado.")


if __name__ == '__main__':
    try:
        # Ruta al archivo CSV
        ruta_archivo = 'C:/Users/lopee/OneDrive/Documentos/GitHub/Limpieza-de-datos-Python-/python/dataset/usp_drug_classification.csv'
        ruta_salida = 'C:/Users/lopee/OneDrive/Documentos/GitHub/Limpieza-de-datos-Python-/python/dataset/dataset_limpio.csv'

        # Crear instancia de la clase LimpiezaDatos
        limpiador = LimpiezaDatos(ruta_archivo)

        # Limpiar el dataset
        print("Iniciando proceso de limpieza de datos...")
        limpiador.limpiar(umbral_columnas=0.5, metodo_relleno="media")
        print("Limpieza de datos completada.")

        # Exportar los datos limpios a un nuevo archivo CSV
        print(f"Exportando datos limpios a: {ruta_salida}")
        limpiador.exportar_datos(ruta_salida)
        print("Exportación completada con éxito.")

        # URL del endpoint REST en el backend Spring Boot
        url = 'http://localhost:8080/api/samples'

        # Enviar datos a la API REST
        print("Enviando datos a la API REST...")
        limpiador.enviar_datos(url)

    except FileNotFoundError as fnf_error:
        print(f"Error: Archivo no encontrado - {fnf_error}")

    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")

