import streamlit as st
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="Resultados - Creciendo Juntos",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Resultados del Análisis: Creciendo Juntos")
st.markdown("""
### Instrucciones
Utiliza esta página para documentar tus hallazgos observados en el **Análisis Exploratorio de Datos**. 
Completa cada sección de forma clara y concisa para generar tu reporte de análisis educativo.
""")

st.divider()

# --- Formulario de Resultados ---
st.header("📋 Formulario de Análisis Educativo")

with st.form("form_resultados"):
    st.subheader("🔍 1. Identificación y Contexto")
    contexto = st.text_area(
        "¿De qué se trata el dataset? ¿Cuál es su origen y propósito?",
        placeholder="Ej: El dataset contiene información de 150 estudiantes inscritos en programas educativos, con datos sobre cursos, calificaciones y progreso académico...",
        height=100
    )

    st.subheader("❗ 2. Calidad de los Datos")
    calidad = st.text_area(
        "¿Qué encontraste sobre datos faltantes y limpieza?",
        placeholder="Ej: El dataset está 95% completo. Se observaron valores nulos en la columna de 'fecha_egreso' para estudiantes activos. La consistencia de tipos es excelente...",
        height=100
    )

    st.subheader("📈 3. Hallazgos Estadísticos Clave")
    estadisticas = st.text_area(
        "¿Cuáles son los números y categorías más relevantes?",
        placeholder="Ej: El promedio de calificación es 3.8/5.0. El 70% de estudiantes están activos. La edad promedio es 22 años. Los cursos más populares son Matemáticas (45%) e Inglés (38%)...",
        height=100
    )

    st.subheader("💡 4. Conclusión Final y Recomendaciones")
    conclusion = st.text_area(
        "¿Cuál es el mensaje principal de los datos y qué se puede mejorar?",
        placeholder="Ej: Los datos indican que hay un 85% de retención estudiantil. Se recomienda implementar apoyo académico adicional en Cálculo donde la tasa de reprobación es del 20%...",
        height=100
    )
    
    # Botón de envío
    enviado = st.form_submit_button("✅ Generar Reporte", use_container_width=True)

# --- Generación de Reporte ---
if enviado:
    if contexto and calidad and estadisticas and conclusion:
        st.divider()
        st.success("✅ Reporte Generado Exitosamente")
        
        fecha_reporte = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        reporte_md = f"""# Reporte de Análisis Exploratorio de Datos (EDA)
## Proyecto: Creciendo Juntos - Plataforma Educativa

**Fecha de Generación:** {fecha_reporte}

---

## 1️⃣ Identificación y Contexto

{contexto}

---

## 2️⃣ Calidad de los Datos

{calidad}

---

## 3️⃣ Hallazgos Estadísticos Clave

{estadisticas}

---

## 4️⃣ Conclusión Final y Recomendaciones

{conclusion}

---

**Generado por:** Creciendo Juntos - Plataforma de Analítica Educativa
"""
        
        # Mostrar reporte
        st.markdown(reporte_md)
        
        # Descargar reporte
        st.download_button(
            label="📥 Descargar Reporte (Markdown)",
            data=reporte_md,
            file_name=f"reporte_eda_creciendo_juntos_{fecha_reporte.replace('/', '-').replace(':', '')}.md",
            mime="text/markdown"
        )
    else:
        st.error("⚠️ Por favor completa todas las secciones antes de generar el reporte.")

## 3️⃣ Hallazgos Estadísticos Clave

{estadisticas}

---

## 4️⃣ Conclusión Final

{conclusion}

---

*Generado por el módulo de Análisis Exploratorio - Proyecto Integrador*
"""
        
        st.markdown("### 📄 Vista Previa del Reporte")
        st.markdown(reporte_md)
        
        st.divider()
        st.subheader("📥 Descargar Reporte")
        st.download_button(
            label="📥 Descargar como Markdown (.md)",
            data=reporte_md,
            file_name=f"reporte_eda_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
            mime="text/markdown",
            use_container_width=True
        )
    else:
        st.error("❌ Por favor, completa todas las secciones antes de generar el reporte.")

# --- Barra Lateral ---
with st.sidebar:
    st.markdown("---")
    st.subheader("💡 Consejos para el Análisis")
    st.markdown("""
    - Sé específico con números y porcentajes
    - Relaciona hallazgos entre secciones
    - Interpreta más allá de solo estadística
    - Proporciona contexto para tus conclusiones
    """)
    
    st.markdown("---")
    st.markdown("© 2026 - Proyecto Integrador de Analítica")
