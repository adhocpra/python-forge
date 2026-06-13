DROP DATABASE IF EXISTS db_name;
CREATE DATABASE db_name;
USE db_name;

CREATE TABLE dept(
    dept_id   INT         NOT NULL PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL
);

CREATE TABLE projects (
    pj_id    INT         NOT NULL PRIMARY KEY,
    name     VARCHAR(50) NOT NULL,
    language VARCHAR(50) NOT NULL,
    dept_id  INT         NOT NULL,
    FOREIGN KEY (dept_id) REFERENCES dept(dept_id)
);

CREATE TABLE developers(
    dv_id       INT         NOT NULL PRIMARY KEY,
    dv_name     VARCHAR(50) NOT NULL,
    dv_location VARCHAR(50) NOT NULL,
    dept_id     INT         NOT NULL,
    FOREIGN KEY (dept_id) REFERENCES dept(dept_id)
);

INSERT INTO dept VALUES (1, 'MR');
INSERT INTO dept VALUES (2, 'PR');
INSERT INTO dept VALUES (3, 'BR');
INSERT INTO dept VALUES (4, 'HR');

INSERT INTO projects VALUES (1, 'House', '.py',   1);
INSERT INTO projects VALUES (2, 'Car',   '.java',  4);
INSERT INTO projects VALUES (3, 'Train', '.C++',   3);

INSERT INTO developers VALUES (1, 'A', 'KTM', 3);
INSERT INTO developers VALUES (2, 'B', 'NY',  1);
INSERT INTO developers VALUES (3, 'C', 'MO',  2);

SELECT * FROM dept;
SELECT * FROM projects;
SELECT * FROM developers;