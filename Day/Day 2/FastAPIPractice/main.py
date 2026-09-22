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

@app.get("/students/{usn}")
def get result(usn):
    return {"Result": "Distinction", "usn": usn}

#Path parameters with type hint

@app.get("/candidates/{rollno}")
def get_candidate(rollno: int):
     return {"Result": "Distinction", "rollno": rollno,"type": str(type(rollno))}