# ================================================
# CONFIGURACIÓN DE API - CRECIENDO JUNTOS
# ================================================
# Archivo de configuración centralizado para conectar con la API Java

# --- CONFIGURACIÓN DE LA API JAVA ---
API_CONFIG = {
    "base_url": "http://localhost:8080",  # Cambia esto por la URL de tu API Java
    "timeout": 10,  # Tiempo máximo de espera (segundos)
    "endpoints": {
        "estudiantes": "/api/estudiantes",
        "cursos": "/api/cursos",
        "calificaciones": "/api/calificaciones",
        "inscripciones": "/api/inscripciones",
        # Agrega los endpoints de tu API según sea necesario
    }
}

# --- INFORMACIÓN DEL PROYECTO ---
PROJECT_INFO = {
    "nombre": "Creciendo Juntos",
    "descripcion": "Plataforma Educativa",
    "version": "1.0.0",
    "icon": "🎓"
}

# Función para obtener URL completa del endpoint
def get_endpoint_url(endpoint_name: str) -> str:
    """Retorna la URL completa del endpoint"""
    base = API_CONFIG["base_url"]
    endpoint = API_CONFIG["endpoints"].get(endpoint_name, "")
    return f"{base}{endpoint}"

# Función para obtener timeout
def get_timeout() -> int:
    """Retorna el timeout configurado"""
    return API_CONFIG["timeout"]
