[TOC]



# 1012 DB 과목평가(출처:[wally-wally](https://github.com/wally-wally/TIL/blob/master/05_DB/%5BSSAFY%5DDB_%231.md#1-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4%EB%9E%80))

### 1.1 데이터베이스(DB)



#### (1) 데이터베이스란?

- 체계화된 데이터의 모임
- 몇개의 자료 파일을 조직적으로 통합하여, 자료 항목의 중복을 없애고 자료를 구조화하여 기억시켜 놓은 자료의 집합체
- RDBMS(관계형 데이터베이스 관리 시스템) : 관계형 모델을 기반으로하는 데이터베이스 관리시스템
  - 종류: MySQL, SQLite, PostgreSQL, ORACLE, MS SQL
  - 모든 데이터를 2차원 테이블로 표현
  - 테이블은 row(record,tuple)과 column(field,item)으로 이루어진 기본 데이터 저장단위
  - 상호관련성을 가진 테이블의 집합
  - 만들거나 이용하기도 쉽고, 확장이 매우 용이하다 



#### (2) 데이터베이스로 얻는 장점들

- 데이터 중복 최소화
- 데이터 무결성 : 정확한 정보를 보장
- 데이터 일관성
- 데이터 독립성 : 물리적 독립성과 논리적 독립성
- 데이터 표준화
- 데이터 보안 유지



#### (3) 데이터베이스 관련 기본 용어 정리

![img](sql_subject_exam.assets/66893305-b5be0c80-f028-11e9-85c7-88fa3278ddff.JPG)

- 스키마: 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조(meta 속성)
- 열: 고유한 데이터 형식이 지정
- 행: 테이블의 데이터가 저장됨
- 기본키(PK): 각 행의 고유값으로 반드시 설정하여야 하며, 데이터 베이스 관리 및 관계 설정시 주요하게 활용됨
  - DB를 조작할때를 PK 대신에 id 즉, column 명으로 조작해야 한다.



### 1.2 SQL(Structured Query Language)

#### (1) SQL 이란?

- 관계형 데이터베이스 관리시스템(Relational Database Management System)의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어
- RDBMS에서 자료의 검색과 관리 데이터베이스 스키마 생성과 수정, 데이터베이스 객체 접근 조정 관리를 위해 고안되었다.



#### (2) SQL 종류

| 언어 | 개념                                       | 예시                                           |
| ---- | ------------------------------------------ | ---------------------------------------------- |
| DDL  | 데이터를 정의하기 위한 언어                | CREATE, DROP, ALTER                            |
| DML  | CRUD와 관련된 언어(저장, 수정, 삭제, 조회) | **INSERT(C), SELECT(R), UPDATE(U), DELETE(D)** |
| DCL  | DB 사용자의 권한 제어를 위해 사용되는 언어 | GRANT, REVOKE, COMMIT, ROLLBAK                 |





### 1.3 Database 생성, Table 생성 및 삭제



#### (1) Database 생성

Ready for sqlite3

```she
sqlite3 tutorial.sqlite3 -- tutorial.sqlite3 DB 파일 생성 및 조회
.databases --database 생성
.mode csv --csv모드로 변경
.import hellodb.csv examples --hellodb.csv 파일을 이용한 examples라는 테이블 생성
```

테이블 전체 조회

```shell
SELECT * FROM examples; --테이블 전체 조회
```

```
1,"길동","홍",600,"충청도",010-2424-1232
```

보기 편하게 출력 형태 변경 

```shell
.headers on
.mode column
SELECT * FROM examples;
```

```
id          first_name  last_name   age         country     phone
----------  ----------  ----------  ----------  ----------  -------------
1           길동          홍           600         충청도         010-2424-1232
```





#### (2) Table 생성

```python
CREATE TABLE classmates(
id INTEGER PRIMARY KEY,
name TEXT);
.tables --테이블 목록 조회 
```

```shell
classmates examples -- 하나의 큰 데이터베이스 안에 classmates, examples 두 개의 테이블이 있다.
```

