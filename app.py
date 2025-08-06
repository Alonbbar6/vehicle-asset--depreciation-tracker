import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from dataLoader import load_data
from depreciation import create_all_schedules

# Load and preprocess data
df_assets = load_data()
df_depreciation = create_all_schedules(df_assets)

st.title("💼 Asset Depreciation Dashboard")

# Show all asset IDs
asset_ids = df_depreciation['ID del vehículo'].unique()
selected_id = st.selectbox("Selecciona un ID de vehículo", asset_ids)

# Filter data
df_asset = df_depreciation[df_depreciation['ID del vehículo'] == selected_id]

if df_asset.empty:
    st.warning(f"No se encontró el activo con ID '{selected_id}'")
else:
    st.subheader(f"📉 Depreciación del activo {selected_id}")
    st.dataframe(df_asset)

    # Plot
    fig, ax = plt.subplots()
    ax.plot(df_asset['Año'], df_asset['Valor final'], marker='o')
    ax.set_xlabel("Año")
    ax.set_ylabel("Valor final")
    ax.set_title(f"Depreciación del activo {selected_id}")
    ax.grid(True)
    st.pyplot(fig)


# use in terminal
#  (streamlit run app.py)

