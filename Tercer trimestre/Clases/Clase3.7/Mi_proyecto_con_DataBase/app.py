import flask from Flask, request, jsonify, return, return_templates #importar flask
import psycopg2 #importar psycopg2 para conectar a la base de datos PostgreSQL
from psycopg2.extras import RealDictCursor #importar RealDictCursor para obtener resultados en formato diccionario
import os #importar os para manejar variables de entorno
from date time import datetime #importar datetime para manejar fechas y horas

# Configuración de la aplicación
app = Flask(__name__)

DB_CONFIG = {
    'host':'localhost',
    'database':'mi_base_de_datosMi_proyecto_dataBase',
    'user':'postgres',
    'password':'123456',
    'port': '5432',
}

def conectar_db(): #crea una  función para conectar con mi base de datos
    try: #intentar conectar a la base de datos
        conexion= psycopg2.connect(**DB_CONFIG) #importar la librería psycopg2 y conectar a la base de datos con los parámetros definidos en DB_CONFIG
        return conexion #Si ocurre un error lo muestra en consola
    except psycopg2.Error as e:
        return None #retorna un  mensaje si8 falla la conexion de postgre
    
    #Crear la tabla Usuario
def crear_tabla_usuario():
    conexion= conectar_db() #conectar a la base de datos
    if conexion:
        cursor= conexion.cursor() #crear un cursor para ejecutar consultas
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Usuario (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """) #crear la tabla Usuario si no existe
        conexion.commit() #guardar los cambios en la base de datos
        cursor.close() #cerrar el cursor
        conexion.close() #cerrar la conexión

#Ruta principal del sitio web
@app.route('/')
def inicio():
    return return_templates('index.html') #retorna el template index.html

#ruta para guardar los datos de una conexion
@app.route('/guardar_usuario', methods=['POST'])
def guardar_usuario():
    try:
        conexion= conectar_db() #conectar a la base de datos
        if conexion is None:
            return
        
        #obtiene los datos enviados en Json

        datos= request.get_json() #obtener los datos enviados en formato JSON
        nombre= datos.get('nombre'.strip) #obtener el nombre del usuario
        email= datos.get('email'.strip) #obtener el email del usuario
        fecha_creacion= datetime.now() #obtener la fecha y hora actual

    #validar que el nombre y el correo no esten vacíos
        if not nombre or not email:
            return jsonify({'mensaje': 'El nombre y el correo son obligatorios'}), 400
        
        #Crear un cursor para ejecutar consultas

        cursor= conexion.cursor() #crear un cursor para ejecutar consultas
        sql_insert= """
        INSERT INTO Usuario (nombre, email, fecha_creacion)
        VALUES (%s, %s, %s)
        RETURNING id;
        """ #conexion o consulta a la tabla Usuario

        #ejecutar las consultas con los valores recibidos 

        cursor.execute(sql_insert, (nombre, email, fecha_creacion))
        usuario_id= cursor.fetchone()[0] #obtener el id del usuario insertado

        conexion.commit() #guardar los cambios en la base de datos
        cursor.close() #cerrar el cursor
        conexion.close() #cerrar la conexión

        #devuelve un mensaje de exito con el id generado
        return jsonify({'mensaje': 'Usuario guardado exitosamente', 'usuario_id': usuario_id}), 