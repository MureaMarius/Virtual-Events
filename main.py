from api import home
from api.authentification import signup, login
from flask import *

app = Flask(__name__, template_folder='templates')

app.add_url_rule('/', view_func=home.home_page)
app.add_url_rule('/create_user', view_func=signup.create_user, methods=['GET', 'POST'])
app.add_url_rule('/login', view_func=login.login, methods=['GET', 'POST'])


def main():
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()


if __name__ == '__main__':
    main()

#Abfds12234**