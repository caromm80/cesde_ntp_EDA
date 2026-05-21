# 📚 Ejemplo de Datos Educativos - Creciendo Juntos

Esta guía muestra ejemplos de estructuras de datos que tu API Java debe retornar para ser compatible con Creciendo Juntos.

---

## 1️⃣ Estudiantes - GET `/api/estudiantes`

### Respuesta JSON Esperada:

```json
[
  {
    "id": 1,
    "nombre": "Juan Carlos Pérez",
    "email": "juan.perez@universidad.edu",
    "documento": "1234567890",
    "fecha_inscripcion": "2024-01-15",
    "estado": "Activo",
    "semestre": 3,
    "promedio_general": 4.2,
    "programa": "Ingeniería de Software"
  },
  {
    "id": 2,
    "nombre": "María García López",
    "email": "maria.garcia@universidad.edu",
    "documento": "0987654321",
    "fecha_inscripcion": "2024-01-20",
    "estado": "Activo",
    "semestre": 2,
    "promedio_general": 3.8,
    "programa": "Administración de Empresas"
  },
  {
    "id": 3,
    "nombre": "Carlos Rodríguez",
    "email": "carlos.rodriguez@universidad.edu",
    "documento": "1122334455",
    "fecha_inscripcion": "2023-08-10",
    "estado": "Inactivo",
    "semestre": 4,
    "promedio_general": 3.5,
    "programa": "Contabilidad"
  }
]
```

### Campos Importantes:
- `id` - Identificador único del estudiante
- `nombre` - Nombre completo
- `email` - Correo institucional
- `estado` - Activo/Inactivo/Graduado/Suspendido
- `promedio_general` - Escala 0-5
- `programa` - Programa académico

---

## 2️⃣ Cursos - GET `/api/cursos`

### Respuesta JSON Esperada:

```json
[
  {
    "id": 101,
    "nombre": "Introducción a Python",
    "codigo": "CS101",
    "profesor": "Dr. Juan López",
    "semestre": 1,
    "creditos": 3,
    "duracion_semanas": 16,
    "estudiantes_inscritos": 45,
    "estudiantes_aprobados": 42,
    "descripcion": "Conceptos básicos de programación en Python"
  },
  {
    "id": 102,
    "nombre": "Bases de Datos SQL",
    "codigo": "DB102",
    "profesor": "Ing. María González",
    "semestre": 2,
    "creditos": 4,
    "duracion_semanas": 16,
    "estudiantes_inscritos": 38,
    "estudiantes_aprobados": 35,
    "descripcion": "Diseño y gestión de bases de datos relacionales"
  },
  {
    "id": 103,
    "nombre": "Desarrollo Web Avanzado",
    "codigo": "WEB201",
    "profesor": "Arq. Carlos Martínez",
    "semestre": 4,
    "creditos": 4,
    "duracion_semanas": 16,
    "estudiantes_inscritos": 32,
    "estudiantes_aprobados": 30,
    "descripcion": "Tecnologías modernas de desarrollo web"
  }
]
```

### Campos Importantes:
- `id` - Identificador único del curso
- `codigo` - Código académico del curso
- `profesor` - Docente a cargo
- `semestre` - Semestre en el que se ofrece
- `creditos` - Créditos académicos
- `estudiantes_inscritos` - Total inscritos
- `estudiantes_aprobados` - Total aprobados

---

## 3️⃣ Calificaciones - GET `/api/calificaciones`

### Respuesta JSON Esperada:

```json
[
  {
    "id": 1001,
    "estudiante_id": 1,
    "curso_id": 101,
    "nombre_estudiante": "Juan Carlos Pérez",
    "nombre_curso": "Introducción a Python",
    "nota_parcial1": 4.5,
    "nota_parcial2": 4.3,
    "nota_proyecto": 4.6,
    "nota_examen_final": 4.2,
    "nota_final": 4.4,
    "estado": "Aprobado",
    "fecha_calificacion": "2024-05-30"
  },
  {
    "id": 1002,
    "estudiante_id": 2,
    "curso_id": 101,
    "nombre_estudiante": "María García López",
    "nombre_curso": "Introducción a Python",
    "nota_parcial1": 3.8,
    "nota_parcial2": 4.0,
    "nota_proyecto": 3.9,
    "nota_examen_final": 3.7,
    "nota_final": 3.85,
    "estado": "Aprobado",
    "fecha_calificacion": "2024-05-30"
  },
  {
    "id": 1003,
    "estudiante_id": 3,
    "curso_id": 102,
    "nombre_estudiante": "Carlos Rodríguez",
    "nombre_curso": "Bases de Datos SQL",
    "nota_parcial1": 2.8,
    "nota_parcial2": 2.5,
    "nota_proyecto": 2.9,
    "nota_examen_final": 2.3,
    "nota_final": 2.6,
    "estado": "Reprobado",
    "fecha_calificacion": "2024-06-01"
  }
]
```

