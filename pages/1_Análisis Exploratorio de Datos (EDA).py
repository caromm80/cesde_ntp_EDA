import streamlit as st
import pandas as pd
import os

# Configuración de la página
st.set_page_config(
    page_title="EDA - Creciendo Juntos",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🔍 Análisis Exploratorio de Datos (EDA) - Creciendo Juntos")
st.markdown("""
Tu misión es actuar como un **detective educativo**. A partir de los datos que cargues o descargues de nuestra API Java, 
debes explorar, entender y extraer insights sobre estudiantes, cursos y desempeño académico.
""")

# --- Barra Lateral ---
with st.sidebar:
    st.header("📋 Instrucciones")
    st.info("""
    1. **Carga los datos**: Usa un archivo local o descárgalos desde la API
    2. **Previsualiza**: Observa las primeras filas del dataset
    3. **Inspecciona**: Mira las dimensiones y tipos de datos
    4. **Analiza Calidad**: ¿Faltan muchos datos? ¿Hay inconsistencias?
    5. **Deduce**: Usa las estadísticas para entender patrones educativos
    """)
    st.warning("⚠️ Este análisis se enfoca en exploración de datos sin gráficos complejos.")

# --- 1. Carga de Datos ---
st.header("📂 Carga de Datos")

col_form1, col_form2 = st.columns(2)

# --- Funciones de Carga ---
@st.cache_data
def load_data_from_file(file_path):
    """Carga datos desde ruta local"""
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        st.error(f"Error al cargar {file_path}: {e}")
        return None

@st.cache_data
def load_data_from_upload(file):
    """Carga datos desde archivo subido"""
    try:
        return pd.read_csv(file)
    except Exception as e:
        st.error(f"Error al cargar el archivo: {e}")
        return None

# Buscar archivos CSV en el directorio
csv_files = [f for f in os.listdir(".") if f.endswith(".csv")]

with col_form1:
    if csv_files:
        selected_file = st.selectbox("📁 Selecciona un archivo CSV local:", csv_files)
    else:
        selected_file = None
        st.info("No hay archivos CSV en el directorio actual")

with col_form2:
    uploaded_file = st.file_uploader("⬆️ O sube un archivo CSV:", type="csv")

# Lógica de selección de archivo
df = None
if selected_file:
    df = load_data_from_file(selected_file)
    if df is not None:
        st.success(f"✅ Dataset '{selected_file}' cargado correctamente")
elif uploaded_file is not None:
    df = load_data_from_upload(uploaded_file)
    if df is not None:
        st.success(f"✅ Dataset '{uploaded_file.name}' cargado correctamente")

# --- Análisis del Dataset ---
if df is not None:
    # --- Paso 1: Primer Impacto ---
    st.divider()
    st.header("Paso 1: 👀 Primer Impacto (Vista Previa)")
    st.markdown("Observa las primeras 10 filas. ¿Qué conceptos o patrones clave identificas?")
    st.dataframe(df.head(10), use_container_width=True)
    
    with st.expander("💡 Tips para interpretar"):
        st.markdown("""
        - **Nombres de Columnas:** Son las 'etiquetas' de la información (Ej: si ves 'Fecha', hay datos temporales)
        - **Valores Iniciales:** Muestran el formato (números, texto, fechas)
        - **Identificadores:** Busca columnas como 'ID' que distingan cada registro
        """)

    # --- Paso 2: La Estructura ---
    st.divider()
    st.header("Paso 2: 🏗️ La Estructura del Dataset")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("📊 Total de Filas", df.shape[0])
    with col2:
        st.metric("📋 Total de Columnas", df.shape[1])
    with col3:
        st.metric("📝 Tamaño en MB", f"{df.memory_usage(deep=True).sum() / 1024**2:.2f}")
    
    st.subheader("Tipos de Datos")
    st.write(df.dtypes)
    
    with st.expander("💡 Entendiendo los Tipos de Datos"):
        st.markdown("""
        - **int64 / float64:** Números (permiten sumas, promedios)
        - **object:** Generalmente texto o categorías
        - **datetime64:** Fechas y horas (útil para tendencias)
        """)
    
    # --- Paso 3: Calidad y Vacíos ---
    st.divider()
    st.header("Paso 3: 🔧 Calidad de los Datos")
    
    container_quality = st.container(border=True)
    
    missing_data = df.isnull().sum()
    missing_percent = (df.isnull().sum() / len(df)) * 100
    
    if missing_data.sum() > 0:
        st.subheader("⚠️ Datos Faltantes Detectados")
        
        missing_df = pd.DataFrame({
            'Columna': missing_data.index,
            'Nulos': missing_data.values,
            'Porcentaje': missing_percent.values.round(2)
        })
        missing_df = missing_df[missing_df['Nulos'] > 0].sort_values('Porcentaje', ascending=False)
        
        st.dataframe(missing_df, use_container_width=True)
        
        st.warning("""
        **Pregunta para reflexionar:** ¿Por qué crees que faltan datos en esas columnas específicas? 
        ¿Podría afectar tus conclusiones?
        """)
    else:
        st.success("✨ ¡Este dataset está completo! No hay datos faltantes detectados.")
    
    # --- Paso 4: Estadísticas ---
    st.divider()
    st.header("Paso 4: 📊 Análisis Estadístico")
    
    tab_numeric, tab_text = st.tabs(["📈 Datos Numéricos", "🔠 Datos de Texto"])
    
    with tab_numeric:
        numeric_cols = df.select_dtypes(include=['number']).columns
        if len(numeric_cols) > 0:
            st.subheader("Estadísticas Descriptivas (Números)")
            stats_df = df.describe()
            st.dataframe(stats_df, use_container_width=True)
            
            with st.expander("📖 Guía de Estadísticas"):
                st.markdown("""
                - **Mean (Promedio):** El valor central. ¿Es lo esperado?
                - **Min / Max:** Límites de los datos. Ayuda a detectar errores
                - **Std (Desviación):** Qué tan dispersos están los datos
                - **25%, 50%, 75%:** Cuartiles que muestran la distribución
                """)
        else:
            st.info("No hay columnas numéricas en este dataset")
    
    with tab_text:
        text_cols = df.select_dtypes(exclude=['number']).columns
        if len(text_cols) > 0:
            st.subheader("Estadísticas Descriptivas (Texto/Categorías)")
            
            text_stats = df.describe(include=['object'])
            st.dataframe(text_stats, use_container_width=True)
            
            st.subheader("Valores Más Frecuentes por Categoría")
            for col in text_cols[:5]:  # Mostrar máximo 5 columnas
                freq = df[col].value_counts().head(5)
                with st.expander(f"🔹 {col}"):
                    st.write(freq)
            
            with st.expander("📖 Guía de Categorías"):
                st.markdown("""
                - **Unique:** Cuántas opciones diferentes hay
                - **Top:** El valor más frecuente (Moda)
                - **Freq:** Cuántas veces aparece el valor top
                """)
        else:
            st.info("No hay columnas de texto/categorías en este dataset")

    # --- Resumen de Investigación ---
    st.divider()
    st.header("📝 Resumen de Investigación")
    
    num_cols = df.select_dtypes(include=['number']).columns.tolist()
    cat_cols = df.select_dtypes(exclude=['number']).columns.tolist()
    
    col_summary1, col_summary2 = st.columns(2)
    
    with col_summary1:
        st.subheader("📊 Análisis de Variables")
        st.write(f"""
        - **Variables Numéricas:** {len(num_cols)}
        - **Variables Categóricas:** {len(cat_cols)}
        - **Registros Completos:** {len(df)}
        """)
    
    with col_summary2:
        st.subheader("🎯 Preguntas para Reflexionar")
        st.write("""
        - ¿Cuál es el contexto de estos datos?
        - ¿Qué patrones ves en la distribución?
        - ¿Hay valores atípicos o sorprendentes?
        """)
    
else:
    st.info("📁 Carga o selecciona un archivo CSV para comenzar el análisis")