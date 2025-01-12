import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 

# Función para cargar los datos desde un archivo Excel
def load_excel_data(file_path):
    excel_file = pd.ExcelFile(file_path)
    sheets_content = {sheet: excel_file.parse(sheet) for sheet in excel_file.sheet_names}
    return excel_file.sheet_names, sheets_content


# Función para verificar la calidad de los datos
def check_data_quality(df):
    quality_check = df.isnull().sum().reset_index()
    quality_check.columns = ["Columna", "Valores Nulos"]
    quality_check["Porcentaje Nulos"] = (quality_check["Valores Nulos"] / len(df)) * 100
    return quality_check


# Función para calcular las frecuencias de una columna
def calculate_frequencies(df, column_name, fill_na_value="Sin Especificar"):
    frequencies = df[column_name].value_counts(dropna=False).reset_index()
    frequencies.columns = [column_name, "Frecuencia"]
    frequencies[column_name] = frequencies[column_name].fillna(fill_na_value)
    frequencies = frequencies.sort_values(by="Frecuencia", ascending=False)
    return frequencies
