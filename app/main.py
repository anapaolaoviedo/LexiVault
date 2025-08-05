# app/main.py

from fastapi import FastAPI

# initialize the FastAPI app
app = FastAPI(
    title="LexiVault API",
    description="A minimalist knowledge vault for storing and querying thoughts.",
    version="0.1.0",
)

@app.get("/")
def read_root():
    """
    A simple root endpoint to confirm the API is running.
    """
    return {"message": "Welcome to LexiVault! The API is up and running."}


# Note: This file will grow as we implement the other parts of the application,
