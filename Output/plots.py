import sys
import os
import matplotlib.pyplot as plt

# Add the parent directory to sys.path so Python can find your modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import your modules
try:
    from depreciation import create_all_schedules
    from dataLoader import load_data
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Make sure your PYTHONPATH includes your project folder or check sys.path modifications.")
    sys.exit(1)

# Load asset data
df_assets = load_data()
df_depreciation = create_all_schedules(df_assets)

# Ask user for asset ID
asset_id = input("Ingrese el ID del vehículo para graficar su depreciación: ").strip()

# Filter depreciation data for the input asset ID (case-insensitive)
df_asset = df_depreciation[df_depreciation['ID del vehículo'].str.lower() == asset_id.lower()]

if df_asset.empty:
    print(f"No se encontró el activo con ID '{asset_id}'.")
    sys.exit(1)

# Plot depreciation schedule
plt.plot(df_asset['Año'], df_asset['Valor final'], marker='o')
plt.title(f'Depreciación del activo {asset_id}')
plt.xlabel('Año')
plt.ylabel('Valor final')
plt.grid(True)
plt.tight_layout()
plt.show()
