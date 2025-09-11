# BYHack2025 Backend

This is the FastAPI backend for the BYHack2025 project. The structure follows modern Python project best practices and is based on the [one-zero-eight/workshops](https://github.com/one-zero-eight/workshops) reference repository.

## Project Structure

```
backend/
├── src/                    # Main application source code
│   ├── api/               # FastAPI application and routing
│   │   ├── app.py         # Main FastAPI application
│   │   ├── dependencies.py # Dependency injection
│   │   ├── docs.py        # API documentation configuration
│   │   ├── exceptions.py  # Custom exception handling
│   │   └── lifespan.py    # Application lifecycle management
│   ├── modules/           # Business logic modules
│   ├── storages/          # Database and storage related code
│   ├── tests/             # Test modules
│   ├── config.py          # Configuration loading
│   ├── config_schema.py   # Configuration schema definitions
│   ├── logging_.py        # Logging configuration
│   └── prepare.py         # Environment setup utilities
├── alembic/               # Database migration scripts
├── pyproject.toml         # Project dependencies and configuration
├── alembic.ini            # Alembic configuration
├── settings.example.yaml  # Example configuration file
├── settings.schema.yaml   # Configuration schema
├── logging.yaml           # Logging configuration
├── Dockerfile             # Docker container configuration
└── docker-compose.yml     # Local development docker setup
```

## Getting Started

### Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Installation

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   # Using uv (recommended)
   uv sync

   # Or using pip
   pip install -e .
   ```

3. Copy the example settings:
   ```bash
   cp settings.example.yaml settings.yaml
   ```

4. Update `settings.yaml` with your configuration values.

### Running the Application

#### Using uv:
```bash
uv run python -m src.api
```

#### Using Python directly:
```bash
python -m src.api
```

The API will be available at `http://localhost:8005`

### Using Docker

#### Development with Docker Compose:
```bash
docker compose up --build
```

## Development

### Adding New Modules

1. Create a new module in `src/modules/`:
   ```
   src/modules/your_module/
   ├── __init__.py
   ├── routes.py      # FastAPI routes
   ├── schemas.py     # Pydantic models
   ├── repository.py  # Data access layer
   └── service.py     # Business logic
   ```

2. Add your router to `src/api/app.py`:
   ```python
   from src.modules.your_module.routes import router as your_module_router
   app.include_router(your_module_router)
   ```

### Database Migrations

Generate a new migration:
```bash
alembic revision --autogenerate -m "your migration message"
```

Apply migrations:
```bash
alembic upgrade head
```

### Testing

Run tests:
```bash
# Using uv
uv run pytest

# Using Python directly
pytest
```

## Configuration

The application uses YAML configuration files. See `settings.example.yaml` for available options.

Key configuration sections:
- `db_url`: Database connection string
- `accounts`: Authentication service configuration
- `api_key`: API access key for external services
- `cors_allow_origin_regex`: CORS configuration

## API Documentation

Once the application is running, you can access:
- Swagger UI: `http://localhost:8005/docs`
- ReDoc: `http://localhost:8005/redoc`
- OpenAPI JSON: `http://localhost:8005/openapi.json`

## Health Check

The API includes a health check endpoint at `/health` that returns the service status.