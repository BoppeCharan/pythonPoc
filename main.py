from fastapi import FastAPI

from pyrebase import pyrebase

app = FastAPI()



config = {
  "apiKey": "AIzaSyDA9EU7UpJF0AgHCTbUL7rYRmqSGwjgGo0",
  "authDomain": "big-business-15632.firebaseapp.com",
  "databaseURL": "https://big-business-15632-default-rtdb.firebaseio.com",
  "projectId": "big-business-15632",
  "storageBucket": "big-business-15632.appspot.com",
  "messagingSenderId": "431498901826",
  "appId": "1:431498901826:web:d4eba4bb0f7380075af0db",
  "measurementId": "G-LKG49BC6FG",

}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
data = {
    "Name": "CharanBoppe",
    "From": "PythonAPI",
    "phoneNumber": "6309833542",
    "Code": "XXXXXX"
}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/sendFirebase")
async def sendData():
    result = db.child("Users").child("uid5").push(data)
    print(result)


@app.get("/getData")
async def getData():
    result = db.child("Users").get()
    return result.val()
