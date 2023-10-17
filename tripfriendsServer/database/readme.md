# Database Description


## Database Name : TripFriends DB

## Tables

1. Place Table

| 필드이름                     | 타입           | 설명             |
|--------------------------|--------------|----------------|
| id                       | int          | 기본키로, 행을 구분한다. |
| representative_image_url | varchar(255) | 여행지 대표 이미지     |
| sub_image_url_list       | varchar(255) | 여행지 나머지 이미지들   |
| loc                      | varchar(255) | 여행지 위치 정보      |
| address                  | varchar(255) | 여행지 주소         |
| open_time                | varchar(30)  | 여행지 운영 시작 시간   |
| close_time               | varchar(30)  | 여행지 운영 종료 시간   |
| name                     | varchar(255) | 여행지 이름         |
| content                  | varchar(255) | 여행지에 대한 설명     |
| created_date             | varchar(255) | 여행지 등록 날짜      |
| hasMission               | int          | 미션이 있나 없나?     |
| missionId                | int          | 미션 id 등록 하기    |

2. User Table

| 필드이름             | 타입           | 설명             |
|------------------|--------------|----------------|
| id               | int          | 기본키로, 행을 구분한다. |
| profile_url      | varchar(255) | 유저 프로필 이미지 등록  |
| name             | varchar(255) | 이름             |
| password         | varchar(255) | 비밀번호           |
| email            | varchar(255) | 이메일            |
| point            | int          | 갖고 있는 포인트      |
| ph_num           | varchar(255) | 핸드폰 번호         |
| created_data     | varchar(255) | 가입일            |
| mission_clear_id | int          | 클리어 한 미션       |
| mission_ing_id   | int          | 진행중인 미션        |

3. Mission Table

| 필드이름      | 타입           | 설명             |
|-----------|--------------|----------------|
| id        | int          | 기본키로, 행을 구분한다. |
| name      | varchar(255) | 미션 제목          |
| level     | int          | 별 개수           |
| content   | varchar(255) | 미션 내용          |
| point     | int          | 적립 포인트         |
| longitude | int          | 좌표(미션)         |
| latitude  | int          | 좌표(미션)             |

4. PostCategory Table

| 필드이름         | 타입           | 설명             |
|--------------|--------------|----------------|
| id           | int          | 기본키로, 행을 구분한다. |
| created_date | varchar(255) | 게시판 생성 날짜      |
| title        | varchar(255) | 게시판 제목         |
| post_cnt     | int          | 게시글의 개수        |

5. Post Table

| 필드이름        | 타입           | 설명             |
|-------------|--------------|----------------|
| id          | int          | 기본키로, 행을 구분한다. |
| user_id     | int          | 게시글을 쓴 사람 Id   |
| board_id    | int          | 게시판 id         |
| created_date | varchar(255) | 기시글 등록 날짜      |
| title       | varchar(255) | 게시글 제목         |

6. DetailPost Table

| 필드이름    | 타입           | 설명             |
|---------|--------------|----------------|
| id      | int          | 기본키로, 행을 구분한다. |
| post_id | int          | 게시글 id를 입력     |
| content | varchar(255) | 내용             |
| img     | varchar(255) | 이미지 url 등록     |

7. Use Point Table

| 필드이름    | 타입   | 설명             |
|---------|------|----------------|
| id      | int  | 기본키로, 행을 구분한다. |
| point   | int  | 사용 포인트 기록      |
| user_id | int  | 어떤 유저가 사용?     |

8. Add Point Table

| 필드이름    | 타입  | 설명             |
|---------|-----|----------------|
| id      | int | 기본키로, 행을 구분한다. |
| point   | int | 적립한 포인트 기록     |
| user_id | int | 어떤 유저에게 적립?    |

## Router

### register Router

| method | input_data                                                                                                                                                  |   |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
| POST   | user_data<br/>1. id<br/>2.profile_url<br/>3. name<br/>4. email<br/>5. point<br/>6. ph_num<br/>7. created_date<br/>8. mission_clear_id<br/>9. mission_ing_id |   |


