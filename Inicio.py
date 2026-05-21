import streamlit as st
from config import PROJECT_INFO, API_CONFIG

# Configuración de la página
st.set_page_config(
    page_title="Creciendo Juntos - Plataforma Educativa",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Estilo Personalizado (Opcional) ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stAlert {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Título Principal ---
st.title("🎓 Creciendo Juntos: Plataforma Educativa")
st.subheader("Transformando la Educación a través de Analítica de Datos")

st.divider()

# --- 1. Introducción ---
col1, col2 = st.columns([2, 1])

with col1:
    st.header("📖 Introducción")
    st.write("""
    **Creciendo Juntos** es una plataforma educativa que integra analítica de datos para mejorar continuamente la experiencia de aprendizaje. 
    A través de este tablero interactivo, exploraremos cómo la ciencia de datos puede revelar patrones en el desempeño estudiantil, 
    identificar oportunidades de mejora y personalizar estrategias educativas.
    
    Nuestro enfoque se centra en la **Exploración de Datos (EDA)**, análisis de inscripciones, calificaciones y progreso académico 
    para generar conocimiento accionable que optimice procesos educativos.
    """)

with col2:
    st.info("💡 **Dato Curioso:** Instituciones que utilizan analítica de datos mejoran el rendimiento estudiantil en un promedio del 15-20%.")

# --- 2. Objetivos ---
st.header("🎯 Objetivos de Creciendo Juntos")

obj_gen, obj_esp = st.columns(2)

with obj_gen:
    st.subheader("Objetivo General")
    st.markdown("""
    - Crear un sistema integral de analítica educativa que permita visualizar, analizar y mejorar continuamente los procesos de enseñanza-aprendizaje a través de datos.
    """)

with obj_esp:
    st.subheader("Objetivos Específicos")
    st.markdown("""
    - Integrar datos desde API Java para monitorear estudiantes, cursos y desempeño académico.
    - Identificar patrones en rendimiento académico y deserción estudiantil.
    - Personalizar recomendaciones educativas basadas en datos.
    - Generar reportes actionables para docentes y administradores.
    """)

st.divider()

# --- 3. Equipo de Trabajo ---
st.header("👥 Equipo de Trabajo")

# Puedes ajustar los nombres aquí
integrantes = [
    {"nombre": "Integrante 1", "rol": "Líder de Proyecto", "emoji": "👨‍💻"},
    {"nombre": "Integrante 2", "rol": "Desarrollo Backend (Java)", "emoji": "👩‍💻"},
    {"nombre": "Integrante 3", "rol": "Analítica de Datos", "emoji": "👨‍🔬"},
]

cols = st.columns(len(integrantes))

for i, persona in enumerate(integrantes):
    with cols[i]:
        st.markdown(f"""
        ### {persona['emoji']} {persona['nombre']}
        **Roles:** {persona['rol']}
        """)

st.divider()

# --- 4. Características del Proyecto ---
st.header("✨ Características Principales")

feat_col1, feat_col2, feat_col3 = st.columns(3)

with feat_col1:
    st.markdown("### 📊 Análisis Exploratorio (EDA)")
    st.write("Herramienta interactiva para explorar datos educativos con estadísticas detalladas, análisis de calidad y detección de patrones.")

with feat_col2:
    st.markdown("### 🔌 Integración API Java")
    st.write("Conexión en tiempo real con la API Java del grupo para consumir datos de estudiantes, cursos y calificaciones.")

with feat_col3:
    st.markdown("### 📈 Generación de Reportes")
    st.write("Reportes interactivos sobre desempeño académico, inscripciones y progreso estudiantil en formato exportable.")

st.divider()

# --- 5. Tecnologías Utilizadas ---
st.header("🛠️ Tecnologías Utilizadas")

tech_col1, tech_col2, tech_col3, tech_col4 = st.columns(4)

with tech_col1:
    st.markdown("### 🐍 Python")
    st.write("Procesamiento de datos y análisis.")

with tech_col2:
    st.markdown("### 🎈 Streamlit")
    st.write("Interfaz web interactiva.")

with tech_col3:
    st.markdown("### ☕ Java API")
    st.write("Backend del grupo.")

with tech_col4:
    st.markdown("### 🐼 Pandas")
    st.write("Análisis de datos.")

st.divider()

# --- 6. Navegación ---
st.header("🗺️ Guía de Navegación")

nav_col1, nav_col2 = st.columns(2)

with nav_col1:
    st.markdown("""
    #### 📋 Secciones Disponibles:
    1. **Análisis Exploratorio de Datos (EDA)**
       - Carga de datasets CSV
       - Estadísticas descriptivas
       - Análisis de calidad
    """)

with nav_col2:
    st.markdown("""
    2. **Consumo de API**
       - Conexión a API Java
       - Datos de estudiantes, cursos y calificaciones
       - Análisis en tiempo real
    
    3. **Resultados del Análisis**
       - Documentación de hallazgos
       - Generación de reportes
    """)

st.divider()

# --- Pie de página ---
st.sidebar.success("👈 Usa el menú lateral para navegar entre las secciones del proyecto.")
st.sidebar.markdown("---")
st.sidebar.write("© 2026 - Creciendo Juntos | Plataforma Educativa")

