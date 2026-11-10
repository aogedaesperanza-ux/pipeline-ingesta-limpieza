import pandas as pd

def extraer_datos(url_csv: str) -> pd.DataFrame:
    """
    Lee un dataset CSV desde una fuente pública y optimiza los tipos de datos
    para reducir el consumo de memoria RAM.
    """
    print("1. Extrayendo datos...")
    df = pd.read_csv(url_csv)
    
    # Optimizamos memoria convirtiendo columnas de texto repetitivo a 'category'
    for col in df.select_dtypes(include=['object']).columns:
        if df[col].nunique() / len(df) < 0.5:
            df[col] = df[col].astype('category')
            
    return df

def transformar_datos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia el dataset: normaliza nombres de columnas, elimina duplicados
    y gestiona valores nulos de forma justificada.
    """
    print("2. Transformando y limpiando datos...")
    df_limpio = df.copy()
    
    # Normalizamos nombres de columnas (minúsculas y sin espacios)
    df_limpio.columns = (
        df_limpio.columns.str.strip()
        .str.lower()
        .str.replace(' ', '_')
    )
    
    # Eliminamos filas exactamente duplicadas
    filas_antes = len(df_limpio)
    df_limpio = df_limpio.drop_duplicates()
    print(f"   -> Duplicados eliminados: {filas_antes - len(df_limpio)}")
    
    # Gestión de valores nulos:
    # - Numéricos: imputamos con la mediana (robusta frente a valores extremos)
    for col in df_limpio.select_dtypes(include=['number']).columns:
        if df_limpio[col].isnull().sum() > 0:
            df_limpio[col] = df_limpio[col].fillna(df_limpio[col].median())
            
    # - Categóricos/Texto: imputamos con la moda (valor más frecuente)
    for col in df_limpio.select_dtypes(include=['category', 'object']).columns:
        if df_limpio[col].isnull().sum() > 0:
            df_limpio[col] = df_limpio[col].fillna(df_limpio[col].mode()[0])
            
    return df_limpio

def cargar_datos(df: pd.DataFrame, ruta_salida: str) -> None:
    """
    Exporta el dataset limpio a formato columnar Parquet.
    """
    print(f"3. Cargando datos procesados en '{ruta_salida}'...")
    df.to_parquet(ruta_salida, engine='pyarrow', index=False)
    print("   -> ¡Carga completada con éxito!")
