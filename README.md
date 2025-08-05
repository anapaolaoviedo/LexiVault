# LexiVault !!!

**Store, retrieve, and query your own thoughts, quotes, or insights.**  
Welcome to **LexiVault**, your personal knowledge engine.  
This project is a minimalist, yet well-architected backend for collecting and querying structured thoughts and quotes.  
It's built for developers who value clean design and functional elegance.

---

## ✨ Key Features & Stack

- **API Endpoints**: Create, retrieve, edit, and delete entries.  
- **Querying**: Filter by tags, search by keywords, and get random entries.  
- **Core Stack**: Built with **FastAPI**, backed by **PostgreSQL** (using SQLAlchemy) for data persistence.  
- **Documentation**: Includes auto-generated API docs via Swagger/OpenAPI.  
- **Extensibility**: Ready for optional LLM integration, Docker deployment, and testing with Pytest.  

---

## 🚀 Getting Started

1. Clone the repository and set up a virtual environment.
2. Install dependencies from `requirements.txt`.
3. Configure your database by creating a `.env` file with your `DATABASE_URL`.
4. Run the application:

```bash
uvicorn app.main:app --reload