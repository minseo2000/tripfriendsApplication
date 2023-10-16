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
            representative VARCHAR(255),
            email VARCHAR(255),
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
            id INT AUTO_INCREMENT PRIMARY KEY,
            profile_url VARCHAR(255),
            name VARCHAR(255),
            password VARCHAR(255),
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


