import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 
from procesamiento import load_excel_data, check_data_quality, calculate_frequencies
from plot import plot_bar_chart, plot_temporal_trends, analyze_changes_vs_failures

def main():
    # Rutas de los archivos
    template_path = r"C:\Users\maxim\Desktop\Data\Template Hidrociclones V1.xlsx"
    data_path = r"C:\Users\maxim\Desktop\Data\Datos hidrociclones v1.xlsx"

    # Cargar los datos
    print("Cargando datos...")
    template_sheets, template_content = load_excel_data(template_path)
    _, data_content = load_excel_data(data_path)

    print("Datos cargados con éxito")

    # Seleccionar hoja de mantención
    mantencion = template_content["Mantencion"]

    # Verificar calidad de datos
    quality_check = check_data_quality(mantencion)
    print("\nCalidad de los Datos en Mantención:")
    print(quality_check)

    # Calcular frecuencias de cambios y fallas
    frecuencia_cambios = calculate_frequencies(mantencion, "¿Se realizo cambio? Si/no")
    print("\nFrecuencia de Cambios en Mantención:")
    print(frecuencia_cambios)

    frecuencia_fallas = calculate_frequencies(mantencion, "Falla")
    print("\nFrecuencia de Fallas en Mantención:")
    print(frecuencia_fallas)

    # Graficar frecuencias de fallas
    plot_bar_chart(
        frecuencia_fallas,
        x_col="Falla",
        y_col="Frecuencia",
        title="Frecuencia de Fallas en Mantención",
        xlabel="Tipo de Falla",
        ylabel="Frecuencia"
    )

    # Graficar tendencias temporales de fallas
    plot_temporal_trends(mantencion, date_col="Fecha", category_col="Falla", top_n=5)

    # Relación entre cambios y fallas
    analyze_changes_vs_failures(mantencion, category_col="Si Apex o Ciclon completo", failure_col="Falla")

    if __name__ == "__main__":
        main()