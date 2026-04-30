# 📋 Guía: Subir Datos a MockAPI

## Opción Directa: Upload CSV en MockAPI

### Paso 1: Crear la Tabla en MockAPI

1. Ve a [mockapi.io](https://mockapi.io)
2. Inicia sesión con tu ID: **69f350d4bd2396bf530fbde8**
3. Click en **"+ Create New"**
4. Nombre exacto: **`reportes`**
5. Click **"Create"**

---

### Paso 2: Agregar Campos a MockAPI

Click en **"+ Add Field"** para cada uno:

| Nombre | Tipo | 
|--------|------|
| ID | Number |
| Fecha | String |
| Hora | String |
| Ciudad | String |
| Departamento | String |
| Tipo_Accidente | String |
| Gravedad | String |
| Clima | String |
| Iluminacion | String |
| Tipo_Via | String |
| Condicion_Via | String |
| Vehiculos_Involucrados | Number |
| Heridos | Number |
| Muertos | Number |
| Edad_Conductor | Number |
| Genero_Conductor | String |
| Alcohol | String |
| Velocidad_Aprox | Number |

---

### Paso 3: Importar tu CSV Directamente

1. En MockAPI, click en **"Import"** o **"Bulk Add"**
2. Selecciona **"CSV"**
3. Sube tu archivo: **`Desarrollos_de_software_20260319.csv`**
4. MockAPI auto-mapea los campos
5. Verifica que reconozca los 300 registros
6. Click **"Import"** ✅

---

### Paso 4: Verificar en Streamlit

1. En Streamlit, ve a la página **"Gestión de Accidentes de Tránsito - MockAPI"**
2. Click en **"🔄 Refrescar Datos"**
3. ¡Listo! Deberían aparecer tus 300 registros

---

## Verificar que Funciona

Abre esta URL en el navegador:
```
https://69f350d4bd2396bf530fbde8.mockapi.io/reportes
```

Deberías ver todos tus datos en formato JSON.

---

## Solución de Problemas

### ❌ Error: "304 Not Found"
- La tabla `reportes` no existe aún
- Crea la tabla y los campos primero

### ❌ Error: Campos no coinciden
- Verifica que los nombres sean **exactos** (mayúsculas/minúsculas)
- Los campos deben ser: `Ciudad` (no `ciudad`), `Tipo_Accidente` (con guión bajo)

### ❌ No ve los datos en Streamlit
- Haz click en **"🔄 Refrescar Datos"**
- Espera a que se conecte (puede tardar 5-10 segundos)
- Verifica la URL en el navegador

---

## URLs del Proyecto

**MockAPI Dashboard:**
```
https://mockapi.io (inicia sesión con tu ID)
```

**Tu API:**
```
https://69f350d4bd2396bf530fbde8.mockapi.io/reportes
```

**Streamlit (local):**
```
streamlit run Inicio.py
```
