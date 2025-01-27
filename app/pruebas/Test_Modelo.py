import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt  # Necesario para guardar la gráfica

def generar_graficas(nombre_archivo_log, nombre_archivo_exp):
    # Crear datos simulados
    np.random.seed(42)
    tamaño = np.random.randint(50, 500, 100)  # Tamaño en m²
    pisos = np.random.randint(1, 20, 100)  # Número de pisos

    precio_logaritmico = 30000 + 2000 * np.log10(tamaño) + 1000 * pisos
    precio_exponencial = 30000 + 2000 * (np.log10(tamaño) ** 2) + 2000 * np.exp(0.05 * pisos)

    df = pd.DataFrame({
        'Tamaño': tamaño,
        'Pisos': pisos,
        'Precio_Log': precio_logaritmico,
        'Precio_Exp': precio_exponencial
    })

    # Crear modelos
    X = df[['Tamaño', 'Pisos']].values
    y_log = df['Precio_Log'].values
    y_exp = df['Precio_Exp'].values

    # Ajustar modelos
    model_log = LinearRegression().fit(X, y_log)
    model_exp = LinearRegression().fit(X, y_exp)
    
    # Predicciones
    pred_log = model_log.predict(X)
    pred_exp = model_exp.predict(X)

    # Evaluar desempeño
    mse_log = mean_squared_error(y_log, pred_log)
    mse_exp = mean_squared_error(y_exp, pred_exp)
    print(f'MSE para modelo logarítmico: {mse_log:.2f}')
    print(f'MSE para modelo exponencial: {mse_exp:.2f}')

    sns.set_theme(style="whitegrid", palette="pastel")

    # Gráfico logarítmico
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=df['Tamaño'], y=y_log, color="skyblue", label="Precio Real Logarítmico")
    sns.lineplot(x=df['Tamaño'], y=pred_log, color="red", label="Predicción Logarítmica")
    plt.title("Modelo Logarítmico de Precios")
    plt.xlabel("Tamaño de la Propiedad (m²)")
    plt.ylabel("Precio Logarítmico")
    plt.legend()
    plt.tight_layout()
    plt.savefig(nombre_archivo_log)  # Guardar gráfica logarítmica
    plt.close()  # Cierra la figura

    # Gráfico exponencial
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=df['Tamaño'], y=y_exp, color="lightgreen", label="Precio Real Exponencial")
    sns.lineplot(x=df['Tamaño'], y=pred_exp, color="orange", label="Predicción Exponencial")
    plt.title("Modelo Exponencial de Precios")
    plt.xlabel("Tamaño de la Propiedad (m²)")
    plt.ylabel("Precio Exponencial")
    plt.legend()
    plt.tight_layout()
    plt.savefig(nombre_archivo_exp)  # Guardar gráfica exponencial
    plt.close()  # Cierra la figura

    print(f"Gráficas guardadas como {nombre_archivo_log} y {nombre_archivo_exp}")
