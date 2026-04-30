import streamlit as st
import pandas as pd
import requests

# Configuración de la página
st.set_page_config(page_title="Gestión de Accidentes de Tránsito - MockAPI", layout="wide")

st.title("🚗 Gestión de Accidentes de Tránsito - MockAPI")
st.markdown("""
### Objetivo
Consumir en tiempo real **300 registros de accidentes de tránsito en Colombia (2023)** desde MockAPI.
Los datos incluyen información sobre ubicación, tipo de accidente, gravedad, participantes y condiciones.
""")

# --- Configuración de la API (MockAPI) ---
MOCK_API_ID = "69f350d4bd2396bf530fbde8"
MOCK_API_BASE_URL = f"https://{MOCK_API_ID}.mockapi.io"

st.info("ℹ️ **Base URL:** " + MOCK_API_BASE_URL)

# --- Botón para Limpiar Caché (En caso de errores de conexión previos) ---
if st.button("🔄 Refrescar Datos (Limpiar Caché)"):
    st.cache_data.clear()
    st.rerun()

# --- Función para obtener datos de MockAPI ---
@st.cache_data
def get_mockapi_data(entity):
    """Probamos primero la ruta directa, si falla probamos con /api/v1"""
    paths_to_try = [
        f"{MOCK_API_BASE_URL}/{entity}",
        f"{MOCK_API_BASE_URL}/api/v1/{entity}"
    ]

    last_error = ""
    for url in paths_to_try:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    return pd.DataFrame(data), None
                else:
                    return pd.DataFrame([data]), None
            else:
                last_error = f"Status {response.status_code} en {url}"
        except Exception as e:
            last_error = f"Error: {e} en {url}"

    return None, last_error

# --- Cargar Datos desde MockAPI ---
with st.spinner("Conectando con MockAPI..."):
    df_reportes, error_r = get_mockapi_data("reportes")

# --- Verificar estado de conexión ---
if df_reportes is None or df_reportes.empty:
    st.error("❌ No se puede conectar a MockAPI")
    st.warning(f"**Error:** {error_r}")
    
    st.info("""
    ### 📋 Para activar esta página:
    
    **Pasos en MockAPI:**
    1. Crea tabla: **`reportes`**
    2. Agrega los 19 campos (Ciudad, Tipo_Accidente, Gravedad, etc.)
    3. Importa tu CSV: **`Desarrollos_de_software_20260319.csv`** (300 registros)
    4. Haz click en **"🔄 Refrescar Datos"**
    
    ### 🔗 URL esperada:
    - `https://69f350d4bd2396bf530fbde8.mockapi.io/reportes`
    """)
    st.stop()
else:
    st.success("✅ Conectado a MockAPI exitosamente")

# --- Sección 1: Gestión de Reportes de Accidentes ---
st.divider()
st.header("📋 Reportes de Accidentes de Tránsito")
st.markdown("Análisis de 300 accidentes registrados en Colombia durante 2023")

if df_reportes is not None and not df_reportes.empty:
    # Filtros
    col_f1, col_f2, col_f3, col_f4 = st.columns(4)

    with col_f1:
        ciudades = ["Todas"] + sorted(df_reportes["Ciudad"].unique().tolist())
        sel_ciudad = st.selectbox("Ciudad:", ciudades, key="sel_ciudad")

    with col_f2:
        tipos_acc = ["Todos"] + sorted(df_reportes["tipo_accidente"].unique().tolist())
        sel_tipo = st.selectbox("Tipo de Accidente:", tipos_acc, key="sel_tipo")

    with col_f3:
        gravedades = ["Todas"] + sorted(df_reportes["Gravedad"].unique().tolist())
        sel_gravedad = st.selectbox("Gravedad:", gravedades, key="sel_gravedad")

    with col_f4:
        climas = ["Todos"] + sorted(df_reportes["clima"].unique().tolist())
        sel_clima = st.selectbox("Clima:", climas, key="sel_clima")

    # Aplicar filtros
    df_filtrado = df_reportes.copy()
    if sel_ciudad != "Todas":
        df_filtrado = df_filtrado[df_filtrado["Ciudad"] == sel_ciudad]
    if sel_tipo != "Todos":
        df_filtrado = df_filtrado[df_filtrado["tipo_accidente"] == sel_tipo]
    if sel_gravedad != "Todas":
        df_filtrado = df_filtrado[df_filtrado["Gravedad"] == sel_gravedad]
    if sel_clima != "Todos":
        df_filtrado = df_filtrado[df_filtrado["clima"] == sel_clima]

    # Métricas principales
    st.divider()
    st.subheader("📊 Métricas")

    col_m1, col_m2, col_m3, col_m4, col_m5 = st.columns(5)

    with col_m1:
        st.metric("Total Registros", len(df_filtrado))
    with col_m2:
        st.metric("Heridos", int(df_filtrado["Heridos"].sum()))
    with col_m3:
        st.metric("Muertos", int(df_filtrado["Muertos"].sum()))
    with col_m4:
        edad_prom = df_filtrado["Edad_Conductor"].mean()
        st.metric("Edad Prom. Conductor", f"{edad_prom:.1f} años")
    with col_m5:
        vel_prom = df_filtrado["Velocidad_Aprox"].mean()
        st.metric("Velocidad Prom.", f"{vel_prom:.0f} km/h")

    # Tabla
    st.divider()
    with st.expander(f"📋 Ver Tabla ({len(df_filtrado)} filas)"):
        st.dataframe(df_filtrado, use_container_width=True, height=400)

    # Descargar
    csv = df_filtrado.to_csv(index=False)
    st.download_button(
        label="📥 Descargar CSV",
        data=csv,
        file_name="accidentes_filtrados.csv",
        mime="text/csv"
    )
else:
    st.info("⏳ Esperando datos de 'reportes'...")

# --- Información Técnica ---
st.divider()
st.subheader("ℹ️ Información Técnica")

st.markdown(f"""
**Detalles de MockAPI:**
- **Base URL:** `https://69f350d4bd2396bf530fbde8.mockapi.io`
- **Entidad:** `/reportes`
- **Total de Registros:** {len(df_reportes)}
- **Período:** 2023

**Campos del CSV:**
ID, Fecha, Hora, Ciudad, Departamento, Tipo_Accidente, Gravedad, Clima, 
Iluminacion, Tipo_Via, Condicion_Via, Vehiculos_Involucrados, Heridos, Muertos,
Edad_Conductor, Genero_Conductor, Alcohol, Velocidad_Aprox
""")
