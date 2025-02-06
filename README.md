#  🌍 API de Continentes y Países con FastAPI

Este proyecto es una API desarrollada con **FastAPI** que permite gestionar información sobre continentes y países mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar).

## Tecnologías Utilizadas

*   **FastAPI:** Framework web de alto rendimiento para Python.
*   **Uvicorn:** Servidor ASGI.
*   **Pydantic:** Validación de datos.
*   **SQLAlchemy:** ORM para la base de datos.
*   **psycopg2:** Driver de PostgreSQL.

## 🚀 Características

*   **Continentes:**
    *  📋 Listar todos los continentes.
    *  🔍 Obtener un continente por su ID.
    *  ➕ Agregar un nuevo continente.
    *  ✏️ Actualizar un continente existente.
    *  ❌ Eliminar un continente.
*   **Países:**
    *  📋 Listar todos los países.
    *  🔍 Obtener un país por su código.
    *  ➕ Agregar un nuevo país.
    *  ✏️ Actualizar un país existente.
    *  ❌ Eliminar un país.

## 📂 Estructura del Proyecto

primer-parcial/
├── Routers/
│   ├── continent.py  # Archivo que maneja las rutas de continentes
│   ├── country.py    # Archivo que maneja las rutas de países
│   └── ...          # Otros archivos de enrutadores (si los hay)
├── main.py           # Punto de entrada de la API
└── README.md
└── requirements.txt # Archivo de dependencias

## 🛠 Instalación

1.  Clona el repositorio:

    ```bash
    git clone [https://github.com/Ivanss1706/primer-parcial.git](https://github.com/Ivanss1706/primer-parcial.git)
    cd primer-parcial
    ```

2.  Crea un entorno virtual (recomendado):

    ```bash
    python3 -m venv .venv  # Linux/macOS
    python -m venv .venv   # Windows
    ```

3.  Activa el entorno virtual:

    ```bash
    source .venv/bin/activate  # Linux/macOS
    .venv\Scripts\activate    # Windows
    ```

4.  Instala las dependencias:

    ```bash
    pip install -r requirements.txt # Instala las dependencias desde el archivo
    ```

5.  Ejecuta la aplicación:

    ```bash
    uvicorn main:app --reload
    ```

    (Asegúrate de tener `uvicorn` instalado: `pip install uvicorn`)

## 📌 Endpoints

### Continentes

*   **Obtener todos los continentes:**

    ```
    GET /continent/
    ```

    Ejemplo de respuesta:

    ```json
    [
      {"cID": 1, "name": "North America"},
      {"cID": 2, "name": "South America"}
    ]
    ```

*   **Obtener un continente por ID:**

    ```
    GET /continent/{id}
    ```

    *   Parámetro: `id` (int) - ID del continente.
    *   Ejemplo: `/continent/1`
    *   Posibles respuestas:
        *   `200 OK`: Devuelve el continente.
        *   `404 Not Found`: `"CONTINENTE NO EXISTENTE"`

*   **Agregar un continente:**

    ```
    POST /continent/
    ```

    Cuerpo JSON:

    ```json
    {
      "cID": 8,
      "name": "New Continent"
    }
    ```

    Posibles respuestas:

    *   `201 Created`: Continente agregado.
    *   `409 Conflict`: `"CONTINENTE YA REGISTRADO"`

*   **Actualizar un continente:**

    ```
    PUT /continent/
    ```

    Cuerpo JSON:

    ```json
    {
      "cID": 1,
      "name": "Updated Continent"
    }
    ```

    Respuestas:

    *   `200 OK`: Continente actualizado.
    *   `400 Bad Request`: `"ERROR AL ACTUALIZAR"` (Usualmente 400 para errores en la solicitud)

*   **Eliminar un continente:**

    ```
    DELETE /continent/{id}
    ```

    Respuestas:

    *   `200 OK`: `"CONTINENTE ELIMINADO"`
    *   `404 Not Found`: `"CONTINENTE NO ENCONTRADO"` (404 es más apropiado que 401)

### 🌎 Países

*   **Obtener todos los países:**

    ```
    GET /country/
    ```

    Ejemplo de respuesta:

    ```json
    [
      {
        "code": "ABW",
        "name": "Aruba",
        "continent": "North America",
        // ... otros campos
      }
    ]
    ```

*   **Obtener un país por código:**

    ```
    GET /country/{code}
    ```

    Ejemplo: `/country/ARG`

    Respuestas:

    *   `200 OK`: Devuelve el país.
    *   `404 Not Found`: `"PAÍS NO EXISTE"`

*   **Agregar un país:**

    ```
    POST /country/
    ```

    Cuerpo JSON:

    ```json
    {
      "code": "MEX",
      "name": "Mexico",
      // ... otros campos
    }
    ```

    Respuestas:

    *   `201 Created`: País agregado.
    *   `409 Conflict`: `"PAÍS YA REGISTRADO"`

*   **Actualizar un país:**

    ```
    PUT /country/
    ```

    Cuerpo JSON:

    ```json
    {
      "code": "ARG",
      "name": "Argentina Updated",
      "population": 38000000
    }
    ```

    Respuestas:

    *   `200 OK`: País actualizado.
    *   `400 Bad Request`: `"ERROR AL ACTUALIZAR"`

*   **Eliminar un país:**

    ```
    DELETE /country/{code}
    ```

    Respuestas:

    *   `200 OK`: `"PAÍS ELIMINADO"`
    *   `404 Not Found`: `"PAÍS NO ENCONTRADO"`
