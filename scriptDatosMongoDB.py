from pymongo import MongoClient
from dotenv import load_dotenv
from faker import Faker
import random
import os
from datetime import datetime

# Cargar variables de entorno
load_dotenv()

# Variables
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_CLUSTER = os.getenv("MONGO_CLUSTER")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

# URI conexión
uri = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_CLUSTER}/?retryWrites=true&w=majority"

# Conexión
client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("✅ Conectado a MongoDB Atlas")
except Exception as e:
    print("❌ Error de conexión:", e)
    exit()

# Seleccionar DB y colección
db = client[MONGO_DB]
coleccion = db[MONGO_COLLECTION]

# Limpiar colección (opcional)
coleccion.delete_many({})

# Faker
fake = Faker('es_ES')
NUM_REGISTROS = 50

# Generar datos
documentos = []

for _ in range(NUM_REGISTROS):
    doc = {
        "email": fake.unique.email(),
        "rendimiento": random.randint(1, 10),
        "feedback_ultimo_mes": fake.sentence(nb_words=6),
        "fecha_ultima_evaluacion": datetime.combine(
            fake.date_this_year(),
            datetime.min.time()
        )
    }
    documentos.append(doc)

# Insertar en MongoDB
resultado = coleccion.insert_many(documentos)

print(f"✅ Insertados {len(resultado.inserted_ids)} documentos en MongoDB")