```
.schema classmates -- `스키마 조회
```

- `Datatype`

![img](sql_subject_exam.assets/66879523-5f85a500-eff9-11e9-82d8-47398c49e371.JPG)

- SQLite는 동적 데이터 타입으로, 기본적으로 affinity에 맞게 들어간다.
  - `동적 데이터 타입` : 사용자가 어느정도 맞춰 쓰면 sqlite가 자동으로 형변환을 해준다.
  - ex) INTEGER type으로 설정한 column에 '123' 이라고 입력해도 자동으로 123으로 바꿔준다.
- BOOLEAN은 정수 0, 1 으로 저장된다.
- `BLOB` : 데이터 타입이 없고 큰 데이터 덩어리를 의미한다.
- 주로 `INTEGER`, `TEXT`, `DATETIME`을 사용한다.



#### (3) Table 삭제

```
DROP TABLE classmates;
.tables
```

```
examples -- 기존에 있던 classmates 테이블 자체가 삭제되고 examples 테이블만 남아있다.
```



### 1.4 SQLite로 CRUD 접근 (DML) 

> 현재 classmates 테이블 상태
>
> ```
> CREATE TABLE classmates (
> name TEXT,
> age INT,
> address TEXT );
> ```



#### (1) Data 추가(INSERT)

```python
INSERT INTO classmates (name,age)
VALUES('홍길동',23);
```

```
name        age         address
----------  ----------  ----------
홍길동         23
```

```
INSERT INTO classmates (name, age, address)
-- 모든 column의 데이터를 넣을 때는 ( ) 이 부분 생략 가능하여 바로 VALUES 부터 쓰면 된다.
-- 즉, 모든 열에 데이터를 넣을 때에는 column을 명시할 필요가 없다.
-- INSERT INTO classmates VALUES('홍길동', 30, '서울');
VALUES ('홍길동', 30 , '서울');
```

```
name        age         address
----------  ----------  ----------
홍길동         23
홍길동         30          서울
```



#### (2) NOT NULL

- 꼭 필요한 정보라면 공백으로 비워두면 안된다는 `NOT NULL` 조건을 추가할 수 있다.

- DROP TABLE classmates; 로 테이블 삭제 후 다시 시작

  ```shell
  CREATE TABLE classmates (
  id INTEGER PRIMARY KEY,
  NAME TXT NOT NULL,
  age INT NOT NULL,
  address )
  ```

  ```
  INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
  ```

  ```
  Error: NOT NULL constraint failed: classmates.address
  ```

  ```shell
  INSERT INTO classmates(name, age, address) VALUES('홍길동',23,'서울')
  ```

- rowid는 자동으로 작성되었는데 직접 id칼럼을 만든 후에는 입력할 칼럼을 명시하지 않으면 자동으로 입력되지 않는다.

  ```
  INSERT INTO classmates VALUES ('김영희', 30, '대전'); -- 이건 안 됨(rowid 일 때 와는 다르다)
  ```

- 그래서 앞으로는 아래와 같이 테이블 생성하여 PK 컬럼을 rowid를 통해 자동으로 작성되도록 한다!

  ```
  CREATE TABLE classmates (
  name TEXT NOT NULL,
  age INT NOT NULL,
  address TEXT NOT NULL );
  ```

  ```
  INSERT INTO classmates VALUES ('홍길동', 30, '서울'), ('김철수', 23, '대전'), (
  '박나래', 23, '광주'), ('이요셉', 33, '구미');
  ```

  ```
  SELECT * FROM classmates;
  ```

  ```
  name        age         address
  ----------  ----------  ----------
  홍길동         30          서울
  김철수         23          대전
  박나래         23          광주
  이요셉         33          구미
  ```

  

#### (3) Data 조회(SELECT)

- classmates에서 id, name column 값만 가져오기

  ```shell
  SELECT rowid, name FROM classmates ; 
  ```

  ```
  rowid       name
  ----------  ----------
  1           홍길동
  2           김철수
  3           박나래
  4           이요셉
  ```

  

- `LIMIT` 속성을 이용하여 classmates에서 id, name cloumn 값을 하나만 가져오기

  ```
  SELECT rowid, name FROM classmates LIMIT 1;
  ```

  ```
  rowid       name
  ----------  ----------
  1           홍길동
  ```

- `LIMIT`, `OFFSET` 속성을 이용하여 classmates에서 id, name column 값을 세번째에 있는 값 하나만 가져오기(`LIMIT`와 `OFFSET`은 한 세트!)

  ```shell
  SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2; -- OFFSET에 적은 숫자 이후부터 시작!
  ```

- `WHERE` 속성을 이용하여 classmates에서 id, name column 주소가 서울인 사람만 가져오기

  ```shell
  SELECT rowid, name FROM classmates WHERE address='서울';
  ```

  ```
  rowid       name
  ----------  ----------
  1           홍길동
  ```

- `DISTINCT`속성을 이용해서 classmates에서 age값 전체를 중복없이 가져오기

  ```shell
  SELECT DISTINCT age FROM classmates; 
  ```

  ```
  age
  ----------
  30
  23
  33
  ```



#### (4) Data 삭제(DELETE)

- 중복이 불가능한(UNIQUE) 값인 rowid를 기준으로 data를 삭제하자.

- classmates 테이블에 id가 4인 레코드 삭제하기

  ```
  DELETE FROM classmates WHERE rowid=4;
  SELECT rowid, * FROM classmates;
  ```

  ```
  rowid       name        age         address
  ----------  ----------  ----------  ----------
  1           홍길동         30          서울
  2           김철수         23          대전
  3           박나래         23          광주
  ```

- 위와 같은 테이블 상황에서 새로운 데이터 추가

  SQLite는 기본적으로 일부 행을 삭제하고 새 행을 삽입하면 삭제 된 행의 값을 재사용하려고 시도한다.

  ```
  INSERT INTO classmates VALUES ('최철순', 45, '서울');
  SELECT rowid, * FROM classmates;
  ```

  ```
  rowid       name        age         address
  ----------  ----------  ----------  ----------
  1           홍길동         30          서울
  2           김철수         23          대전
  3           박나래         23          광주
  4           최철순         45          서울
  ```



- `AUTOINCREMENT` 속성을 사용하면 삭제 된 행의 값을 재사용하지 않고 새로운 값이 적용된다

  ```
  CREATE TABLE tests (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL );
  INSERT INTO tests (id, name) VALUES (1, '홍길동'), (2, '김철수');
  SELECT * FROM tests;
  ```

  

  ```
  id          name
  ----------  ----------
  1           홍길동
  2           김철수
  ```

  ```
  DELETE FROM tests WHERE id=2;
  INSERT INTO tests (name) VALUES ('최철순');
  SELECT * FROM tests;
  ```

  ```
  id          name
  ----------  ----------
  1           홍길동
  3           최철순
  ```

  ​	

- 하지만 SQLite는 **특정한 요구사항(삭제된 행의 값을 재사용하지 못하게 한다면)이 없다면** **`AUTOINCREMENT` 속성을 사용하지 않아야 한다**고 공식문서에 명세되어 있다.
  - 내부적으로 CPU, 메모리, 디스크 공간을 추가로 불필요하게 사용하므로 엄격하게 필요하지 않을 경우 사용을 피해야 한다.
  - rowid의 최대값은 64비트 8바이트 실수의 최대값 = `9,223,372,036,854,775,807`
  - rowid의 최대값에 도달했을 때의 상황(INSERT INTO를 한다면)
    - AUTOINCREMENT가 없을 때 : 중간에 없는 ID를 재사용하므로 에러가 나지 않을 것.
    - AUTOINCREMENT가 있을 때 : 최대 레코드를 넘어서기 때문에 에러가 발생함.

#### (5) Data 수정(UPDATE)

- classmates 테이블에서 id가 4인 레코드를 이름은 홍길동으로, 주소를 제주도로 바꾸기

  ```
  UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=4;
  SELECT rowid, * FROM classmates;
  ```

  ```
  rowid       name        age         address
  ----------  ----------  ----------  ----------
  1           홍길동         30          서울
  2           김철수         23          대전
  3           박나래         23          광주
  4           홍길동         45          제주도
  ```

____________________

✔️ **데이터 추가, 읽기, 수정, 삭제 정리**

![img](https://user-images.githubusercontent.com/52685250/66893625-7643f000-f029-11e9-8004-92998c4c67d9.JPG)

______________





### 1.5 심화 내용 (`users.csv`)

Ready for sqlite3

```shell
.mode csv -- csv 모드로 변경
.import users.csv users -- hellodb.csv 파일을 이용한 examples 라는 테이블 생성
.tables
.headers on
```

#### (1) WHERE 심화

- users에서 age가 30 이상인 사람만 가져오기

  ```shell
  SELECRT * FROM users WHERE age>=30;
  ```



- users에서 age가 30 이상의 사람만 가져오기

  ```shell
  .schema --스키마로 column명을 먼저 확인하자
  ```

  ```shell
  CREATE TABLE users(
    "id" TEXT,
    "first_name" TEXT,
    "last_name" TEXT,
    "age" TEXT,
    "country" TEXT,
    "phone" TEXT,
    "balance" TEXT
  );
  ```

  ```
  SELECT first_name FROM users WHERE age>=30;
  ```

  ​	

- users에서 `age가 30 이상`**이고** `성이 김`인 사람의 성과 나이만 가져오기

  ```shell
  SELECT last_name, age FROM users WHERE age>=30 and last_name='김';
  ```



#### (2) 계산함수 - `COUNT()`, `AVG()`, `MAX()`, `MIN()`

- users 테이블의 레코드 총 개수 - `COUNT()`

  레코드의 개수 반환 : `SELECT COUNT(column) FROM table;`

  ```
  SELECT COUNT(*) FROM users; -- 어떤 column인지 안 나와 있으므로 *로 작성함
  ```

  ```
  COUNT(*)
  1000
  ```



- 30살 이상인 사람들의 평균 나이는? - `AVG()`

  `AVG()`, `SUM()`, `MIN()`, `MAX()` : 이 표현식들은 기본적으로 숫자(INTEGER)일 때만 가능함

  ```
  SELECT AVG(age) FROM users WHERE age>=30;
  ```

  ```
  AVG(age)
  35.1763285024155
  ```

- users에서 계좌 잔액(balance)이 가장 높은 사람과 액수는? - `MAX()`

  ```shel
  SELECT first_name, MAX(balance) FROM users;
  ```

  ```shell
  first_name, MAX(balance)
  "선영",990000
  ```

- users에서 30살 이상인 사람의 계좌 평균 잔액은? -`AVG()`

  ```SHELL
  SELECT AVG(balance) FROM users WHERE age>=30;
  ```

  ```
  AVG(balance)
  153541.425120773
  ```

  

#### (3) LIKE(wild cards)

- `_` : 반드시 이 자리에 한 개의 문자가 존재해야 한다.
- `%` : 이 자리에 문자열이 있을수도, 없을수도 있다.

![img](sql_subject_exam.assets/66888622-4b9e6b00-f01a-11e9-8d74-30ac61b41267.JPG)

- `2_3_%` : 무조건 세번째 값이 3임(2035) / `2_%3_%` : 세번째 값이 3이 될 수도 있고 안 될 수도 있음(20035)

- users에서 20대인 사람만 뽑기

  ```shell
  SELECT * FROM users WHERE age LIKE '2%'; -age가 2로 시작하는 경우
  ```

- users에서 지역번호가 02인 사람만 뽑기

  ```shell
  SELECT * FROM users WHERE phone LIKE '02-%';
  ```

- users에서 이름이 '준'으로 끝나는 사람만 뽑기

  ```shell
  SELECT * FROM users WHERE first_name LIKE '%준';
  ```

- users에서 중간 번호가 5114인 사람만 뽑기

  `%5114%`로 하면 5114가 끝자리인 사람이 나올 수도 있다.

  ```shell
  SELECT * FROM users WHERE phone LIKE '%-5114-%';
  ```



#### (4) ORDER(정렬)

- 오름차순 : `ASC` (default 이므로 생략 가능) / 내림차순 : `DESC`

- users에서 나이순으로 오름차순 정렬하여 상위 10개만 뽑기

  ```shell
  SELECT * FROM users ORDER BY age ASC LIMIT 10; --ASC 생략가능
  ```

- users에서 나이순, 성 순으로 오름차순 정렬하여 상위 10개만 뽑기

  ```SHELL
  SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;
  ```

- users에서 계좌잔액 순으로 내림차순 정렬하여 해당하는 사람과 성의 이름을 10개

  ```shell
  SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10; 
  ```

  ```SHELL
  "김","선영"
  "나","상현"
  "이","정호"
  "이","상철"
  "최","지아"
  "박","준서"
  "문","미영"
  "고","하윤"
  "유","은정"
  "안","서윤"
  ```

  

### 1.6 ALTER

#### (1) 테이블명 변경

- `ALTER TABLE exist_table RENAME TO new_table`

- 새로운 테이블 articles 생성

  - 조건 title: TEXT NOT NULL, content: TEXT NOT NULL

  ```SHELL
  CREATE TABLE articles (
  title TEXT NOT NULL,
  content TEXT NOT NULL);
  INSERT INTO articles VALUES('1번제목','1번내용');
  ```

  ```
  .tables
  ```

  ```
  articles    classmates  examples    tests       users
  ```

  ```shell
  ALTER TABLE articles RENAME TO news;
  ```

  ```
  classmates  examples    news        tests       users -- articles => news
  ```

#### (2) 새로운 컬럼 추가

- `ALTER TABLE table ADD COLUMN col_name DATATYPE;`

- 새로운 컬럼 created_at 추가(created_at:DATETIME)

  ```SHELL
  ALTER TABLE news ADD COLUMN created_at DATETIME NOT NULL;
  ```

  - 기존 데이터에 NOT NULL 조건으로 인해 NULL 값으로 새로운 컬럼이 추가될 수 없으므로 아래와 같은 에러가 발생한다. NOT NULL 조건을 없애거나 기본값(DEFAULT)을 지정해야 한다.

  ```
  Error: Cannot add a NOT NULL column with default value NULL
  ```

- 에러 해결 방법(1) - NOT NULL 조건 없애기

  ```
  ALTER TABLE news ADD COLUMN created_at DATETIME;
  INSERT INTO news VALUES ('title', 'content', datetime('now', 'localtime'));
  SELECT * FROM news;
  ```

  ```
  title,content,created_at
  "1번제목","1번 내용",      => 기존에 추가한 것은 DATETIME 칸에 공백으로 저장됨
  title,content,"2019-10-16 14:10:39"
  ```

- 에러 해결 방법(2) - DEFAULT 지정 

  ```
  ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT 1;
  SELECT * FROM news;
  ```

  ```
  title       content     created_at  subtitle
  ----------  ----------  ----------  ----------
  1번제목        1번 내용                   1
  title       content     2019-10-16  	1
  ```

  



## 2.  `SQL과 django ORM`

### 기본 준비 사항

```
# 폴더구조

