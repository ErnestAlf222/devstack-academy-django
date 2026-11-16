# DeviLearning

Plataforma de cursos en línea construida con Django 5.2, SQLite y Tailwind CSS.

## Estado del backend

### Arquitectura de apps

```mermaid
flowchart LR
    subgraph Proyecto["devilearn (configuración)"]
        URLS["urls.py raíz"]
        SET["settings.py<br/>AUTH_USER_MODEL = profiles.User<br/>DB: SQLite"]
    end

    URLS -->|/admin/| ADMIN["Django Admin"]
    URLS -->|/courses/| C["apps.courses"]
    URLS -->|/dashboard/| D["apps.dashboard"]
    URLS -->|/profiles/| P["apps.profiles"]

    C --- CM["Modelos: Category, Course, CourseCategory,<br/>Module, Enrollment, Progress, Review"]
    P --- PM["Modelos: User, InstructorProfile"]
    D --- DM["Solo vista (sin modelos)"]

    ADMIN --- PA["Admin registrado:<br/>User, InstructorProfile"]
```

### Rutas implementadas

| Prefijo      | Ruta        | Vista            | Nombre          |
|--------------|-------------|------------------|-----------------|
| `/courses/`  | `""`        | `course_list`    | `course_list`   |
| `/courses/`  | `detail/`   | `course_detail`  | `course_detail` |
| `/courses/`  | `lessons/`  | `course_lessons` | `course_lessons`|
| `/dashboard/`| `""`        | `index`          | `dashboard`     |
| `/profiles/` | `""`        | `index`          | `profiles`      |
| `/admin/`    | —           | Django Admin     | —               |

### Diagrama de modelos (ER)

```mermaid
erDiagram
    User {
        int id PK
        string username
        string email
        bool is_instructor
    }
    InstructorProfile {
        int id PK
        int user_id FK "OneToOne"
        text bio
        url photo
        url website
        url linkedin_url
        url social_network
    }
    Category {
        int id PK
        string name
        slug slug UK
    }
    Course {
        int id PK
        int owner_id FK
        string title
        slug slug UK
        text overview
        date created_at
    }
    CourseCategory {
        int id PK
        int course_id FK
        int category_id FK
    }
    Module {
        int id PK
        int course_id FK
        string title
        text description
    }
    Enrollment {
        int id PK
        int user_id FK
        int course_id FK
        datetime enrolled_at
    }
    Progress {
        int id PK
        int user_id FK
        int course_id FK
        string status
        float progress
        datetime updated_at
    }
    Review {
        int id PK
        int user_id FK
        int course_id FK
        smallint rating
        text comment
        datetime created_at
    }

    User ||--o| InstructorProfile : "tiene"
    User ||--o{ Course : "es dueño (owned_courses)"
    Course ||--o{ CourseCategory : ""
    Category ||--o{ CourseCategory : ""
    Course ||--o{ Module : "contiene"
    User ||--o{ Enrollment : "se inscribe"
    Course ||--o{ Enrollment : ""
    User ||--o{ Progress : "avanza"
    Course ||--o{ Progress : ""
    User ||--o{ Review : "califica"
    Course ||--o{ Review : ""
```

> `Course ↔ Category` es una relación muchos a muchos a través de `CourseCategory`.
> `Enrollment`, `Progress` y `Review` tienen restricción única `(user, course)`.

### Avance

- [x] Usuario personalizado (`profiles.User`) con `is_instructor`
- [x] Perfil de instructor y registro en el admin
- [x] Modelos de cursos, módulos, inscripciones, progreso y reseñas
- [x] Migraciones iniciales
- [x] Rutas y vistas base (plantillas) de cursos, dashboard y perfiles
- [ ] Admin para los modelos de `courses`
- [ ] Lógica de vistas con datos reales (hoy solo renderizan plantillas)
- [ ] Autenticación (login/registro)
- [ ] Modelo de lecciones (la ruta `lessons/` existe, sin modelo aún)

## Desarrollo

```bash
python manage.py migrate
python manage.py runserver
npm run build   # o el script de Tailwind definido en package.json
```
