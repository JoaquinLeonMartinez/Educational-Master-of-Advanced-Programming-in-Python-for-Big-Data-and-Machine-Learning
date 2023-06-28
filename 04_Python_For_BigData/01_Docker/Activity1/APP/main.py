from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()
client = MongoClient("mongodb://localhost:80") #27017
db = client["Actividad_1_Joaquin_Leon_Martinez"]
collection = db["mycollection"]

@app.get("/")
async def root():
    return {"message":"Actividad 1 con mongoDB"}#data["message"]