import streamlit as st
import pandas as pd
import requests
import sys
sys.path.append('..')
from config import get_endpoint_url, get_timeout, API_CONFIG

# Configuración de la página
st.set_page_config(page_title="Creciendo Juntos - Consumo de API", layout="wide")

st.title("🎓 Creciendo Juntos: Consumo de API Java")
st.markdown("""
### Objetivo
Consumir datos en tiempo real desde la API Java del grupo. 
Esta página permite visualizar, filtrar y analizar información sobre estudiantes, cursos y desempeño académico.
""")

# --- Configuración de la API (Java) ---
API_BASE_URL = API_CONFIG["base_url"]
API_TIMEOUT = API_CONFIG["timeout"]

st.info(f"ℹ️ **Base URL API:** `{API_BASE_URL}`")

# --- Sección para configurar la API ---
with st.sidebar:
    st.header("⚙️ Configuración de API")
    
    custom_url = st.text_input(
        "URL Base de la API Java:",
        value=API_BASE_URL,
        help="Ej: http://localhost:8080 o http://tu-servidor.com:8080"
    )
    
    custom_timeout = st.number_input(
        "Timeout (segundos):",
        value=API_TIMEOUT,
        min_value=5,
        max_value=60
    )
    
    st.markdown("**Endpoints Disponibles:**")
    for endpoint_name, endpoint_path in API_CONFIG["endpoints"].items():
        st.write(f"- `{endpoint_name}`: `{endpoint_path}`")

# --- Botón para Limpiar Caché ---
if st.button("🔄 Refrescar Datos (Limpiar Caché)"):
    st.cache_data.clear()
    st.rerun()

# --- Función para obtener datos de API Java ---
@st.cache_data
def get_java_api_data(endpoint_path: str, api_url: str, timeout: int):
    """Consume datos desde la API Java del grupo"""
    url = f"{api_url}{endpoint_path}"
    
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list):
                return pd.DataFrame(data), None
            elif isinstance(data, dict):
                # Si la respuesta es un objeto con una propiedad que contiene el array
                if "data" in data:
                    return pd.DataFrame(data["data"]), None
                else:
                    return pd.DataFrame([data]), None
            else:
                return None, "Formato de respuesta no reconocido"
        else:
            return None, f"Error HTTP {response.status_code}: {response.text[:100]}"
    except requests.exceptions.ConnectionError:
        return None, f"No se puede conectar a {url}. Verifica que la API esté corriendo."
    except requests.exceptions.Timeout:
        return None, f"Timeout: La API tardó más de {timeout} segundos en responder."
    except Exception as e:
        return None, f"Error: {str(e)}"

# --- Selector de Entidad ---
st.divider()
st.header("📊 Selecciona la Entidad a Consultar")

col_entity1, col_entity2, col_entity3 = st.columns(3)

with col_entity1:
    selected_entity = st.radio(
        "Elige una entidad:",
        options=list(API_CONFIG["endpoints"].keys()),
        horizontal=False
    )

# --- Cargar datos de la entidad seleccionada ---
endpoint_path = API_CONFIG["endpoints"][selected_entity]

with st.spinner(f"Conectando a API Java para obtener {selected_entity}..."):
    df_data, error = get_java_api_data(endpoint_path, custom_url, custom_timeout)

# --- Verificar estado de conexión ---
if df_data is None or df_data.empty:
    st.error("❌ No se puede conectar a la API Java")
    st.warning(f"**Error:** {error}")
    
    st.info(f"""
    ### 📋 Para activar esta página:
    
    **Verifica que:**
    1. La API Java esté corriendo en: `{custom_url}`
    2. El endpoint exista: `{custom_url}{endpoint_path}`
    3. La API retorne datos en formato JSON (lista o diccionario)
    4. El timeout sea suficiente (actual: {custom_timeout}s)
    
    **Pasos en tu API Java:**
    - Asegúrate de que el endpoint `{endpoint_path}` esté disponible
    - Retorna los datos en formato JSON
    - Maneja CORS si es necesario
    - Responde dentro del timeout configurado
    """)
    st.stop()
else:
    st.success(f"✅ Conectado exitosamente. Se obtuvieron {len(df_data)} registros de {selected_entity}")

# --- Sección: Visualización de Datos ---
st.divider()
st.header(f"📋 Datos de {selected_entity.title()}")

# Mostrar primeras filas
with st.expander(f"👁️ Preview - Primeras 10 filas"):
    st.dataframe(df_data.head(10), use_container_width=True)

# Métricas básicas
st.subheader("📊 Estadísticas Básicas")
col_m1, col_m2, col_m3, col_m4 = st.columns(4)

with col_m1:
    st.metric("Total Registros", len(df_data))
with col_m2:
    st.metric("Columnas", len(df_data.columns))
with col_m3:
    st.metric("Filas Completas", len(df_data.dropna()))
with col_m4:
    st.metric("Filas con Datos Faltantes", len(df_data) - len(df_data.dropna()))

# Información de columnas
st.subheader("🏗️ Estructura de Datos")
col_desc1, col_desc2 = st.columns(2)

with col_desc1:
    st.write("**Columnas y Tipos:**")
    st.dataframe(pd.DataFrame({
        "Columna": df_data.columns,
        "Tipo": df_data.dtypes.astype(str)
    }), use_container_width=True)

with col_desc2:
    st.write("**Información Faltante:**")
    missing = df_data.isnull().sum()
    st.dataframe(pd.DataFrame({
        "Columna": missing.index,
        "Valores Faltantes": missing.values
    }), use_container_width=True)

# Tabla completa
st.divider()
with st.expander(f"📋 Ver Tabla Completa ({len(df_data)} filas)"):
    st.dataframe(df_data, use_container_width=True, height=400)

# Descargar datos
csv = df_data.to_csv(index=False)
st.download_button(
    label=f"📥 Descargar {selected_entity.title()} como CSV",
    data=csv,
    file_name=f"{selected_entity}_creciendo_juntos.csv",
    mime="text/csv"
)

# --- Información Técnica ---
st.divider()
st.subheader("ℹ️ Información Técnica")

st.markdown(f"""
**Detalles de Conexión:**
- **Base URL:** `{custom_url}`
- **Endpoint:** `{endpoint_path}`
- **URL Completa:** `{custom_url}{endpoint_path}`
- **Total de Registros:** {len(df_data)}
- **Timeout:** {custom_timeout} segundos

**Estructura de Respuesta:**
La API debe retornar un JSON en uno de estos formatos:
- **Lista directa:** `[{{"id": 1, ...}}, {{"id": 2, ...}}]`
- **Objeto con propiedad data:** `{{"data": [{{"id": 1, ...}}, {{"id": 2, ...}}]}}`
""")
