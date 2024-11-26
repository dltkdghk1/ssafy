-- Table 구조 확인
SELECT * FROM examples;
PRAGMA table_info('new_examples');

-- 1. Create a table

CREATE TABLE examples (
    ExamId INTEGER PRIMARY KEY AUTOINCREMENT, --> 자동으로 증가하는 pk
    LastName VARCHAR(50) NOT NULL, --> LastName(필드명), 최대 50자, 필수로 입력
    FirstName VARCHAR(50) NOT NULL --> FirstName(필드명), 최대 50자, 필수로 입력
)

-- 2. Modifying table fields (테이블 필드 수정)

-- 2.1 ADD COLUMN (열 추가)
ALTER TABLE
 examples
ADD COLUMN
 Country VARCHAR(100) NOT NULL DEFAULT 'default value'; -- country 열 추가, 기본값 설정
    

-- sqlite는 단일 문을 사용하여 한번에 여러 열을 추가하는 것을 지원하지 않음
ALTER Table 
 examples
ADD COLUMN 
 Age INTEGER NOT NULL DEFAULT 0;
-- 필드명, 데이터 타입, 필수 입력, 기본값 0


ALTER TABLE 
 examples
ADD COLUMN
 Adress VARCHAR(100) NOT NULL DEFAULT 'default value';
-- Adress 열 추가, 필수 입력, 기본값 설정


-- 2.2 RENAME COLUMN (열 이름 변경)
ALTER TABLE examples
RENAME COLUMN Adress TO PostCode;
-- Adress 열을 PostCode로 이름 변경


-- 2.3 Delete a COLUMN (열 삭제)
ALTER TABLE examples
DROP COLUMN postCode;
-- PostCode 열 삭제


-- 2.4 RENAME TO (테이블 이름 변경)
ALTER TABLE examples
RENAME TO new_examples;
-- example 테이블을 new_examples로 테이블 이름 변경


-- 3. Delete a table(테이블삭제)
DROP TABLE new_examples;

DROP TABLE examples

-- sqlite는 컬럼 수정 불가
-- 대신 테이블의 이름을 바꾸고, 새 테이블을 만들고 데이터를 새 테이블에 복사하는 방식을 사용
