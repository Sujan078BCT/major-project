# FastAPI Project - Complete REST API with Authentication

A comprehensive FastAPI project demonstrating modern Python web development practices, including authentication, database integration, validation, and testing.

## 🎯 Project Overview

This project showcases a production-ready FastAPI application with the following key features:

- **RESTful API** with CRUD operations for Items and Users
- **JWT Authentication** with password hashing
- **SQLAlchemy ORM** with SQLite database
- **Pydantic validation** with comprehensive data constraints
- **CORS middleware** for cross-origin requests
- **Comprehensive testing** with pytest
- **Modern project structure** following best practices

## 🚀 Features

### Authentication & Security
- JWT token-based authentication
- Password hashing with bcrypt
- Protected routes requiring authentication
- User registration and login endpoints

### Data Management
- **Items API**: Public read access, authenticated write operations
- **Users API**: Fully authenticated CRUD operations
- **Pagination** support for list endpoints
- **Data validation** with Pydantic schemas

### API Endpoints

#### Public Endpoints
- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /items` - List all items (with pagination)
- `GET /items/{item_id}` - Get specific item
- `POST /register` - User registration
- `POST /token` - User login

#### Protected Endpoints (Require Authentication)
- `GET /users/me` - Get current user profile
- `GET /users` - List all users
- `GET /users/{user_id}` - Get specific user
- `POST /items` - Create new item
- `PUT /items/{item_id}` - Update item
- `DELETE /items/{item_id}` - Delete item
- `PUT /users/{user_id}` - Update user
- `DELETE /users/{user_id}` - Delete user

## 🛠️ Technology Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **Pydantic** - Data validation using Python type annotations
- **JWT** - JSON Web Tokens for authentication
- **bcrypt** - Password hashing
- **pytest** - Testing framework
- **uvicorn** - ASGI server

## 📋 Prerequisites

- Python 3.9 or higher
- pip or uv package manager

## 🔧 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fastapi-project
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -e .
   # Or install dev dependencies for testing
   pip install -e ".[dev]"
   ```

4. **Initialize the database**
   ```bash
   python -m app.init_db
   ```

5. **Run the application**
   ```bash
   python -m app.main
   # Or using uvicorn directly
   uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000`

## 📚 API Documentation

Once the server is running, you can access:

- **Interactive API docs**: http://localhost:8000/docs
- **Alternative API docs**: http://localhost:8000/redoc
- **OpenAPI schema**: http://localhost:8000/openapi.json

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_auth.py -v

# Run with coverage
python -m pytest tests/ --cov=app --cov-report=html
```

### Test Coverage
The project includes comprehensive tests for:
- Authentication (login, register, token validation)
- CRUD operations for Items and Users
- Data validation and error handling
- Authorization and protected routes
- Basic API functionality

## 📁 Project Structure

```
fastapi-project/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application and routes
│   ├── models.py        # SQLAlchemy database models
│   ├── schemas.py       # Pydantic data validation schemas
│   ├── crud.py          # Database CRUD operations
│   ├── auth.py          # Authentication and security
│   ├── database.py      # Database configuration
│   ├── settings.py      # Application settings
│   └── init_db.py       # Database initialization
├── tests/
│   ├── __init__.py
│   ├── conftest.py      # Pytest fixtures
│   ├── test_auth.py     # Authentication tests
│   ├── test_items.py    # Items API tests
│   ├── test_users.py    # Users API tests
│   └── test_basic.py    # Basic API tests
├── pyproject.toml       # Project configuration and dependencies
├── README.md           # This file
└── fastapi_project.db  # SQLite database (created on first run)
```

## 🔐 Authentication Flow

1. **Register a new user**:
   ```bash
   POST /register
   {
     "username": "john_doe",
     "email": "john@example.com",
     "password": "secretpassword",
     "full_name": "John Doe"
   }
   ```

2. **Login to get access token**:
   ```bash
   POST /token
   Content-Type: application/x-www-form-urlencoded
   
   username=john_doe&password=secretpassword
   ```

3. **Use the token for authenticated requests**:
   ```bash
   GET /users/me
   Authorization: Bearer <your_access_token>
   ```

## 📝 Data Validation

The project uses Pydantic for comprehensive data validation:

- **Item validation**: Name cannot be empty, price must be positive
- **User validation**: Username required, valid email format, password minimum length
- **Update operations**: Partial updates with validation constraints

## 🎓 Learning Resources

### FastAPI Concepts Demonstrated
- **Dependency Injection**: Database sessions, authentication
- **Path Parameters**: URL path validation
- **Query Parameters**: Pagination and filtering
- **Request/Response Models**: Pydantic schemas
- **Middleware**: CORS handling
- **Error Handling**: HTTP exceptions and validation errors

### Best Practices Implemented
- **Separation of Concerns**: Models, schemas, CRUD operations
- **Type Hints**: Full type annotation throughout
- **Configuration Management**: Environment-based settings
- **Testing**: Comprehensive test coverage
- **Documentation**: Auto-generated API docs

### Key Learning Points
1. **Modern Python Web Development**: FastAPI vs traditional frameworks
2. **API Design**: RESTful principles and best practices
3. **Security**: JWT authentication and password hashing
4. **Database Integration**: SQLAlchemy ORM patterns
5. **Data Validation**: Pydantic schema design
6. **Testing**: pytest fixtures and test organization

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues or have questions:
1. Check the [FastAPI documentation](https://fastapi.tiangolo.com/)
2. Review the test files for usage examples
3. Open an issue in the repository

---

**Happy coding! 🚀**
