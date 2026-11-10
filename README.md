# Pre-entrega: Construcción de un Pipeline de Ingesta y Limpieza (ETL)

## Descripción del Proyecto
Pipeline modular en Python diseñado para automatizar la extracción, limpieza, transformación y carga (ETL) de datos tabulares utilizando **Pandas** y **PyArrow**, optimizando el uso de memoria y almacenamiento para flujos de Machine Learning.

## Estructura del Repositorio
```text
├── src/
│   └── etl_pipeline.py       # Módulo con las funciones de extracción, limpieza y carga
├── main.py                   # Script principal de ejecución del pipeline
├── datos_procesados.parquet  # Archivo de salida optimizado
├── requirements.txt          # Dependencias del proyecto
├── .gitignore                # Exclusión de datasets crudos pesados (*.csv) y caché
└── README.md                 # Documentación técnica