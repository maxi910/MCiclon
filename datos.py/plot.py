import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np  

# Función para graficar frecuencias como barras
def plot_bar_chart(data, x_col, y_col, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    plt.bar(data[x_col], data[y_col], color="skyblue")
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


# Función para graficar tendencias temporales de fallas
def plot_temporal_trends(df, date_col, category_col, top_n=5):
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    temporal_data = df.groupby([df[date_col].dt.to_period("M"), category_col]).size().unstack(fill_value=0)
    top_categories = temporal_data.sum(axis=0).sort_values(ascending=False).head(top_n).index
    temporal_data_top = temporal_data[top_categories]

    temporal_data_top.plot(figsize=(12, 6), marker='o')
    plt.title("Tendencias Temporales de Fallas Más Frecuentes", fontsize=14)
    plt.xlabel("Fecha (Mes)", fontsize=12)
    plt.ylabel("Frecuencia", fontsize=12)
    plt.legend(title="Tipo de Falla")
    plt.grid(axis='both', linestyle='--', alpha=0.7)
    plt.show()


# Función para analizar la relación entre cambios y fallas
def analyze_changes_vs_failures(df, category_col, failure_col):
    changes_vs_failures = df.groupby(category_col)[failure_col].value_counts().unstack(fill_value=0)
    top_changes = changes_vs_failures.loc[changes_vs_failures.sum(axis=1).sort_values(ascending=False).head(3).index]

    top_changes.plot(kind="bar", stacked=True, figsize=(12, 6), edgecolor="black")
    plt.title("Relación entre Cambios (Apex/Ciclón Completo) y Fallas", fontsize=14)
    plt.xlabel("Tipo de Cambio", fontsize=12)
    plt.ylabel("Frecuencia de Fallas", fontsize=12)
    plt.legend(title="Tipo de Falla")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=0)
    plt.show()
