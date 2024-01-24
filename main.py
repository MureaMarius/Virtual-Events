from api import home
from flask import *

app = Flask(__name__, template_folder='templates')

app.add_url_rule('/', view_func=home.home_page)


def main():
    app.run()


if __name__ == '__main__':
    main()
