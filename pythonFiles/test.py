
from db_functions import add_asset, update_asset, delete_asset

if __name__ == "__main__":
    new_asset = {
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
    add_asset(new_asset)
    print("Added asset VH005")

    update_asset("VH005", {"Costo de adquisición": 26000, "Justificación técnica": "Actualización de costo"})
    print("Updated asset VH005")

    delete_asset("VH005")
    print("Deleted asset VH005")
