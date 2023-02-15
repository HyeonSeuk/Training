-- 문제1
CREATE TABLE posts (
postld INT AUTO_INCREMENT,
title VARCHAR(50) NOT NULL,
content VARCHAR(200) NOT NULL,
PRIMARY KEY (postld)
);

-- 문제2
ALTER TABLE posts
ADD writer VARCHAR(100) DEFAULT 'Anonymous',
ADD created_at datetime DEFAULT CURRENT_TIMESTAMP;

-- 문제3
ALTER TABLE posts
MODIFY content text;

-- 문제4
ALTER TABLE posts
DROP COLUMN writer;

-- 문제5
DROP TABLE posts;

-- 문제6
CREATE TABLE IF NOT EXISTS posts(
postld INT AUTO_INCREMENT,
title VARCHAR(50) NOT NULL,
content text NOT NULL,
writer VARCHAR(20) DEFAULT 'Anonymous',
created_at datetime DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (postld)
);

-- 문제7
DROP TABLE IF EXISTS posts;