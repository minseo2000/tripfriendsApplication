from flask import Flask, request,jsonify
import db


def create_app():
    app = Flask(__name__)


    @app.route('/ping', methods=['GET'])
    def ping():
        return 'pong'

    @app.route('/register', methods=['POST', 'GET'])
    def register():

        user_data = request.json
        db.inputUserTable(user_data)

        return '200'

    return app




if __name__ == "__main__":

    create_app().run(host='0.0.0.0', port=50002, debug=True)
