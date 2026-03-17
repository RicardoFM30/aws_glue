from faker import Faker
import random
import pymysql  # Para conectarnos a MariaDB RDS

# Configuración
fake = Faker('es_ES')  # Español
NUM_REGISTROS = 50

# Conexión a MariaDB RDS
conn = pymysql.connect(
    host='rds-empleados.ctycw62ymi0u.us-east-1.rds.amazonaws.com',
    user='admin',
    password='12345678',
    database='empleados_db',
    port=3306,
)

cur = conn.cursor()

# Datos posibles
departamentos = ['Ventas', 'Marketing', 'IT', 'Recursos Humanos', 'Finanzas']
puestos = ['Analista', 'Developer', 'Tester', 'Manager', 'Lead']
proyectos = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Omega']
roles = ['Developer', 'Tester', 'Analyst', 'Manager', 'Lead']

# Limpiar tablas antes de insertar
cur.execute("DELETE FROM proyectos_empleados;")

# Generar datos
for _ in range(NUM_REGISTROS):
    # Tabla proyectos_empleados
    proyecto = random.choice(proyectos)
    horas = random.randint(10, 160)
    rol = random.choice(roles)
    
    cur.execute("""
        INSERT INTO proyectos_empleados (email, proyecto, horas_trabajadas, rol)
        VALUES (%s, %s, %s, %s)
    """, (email, proyecto, horas, rol))
    
# Guardar cambios y cerrar
conn.commit()
cur.close()
conn.close()

print(f"Se han insertado {NUM_REGISTROS} registros en cada tabla con Faker.")