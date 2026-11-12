# import dependency
from fastapi import FastAPI

# create app
app = FastAPI()

# Home Route
@app.get("/")
def home() :
    return {
        "message":"API is running"
    }

# Users Route
@app.get("/users")
def users() :
    return{
        "users": [
            "Anuj","Rohit","Saurabh"
        ]
    }