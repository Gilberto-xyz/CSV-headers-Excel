from tqdm import tqdm
import pandas as pd
import xlsxwriter
import os

# Cargar el archivo CSV
# Buscar cualquiera de los archivos CSV o Excel que se encuentran en la carpeta actual
documentos = os.listdir()
docs_csv = [doc for doc in documentos if doc.endswith('.csv')] # Si termina en .csv, en automatico lo tomamos como el archivo a leer
docs_excel = [doc for doc in documentos if doc.endswith('.xlsx')] # Si termina en .xlsx, en automatico lo tomamos como el archivo a leer con los headers

archivo_csv = pd.read_csv(docs_csv[0], header=None) # Cargar el primer archivo CSV encontrado
archivo_excel = pd.read_excel(docs_excel[0]) # Cargar el primer archivo Excel encontrado
encabezados = list(archivo_excel.columns) # Obtener los encabezados del archivo Excel

archivo_csv.columns = encabezados# Asignar los encabezados al archivo CSV

writer = pd.ExcelWriter('ArchivoUnido.xlsx', engine='xlsxwriter', options={'use_zip64': True}) # Crear el archivo Excel 
archivo_csv.to_excel(writer, index=False) # Guardar el archivo CSV en el archivo Excel
writer.save() # Guardar el archivo Excel
