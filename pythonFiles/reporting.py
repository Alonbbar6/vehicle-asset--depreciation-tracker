import pandas as pd
import matplotlib.pyplot as plt
from pythonFiles.dataLoader import load_data

# Step 1: Load the data
try:
    df = load_data()
    print("✅ Datos cargados exitosamente.")
except Exception as e:
    print(f"❌ Error al cargar los datos: {e}")
    exit()

# Step 2: Show available columns (in Spanish)
print("\n📊 Columnas disponibles:")
print(df.columns.tolist())

# Step 3: Analyze asset counts by a selected Spanish column
columna_analisis = input("📝 Escriba el nombre de la columna a analizar: ")
  # You can change this to another column

if columna_analisis in df.columns:
    try:
        conteo = df[columna_analisis].value_counts()
        print(f"\nActivos por '{columna_analisis}':")
        print(conteo)

        # Step 4: Plot
        conteo.plot(kind='bar', title=f'Cantidad de Activos por {columna_analisis}')
        plt.xlabel(columna_analisis)
        plt.ylabel('Cantidad')
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"❌ Error al graficar '{columna_analisis}': {e}")
else:
    print(f"❌ La columna '{columna_analisis}' no existe en el DataFrame.")


# run this line
# cd /Users/user/Desktop/Zoilas_project
# python3 -m pythonFiles.reporting
