CREATE DATABASE IF NOT EXISTS asset_tracker;
USE asset_tracker;

CREATE TABLE IF NOT EXISTS assets (
    asset_id VARCHAR(50) PRIMARY KEY,
    descripcion VARCHAR(255),
    categoria VARCHAR(100),
    fecha_adquisicion DATE,
    costo DECIMAL(15,2),
    ubicacion VARCHAR(100),
    estado VARCHAR(50),
    fecha_mantenimiento DATE,
    años_depreciacion INT
);


SHOW TABLES;
SELECT * FROM assets LIMIT 10;
