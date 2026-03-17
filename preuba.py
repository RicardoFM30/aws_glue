from pymongo import MongoClient
#from dotenv import load_dotenv
import os

# load_dotenv()

usuario= "admin"
password = "admin"
cluster= "awsGlueAtlas"

cliente = MongoClient('mongodb+srv://admin:admin@awsglueatlas.jggrcfu.mongodb.net/?appName=awsGlueAtlas')

try:
   cliente.admin.command('ping')
   print("NOS CONECTAMOS CORRECTAMENTE")
except Exception as e:
   print(e)
