-- 문제1
CREATE TABLE users (
userld INT AUTO_INCREMENT NOT NULL,
first_name VARCHAR(20) NOT NULL,
last_name VARCHAR(20) NOT NULL,
birthday date NOT NULL,
city VARCHAR(100),
country VARCHAR(100),
email VARCHAR(100),
created_at datetime DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (userld)
);

-- 문제2
INSERT INTO
	users (first_name, last_name, birthday, city, country, email)
VALUES
	('Beemo', 'Jeong', '1000-01-01', '', '','beemo@hphk.kr'),
	('Jieun', 'Lee', '1993-05-16', 'Seoul', 'Korea', ''),
	('Dami', 'Kim', '1995-04-09', 'Seoul', 'Korea', ''),
	('Kwangsoo', 'Lee', '1985-07-14', 'Seoul', 'Korea', '');
	
-- 문제3
INSERT INTO
	users (first_name, last_name, birthday, city, country)
VALUES
	('hello', 'world', '2023-02-14', 'Seoul', 'Korea'),
    ('hell', 'worl', '2023-02-13', 'Seoul', 'Korea'),
    ('hel', 'wor', '2023-02-12', 'Seoul', 'Korea'),
    ('he', 'wo', '2023-02-11', 'Seoul', 'Korea'),
    ('h', 'w', '2023-02-10', 'Seoul', 'Korea');

-- 문제4
UPDATE
	users
SET
	first_name = 'Hyeonseok',
    last_name = 'Seo',
    birthday = '1997-12-20'
WHERE
	userld = 2;

-- 문제5
UPDATE
	users
SET
	country = 'Korea'
WHERE
	country = '';

-- 문제6
DELETE FROM
	users
WHERE
	first_name = 'Beemo';

-- 문제7
DELETE FROM
	users
WHERE
	first_name = 'Kwangsoo'
    AND last_name = 'Lee';

-- 문제8
DELETE FROM
	users
ORDER BY
	userld DESC
LIMIT 1;