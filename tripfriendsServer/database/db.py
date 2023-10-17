import pymysql

'''
host = '127.0.0.1'
user = 'root'
password = '1693'
database = 'tripfriendsDB'
'''

print('host, user, password, database 순으로 스페이로 나눠 입력하세요')
host, user, password, database = input('').split(' ')

def connectToDb():

    try:
    # 데이터베이스 연결
        connection = pymysql.connect(host=host, user=user, password=password, database=database)
    except pymysql.MySQLError as E:
        print(E)
    return connection
def makeDb():

    try:
        # 데이터베이스 연결
        connection = pymysql.connect(host=host, user=user, password=password)

        # 커서 생성
        cursor = connection.cursor()

        database = 'tripfriendsDB'
        # 데이터베이스를 만들 때 IF NOT EXISTS를 사용하여 이미 존재하는 경우 무시
        create_db_query = f"CREATE DATABASE IF NOT EXISTS {database}"
        cursor.execute(create_db_query)

        print(f"데이터베이스 '{database}'가 생성되었습니다.")

    except Exception as e:
        print(f"데이터베이스 생성 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()
def makePlaceTable():



    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 테이블 생성 쿼리 작성
        create_table_query = """
        CREATE TABLE IF NOT EXISTS place_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            representative_url VARCHAR(255),
            address VARCHAR(255),
            open_time VARCHAR(255),
            close_time VARCHAR(255),
            name VARCHAR(255),
            content VARCHAR(255),
            created_date VARCHAR(255),
            hasMission VARCHAR(255),
            missionId VARCHAR(255)
        )
        """

        # 테이블 생성
        cursor.execute(create_table_query)

        print("Place 테이블이 생성되었습니다.")

    except Exception as e:
        print(f"Place 테이블 생성 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()
def makeUserTable():



    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 테이블 생성 쿼리 작성
        create_table_query = """
        CREATE TABLE IF NOT EXISTS user_table (
            id VARCHAR(255) PRIMARY KEY,
            profile_url VARCHAR(255),
            name VARCHAR(255) unique key,
            email VARCHAR(255),
            point int,
            ph_num VARCHAR(255),
            created_date VARCHAR(255),
            mission_clear_id json,
            mission_ing_id json
        )
        """

        # 테이블 생성
        cursor.execute(create_table_query)

        print("User 테이블이 생성되었습니다.")

    except Exception as e:
        print(f"User 테이블 생성 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()
def makeMissionTable():

    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 테이블 생성 쿼리 작성
        create_table_query = """
        CREATE TABLE IF NOT EXISTS mission_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            level int,
            content VARCHAR(255),
            point int,
            longitude int,
            latitude int,
            place_id int,
            user_id varchar(255)
        )
        """

        # 테이블 생성
        cursor.execute(create_table_query)

        print("Mission 테이블이 생성되었습니다.")

    except Exception as e:
        print(f" Mission 테이블 생성 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()
def makePostCategoryTable():



    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 테이블 생성 쿼리 작성
        create_table_query = """
        CREATE TABLE IF NOT EXISTS post_category_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            created_date VARCHAR(255),
            title VARCHAR(255),
            post_cnt int
        )
        """

        # 테이블 생성
        cursor.execute(create_table_query)

        print("PostCategory 테이블이 생성되었습니다.")

    except Exception as e:
        print(f"PostCategory테이블 생성 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()
def makePostTable():



    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 테이블 생성 쿼리 작성
        create_table_query = """
        CREATE TABLE IF NOT EXISTS post_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id varchar(255),
            board_id int,
            created_date varchar(255),
            title varchar(255)
        )
        """

        # 테이블 생성
        cursor.execute(create_table_query)

        print("Post 테이블이 생성되었습니다.")

    except Exception as e:
        print(f"Post 테이블 생성 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()
def makeDetailPostTable():



    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 테이블 생성 쿼리 작성
        create_table_query = """
        CREATE TABLE IF NOT EXISTS detail_post_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            post_id int,
            content varchar(255),
            img varchar(255)
        )
        """

        # 테이블 생성
        cursor.execute(create_table_query)

        print("DetailPost 테이블이 생성되었습니다.")

    except Exception as e:
        print(f"DetailPost 테이블 생성 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()
def makeUsePointTable():



    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 테이블 생성 쿼리 작성
        create_table_query = """
        CREATE TABLE IF NOT EXISTS use_point_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            point int,
            user_id int
        )
        """

        # 테이블 생성
        cursor.execute(create_table_query)

        print("use_point 테이블이 생성되었습니다.")

    except Exception as e:
        print(f"use_point 테이블 생성 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()
def makeAddPointTable():



    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 테이블 생성 쿼리 작성
        create_table_query = """
        CREATE TABLE IF NOT EXISTS add_point_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            point int,
            user_id int
        )
        """

        # 테이블 생성
        cursor.execute(create_table_query)

        print("add_point 테이블이 생성되었습니다.")

    except Exception as e:
        print(f"add_point 테이블 생성 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()


def inputUserTable(user_data):
    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 데이터 삽입 쿼리 작성
        insert_data_query = """
        INSERT INTO user_table (
            id,
            profile_url,
            name,
            email,
            point,
            ph_num,
            created_date,
            mission_clear_id,
            mission_ing_id
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # 삽입할 데이터

        cursor.execute(insert_data_query, user_data)


        # 변경 사항을 데이터베이스에 반영
        connection.commit()

        print("User Table에 데이터가 성공적으로 삽입되었습니다.")

    except Exception as e:
        print(f"User Table 데이터 삽입 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()

def selectUserTable(uid):

    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 데이터 삽입 쿼리 작성
        insert_data_query = """
        SELECT profile_url, name, email, ph_num, created_date, mission_clear_id, mission_ing_id FROM user_table WHERE id=%s;
        """

        # 삽입할 데이터

        cursor.execute(insert_data_query, uid)
        user_data = cursor.fetchone()

        print("User Table에 데이터를 성공적으로 조회했습니다.")

        return user_data

    except Exception as e:
        print(f"User Table 데이터 삽입 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()

def updateUserTable(uid, update_data):
    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        profile_url = update_data['profile_url']
        name = update_data['name']
        email = update_data['email']
        point = update_data['point']
        ph_num = update_data['ph_num']
        mission_clear_id = update_data['mission_clear_id']
        mission_ing_id = update_data['mission_ing_id']

        if profile_url:
            insert_data_query = """
                    UPDATE user_table SET profile_url=%s WHERE id=%s;
                    """
        elif name:
            insert_data_query = """
                                UPDATE user_table SET name=%s WHERE id=%s;
                                """
        elif email:
            insert_data_query = """
                                UPDATE user_table SET email=%s WHERE id=%s;
                                """
        elif point:
            insert_data_query = """
                                UPDATE user_table SET point=%s WHERE id=%s;
                                """
        elif ph_num:
            insert_data_query = """
                                UPDATE user_table SET ph_num=%s WHERE id=%s;
                                """
        elif mission_clear_id:
            insert_data_query = """
                                UPDATE user_table SET mission_clear_id=%s WHERE id=%s;
                                """
        elif mission_ing_id:
            insert_data_query = """
                                UPDATE user_table SET mission_ing_id=%s WHERE id=%s;
                                """
        else:
            return 1


        # 삽입할 데이터

        cursor.execute(insert_data_query, uid)
        user_data = cursor.fetchone()

        print(uid,"를 성공적으로 업데이트 했습니다.")

        return user_data

    except Exception as e:
        print(f"User Table 데이터 업데이트 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()

def deleteUserTable(uid):
    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 데이터 삽입 쿼리 작성
        insert_data_query = """
        DELETE FROM user_table where id=%s
        """

        # 삽입할 데이터

        cursor.execute(insert_data_query, uid)
        user_data = cursor.fetchone()

        print(uid, "User Table에서 데이터를 성공적으로 삭제했습니다.")

        return user_data

    except Exception as e:
        print(f"User Table 데이터 삭제 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()




## post category table

def selectPostCategoryTable():
    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 데이터 삽입 쿼리 작성
        insert_data_query = """
        SELECT * FROM post_category_table;
        """

        # 삽입할 데이터

        cursor.execute(insert_data_query)
        post_category = cursor.fetchall()

        print(post_category, "post category 테이블에서 조회를 성공했습니다..")

        return post_category

    except Exception as e:
        print(f"post category 데이터 조회 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()
def inputPostCategoryTable(post_data):
    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 데이터 삽입 쿼리 작성
        insert_data_query = """
        insert into post_category_table(title, post_cnt, created_date)
        values (%s, %s, %s)
        """

        # 삽입할 데이터

        cursor.execute(insert_data_query, post_data)
        connection.commit()

        print("post_category_table에 데이터를 성공적으로 입력했습니다.")


    except Exception as e:
        print(f"post_category_table 데이터 입력 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()
def updatePostCategoryTable(post_category_data):
    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        title = post_category_data['title']
        post_cnt = post_category_data['post_cnt']

        if title:
            insert_data_query = """
                    UPDATE post_category_post SET title=%s WHERE id=%s;
                    """
            cursor.execute(insert_data_query, title)
        elif post_cnt:
            insert_data_query = """
                    UPDATE post_category_post SET post_cnt=%s WHERE id=%s;
                    """
            cursor.execute(insert_data_query, post_cnt)

        # 삽입할 데이터


        connection.commit()

        print("post_category_post 테이블에 데이터 업데이트 성공")

    except Exception as e:
        print(f"post_category_post테이블 업데이트 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()
def deletePostCategoryTable(post_category_id):
    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 데이터 삽입 쿼리 작성
        insert_data_query = """
        DELETE FROM post_category_table where id=%s
        """

        # 삽입할 데이터

        cursor.execute(insert_data_query, post_category_id)
        connection.commit()
        print("post_category_table 데이터를 성공적으로 삭제했습니다.")


    except Exception as e:
        print(f"post_category_table 데이터 삭제 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()


def selectPostTable(board_id):
    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 데이터 삽입 쿼리 작성
        insert_data_query = """
        SELECT * FROM post_table where board_id=%s;
        """

        # 삽입할 데이터

        cursor.execute(insert_data_query, board_id)
        post = cursor.fetchall()

        print(post, "post 테이블에서 조회를 성공했습니다..")

        return post

    except Exception as e:
        print(f"post 데이터 조회 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()
def inputPostTable(post_data):
    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 데이터 삽입 쿼리 작성
        insert_data_query = """
        insert into post_table(user_id, board_id, created_date, title) values (%s, %s, %s, %s);
        """

        # 삽입할 데이터

        cursor.execute(insert_data_query, post_data)

        connection.commit()

        print( "post_table 테이블에 데이터 삽입을 성공했습니다..")


    except Exception as e:
        print(f"post_table 테이블에 데이터 삽입 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()
def updatePostTable(title):
    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        if title:
            insert_data_query = """
                    UPDATE post_post SET title WHERE id=%s;
                    """

            # 삽입할 데이터

            cursor.execute(insert_data_query)

        connection.commit()


        print("post 테이블에 업데이트를 성공했습니다..")


    except Exception as e:
        print(f"post  데이터 업데이트 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()
def deletePostTable(post_id):
    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 데이터 삽입 쿼리 작성
        insert_data_query = """
        delete from post_table where id=%s
        """

        # 삽입할 데이터

        cursor.execute(insert_data_query, post_id)
        connection.commit()

        print("post 테이블에서 삭제를 성공했습니다..")


    except Exception as e:
        print(f"post 데이터 삭제 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()

def selectDetailPostTable(post_id):
    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()
        # 데이터 삽입 쿼리 작성
        insert_data_query = '''
        SELECT * FROM detail_post_table WHERE post_id=%s
        '''

        # 삽입할 데이터

        cursor.execute(insert_data_query, post_id)
        detail_post = cursor.fetchall()

        print(detail_post, "detail_post 테이블에서 조회를 성공했습니다..")

        return detail_post

    except Exception as e:
        print(f"detail_post 데이터 조회 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()
def inputDetailPostTable(detail_post_data):
    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 데이터 삽입 쿼리 작성
        insert_data_query = """
        insert into detail_post_table(post_id, content, img) values(%s, %s, %s)
        """

        # 삽입할 데이터

        cursor.execute(insert_data_query, detail_post_data)
        connection.commit()

        print(detail_post_data, "detail_post 테이블에 데이터 삽입을 성공했습니다..")

    except Exception as e:
        print(f"detail_post 데이터 삽입 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()
def updateDetailPostTable(detail_post_update):
    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        uid = detail_post_update['id']
        content = detail_post_update['content']
        img = detail_post_update['img']

        # 데이터 삽입 쿼리 작성
        if content:
            insert_data_query = """
                    update detail_post_table SET content=%s where id=%s
                    """

            # 삽입할 데이터

            cursor.execute(insert_data_query, (content, uid))
        elif img:
            insert_data_query = """
                                update detail_post_table SET img=%s where id=%s
                                """

            # 삽입할 데이터

            cursor.execute(insert_data_query, (img, uid))
        
        connection.commit()

        print("detail_post 테이블에 데이터 업데이트를 성공했습니다..")

    except Exception as e:
        print(f"detail_post 데이터 업데이트 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()
def deleteDetailPostTable(uid, board_id):
    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 데이터 삽입 쿼리 작성
        insert_data_query = """
           delete from detail_post_table where id=%s and board_id=%s
           """

        # 삽입할 데이터

        cursor.execute(insert_data_query, (uid, board_id))

        print( "detail_post 테이블에 데이터 삭제를 성공했습니다..")

    except Exception as e:
        print(f"detail_post 데이터 삭제 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()

#-----------------------------------------여행 지 코드 작성


def selectPlaceByPlaceId(place_id):
    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 데이터 삽입 쿼리 작성
        insert_data_query = """
        SELECT * from place_table where id=%s;
        """

        # 삽입할 데이터

        cursor.execute(insert_data_query, place_id)
        place_data = cursor.fetchone()

        print("unknown Place 데이터를 성공적으로 조회했습니다.")
        return place_data


    except Exception as e:
        print(f"unknown Place 데이터 조회 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()
def inputUnknownPlaceData():

    from dataloader import UnknownPlaceList

    unknownPlaceList = UnknownPlaceList()

    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 데이터 삽입 쿼리 작성
        insert_data_query = """
        INSERT INTO place_table (name, address)
        VALUES (%s, %s)
        """

        # 삽입할 데이터

        for i in range(1, len(unknownPlaceList)):
            data = (unknownPlaceList[i][0], unknownPlaceList[i][1])
            cursor.execute(insert_data_query, data)


        # 변경 사항을 데이터베이스에 반영
        connection.commit()

        print("unknown Place 데이터가 성공적으로 삽입되었습니다.")

    except Exception as e:
        print(f"unknown Place 데이터 삽입 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()
def selectPlace():
    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 데이터 삽입 쿼리 작성
        insert_data_query = """
        SELECT * from place_table;
        """

        # 삽입할 데이터

        cursor.execute(insert_data_query)
        place_data = cursor.fetchall()

        print("unknown Place 데이터를 성공적으로 조회했습니다.")
        return place_data


    except Exception as e:
        print(f"unknown Place 데이터 조회 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()

def deletePlace(name):
    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 데이터 삽입 쿼리 작성
        insert_data_query = """
        delete from place_table where naem=%s;
        """

        # 삽입할 데이터

        cursor.execute(insert_data_query, name)
        place_data = cursor.fetchall()

        print("unknown Place 데이터를 성공적으로 삭제했습니다.")
        return place_data


    except Exception as e:
        print(f"unknown Place 데이터 삭제 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()

def updatePlace(update_data):

    place_id = update_data['id']
    name = update_data['name']
    address = update_data['address']
    open_time = update_data['open_time']
    close_time = update_data['close_time']
    content = update_data['content']
    hasMission = update_data['hasMission']
    missionId = update_data['missionId']

    try:
        # 데이터베이스 연결
        connection = connectToDb()
        cursor = connection.cursor()

        if name:

            # 데이터 삽입 쿼리 작성
            insert_data_query = """
            update place_table set name=%s where id=%s
            """
            cursor.execute(insert_data_query, (name, place_id))
        elif address:
            insert_data_query = """
                        update place_table set address=%s where id=%s
                        """
            cursor.execute(insert_data_query, (address, place_id))
        elif open_time:
            insert_data_query = """
                        update place_table set open_time=%s where id=%s
                        """
            cursor.execute(insert_data_query, (open_time, place_id))
        elif close_time:
            insert_data_query = """
                        update place_table set close_time=%s where id=%s
                        """
            cursor.execute(insert_data_query, (close_time, place_id))
        elif content:
            insert_data_query = """
                        update place_table set content=%s where id=%s
                        """
            cursor.execute(insert_data_query, (content, place_id))
        elif hasMission:
            insert_data_query = """
                        update place_table set hasMission=%s where id=%s
                        """
            cursor.execute(insert_data_query, (hasMission, place_id))
        elif missionId:
            insert_data_query = """
                        update place_table set missionId=%s where id=%s
                        """
            cursor.execute(insert_data_query, (missionId, place_id))
        else:
            return 1
        connection.commit()
        print("unknown Place 데이터를 성공적으로 업데이트 했습니다.")

    except Exception as e:
        print(f"unknown Place 데이터 업데이트 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()


def inputMissionTable(mission_data):
    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 데이터 삽입 쿼리 작성
        insert_data_query = """
        insert into mission_table(name, level, content, point, longitude, latitude, place_id, user_id) values(%s, %s, %s, %s, %s, %s, %s, %s)
        """

        # 삽입할 데이터

        cursor.execute(insert_data_query, mission_data)
        connection.commit()

        print(mission_data, "mission 테이블에 데이터 삽입을 성공했습니다..")

    except Exception as e:
        print(f"mission 테이블 데이터 삽입 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()

def selectMissionTable():
    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 데이터 삽입 쿼리 작성
        insert_data_query = """
        select * from mission_table
        """

        # 삽입할 데이터

        cursor.execute(insert_data_query)
        mission_data= cursor.fetchall()

        print("mission 테이블에서 데이터 조회를 성공했습니다..")
        return mission_data

    except Exception as e:
        print(f"mission 테이블 데이터 조회 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()

def selectMissionTableById(user_id):
    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 데이터 삽입 쿼리 작성
        insert_data_query = """
        select * from mission_table where user_id=%s
        """

        # 삽입할 데이터

        cursor.execute(insert_data_query, user_id)
        mission_data= cursor.fetchall()

        print("mission 테이블에서 데이터 조회를 성공했습니다..")
        return mission_data

    except Exception as e:
        print(f"mission 테이블 데이터 조회 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()

def selectMissionTableByMissionId(user_id, mission_id):
    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 데이터 삽입 쿼리 작성
        insert_data_query = """
        select * from mission_table where user_id=%s and id=%s
        """

        # 삽입할 데이터

        cursor.execute(insert_data_query, (user_id, mission_id))
        mission_data= cursor.fetchall()

        print("mission 테이블에서 데이터 조회를 성공했습니다..")
        return mission_data

    except Exception as e:
        print(f"mission 테이블 데이터 조회 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()
            
def deleteMissionTable(mission_id):
    try:
        # 데이터베이스 연결
        connection = connectToDb()

        # 커서 생성
        cursor = connection.cursor()

        # 데이터 삽입 쿼리 작성
        insert_data_query = """
        delete from mission_table id=%s
        """

        # 삽입할 데이터

        cursor.execute(insert_data_query, mission_id)
        connection.commit()

        print("mission 테이블에 데이터 삭제를 성공했습니다..")

    except Exception as e:
        print(f"mission 테이블 데이터 삭제 중 오류 발생: {str(e)}")

    finally:
        # 연결 및 커서 닫기
        if connection:
            connection.close()


if __name__ == "__main__":

    print('-'*50)
    print('메인 파일 실행')
    print('-' * 50)

    makeDb()
    makeDetailPostTable()
    makeMissionTable()
    makePostTable()
    makePlaceTable()
    makeUserTable()
    makePostCategoryTable()
    makeUsePointTable()
    makeAddPointTable()

    user_test_id = [
        'pms1001',
        'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.ytn.co.kr%2F_ln%2F0134_201701041140063243&psig=AOvVaw36tlO8tUphwnS6RHlCVcOL&ust=1697549104386000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCPDD47LV-oEDFQAAAAAdAAAAABAE',
        '박민서',
        'qlqlxks123@naver.com',
        100,
        '010-7339-4768',
        '2023 10 16',
        '{}',
        '{}'
    ]
    inputUserTable(user_test_id)
    #print(selectUserTable('pms1001'))

    post_category_test_data = [
        '여행 카테고리',
        10,
        '2023 10 17'
    ]

    post_test_data = [
        'pms1001',
        1,
        '2023 10 17 12 47',
        '오늘 하루 최고 였다.'
    ]

    detail_post_test_data = [
        1,
        '오늘 하루는 정말 보람 찬 하루 였다.',
        'http://127.0.0.1'
    ]

    inputPostCategoryTable(post_category_test_data)
    inputPostTable(post_test_data)
    inputDetailPostTable(detail_post_test_data)


    inputUnknownPlaceData()

    mission_test_data = [
        '미션1',
        5,
        '구석에 있는 QR코드를 찾아보세요!',
        30,
        '30.303030',
        '20.202020',
        1,
        'pms1001'
    ]
    inputMissionTable(mission_test_data)
    print(selectMissionTable())