TIL
	00_StartCamp
	...
	04_db
		00_sql # only SQL
			hellodb.csv
			tutorial.sqlite3
			users.csv
		01_sql_orm # SQL + ORM
			...
			users.csv # 해당 디렉토리로 다운로드
```

- django app
  - 가상환경 세팅

  - django project : `sql`

  - django app : `users`

  - `django_extensions` 설치 및 등록

  - users.csv 파일에 맞춰 `models.py` 작성 및 migratation

    ```
    # users/models.py
    
    from django.db import models
    
    class User(models.Model):
        first_name = models.CharField(max_length=10)
        last_name = models.CharField(max_length=10)
        age = models.IntegerField()
        country = models.CharField(max_length=10)
        phone = models.CharField(max_length=15)
        balance = models.IntegerField()
    ```

    ```
    $ python manage.py makemigrations
    $ python manage.py migrate 
    ```

    아래의 명령어를 통해서 실제 쿼리문 확인

    ```
    $ python manage.py sqlmigrate users 0001
    ```

_______________



### 문제

> 아래의 문제들을 보면서 서로 대응되는 ORM문과 SQL문을 작성하시오.
>
> **vscode 터미널을 좌/우로 나누어 진행하시오. (sqlite / shell_plus)**

`.headers on` 을 켜고 작성해주세요.

❗ django queryset official homepage



#### 1. 기본 CRUD 로직

1. 모든 USER 레코드 조회

   ```SHELL
   # ORM
   from users.model import User
   
   User.objects.all()
   ```

   ```
   -- sql
   SELECT * FROM users_user;
   ```



2. user 레코드 생성

   ```shell
   #orm
   
   User.objects.create(first_name='중구', last_name='이', age=30, country='충청남도', phone='010-1234-5678', balance=45000)
   ```

   ```shell
   --sql
   
   INSERT INTO users_user VALUES (102, '중구', '이', 30, '충청남도', '010-1234-5678', 45000)
   ```

   

3. 해당 user 레코드 조회

   - 101번 id 전체 레코드 조회

   ```python
   #orm
   
   User.objects.get(pk=101)
   ```

   ```python
   #sql
   
   SELECT * FROM users_user WHERE id=101;
   ```





4. 해당 user 레코드 수정

   - ORM: `101` 번 글의 `last_name` 을 '김' 으로 수정
   - SQL: `101` 번 글의 `first_name` 을 '철수' 로 수정

   ```python
   #orm
   
   user=User.objects.get(pk=101)
   user.last_name= '김'
   user.save()
   ```

   ```python
   #sql
   
   UPDATE users_user SET first_name='철수' where id=101;
   ```

   

5. 해당 user 레코드 삭제

   - ORM: `101` 번 글 삭제
   - `SQL`: `101` 번 글 삭제 (ORM에서 삭제가 되었기 때문에 아무런 응답이 없음)

   ```
   # orm
   user = User.objects.get(pk=101)
   user.delete()
   ```

   ```
   -- sql
   DELETE FROM users_user WHERE id=101;
   ```

____________



#### 2. 조건에 따른 쿼리문

1. 전체 인원 수

   - User의 전체 인원수 

   ```python
   #orm
   
   User.objects.all().count() 
   len(User.objects.all())
   ```

   ```python
   #sql
   
   SELECT COUNT(*) FROM users_user;
   ```

   

2. 나이가 30인 사람의 이름

   - orm : `.values`활용
     - 예시: `User.objects.filter(조건).values(컬럼이름)`

   ```python
   #orm
   
   User.objdets.filter(age=30).values('first_name')
   ```

   ```python
   #sql
   
   SELECT first_name FROM users_user WHERE age=30;
   ```

   

3. 나이가 30살 이상인 사람의 인원수 

   - ORM: `__gte` , `__lte` , `__gt`, `__lt` -> 대소관계 활용 (참고 문서)

   ```python
   #orm
   
   User.objects.filter(age__gte=30).count()
   ```

   ```pytohn
   #sql
   
   SELECT COUNT(*) FROM users_user WHERE age>=30;
   ```

   

4. 나이가 20살 이하인 사람의 인원 수

   ```
   # orm
   User.objects.filter(age__lte=20).count()
   ```

   ```
   -- sql
   SELECT COUNT(*) FROM users_user WHERE age <= 20;
   ```



5. 나이가 30이면서 성이 김씨인 사람의 인원 수

   ```python
   #orm
   
   User.objects.filter(last_name='김',age=30).coint()
   ```

   ```python
   #sql
   
   SELECT COUNT(*) FROM users_user WHERE last_name='김' and age=30;
   ```

   

6. 나이가 30이거나 성이 김씨인 사람

   ```python
   #ORM
   User.objects.filter(Q(age=30) | Q(last_name='김'))
   ```

   ```
   -- sql
   SELECT * FROM users_user WHERE age=30 or last_name='김';
   ```

7. 지역번호가 02인 사람의 인원 수

   - `ORM`: `__startswith` => ORM의 `__startswith`은 기본적으로 SQL에서는 `%` wild card로 넘어간다.

   ```python
   #Orm
   
   User.objects.filter(phone__startswith='02-').count()
   ```

   ```python
   #sql
   
   SELECT COUNT(*) FROM users_user WHERE phone LIKE '02-%';
   ```

   

8. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   ```
   # orm
   User.objects.extra(where=["country='강원도'", "last_name='황'"]).values('first_name')
   User.objects.filter(country='강원도', last_name='황').values('first_name') # 이걸로!
   
   # '은정'만 뽑아 올려면 다음과 같이 작성해야 한다.
   # <QuerySet [{'first_name': '은정'}]> => QuerySet의 첫 번째 요소 임을 주의!
   User.objects.filter(country='강원도', last_name='황').values('first_name').first().get('first_name')
   ```

   ```
   -- sql
   SELECT first_name FROM users_user WHERE country='강원도' and last_name='황';
   ```



#### 3. 정렬 및 LIMIT, OFFSET

 1. 나이가 많은 사람순으로 10명

    ```PYTHON
    # orm
    User.objects.order_by('-age')[:10]
    ```

    

    ```
    -- sql
    SELECT * FROM users_user ORDER BY age DESC LIMIT 10;
    ```

2. 잔액이 적은 사람순으로 10명

   ```PYTHON
   # orm
   User.objects.order_by('balance')[:10]
   ```

   ```PYTHON
   -- sql
   SELECT * FROM users_user ORDER BY balance LIMIT 10;
   ```

   

3. 잔고는 오름차순, 나이는 내림차순으로 10명? (order_by는 먼저 쓴게 정렬 우선순위가 높다.)

   ```PYTHON
   #ORM
   
   User.objects.order_by('balance','-age')[:10]
   ```

   ```py
   #sql
   
   SELECT * FROM user_user ORDER_BY balance,age DESC LIMIT 10;
   ```

   

4. 성, 이름 내림차순 순으로 5번째 있는 사람

   ```PY
   #ORM
   
   User.objects.order_by('-last_name','-first_name')[4]
   ```

   ```py
   #SQL
   
   SELECT * FROM users_user ORDER BY last_name DESC, first_name DESC LIMIT 1 OFFSER 4;
   ```

   

#### 4. 표현식

> ORM: `aggregate` 사용
>
> https://docs.djangoproject.com/en/2.2/topics/db/aggregation/#aggregation
>
> - '종합', '합계' 등의 사전적 의미
> - 특정 필드 전체의 합, 평균 등을 계산할 때 사용

1. 전체 평균 나이

   ```PYTHON
   #orm
   
   from django.db.models import Avg, Max, Sum # shell_plus로 켜면 자동으로 import 해준다.
   # python 파일에서 작성할 때는 위 구문을 반드시 작성해줘야 한다
   
   User.objects.aggregate(Avg('age'))
   ```

   ```python
   #sql
   
   SELECT AVG(age) FROM users_user;
   
   ```

   

2. 김씨의 평균 나이

   ```python
   #orm
   
   User.objects.filter(last_name='김').aggregate(Avg('age'))
   ```

   ```python
   #SQL
   
   SELECT AVG(age) FROM users_user WHERE last_name='김';
   ```

   

3. 강원도에 사는 사람의 평균 계좌 잔고

   ```python
   #orm
   
   User.objects.filter(country='강원도').aggregate(Avg('balance'))
   ```

   ```python
   #sql
   
   SELECT AVG(balance) FROM users_user WHERE country='강원도';
   ```

   

4. 계좌 잔약 중 가장 높은 값

   ```python
   #orm
   
   User.objects.aggregate(Max('balance'))
   ```

   ```
   -- sql
   SELECT MAX(balance) FROM users_user;
   ```

5. 계좌 잔액 총액

   ```pyrhon
   #orm
   
   User.objects.aggregate(Max('balance'))
   ```

   ```python
   #sql
   
   SELECT SUM(balance) FROM users_user;
   ```

   