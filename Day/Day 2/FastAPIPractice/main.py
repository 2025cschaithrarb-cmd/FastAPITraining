from fastapi import FastAPI
app = FastAPI()
@app.get("/")

def home():
    return {"page": "Home"}   
@app.get("/about")
def about():
    return {"page": "About","Author": "Chaithra"}
@app.get("/health")
def health():
    return {"Status": "OK"}
#Post Request
@app.post("/create")
def create():
    return {"message": "Created"}

 #Path parameters
def get result(usn):
@app.get("/students/{usn}")
     return {"Result": "Distinction", "usn": usn}