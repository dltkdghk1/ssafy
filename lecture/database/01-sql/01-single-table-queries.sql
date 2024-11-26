-- Active: 1730436455428@@127.0.0.1@3306
-- 단일데이터에서 조회하기
-- 01. Querying data

-- employees 테이블에서 LastName만 조회
SELECT
    LastName
FROM
    employees;

SELECT
    LastName, FirstName
FROM
    employees;


-- employees 테이블에서 모든 필드 조회
SELECT
    *
FROM
    employees;


-- 별칭
SELECT
    FirstName AS '이름'
FROM
    employees;


-- 밀리초를 분으로 변환
SELECT
    Name,
    Milliseconds / 60000 AS '재생시간(분)'
FROM
    tracks;


-- 02. Sorting data

-- ORDER BY는 오름차순 정렬(python에서 sort()와 같다)
SELECT
    FirstName
FROM
    employees
ORDER BY
    FirstName;


-- 내림차순 정렬은  DESC(python에서 sort(reverse=True)와 같다)
SELECT
    FirstName
FROM
    employees
ORDER BY
    FirstName DESC;

 
-- Country는 내림차순 정렬, 같은 Country내에서는 City를 오름차순 정렬
SELECT
 Country, City
FROM
 customers
ORDER BY
 Country DESC,
 City;


-- 정렬을 계산된 값을 기준으로 정렬도 가능하다. ABORT
SELECT
 Name,
 Milliseconds / 60000 AS '세션 시간(분)'
FROM
 tracks
ORDER BY
 Milliseconds DESC;

-- NULL 정렬 예시
SELECT
    ReportsTo
FROM
    employees
ORDER BY
    ReportsTo;

-- 03. Filtering data

-- 
SELECT
 Country
FROM
 customers
ORDER BY
 Country;


-- DISTINCT 중복제거
SELECT DISTINCT
 Country
FROM
 customers
ORDER BY
 Country;


-- WHERE은 조건을 지정(python에서 if문이나 리스트 컨프리헨션 조건부와 비슷)
-- City가 'Prague'인 고객만 선택
SELECT
 Lastname, FirstName, City
FROM
 customers
WHERE
 City = 'Prague';


-- City가 'Prague'가 아닌 고객만 선택
SELECT
 Lastname, FirstName, City
FROM
 customers
WHERE
 City != 'Prague';


-- AND는 두 조건을 모두 만족(python의 and 연산자와 비슷)
-- Company는 NULL값이고, Country는 'USA'
-- NULL은 IS를 사용해야함 =는 인식 못함
SELECT
 LastName, FirstName, Company, Country
FROM
 customers
WHERE
 Company IS NULL
 AND Country = 'USA';


-- OR은 두 조건 중 하나만 만족(python의 and 연산자와 비슷)
-- Company는 NULL값이거나 Country는 'USA'
SELECT
 LastName, FirstName, Company, Country
FROM
 customers
WHERE
 Company IS NULL
 OR Country = 'USA';


-- BETWEEN은 범위지정 100000이상 500000 이하
SELECT
 Name, Bytes
FROM
 tracks
WHERE
Bytes BETWEEN 100000 AND 5000000;
--  Bytes >= 10000
--  AND Bytes <= 500000;


-- 범위 내 값을 선택하고 정렬
SELECT
 Name, Bytes
FROM
 tracks
WHERE
Bytes BETWEEN 100000 AND 5000000
ORDER BY
 Bytes;


-- IN은 여러값중에 하나와 일치하는지 확인(python내의 멤버쉽 연산자와 비슷)
SELECT
 LastName, FirstName, Country
FROM
 customers
WHERE
Country IN ('Canada', 'Germany', 'France');
--  Country = 'Canada'
--  OR Country = 'Germany'
--  OR Country = 'France'


-- NOT IN은 여러값과 일치하는지 않는지 확인(python내의 멤버쉽 연산자와 비슷)
SELECT
 LastName, FirstName, Country
FROM
 customers
WHERE
Country NOT IN ('Canada', 'Germany', 'France');


-- 패턴 매칭 LIKE
-- EX) LastName이 son으로 끝나는 단어(%사용하면 됨)
SELECT
 LastName, FirstName
FROM
 customers
WHERE
 LastName LIKE '%son';


-- '_'는 한글자를 의미
SELECT
 LastName, FirstName
FROM
 customers
WHERE
 FirstName LIKE '___a'; -- a앞에 3글자가 있다


-- LIMIT 결과의 개수 제한
SELECT
 TrackId, Name, Bytes
FROM
 tracks
ORDER BY
 Bytes DESC -- 내림차순 정렬
LIMIT 7; -- 큰 값 7개


-- LIMIT 두 개의 인자 줄 때
SELECT
 TrackId, Name, Bytes
FROM
 tracks
ORDER BY
 Bytes DESC
-- LIMIT 3, 4;
LIMIT 4 OFFSET 3;


-- 04. Grouping 

-- 국가 별로 그룹화(같은 Country를 가진 객체를 그룹으로 묶는다)
-- 그 다음에 COUNT(*) 각 그룹내의 객체의 개수를 센다.
SELECT
 Country, COUNT(*)
FROM
 customers
GROUP BY
 Country;


-- AVG()는 평균을 계산
SELECT
 Composer,
 AVG(Bytes)
FROM
 tracks
GROUP BY
 Composer
ORDER BY
 AVG(Bytes) DESC;


-- HAVING
-- 과일가게에 손님이 "평균가격이 5000원 미만을 담아주세요"
-- 1단계 : 과일 종류별로 그룹지어야한다.(ex. 사과, 배, 포도 등등)
-- 2단계 : 각 그룹의 평균 가격을 계산
-- 3단계 : 마지막으로 평균가격이 5000원 미만인 그룹을 선택

-- WHERE을 쓴다
-- -> 그룹짓기 전에(1단계 전에) 아직 평균가격을 모르는 상태에서 필터링 안된다, 에러가 난다.ABORT
-- HAVING 2단계후에 평균가격을 알고 알고 있는 상태에서 필터링
-- 만약 AVG같은 집계함수의 결과를 필터링하고 싶다. -> 무조건 HAVING

-- 이 쿼리는ERROR가 뜬다
SELECT
 Composer,
 AVG(Milliseconds / 60000) AS avgOFMinute
FROM
 tracks
WHERE
 avgOFMinute < 10
GROUP BY
Composer;


SELECT
 Composer,
 AVG(Milliseconds / 60000) AS avgOFMinute
FROM
 tracks
GROUP BY
Composer
HAVING
 avgOFMinute < 10;