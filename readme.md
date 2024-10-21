# Deliver Hero

Deliver Hero es una aplicación FastAPI para la gestión de pedidos de un restaurante.

## Requisitos previos

- Git
- PostgreSQL

## Configuración del entorno de desarrollo

### 1. Instalar pyenv

```bash
# Instalar dependencias necesarias
sudo apt-get update
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

# Instalar pyenv
curl https://pyenv.run | bash

# Añadir pyenv al PATH (añade estas líneas a tu .bashrc o .zshrc)
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"

# Reinicia tu shell o ejecuta
source ~/.bashrc  # o source ~/.zshrc si usas zsh
```

### 2. Instalar Python

```bash
# Instalar Python 3.10.2
pyenv install 3.10.2

# Seleccionar la versión instalada como global
pyenv global 3.10.2
```

### 3. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/deliver-hero.git
cd deliver-hero
```

### 4. Instalar dependencias

```bash
# Crear un entorno virtual para el proyecto
python -m venv venv

# Activar el entorno virtual
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 5. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
DATABASE_URL=postgresql://user:password@localhost:5433/dbname
SECRET_KEY=tu_clave_secreta_muy_segura
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Asegúrate de que el `DATABASE_URL` coincida con la configuración en el `docker-compose.yml`.

### 6. Levantar la base de datos con Docker Compose

Asegúrate de tener un archivo `docker-compose.yml` en la raíz de tu proyecto con el siguiente contenido:

```yaml
version: '3.8'

services:
  db:
    image: postgres:13
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: dbname
    ports:
      - "5433:5432"

volumes:
  postgres_data:
```

Luego, ejecuta:

```bash
docker-compose up -d
```

Esto iniciará un contenedor de PostgreSQL en segundo plano.
### 7. Ejecutar migraciones
Cuando la base de datos esté en funcionamiento debes ejecutar
```bash
alembic upgrade head
```

## Ejecutar la aplicación

```bash
uvicorn app.main:app --reload
```

La aplicación estará disponible en `http://localhost:8000`.

## Documentación API

Una vez que la aplicación esté en ejecución, puedes acceder a la documentación interactiva de la API en:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Desarrollo

### Crear una nueva migración

Después de hacer cambios en los modelos, crea una nueva migración con:

```bash
alembic revision --autogenerate -m "Descripción de los cambios"
```

### Aplicar migraciones

```bash
alembic upgrade head
```

## Pruebas

Para ejecutar las pruebas (asumiendo que tienes pruebas configuradas):

```bash
pytest
```

## Detener y limpiar

Cuando hayas terminado de trabajar en el proyecto, puedes detener el contenedor de la base de datos con:

```bash
docker-compose down
```

Si quieres eliminar también el volumen de datos, usa:

```bash
docker-compose down -v
```
