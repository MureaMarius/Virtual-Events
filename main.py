from flask import Flask

from authentification import signup
from authentification.signup import app


def main():
    app.run()


if __name__ == '__main__':
    main()
