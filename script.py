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
cur.execute("DELETE FROM empleados;")
cur.execute("DELETE FROM proyectos_empleados;")
cur.execute("DELETE FROM evaluaciones;")

# Generar datos
for _ in range(NUM_REGISTROS):
    # Tabla empleados
    nombre = fake.name()
    email = fake.unique.email()
    departamento = random.choice(departamentos)
    puesto = random.choice(puestos)
    sueldo = random.randint(20000, 120000)
    antiguedad = random.randint(0, 20)
    
    cur.execute("""
        INSERT INTO empleados (nombre, email, departamento, puesto, sueldo, antiguedad)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (nombre, email, departamento, puesto, sueldo, antiguedad))
    
    # Tabla proyectos_empleados
    proyecto = random.choice(proyectos)
    horas = random.randint(10, 160)
    rol = random.choice(roles)
    
    cur.execute("""
        INSERT INTO proyectos_empleados (email, proyecto, horas_trabajadas, rol)
        VALUES (%s, %s, %s, %s)
    """, (email, proyecto, horas, rol))
    
    # Tabla evaluaciones
    rendimiento = random.randint(1, 10)
    feedback = fake.sentence(nb_words=6)
    fecha_eval = fake.date_this_year()
    
    cur.execute("""
        INSERT INTO evaluaciones (email, rendimiento, feedback_ultimo_mes, fecha_ultima_evaluacion)
        VALUES (%s, %s, %s, %s)
    """, (email, rendimiento, feedback, fecha_eval))

# Guardar cambios y cerrar
conn.commit()
cur.close()
conn.close()

print(f"Se han insertado {NUM_REGISTROS} registros en cada tabla con Faker.")