from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to the Cloud Health API"}


@app.get("/health")
def health():
    return {"status": "healthy"}
