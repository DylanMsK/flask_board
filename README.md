# **flask** 게시판 만들기

### 파이썬 환경설정

[link](https://github.com/mcDeeplearning/TIL/blob/master/%ED%8C%8C%EC%9D%B4%EC%8D%AC%20%ED%99%98%EA%B2%BD%EC%84%A4%EC%A0%95.md)



### 설정

```bash
$ sudo apt-get update
$ sudo apt-get install postgresql postgresql-contrib libpq-dev
# ubuntu에 postgresql 설치
$ pip install psycopg2 psycopg2-binary
# python(flask)에서 postgresql를 사용하기 편하게 도와주는 친구들
$ pip install Flask-SQLAlchemy Flask-Migrate
# import 해서 쓸 친구들
```



### DB 설정

```bash
$ psql
ubunto= CREATE DATABASE <db이름> WITH template=template0 encoding='UTF8';
# \q로 밖으로 나감
# \d <table 이름> 으로 테이블 보기
```



### models.py 설정



### app.py 설정



### migration

```bash
$ flask db init		# flask db initialize, migrations 폴더 생성
$ flask db migrate	# sql 코드를 python코드로 짤수있게해줌
$ flask db upgrade	# 지금까지 한 작업을 반영
```

