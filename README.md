# BYHack2025

This is the repository for the tatar.by hackathon project. The project is organized with a clean separation between frontend and backend components.

## Project Structure

```
├── frontend/          # Frontend application (empty, ready for development)
├── backend/           # FastAPI backend application
└── README.md          # This file
```

### Frontend

The `frontend/` directory is currently empty and ready for frontend development. You can use any frontend framework of your choice (React, Vue.js, Angular, etc.).

### Backend

The `backend/` directory contains a full-featured FastAPI application following modern Python project best practices. The structure is based on the [one-zero-eight/workshops](https://github.com/one-zero-eight/workshops) reference repository.

Key features:
- ✅ FastAPI application with modern async/await patterns
- ✅ Structured project layout with modules, API routes, and storage layers
- ✅ Database migrations using Alembic
- ✅ Docker support for development and production
- ✅ Comprehensive configuration management
- ✅ Logging and error handling
- ✅ Health check endpoint

See the [backend README](backend/README.md) for detailed setup and development instructions.

## Quick Start

### Backend Development

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

3. Set up configuration:
   ```bash
   cp settings.example.yaml settings.yaml
   # Edit settings.yaml with your configuration
   ```

4. Run the development server:
   ```bash
   uv run python -m src.api
   ```

The API will be available at `http://localhost:8005` with:
- Swagger documentation: `http://localhost:8005/docs`
- Health check: `http://localhost:8005/health`

### Frontend Development

The frontend directory is ready for your chosen frontend framework. You can initialize any frontend project in the `frontend/` directory.

## Development Workflow

1. **Backend**: Develop your API endpoints in the `backend/src/modules/` directory
2. **Frontend**: Build your user interface in the `frontend/` directory
3. **Integration**: Connect your frontend to the backend API

## Contributing

This project structure provides a solid foundation for hackathon development with:
- Clear separation of concerns
- Modern development practices
- Easy deployment options
- Comprehensive tooling support
