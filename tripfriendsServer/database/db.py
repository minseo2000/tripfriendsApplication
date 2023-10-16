import pymysql

host = '127.0.0.1'
user = 'root'
password = '1693'
database = 'tripfriendsDB'

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
            latitude int 
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
            user_id int,
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
        CREATE TABLE IF NOT EXISTS make_detail_post_table (
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
    #inputUserTable(user_test_id)
    print(selectUserTable('pms1001'))



