from flask import Flask

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')  # Используем конфигурацию для разработки

from app import routes