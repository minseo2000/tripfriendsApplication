from flask import Flask





def create_app()

    app = Flask(__name__)



    return app



if __name__ == '__main__':

    create_app().run(host='0.0.0.0', port=50000, debug=True)