### Campos Importantes:
- `estudiante_id` - ID del estudiante
- `curso_id` - ID del curso
- `nota_final` - Calificación final (0-5)
- `estado` - Aprobado/Reprobado
- `fecha_calificacion` - Cuándo se calificó

---

## 4️⃣ Inscripciones - GET `/api/inscripciones`

### Respuesta JSON Esperada:

```json
[
  {
    "id": 5001,
    "estudiante_id": 1,
    "curso_id": 101,
    "nombre_estudiante": "Juan Carlos Pérez",
    "nombre_curso": "Introducción a Python",
    "fecha_inscripcion": "2024-01-22",
    "estado_inscripcion": "Activa",
    "grupo": "A",
    "horario": "Lunes y Miércoles 10:00-12:00",
    "salon": "A-205"
  },
  {
    "id": 5002,
    "estudiante_id": 1,
    "curso_id": 102,
    "nombre_estudiante": "Juan Carlos Pérez",
    "nombre_curso": "Bases de Datos SQL",
    "fecha_inscripcion": "2024-01-25",
    "estado_inscripcion": "Activa",
    "grupo": "B",
    "horario": "Martes y Jueves 14:00-16:00",
    "salon": "B-301"
  },
  {
    "id": 5003,
    "estudiante_id": 2,
    "curso_id": 101,
    "nombre_estudiante": "María García López",
    "nombre_curso": "Introducción a Python",
    "fecha_inscripcion": "2024-01-23",
    "estado_inscripcion": "Activa",
    "grupo": "A",
    "horario": "Lunes y Miércoles 10:00-12:00",
    "salon": "A-205"
  }
]
```

### Campos Importantes:
- `estudiante_id` - ID del estudiante
- `curso_id` - ID del curso
- `fecha_inscripcion` - Cuándo se inscribió
- `estado_inscripcion` - Activa/Cancelada/Completada
- `grupo` - Grupo de estudio
- `horario` - Cuándo se dicta
- `salon` - Dónde se dicta

---

## 🔧 Implementación en Spring Boot

### Controlador REST:

```java
@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "http://localhost:8501")
public class EducacionController {
    
    @Autowired
    private EstudianteService estudianteService;
    
    @Autowired
    private CursoService cursoService;
    
    @Autowired
    private CalificacionService calificacionService;
    
    @Autowired
    private InscripcionService inscripcionService;
    
    @GetMapping("/estudiantes")
    public ResponseEntity<List<Estudiante>> getEstudiantes() {
        return ResponseEntity.ok(estudianteService.getAll());
    }
    
    @GetMapping("/cursos")
    public ResponseEntity<List<Curso>> getCursos() {
        return ResponseEntity.ok(cursoService.getAll());
    }
    
    @GetMapping("/calificaciones")
    public ResponseEntity<List<Calificacion>> getCalificaciones() {
        return ResponseEntity.ok(calificacionService.getAll());
    }
    
    @GetMapping("/inscripciones")
    public ResponseEntity<List<Inscripcion>> getInscripciones() {
        return ResponseEntity.ok(inscripcionService.getAll());
    }
}
```

### Entidades (Models):

```java
@Entity
@Table(name = "estudiantes")
public class Estudiante {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(nullable = false)
    private String nombre;
    
    @Column(unique = true)
    private String email;
    
    private String documento;
    
    private LocalDate fechaInscripcion;
    
    private String estado; // Activo, Inactivo, Graduado
    
    private Integer semestre;
    
    private Double promedioGeneral;
    
    private String programa;
    
    // Getters y Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    // ... etc
}
```

---

## 📊 Análisis que Puedes Hacer

Con esta estructura de datos, puedes analizar:

### 1. **Desempeño Académico**
- Promedio general por estudiante
- Tasa de aprobación por curso
- Tendencias de calificaciones

### 2. **Retención Estudiantil**
- Estudiantes activos vs inactivos
- Tasa de deserción por programa
- Relación entre calificaciones y permanencia

### 3. **Oferta Académica**
- Cursos más demandados
- Ratio profesor-estudiante
- Distribución de créditos

### 4. **Inscripciones**
- Patrones de inscripción por semestre
- Distribución por grupo
- Capacidad vs ocupación de salones

---

## 🎯 Cómo Configurar en config.py

Una vez tu API Java esté retornando estos datos:

```python
API_CONFIG = {
    "base_url": "http://localhost:8080",
    "timeout": 10,
    "endpoints": {
        "estudiantes": "/api/estudiantes",
        "cursos": "/api/cursos",
        "calificaciones": "/api/calificaciones",
        "inscripciones": "/api/inscripciones",
    }
}
```

Luego abre Streamlit y navega a la página "Consumo de API" para visualizar y analizar los datos.

---

**¡Con esta estructura estás listo para comenzar tu análisis educativo en Creciendo Juntos! 🎓**
