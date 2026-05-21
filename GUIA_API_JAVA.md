# 🎓 Creciendo Juntos - Guía de Integración con API Java

## 📋 Descripción del Proyecto

**Creciendo Juntos** es una plataforma educativa de analítica de datos que se integra con una API Java del grupo para visualizar, analizar y generar insights sobre:

- **Estudiantes**: Información demográfica y datos de inscripción
- **Cursos**: Catálogo de cursos disponibles
- **Calificaciones**: Desempeño académico y notas
- **Inscripciones**: Registro de estudiantes en cursos

---

## 🚀 Instalación Rápida

### 1. Requisitos Previos

- **Python 3.8+**
- **pip** (gestor de paquetes de Python)
- **API Java corriendo** en tu servidor/máquina

### 2. Instalar Dependencias

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuración de la API Java

### Archivo: `config.py`

Edita el archivo `config.py` para configurar la conexión a tu API Java:

```python
API_CONFIG = {
    "base_url": "http://localhost:8080",  # URL de tu API Java
    "timeout": 10,  # Segundos máximos de espera
    "endpoints": {
        "estudiantes": "/api/estudiantes",
        "cursos": "/api/cursos",
        "calificaciones": "/api/calificaciones",
        "inscripciones": "/api/inscripciones",
    }
}
```

### Pasos de Configuración:

1. **Actualiza `base_url`:**
   - Si la API está en tu máquina local: `http://localhost:8080`
   - Si está en un servidor remoto: `http://tu-servidor.com:puerto`

2. **Verifica los endpoints:**
   - Asegúrate de que los endpoints coincidan con los de tu API Java
   - Ejemplo: Si tu API tiene `/api/v1/estudiantes`, actualiza la configuración

3. **Ajusta el timeout si es necesario:**
   - Para conexiones lentas, aumenta el valor (ej: 30 segundos)

---

## ▶️ Ejecución de la Aplicación

### Opción 1: Ejecutar localmente

```bash
streamlit run Inicio.py
```

La aplicación se abrirá en `http://localhost:8501`

### Opción 2: Ejecutar desde el terminal

```bash
python -m streamlit run Inicio.py
```

---

## 📊 Secciones de la Aplicación

### 1. **Inicio (Inicio.py)**
- Bienvenida y presentación del proyecto
- Objetivos educativos
- Información sobre el equipo de trabajo
- Guía de navegación

### 2. **Análisis Exploratorio de Datos (1_Análisis Exploratorio de Datos.py)**
- Carga de archivos CSV locales
- Visualización de primeras filas
- Estadísticas descriptivas
- Análisis de calidad de datos
- Detección de valores faltantes

### 3. **Consumo de API (3_Consumo_de_API.py)** ⭐ **PRINCIPAL**
- Conexión a la API Java en tiempo real
- Selección de entidades (estudiantes, cursos, etc.)
- Filtros y búsquedas
- Visualización de datos
- Descarga de datos como CSV
- Panel de configuración en la barra lateral

### 4. **Resultados del Análisis (2_Resultados (EDA).py)**
- Formulario para documentar hallazgos
- Generación de reportes
- Descarga de reportes en Markdown

---

## 🔧 Verificar Conexión con API Java

### Test 1: Validar URL de la API

1. Abre `3_Consumo_de_API.py`
2. En la barra lateral, verifica el **Base URL**
3. Haz clic en **"🔄 Refrescar Datos"**

### Test 2: Desde la Terminal (usando curl)

```bash
# Verificar que la API responde
curl http://localhost:8080/api/estudiantes

# Ejemplo de respuesta esperada:
[
  {"id": 1, "nombre": "Juan", ...},
  {"id": 2, "nombre": "María", ...}
]
```

### Test 3: Verificar Endpoints Disponibles

```bash
curl http://localhost:8080/api/cursos
curl http://localhost:8080/api/calificaciones
curl http://localhost:8080/api/inscripciones
```

