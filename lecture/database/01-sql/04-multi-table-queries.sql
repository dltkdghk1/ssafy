-- 공통 : 테이블 조회, 삭제, 구조 확인
SELECT * FROM articles;
SELECT * FROM users;
DROP TABLE articles;
DROP TABLE users;
PRAGMA table_info('articles');


-- 1. articles 테이블, user 테이블 생성
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT, -- 자동으로 증가하는 pk
  name VARCHAR(50) NOT NULL -- 사용자 이름, 최대 50자, 필수 입력
);


CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(50) NOT NULL,
  content VARCHAR(100) NOT NULL,
  userId INTEGER NOT NULL, -- 작성자 id
  FOREIGN KEY (userId)  -- 외래키 설정
    REFERENCES users(id) -- users테이블의 id(pk)를 참조
);


INSERT INTO 
  users (name)
VALUES 
  ('하석주'),
  ('송윤미'),
  ('유하선');

INSERT INTO
  articles (title, content, userId)
VALUES 
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', 1),
  ('제목4', '내용4', 4), -- 주의 : userId 4는 users 테이블에 없음 !
  ('제목5', '내용5', 1);


-- INNER JOIN ON : 두 테이블의 일치하는 데이터만 결합
SELECT * FROM articles
INNER JOIN users
 ON users.id = articles.UserId;

-- Mission INNER JOIN 후 특정 사용자 (id = 1)인 글의 제목과 이름 조회
SELECT articles.title, users.name from articles
INNER JOIN users
 ON users.id = articles.userId
WHERE users.id = 1;


-- LEFT JOIN : 왼쪽 테이블(articles, select로 가져온 것) 모든 데이터와, 
-- 오른쪽 테이블(users)과 일치하는 데이터를 결합(만약에 userId가 4인 경우는 NULL 값으로)
SELECT * FROM articles
LEFT JOIN users
 ON users.id = articles.UserId;
-- 큰따옴표나 작은 따옴표 넣는 경우 2가지
-- 1. 문자열 값 표현할 때 WHERE name = "John"
-- 2. 테이블 명(또는 필드명)이 공백이 있거나 특수문자가 있는 경우 "articles table"

-- Mission : 글이 업는 사용자 찾기
SELECT * FROM users
LEFT JOIN articles
 ON users.id = articles.UserId
WHERE articles.userId IS NULL;
