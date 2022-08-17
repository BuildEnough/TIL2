CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

.mode csv
.import users.csv users


-- 30세 이상인 사람들
SELECT * FROM users WHERE age >= 30;

-- 30세 이상인 사람들의 이름
SELECT first_name FROM users WHERE age >= 30;

-- 30세 이상인 사람들의 이름 3명만
SELECT first_name FROM users WHERE age >= 30 LIMIT 3;

-- 30세 이상이고 성이 김인 사람
SELECT age, first_name FROM users WHERE age >= 30 and last_name = '김';