---

## 🐛 Solución de Problemas

### Error: "No se puede conectar a la API Java"

**Posibles causas:**
1. La API Java no está corriendo
2. La URL base es incorrecta
3. El timeout es muy corto

**Soluciones:**
```bash
# 1. Verifica que la API esté corriendo (ejemplo en Java)
# En terminal: java -jar aplicacion.jar

# 2. Verifica la URL configurada en config.py
# Debe ser: http://localhost:8080 (sin trailing slash)

# 3. Aumenta el timeout en config.py
# Cambia "timeout": 10 por "timeout": 30
```

### Error: "Formato de respuesta no reconocido"

**Posibles causas:**
- La API retorna un formato diferente al esperado

**Soluciones:**
- La API debe retornar JSON en estos formatos:
  ```json
  // Opción 1: Array directo
  [{"id": 1, ...}, {"id": 2, ...}]
  
  // Opción 2: Objeto con propiedad "data"
  {"data": [{"id": 1, ...}, {"id": 2, ...}]}
  ```

### Error de CORS (Cross-Origin)

Si ves errores de CORS, tu API Java necesita configuración CORS:

**En Spring Boot:**
```java
@Configuration
public class CorsConfig {
    @Bean
    public WebMvcConfigurer corsConfigurer() {
        return new WebMvcConfigurer() {
            @Override
            public void addCorsMappings(CorsRegistry registry) {
                registry.addMapping("/api/**")
                    .allowedOrigins("http://localhost:8501")
                    .allowedMethods("GET", "POST", "PUT", "DELETE");
            }
        };
    }
}
```

---

## 📝 Estructura de Archivos

```
cesde_ntp_EDA/
├── Inicio.py                                 # Página principal
├── config.py                                 # ⭐ Configuración de API
├── requirements.txt                          # Dependencias Python
├── pages/
│   ├── 1_Análisis Exploratorio de Datos.py  # EDA
│   ├── 2_Resultados (EDA).py                # Resultados
│   └── 3_Consumo_de_API.py                  # ⭐ Consumo de API Java
├── CHECKLIST_REQUISITOS.md
├── CUMPLIMIENTO_REQUISITOS.md
├── README.md                                 # Este archivo
└── README_CAMBIOS.md                         # Cambios realizados
```

---

## 🔌 Ejemplo de Respuesta de API Java Esperada

### GET `/api/estudiantes`

```json
[
  {
    "id": 1,
    "nombre": "Juan Pérez",
    "email": "juan@example.com",
    "estado": "Activo",
    "promedio": 4.2
  },
  {
    "id": 2,
    "nombre": "María García",
    "email": "maria@example.com",
    "estado": "Activo",
    "promedio": 3.8
  }
]
```

### GET `/api/cursos`

```json
[
  {
    "id": 1,
    "nombre": "Introducción a Python",
    "codigo": "CS101",
    "duracion_semanas": 8,
    "estudiantes_inscritos": 45
  },
  {
    "id": 2,
    "nombre": "Bases de Datos",
    "codigo": "DB101",
    "duracion_semanas": 10,
    "estudiantes_inscritos": 38
  }
]
```

---

## 💡 Próximos Pasos

1. **Configurar la API Java** según los datos de tu institución
2. **Verificar la conectividad** usando los tests anteriores
3. **Explorar los datos** usando la sección de Análisis Exploratorio
4. **Generar reportes** con los hallazgos educativos
5. **Personalizar endpoints** en `config.py` según tus necesidades

---

## 📞 Soporte Técnico

Si encuentras problemas:

1. Verifica que la API Java esté corriendo
2. Revisa los logs de tu aplicación Java
3. Intenta desde la terminal con `curl`
4. Aumenta los valores de timeout
5. Verifica que los endpoints sean correctos

---

**¡Bienvenido a Creciendo Juntos! 🎓**
