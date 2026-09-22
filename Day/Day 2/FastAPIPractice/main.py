from fastapi import FastAPI
app = FastAPI()
@app.get("/")

def hoome():
    return {"page": "Home"}   
@app.get("/about")
def about():
    return {"page": "About","Author": "Chaithra"}
@app.get("/health")
def health():
    return {"Status": "OK"}