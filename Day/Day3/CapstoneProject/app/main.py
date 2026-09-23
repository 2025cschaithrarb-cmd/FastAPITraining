#This file is the enry point of applications
from fastapi import FastAPI
from app.config import settings
from app.database import ping_database 
#Creating fstapi app instance
app = FastAPI(title=settings.APP_NAME)
#This function runs when the server starts. It checks the DB connection.
@app.on_event("startup")
def startup_event():
    if not ping_database():
        raise RuntimeError("Could not connect to MongoDB")
    print(f"[startup]Connected to MongoDB. App:{settings.APP_NAME}")
#Checks basic helth checks API endpoint and confirms 
# GET / is running and reachable.(/ is considered as a root)
@app.get("/",tags=["Health"])
def health_check():
    return {"status":"ok","app":settings.APP_NAME}
