import json
import os

FILE = "data.json"

def load():
    if not os.path.exists(FILE):
        with open(FILE, "w") as f:
            json.dump([], f)
    with open(FILE, "r") as f:
        return json.load(f)

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_definicions():
    return load()

def insert_definicion(termino, definicion):
    data = load()

    # Si existe, actualiza
    for item in data:
        if item["termino"].lower() == termino.lower():
            item["definicion"] = definicion
            save(data)
            return

    # Si no existe, crea nuevo
    new_id = max([x["id"] for x in data], default=0) + 1
    data.append({
        "id": new_id,
        "termino": termino,
        "definicion": definicion
    })
    save(data)

def delete_definicion(id):
    data = load()
    data = [x for x in data if x["id"] != id]
    save(data)

