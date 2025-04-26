from flask import Flask, request, jsonify
from dotenv import load_dotenv
from config import DevelopmentConfig
from app import app
load_dotenv() # Загрузка данных из .env файла

@app.route("/")
def index():
    return 'Тест Flask API'

if __name__ == '__main__':
    app.run()
