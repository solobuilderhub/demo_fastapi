# main.py
from fastapi import FastAPI
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

def get_db_connection():
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME")
    print(host, user, password, database)
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return connection

@app.post("/insert-dummy-data/")
def insert_dummy_data():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS dummy (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
    cursor.execute("INSERT INTO dummy (name) VALUES ('dummy data')")
    connection.commit()
    cursor.close()
    connection.close()
    return {"message": "Dummy data inserted successfully okay in docker!"}

@app.get("/get-dummy-data/")
def get_dummy_data():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM dummy")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return {"data": data}