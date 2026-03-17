from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, current_date
from faker import Faker
import random
import pandas as pd

# Configuración
fake = Faker('es_ES')
NUM_REGISTROS = 50

# Generar datos de evaluaciones
emails = [fake.unique.email() for _ in range(NUM_REGISTROS)]
rendimiento = [random.randint(1, 10) for _ in range(NUM_REGISTROS)]
feedback = [fake.sentence(nb_words=6) for _ in range(NUM_REGISTROS)]
fecha_eval = pd.to_datetime([fake.date_this_year() for _ in range(NUM_REGISTROS)])

# Crear DataFrame con pandas
df = pd.DataFrame({
    "email": emails,
    "rendimiento": rendimiento,
    "feedback_ultimo_mes": feedback,
    "fecha_ultima_evaluacion": fecha_eval
})

# Crear sesión Spark
spark = SparkSession.builder \
    .appName("GlueMongoDB") \
    .config("spark.mongodb.output.uri", "mongodb+srv://usuario:contraseña@cluster0.mongodb.net/empresa.evaluaciones") \
    .getOrCreate()

# Convertir pandas a Spark DataFrame
sdf = spark.createDataFrame(df)

# Guardar en MongoDB Atlas
sdf.write.format("mongo").mode("append").save()

print("Datos cargados en MongoDB Atlas con éxito")