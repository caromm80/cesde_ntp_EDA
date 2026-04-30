# 🔍 Diagnóstico: Error 404 en MockAPI

## ¿Qué está pasando? 🤔

El error `404` que ves significa:

```
Status 404 en https://69f350d4bd2396bf530fbde8.mockapi.io/api/v1/reportes
Status 404 en https://69f350d4bd2396bf530fbde8.mockapi.io/api/v1/vehiculos
```

**Traducción:** "No encontré las entidades `reportes` y `vehiculos` en tu proyecto de MockAPI"

---

## Causas Posibles

| # | Causa | Solución |
|---|-------|----------|
| 1️⃣ | Las entidades **NO han sido creadas** en MockAPI | Crear entidades en MockAPI (ver abajo) |
| 2️⃣ | El nombre está **mal escrito** (mayúsculas, espacios, tildes) | Asegúrate de que sea exactamente: `reportes` y `vehiculos` |
| 3️⃣ | Hay **errores de conexión a internet** | Verifica tu conexión |
| 4️⃣ | El **ID de proyecto es incorrecto** | Debe ser: `69f350d4bd2396bf530fbde8` |

---

## ✅ Solución Rápida

### Paso 1: Usa el Modo Demo (AHORA)

En la página de MockAPI, selecciona:
```
📊 Modo Demo (Datos de Ejemplo)
```

Esto te permite explorar toda la funcionalidad con datos de prueba sin necesidad de MockAPI.

---

### Paso 2: Configura MockAPI (DESPUÉS)

Cuando quieras usar datos reales de MockAPI:

1. **Abre [mockapi.io](https://mockapi.io)**
2. **Inicia sesión**
3. **Ve a tu proyecto con ID:** `69f350d4bd2396bf530fbde8`
4. **Crea la Entidad 1 llamada: `reportes`**

   Campos:
   ```
   - id (Object ID - Auto)
   - fecha (Faker.js → date.recent)
   - fecha_hora (String)
   - ciudad (Faker.js → address.city)
   - tipo_accidente (Faker.js → vehicle.type)
   - severidad (Faker.js → datatype.number 1-5)
   ```

5. **Crea la Entidad 2 llamada: `vehiculos`**

   Campos:
   ```
   - id (Object ID - Auto)
   - placa (String)
   - tipo_vehiculo (Faker.js → vehicle.type)
   - marca (Faker.js → vehicle.manufacturer)
   - ciudad (Faker.js → address.city)
   - año (Faker.js → datatype.number)
   - estado (String)
   ```

6. **Genera 10-15 registros en cada entidad**
7. **Vuelve a la aplicación y selecciona "Modo Real (MockAPI)"**

---

## Verificación

Después de crear las entidades, prueba estas URLs en tu navegador:

✅ **Debe funcionar después de configurar:**
- `https://69f350d4bd2396bf530fbde8.mockapi.io/reportes`
- `https://69f350d4bd2396bf530fbde8.mockapi.io/vehiculos`

Si no ves `[]` o datos JSON, aún falta configurar las entidades.

---

## Resumen

| Paso | Acción | Estado |
|------|--------|--------|
| ✅ Ahora | Usa **Modo Demo** en la app | DISPONIBLE |
| ⏳ Después | Crea entidades en MockAPI | MANUAL |
| ⏳ Después | Cambia a **Modo Real** | AUTOMÁTICO |

**No es un error, es que aún no configuraste MockAPI.** El Modo Demo te permite usar la app YA. 🚀

