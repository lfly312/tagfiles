from flask import Flask

#You must assign the value of "app" before importing views because this "app" will be used in views
app = Flask(__name__)
app.config.from_object('config')

from app import views