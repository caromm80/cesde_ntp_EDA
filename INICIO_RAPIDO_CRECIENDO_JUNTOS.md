# ⚡ Guía Rápida: Creciendo Juntos en 5 Minutos

## 🎯 Objetivo
Transformar tu proyecto de EDA en una plataforma educativa conectada con tu API Java.

---

## ✅ Checklist Rápida

### Paso 1: Preparación (1 minuto)
```bash
# Asegúrate de tener las dependencias
pip install -r requirements.txt
```

### Paso 2: Configurar API (2 minutos)

Abre `config.py` y actualiza:

```python
API_CONFIG = {
    "base_url": "http://localhost:8080",  # 👈 CAMBIAR AQUÍ
    "timeout": 10,
    "endpoints": {
        "estudiantes": "/api/estudiantes",      # 👈 ADAPTAR AQUÍ
        "cursos": "/api/cursos",
        "calificaciones": "/api/calificaciones",
        "inscripciones": "/api/inscripciones",
    }
}
```

### Paso 3: Ejecutar (1 minuto)
```bash
streamlit run Inicio.py
```

### Paso 4: Verificar (1 minuto)
1. Abre: http://localhost:8501
2. Haz clic en "Consumo de API" (página 3)
3. Haz clic en "🔄 Refrescar Datos"
4. ¿Ves datos? ✅ ¡Listo!

---

## 📁 Archivos Importantes

| Archivo | Propósito | Acción |
|---------|-----------|--------|
| **config.py** | ⚙️ Configuración | Editar con tu API |
| **Inicio.py** | 🏠 Página principal | Solo lectura |
| **pages/3_Consumo_de_API.py** | 🎓 API Java | Solo lectura |
| **GUIA_API_JAVA.md** | 📚 Guía completa | Consultar si hay errores |
| **EJEMPLO_DATOS_EDUCATIVOS.md** | 📊 Ejemplos JSON | Referencia de formatos |

---

## 🚀 Comandos Esenciales

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
streamlit run Inicio.py

# Verificar API desde terminal
curl http://localhost:8080/api/estudiantes
```

---

## ⚠️ Errores Comunes

### ❌ "No se puede conectar a la API Java"

**Solución:**
1. Verifica que tu API esté corriendo
2. Revisa URL en `config.py`
3. Haz clic en "🔄 Refrescar Datos" en Streamlit

### ❌ "Formato de respuesta no reconocido"

**Solución:**
- Tu API debe retornar JSON como array: `[{...}, {...}]`
- O como objeto: `{"data": [{...}, {...}]}`

### ❌ CORS Error

**Solución (Spring Boot):**
```java
@CrossOrigin(origins = "http://localhost:8501")
@RestController
@RequestMapping("/api")
public class EducacionController { ... }
```

---

## 📊 Navegación en la App

```
🏠 INICIO
  └─ Información general de Creciendo Juntos

📊 PÁGINA 1: Análisis Exploratorio (EDA)
  └─ Cargar CSV y explorar datos

🎓 PÁGINA 2: Consumo de API ⭐
  └─ Conectar a tu API Java
  └─ Configurar en sidebar
  └─ Ver datos en tiempo real

📝 PÁGINA 3: Resultados
  └─ Documentar hallazgos
  └─ Generar reportes
```

---

## 🔌 Estructura Mínima de API Java

Tu API debe tener al menos:

```
GET /api/estudiantes    → Lista de estudiantes
GET /api/cursos         → Lista de cursos
GET /api/calificaciones → Lista de calificaciones
GET /api/inscripciones  → Lista de inscripciones
```

**Formato respuesta:**
```json
[
  {"id": 1, "nombre": "Juan", ...},
  {"id": 2, "nombre": "María", ...}
]
```

---

## 💡 Tips Rápidos

✅ Edita SOLO `config.py` para cambiar tu API
✅ Los otros archivos ya están listos para usar
✅ Usa "🔄 Refrescar Datos" para probar cambios
✅ Consulta GUIA_API_JAVA.md si hay problemas
✅ Abre EJEMPLO_DATOS_EDUCATIVOS.md para ver formatos

---

## 🎓 ¿Qué Hace Cada Página?

### 📖 Inicio.py
- Presentación del proyecto
- Objetivos educativos
- Información del equipo

### 🔍 Análisis Exploratorio (EDA)
- Cargar archivos CSV
- Ver estadísticas
- Analizar calidad de datos

### 🎓 Consumo de API (PRINCIPAL)
- **Panel de configuración** en la barra lateral
- **Selector de entidades** (radio buttons)
- **Visualización** de datos en tiempo real
- **Descarga** como CSV
- **Estadísticas** automáticas

### 📝 Resultados del Análisis
- Formulario para documentar
- Generar reporte en Markdown
- Descargar documento

---

## 🔄 Flujo de Trabajo Típico

```
1. Editar config.py
   ↓
2. Ejecutar: streamlit run Inicio.py
   ↓
3. Ir a página "Consumo de API"
   ↓
4. Hacer click "🔄 Refrescar Datos"
   ↓
5. ¿Ves datos? Haz análisis
   ↓
6. Documenta hallazgos en "Resultados"
   ↓
7. Descarga reporte
```

---

## 📞 Ayuda Rápida

**Problema** | **Solución Rápida**
---|---
API no conecta | Verifica URL en `config.py`
Error JSON | Asegúrate que API retorne array o {"data": [...]}
CORS error | Agrega @CrossOrigin en Spring Boot
Timeout | Aumenta valor en `config.py`
Cambios no aparecen | Haz clic en "🔄 Refrescar Datos"

---

## 📚 Lee Después

1. **GUIA_API_JAVA.md** - Guía completa (30-45 min)
2. **EJEMPLO_DATOS_EDUCATIVOS.md** - Ejemplos JSON (10 min)
3. **README_CAMBIOS.md** - Qué cambió (5 min)

---

**¡Ya estás listo! Abre Streamlit y comienza. 🚀**

```bash
streamlit run Inicio.py
```
