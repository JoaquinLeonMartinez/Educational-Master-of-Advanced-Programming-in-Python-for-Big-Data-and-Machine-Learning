# Author: Joaquin Leon Martinez

# Ejecutar antes el metodo GET "generate model" para que se te genere el modelo
# Ejecutar el POST llamado "insertDataWithPrediction" para que te haga la prediccion y la inserte

from fastapi import FastAPI
import pandas as pd
import json
import csv
from models import Iris, IrisNoSpecie
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

app = FastAPI()

MEDIA_ROOT = "iris_dataset.csv"
filename = 'iris_model.sav'

@app.get("/")
async def root():
    return "Bienvenido FastAPI"


@app.get("/iris/")
async def iris():
    df = pd.read_csv(MEDIA_ROOT)
    data = df.to_json(orient="index")
    data = json.loads(data)
    return data

@app.get("/generateModel/")
async def generateModel():
    df = pd.read_csv("iris_dataset.csv")
    X = df.drop(["Species"], axis = 1)
    Y = df["Species"]
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state = 0)
    clf = DecisionTreeClassifier()
    # Entreno con los datos que se indican entre parentesis
    clf.fit(X_train, Y_train)
    # Ahora ya esta entrenado, toca guardarlo
    pickle.dump(clf, open(filename, 'wb'))
    
    return "Se ha entrenado y guardado el modelo exitosamente"

@app.post("/insertDataWithPrediction/")
async def insertDataWithPrediction(item: IrisNoSpecie):
    
    # 1 - Cargamos el modelo guardado previamente
    loaded_model = pickle.load(open(filename, 'rb'))
    # 2 - Hacemos la prediccion con los datos obtenidos del request
    entryData = [[item.SepalLengthCm, item.SepalWidthCm, item.PetalLengthCm, item.PetalWidthCm]]
    prediction = loaded_model.predict(entryData)
    # 3 - Lo convertimos a string
    prediction = ''.join(prediction)
    
    with open(MEDIA_ROOT, 'a', newline = '') as csvfile:
        fieldnames = ['SepalLengthCm','SepalWidthCm',
                      'PetalLengthCm','PetalWidthCm','Species']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'SepalLengthCm': item.SepalLengthCm,
                        'SepalWidthCm': item.SepalWidthCm,
                        'PetalLengthCm': item.PetalLengthCm,
                        'PetalWidthCm': item.PetalWidthCm,
                        'Species': prediction})
    return prediction
    
    
@app.post("/insertData/")
async def insertData(item: Iris):
    with open(MEDIA_ROOT, 'a', newline = '') as csvfile:
        fieldnames = ['SepalLengthCm','SepalWidthCm',
                      'PetalLengthCm','PetalWidthCm','Species']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'SepalLengthCm': item.SepalLengthCm,
                        'SepalWidthCm': item.SepalWidthCm,
                        'PetalLengthCm': item.PetalLengthCm,
                        'PetalWidthCm': item.PetalWidthCm,
                        'Species': item.Species})
    return item

@app.put("/updateData/{item_id}")
async def updateData(item_id: int, item: Iris):
    df = pd.read_csv(MEDIA_ROOT)
    if item_id >= df.size | item_id == 0:
        item_id = 1 # Por defecto borramos el primer elemento
    
    df.loc[df.index[item_id], 'SepalLengthCm'] = item.SepalLengthCm
    df.loc[df.index[item_id], 'SepalWidthCm'] = item.SepalWidthCm
    df.loc[df.index[item_id], 'PetalLengthCm'] = item.PetalLengthCm
    df.loc[df.index[item_id], 'PetalWidthCm'] = item.PetalWidthCm
    df.loc[df.index[item_id], 'Species'] = item.Species
    df.to_csv(MEDIA_ROOT, index=False)
    return {"item_id": item_id, **item.dict()}


@app.delete("/deleteData/")
async def deleteData():
    df = pd.read_csv(MEDIA_ROOT)
    df.drop(df.index[-1], inplace=True)
    df.to_csv(MEDIA_ROOT, index=False)
    return "Eliminado"