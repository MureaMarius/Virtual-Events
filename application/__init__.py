from flask import Flask

from database.connector import ConnectionToMySqlServer
from utilities import constants

app = Flask(__name__, template_folder='templates', static_folder='/static')

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

my_connection = ConnectionToMySqlServer(constants.Db_constants.DB_USERNAME, constants.Db_constants.DB_PASSWORD)
my_connection.connect_to_mysql_server()

from api import authentification