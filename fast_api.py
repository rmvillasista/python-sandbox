from fastapi import FastAPI

app = FastAPI(title="Zero to Hero API", version="1.0.0")

@app.get("/")
async def root():
    return {"status": "online", "message": "Welcome to FastAPI!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}