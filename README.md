# CSV a Excel

Este script de Python carga un archivo CSV y un archivo Excel de la carpeta actual, asigna los encabezados del archivo Excel al archivo CSV y luego guarda el archivo CSV en un nuevo archivo Excel llamado "ArchivoUnido.xlsx".

## Requisitos

Para ejecutar este script, necesitarás tener instaladas las siguientes bibliotecas de Python:

- pandas
- xlsxwriter
- tqdm

Puedes instalar estas bibliotecas usando `pip` con el siguiente comando:

<code>pip install pandas xlsxwriter tqdm</code>

o instalar mediante los requerimientos del archivo `requirements.txt` con el siguiente comando:

<code> pip install -r requirements.txt</code>


## Uso

Para usar este script, asegúrate de tener un archivo CSV y un archivo Excel en la carpeta actual. El archivo Excel debe contener los encabezados que se asignarán al archivo CSV.

Luego, ejecuta el script con el siguiente comando:

<code>python CSV2ExcelAuto.py</code>


Donde `<CSV2ExcelAuto.py>` es el nombre del archivo que contiene el script.

Después de ejecutar el script, se creará un nuevo archivo Excel llamado "ArchivoUnido.xlsx" que contiene los datos del archivo CSV con los encabezados del archivo Excel.
