# db_functions.py
from sqlalchemy import create_engine, text
import mysql.connector

import pandas as pd

# Update this with your actual DB name
engine = create_engine("mysql+pymysql://root:Pocholo10@localhost/asset_tracker")

def list_assets():
    query = "SELECT * FROM assets"
    df = pd.read_sql(query, con=engine)
    return df

def add_asset(asset_data):
    """
    Add a new asset.
    asset_data: dict with keys matching table columns, e.g.:
    {
        "ID del vehículo": "VH005",
        "Grupo de Familia": "Transporte",
        "Subfamilia": "Camioneta",
        "Marca/Modelo": "Ford F-150",
        "Año de adquisición": 2024,
        "Costo de adquisición": 25000,
        "Vida útil estimada (años)": 10,
        "Valor residual": 5000,
        "Método de depreciación": "Lineal",
        "Justificación técnica": "Nuevo vehículo para flota",
        "Fecha de revisión": "2024-08-01",
        "Depreciación anual": 2000.0
    }
    """
    with engine.connect() as conn:
        # Use parameterized query to avoid SQL injection
        query = text("""
            INSERT INTO assets 
            (`ID del vehículo`, `Grupo de Familia`, Subfamilia, `Marca/Modelo`,
             `Año de adquisición`, `Costo de adquisición`, `Vida útil estimada (años)`,
             `Valor residual`, `Método de depreciación`, `Justificación técnica`,
             `Fecha de revisión`, `Depreciación anual`)
            VALUES (:id_vehiculo, :grupo, :subfamilia, :marca_modelo, :anio_adq,
                    :costo_adq, :vida_util, :valor_residual, :metodo_dep,
                    :justificacion, :fecha_revision, :depreciacion_anual)
        """)
        conn.execute(query, {
            "id_vehiculo": asset_data["ID del vehículo"],
            "grupo": asset_data["Grupo de Familia"],
            "subfamilia": asset_data["Subfamilia"],
            "marca_modelo": asset_data["Marca/Modelo"],
            "anio_adq": asset_data["Año de adquisición"],
            "costo_adq": asset_data["Costo de adquisición"],
            "vida_util": asset_data["Vida útil estimada (años)"],
            "valor_residual": asset_data["Valor residual"],
            "metodo_dep": asset_data["Método de depreciación"],
            "justificacion": asset_data["Justificación técnica"],
            "fecha_revision": asset_data["Fecha de revisión"],
            "depreciacion_anual": asset_data["Depreciación anual"]
        })
        conn.commit()
    print("Asset added successfully!")

def update_asset(id_vehiculo, update_data):
    """
    Update an asset by ID.
    id_vehiculo: string, asset ID
    update_data: dict with columns to update and new values
    """
    # Map original keys to safe parameter names (replace spaces with _)
    param_keys = {k: k.replace(' ', '_') for k in update_data.keys()}

    # Build set clause with safe param names
    set_clause = ", ".join([f"`{k}` = :{param_keys[k]}" for k in update_data.keys()])

    query = text(f"""
        UPDATE assets
        SET {set_clause}
        WHERE `ID del vehículo` = :id_vehiculo
    """)

    # Build parameters dict with safe keys
    params = {param_keys[k]: v for k, v in update_data.items()}
    params["id_vehiculo"] = id_vehiculo

    with engine.connect() as conn:
        conn.execute(query, params)
        conn.commit()

    print(f"Asset {id_vehiculo} updated successfully!")

def delete_asset(id_vehiculo):
    """
    Delete asset by ID.
    """
    query = text("""
        DELETE FROM assets
        WHERE `ID del vehículo` = :id_vehiculo
    """)
    with engine.connect() as conn:
        conn.execute(query, {"id_vehiculo": id_vehiculo})
        conn.commit()
    print(f"Asset {id_vehiculo} deleted successfully!")

def get_connection():
    return mysql.connector.connect(
        host="localhost",       # or your MySQL server host
        user="root",   # replace with your MySQL username
        password="Pocholo10",  # replace with your MySQL password
        database="asset_tracker"   # replace with your database name
    )
