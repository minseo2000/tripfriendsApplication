from flask import Flask, request,jsonify
from flask_cors import CORS
import db

# have to add system clock

def create_app():
    app = Flask(__name__)
    CORS(app)

    db.makeDb()
    db.makePostTable()
    db.makeMissionTable()
    db.makeDetailPostTable()
    db.makeUserTable()
    db.makeAddPointTable()
    db.makePlaceTable()
    db.makePostCategoryTable()
    db.makeUsePointTable()


    @app.route('/ping', methods=['GET'])
    def ping():
        return 'pong'

    @app.route('/register', methods=['POST', 'GET'])
    def register():

        user_data = request.json
        db.inputUserTable(user_data)

        return '200'
    
    
    
    
    
    
    
    #----------------------------------------------------------------------------------------게시판
    @app.route('/create_post_category', methods=['POST'])
    def input_post_category_table():
        post_category_json_data = request.json

        post_category_list = []
        post_category_list.append(post_category_json_data['title'])
        post_category_list.append(post_category_json_data['post_cnt'])
        post_category_list.append(post_category_json_data['created_date'])

        db.inputPostCategoryTable(post_category_list)

        return '200'
    @app.route('/get_post_category', methods=['GET'])
    def select_post_category_table():

        category_post_data = db.selectPostCategoryTable()

        return jsonify(category_post_data)
    @app.route('/delete_post_category', methods=['POST'])
    def delete_post_category_table():
        post_category_json_data = request.json

        pid = post_category_json_data['post_category_id']

        db.deletePostCategoryTable(pid)

        return '200'

    @app.route('/create_post', methods=['POST'])
    def input_post_table():
        post_data = request.json

        post_data_list = []
        post_data_list.append(post_data['user_id'])
        post_data_list.append(post_data['board_id'])
        post_data_list.append(post_data['created_date'])
        post_data_list.append(post_data['title'])

        db.inputPostTable(post_data_list)

        return '200'

    @app.route('/get_post', methods=['GET'])
    def select_post_table():

        board_id = request.args.get('board_id')

        post_data = db.selectPostTable(board_id=board_id)
        print(post_data)
        return jsonify(post_data)
    @app.route('/delete_post', methods=['POST'])
    def delete_post_table():

        data = request.json
        post_id = data['post_id']

        db.deletePostTable(post_id)

        return '200'

    @app.route('/create_detail_post', methods=['POST'])
    def input_detail_post_table():

        detail_post_data = request.json

        detail_post_data_list = []
        detail_post_data_list.append(detail_post_data['post_id'])
        detail_post_data_list.append(detail_post_data['content'])
        detail_post_data_list.append(detail_post_data['img'])

        db.inputDetailPostTable(detail_post_data_list)

        return '200'
    @app.route('/get_detail_post', methods=['GET'])
    def select_detail_post_table():
        post_id = request.args.get('post_id')

        detail_post_data = db.selectDetailPostTable(post_id)

        return jsonify(detail_post_data)

    @app.route('/delete_detail_post', methods=['POST'])
    def delete_detail_post_table():
        data = request.json

        user_id = data['user_id']
        board_id = data['board_id']

        db.deleteDetailPostTable(user_id, board_id)

    @app.route('/get_place', methods=['GET'])
    def get_place():

        place_data = db.selectPlace()

        return jsonify(place_data)

    @app.route('/get_detail_place', methods=['GET'])
    def get_place_by_id():
        place_id = request.args.get('place_id')

        place_data = db.selectPlaceByPlaceId(place_id)

        return jsonify(place_data)

    @app.route('/get_mission', methods=['GET'])
    def select_mission_table():

        mission_data = db.selectMissionTable()

        return jsonify(mission_data)

    @app.route('/get_mission_by_id', methods=['GET'])
    def select_mission_table_by_id():
        user_id = request.args.get('user_id')

        mission_data = db.selectMissionTableById(user_id)

        return jsonify(mission_data)

    @app.route('/get_mission_by_user_mission_id', methods=['GET'])
    def select_mission_table_by_user_mission_id():
        user_id = request.args.get('user_id')
        mission_id = request.args.get('mission_id')

        mission_data = db.selectMissionTableByMissionId(user_id, mission_id)

        return jsonify(mission_data)



    return app




if __name__ == "__main__":

    create_app().run(host='0.0.0.0', port=50002, debug=True)
