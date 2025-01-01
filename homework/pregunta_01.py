"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.

    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minúsculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
# pylint: disable=import-outside-toplevel
import pandas as pd

def pregunta_01():

#Abrir un archivo
  with open('files/input/clusters_report.txt', 'r', encoding='utf-8') as file:
      data = file.readlines()

#Quitar el salto de línea

  data=[x.replace('\n','') for x in data]

#Operar por cada línea

  lines = []
  for line in data:
      
      #hacer un not para que omita lo que empieza con ---, porque eso no es data para operar
      if not line.startswith('---') and line.strip():
          lines.append(line)         
  lines = [' '.join(line.split()) for line in lines]

#Limpieza de líneas, primero utilizar solo las que inicien con digitos y que empiece después de la línea 2  
  separated_lines =[]
  current_line = ''
  for line in lines [2:]:
      line = line.strip()
      if line [0].isdigit():
          if current_line:
              separated_lines.append(current_line)
          current_line = line
      else:
          current_line += ' ' + line
  if current_line:
      separated_lines.append(current_line)

#Agrupar la data por cada tipo de línea, col 1 es un dígito del 1 al 13, col2 es un número de más de dos digitos, 
# col3 es un porcentaje, primero como string luego reemplazamos los símbolos para interpretación y la col 4 son 
# textos separados por coma.

  data_extracted = []

  for line in separated_lines:
      parts = line.split()

      cluster = int(parts[0])
      quantity = int(parts[1])
      percentage_str = parts[2].replace(',','.')
      percentage = float(percentage_str.replace("%", ""))
      keywords = ' '.join(parts[3:]).strip()
      keywords = keywords.replace('%', '').strip()
      keywords = ', '.join([keyword.strip() for keyword in keywords.split(',')])
      keywords = keywords.replace('.', '')

#Agrupar los datos en una sola estructura
      data_extracted.append({
          'cluster': cluster,
          'cantidad_de_palabras_clave': quantity,
          'porcentaje_de_palabras_clave': percentage,
          'principales_palabras_clave': keywords
      })

#Crear un nuevo data frame con lo recolectado
  df = pd.DataFrame(data_extracted)
  return df

