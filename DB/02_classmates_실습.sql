CREATE TABLE classmates (
  name TEXT,
  age INT,
  address TEXT
);

-- CREATE TABLE students(
-- id INTEGER PRIMARY KEY,
-- name TEXT NOT NULL,
-- age INTEGER DEFAULT 1 CHECK (0 < age)
-- );

INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
-- 값을 3개 넣어야 함 2개만 넣어서 오류가 뜸

SELECT * FROM  classmates;

INSERT INTO classmates (name, age, address) VALUES ('홍길동', 23, '서울');
INSERT INTO classmates VALUES ('김철수', 40, '서울');

SELECT * FROM  classmates;


