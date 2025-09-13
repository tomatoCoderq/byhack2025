# 🌟 ByHack2025 - Interactive Storytelling Platform

[![Python](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.112+-green.svg)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-blue.svg)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-Integrated-orange.svg)](https://openai.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Hackathon](https://img.shields.io/badge/Hackathon-tatar.by-red.svg)](https://tatar.by/)

Интерактивная платформа для создания историй с ИИ, разработанная для хакатона tatar.by 2025. Платформа позволяет пользователям создавать увлекательные истории с помощью персонажей и искусственного интеллекта.

## 🚀 Описание проекта

ByHack2025 — это инновационная платформа для интерактивного повествования, которая объединяет творчество пользователей с возможностями искусственного интеллекта. Пользователи могут создавать персонажей, начинать сессии историй и взаимодействовать с ИИ для создания уникальных повествований.

### ✨ Основные возможности

- 👤 **Управление пользователями**: Регистрация и авторизация пользователей
- 🎭 **Система персонажей**: Создание и управление персонажами с описаниями и аватарами
- 📖 **Интерактивные истории**: Создание сессий историй с выбранными персонажами
- 🤖 **ИИ-интеграция**: Генерация историй с помощью OpenAI API
- 🗄️ **База данных**: Хранение данных в PostgreSQL
- 🐳 **Docker**: Контейнеризация для легкого развертывания

### 🚧 Текущий статус

**Готово:**
- ✅ Backend API с FastAPI
- ✅ Система управления пользователями
- ✅ CRUD операции для персонажей
- ✅ Управление сессиями историй
- ✅ Интеграция с базой данных PostgreSQL
- ✅ Docker конфигурация
- ✅ Структура для интеграции с OpenAI

**В разработке:**
- 🔄 Frontend интерфейс
- 🔄 Полная интеграция с OpenAI API для генерации историй
- 🔄 Система аутентификации и авторизации
- 🔄 Расширенные возможности персонажей

## 🛠️ Технический стек

### Backend
- **FastAPI** - Современный веб-фреймворк для Python
- **SQLModel** - ORM для работы с базой данных
- **PostgreSQL** - Реляционная база данных
- **Alembic** - Миграции базы данных
- **Pydantic** - Валидация данных
- **Uvicorn** - ASGI сервер
- **OpenAI API** - Генерация контента с помощью ИИ

### Инфраструктура
- **Docker & Docker Compose** - Контейнеризация
- **uv** - Быстрый менеджер пакетов Python

### Планируемый Frontend
- Современный фронтенд (в разработке)

## ⚙️ Конфигурация

### Переменные окружения

Приложение использует YAML файл конфигурации (`settings.yaml`). Основные параметры:

| Параметр | Описание | Обязательный | Пример |
|----------|----------|--------------|---------|
| `db_url` | URL подключения к PostgreSQL | ✅ | `postgresql+asyncpg://user:pass@host:5432/db` |
| `openai_api_key` | Ключ API OpenAI | ✅ | `sk-...` |
| `cors_allow_origin_regex` | Регекс для CORS | ❌ | `.*` (разрешить все) |
| `app_root_path` | Префикс пути API | ❌ | `/api/v1` |

### Переменные окружения для Docker

Вы также можете использовать переменные окружения:

```bash
export DB_URL="postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"
export OPENAI_API_KEY="your_api_key"
export CORS_ALLOW_ORIGIN_REGEX=".*"
```

## 🏗️ Архитектура

```
├── backend/                 # FastAPI приложение
│   ├── src/
│   │   ├── api/            # API endpoints и приложение
│   │   │   ├── app.py      # Главное FastAPI приложение
│   │   │   └── __main__.py # Точка входа для uvicorn
│   │   ├── modules/        # Бизнес-логика
│   │   │   ├── users/      # Управление пользователями
│   │   │   │   ├── routes.py      # API endpoints
│   │   │   │   ├── repository.py  # Слой данных
│   │   │   │   └── schemas.py     # Pydantic модели
│   │   │   ├── characters/ # Управление персонажами
│   │   │   └── stories/    # Сессии историй
│   │   ├── storages/       # Слой данных
│   │   │   └── sql/        # PostgreSQL модели
│   │   │       ├── models.py      # SQLModel модели
│   │   │       └── dependencies.py # DI для сессий БД
│   │   ├── config.py       # Конфигурация приложения
│   │   └── config_schema.py # Схема конфигурации
│   ├── migrations/         # Миграции базы данных (Alembic)
│   ├── settings.example.yaml # Пример конфигурации
│   ├── pyproject.toml      # Зависимости Python (uv)
│   ├── requirements.txt    # Зависимости Python (pip)
│   └── docker-compose.yml  # Docker конфигурация
└── frontend/               # Фронтенд (в планах)
```

## 🚀 Быстрый старт

### Предварительные требования

- Python 3.12+ (рекомендуется 3.13+)
- Docker и Docker Compose
- uv (рекомендуется) или pip

### Установка и запуск

1. **Клонирование репозитория**
   ```bash
   git clone https://github.com/tomatoCoderq/byhack2025.git
   cd byhack2025
   ```

2. **Настройка backend**
   
   **Вариант A: С uv (рекомендуется)**
   ```bash
   cd backend
   
   # Установка uv (если не установлен)
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # Установка зависимостей
   uv sync
   ```
   
   **Вариант B: С pip**
   ```bash
   cd backend
   
   # Создание виртуального окружения
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # или venv\Scripts\activate на Windows
   
   # Установка зависимостей
   pip install -r requirements.txt
   ```

3. **Запуск базы данных**
   ```bash
   # В директории backend
   docker-compose up -d db
   ```

4. **Настройка конфигурации**
   ```bash
   # Скопируйте файл примера конфигурации
   cp settings.example.yaml settings.yaml
   
   # Отредактируйте settings.yaml и укажите ваши значения:
   # - db_url: URL подключения к PostgreSQL
   # - openai_api_key: Ваш ключ OpenAI API
   # - cors_allow_origin_regex: Разрешенные домены для CORS
   ```
   
   Или создайте файл вручную:
   ```bash
   cat > settings.yaml << EOF
   db_url: "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"
   openai_api_key: "your_openai_api_key_here"
   cors_allow_origin_regex: ".*"
   EOF
   ```

5. **Запуск миграций** (если необходимо)
   ```bash
   # С uv
   uv run alembic upgrade head
   
   # С pip (в активированном venv)
   python -m alembic upgrade head
   ```

6. **Запуск API сервера**
   ```bash
   # С uv
   uv run -m src.api --reload
   
   # С pip (в активированном venv)
   python -m src.api --reload
   ```

7. **Открыть в браузере**
   - API: http://localhost:8000
   - Документация API: http://localhost:8000/docs
   - Альтернативная документация: http://localhost:8000/redoc

## 📚 API Документация

### Основные эндпоинты

#### Пользователи (`/users`)
- `POST /users/register` - Регистрация нового пользователя
- `POST /users/login` - Авторизация пользователя (демо)

#### Персонажи (`/characters`)
- `GET /characters` - Список всех персонажей
- `GET /characters/{id}` - Получение персонажа по ID
- `POST /characters` - Создание нового персонажа

#### Истории (`/stories`)
- `POST /stories` - Создание новой сессии истории
- `GET /stories` - Список сессий историй
- `GET /stories/{id}` - Получение сессии истории по ID
- `PATCH /stories/{id}` - Обновление статуса сессии

#### Система (`/`)
- `GET /` - Проверка статуса API
- `GET /health` - Проверка здоровья системы

### Примеры запросов

**Регистрация пользователя:**
```bash
curl -X POST "http://localhost:8000/users/register" \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice"}'
```

**Создание персонажа:**
```bash
curl -X POST "http://localhost:8000/characters" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Волшебник Алдрик",
    "description": "Мудрый волшебник из древнего леса",
    "avatar_url": "https://example.com/wizard.jpg"
  }'
```

**Начало сессии истории:**
```bash
curl -X POST "http://localhost:8000/stories" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "your-user-uuid",
    "character_id": "character-uuid"
  }'
```

## 🗄️ Модель данных

### User (Пользователь)
- `id` (UUID) - Уникальный идентификатор
- `name` (str) - Имя пользователя

### Character (Персонаж)
- `id` (UUID) - Уникальный идентификатор
- `name` (str) - Имя персонажа
- `description` (str, optional) - Описание персонажа
- `avatar_url` (str, optional) - URL аватара

### StorySession (Сессия истории)
- `id` (UUID) - Уникальный идентификатор
- `user_id` (UUID) - ID пользователя
- `character_id` (UUID) - ID персонажа
- `created_at` (datetime) - Время создания
- `status` (enum) - Статус: `active`, `completed`, `cancelled`

## 🔧 Разработка

### Структура проекта

- **Модульная архитектура**: Каждый модуль (users, characters, stories) изолирован
- **Слои абстракции**: API → Business Logic → Repository → Database
- **Dependency Injection**: Использование FastAPI DI для сессий БД
- **Type Safety**: Полная типизация с Pydantic и SQLModel

### Полезные команды

```bash
# Установка зависимостей разработки
uv sync --dev
# или с pip: pip install -r requirements.txt

# Линтинг кода
uv run ruff check .
# или с pip: python -m ruff check .

# Форматирование кода
uv run ruff format .
# или с pip: python -m ruff format .

# Создание новой миграции
uv run alembic revision --autogenerate -m "Description"
# или с pip: python -m alembic revision --autogenerate -m "Description"

# Применение миграций
uv run alembic upgrade head
# или с pip: python -m alembic upgrade head

# Запуск с автоперезагрузкой
uv run -m src.api --reload
# или с pip: python -m src.api --reload
```

## 🐛 Устранение неисправностей

### Часто встречающиеся проблемы

**1. Ошибка подключения к базе данных**
```bash
# Убедитесь, что PostgreSQL запущен
docker-compose ps

# Перезапустите базу данных
docker-compose down db && docker-compose up -d db

# Проверьте URL подключения в settings.yaml
```

**2. Отсутствует файл settings.yaml**
```bash
# Скопируйте файл примера
cp settings.example.yaml settings.yaml

# Отредактируйте необходимые значения
```

**3. Модуль не найден**
```bash
# Убедитесь, что находитесь в директории backend
cd backend

# Установите зависимости
uv sync  # или pip install -r requirements.txt
```

**4. Ошибка миграций**
```bash
# Сбросьте миграции (ОСТОРОЖНО: удалит данные)
docker-compose down -v
docker-compose up -d db
uv run alembic upgrade head
```

## 🤝 Участие в разработке

1. Форкните репозиторий
2. Создайте ветку для новой функции (`git checkout -b feature/amazing-feature`)
3. Зафиксируйте изменения (`git commit -m 'Add amazing feature'`)
4. Отправьте ветку (`git push origin feature/amazing-feature`)
5. Откройте Pull Request

### Стандарты кода

- Используйте **ruff** для линтинга и форматирования
- Следуйте **PEP 8** стандартам
- Добавляйте типы ко всем функциям
- Пишите понятные docstrings
- Покрывайте код тестами

## 📝 Лицензия

Этот проект лицензирован под MIT License - см. файл [LICENSE](LICENSE) для деталей.

## 👥 Команда

Проект разработан для хакатона **tatar.by 2025**.

## 🙏 Благодарности

- Организаторам хакатона tatar.by
- Команде FastAPI за отличный фреймворк
- OpenAI за API для генерации контента
- Сообществу Python за отличные инструменты

---

**Сделано с ❤️ для хакатона tatar.by 2025**
