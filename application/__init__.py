import os

from flask import Flask
from dotenv import load_dotenv
from database.connector import ConnectionToMySqlServer

load_dotenv(dotenv_path="config.env")
app = Flask(__name__, template_folder='templates', static_folder='/static')

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

my_connection = ConnectionToMySqlServer(os.environ.get("DB_USERNAME"), os.environ.get("DB_PASSWORD"))
my_connection.connect_to_mysql_server()

cursor = my_connection.connection.cursor()

from api import account, events_api