# Author: Joaquin Leon Martinez

# Ejecutar antes el metodo GET "Create model" para que se te genere el modelo
# Ejecutar el POST llamado "insertData" para que te haga la prediccion y la inserte
'''
Ejemplo de body para la peticion:
{
    "SepalLengthCm": 1,
    "SepalWidthCm": 3,
    "PetalLengthCm": 2,
    "PetalWidthCm": 1
}
'''

from flask import Flask, request
import pandas as pd
import json
import csv
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

filename = 'iris_model.sav'
app= Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bienvenido a Flask"

@app.route("/iris/", methods=["GET"])
def irisData():
    df = pd.read_csv("iris_dataset.csv")
    describe = df.describe().to_json(orient="index")
    describe = json.loads(describe)
    return describe

@app.route("/createModel/", methods=["GET"])
def createModelAndSave(): 
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


@app.route("/insertData/", methods=["POST"])
def insertData(): # Suponemos que e input son los 4 valores sin la especie
    data = request.data
    data = json.loads(data)
    
    # 1 - Cargamos el modelo guardado previamente
    loaded_model = pickle.load(open(filename, 'rb'))
    # 2 - Hacemos la prediccion con los datos obtenidos del request
    entryData = [[data['SepalLengthCm'], data['SepalWidthCm'], data['PetalLengthCm'], data['PetalWidthCm']]]
    prediction = loaded_model.predict(entryData)
    # 3 - Lo convertimos a string
    prediction = ''.join(prediction)
    
    
    with open("iris_dataset.csv", "a", newline="") as csvfile:
        fieldnames = ['SepalLengthCm', 'SepalWidthCm',
                      'PetalLengthCm', 'PetalWidthCm', 'Species']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
            'SepalLengthCm': data['SepalLengthCm'],
            'SepalWidthCm': data['SepalWidthCm'],
            'PetalLengthCm': data['PetalLengthCm'],
            'PetalWidthCm': data['PetalWidthCm'],
            'Species': prediction})
    
    return prediction
     

@app.route("/updateData/", methods=["PUT"])
def updateData():
    data = request.data
    data = json.loads(data)
    df = pd.read_csv("iris_dataset.csv")
    df.loc[df.index[-1], "SepalLengthCm"] = data["SepalLengthCm"]
    df.loc[df.index[-1], "SepalWidthCm"] = data["SepalWidthCm"]
    df.loc[df.index[-1], "PetalLengthCm"] = data["PetalLengthCm"]
    df.loc[df.index[-1], "PetalWidthCm"] = data["PetalWidthCm"]
    df.loc[df.index[-1], "Species"] = data["Species"]
    
    df.to_csv("iris_dataset.csv", index=False)
    result = df.iloc[-1].to_json(orient="index")
    return result
    

@app.route("/deleteData/", methods=["DELETE"])
def deleteData():    
    df = pd.read_csv("iris_dataset.csv")
    df.drop(df.index[-1], inplace=True)
    df.to_csv("iris_dataset.csv", index=False)
    result = df.iloc[-1].to_json(orient="index")
    return json.loads(result)


if __name__ == "__main__":
    app.run(debug=True)
    
    