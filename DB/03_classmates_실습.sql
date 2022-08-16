CREATE TABLE classmates(
  name TEXT NOT NULL,
  age INT NOT NULL,
  address TEXT NOT NULL
);

-- INSERT INTO classmates VALUES ('홍길동', 30, '서울')
-- INSERT INTO classmates VALUES ('김철수', 30, '제주')

INSERT INTO classmates VALUES 
('홍길동', 30, '서울'), 
('김철수', 30, '제주'),
('이호영', 26, '인천'),
('박민희', 29, '대구'),
('최혜영', 28, '전주');

-- SELECT * FROM classmates;

SELECT rowid, name FROM classmates;

SELECT rowid, name FROM classmates LIMIT 1;

SELECT rowid, name FROM classmates LIMIT 2;

SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;

SELECT rowid, name FROM classmates LIMIT 2 OFFSET 2;


SELECT rowid, name, age, address FROM classmates WHERE address='서울';

SELECT * FROM classmates WHERE address='서울';

SELECT DISTINCT age FROM classmates;

SELECT DISTINCT address FROM classmates;



DELETE FROM classmates WHERE rowid=5;

SELECT rowid, * FROM classmates;