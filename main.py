from src.etl_pipeline import extraer_datos, transformar_datos, cargar_datos

def ejecutar_pipeline():
    # Dataset público estándar (Titanic) ideal para probar limpieza de nulos
    url_dataset = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    archivo_salida = "datos_procesados.parquet"
    
    # Ejecución secuencial de las etapas ETL
    df_crudo = extraer_datos(url_dataset)
    df_transformado = transformar_datos(df_crudo)
    cargar_datos(df_transformado, archivo_salida)
    
    print("\nResumen final de datos limpios:")
    print(df_transformado.info())

if __name__ == "__main__":
    ejecutar_pipeline()
