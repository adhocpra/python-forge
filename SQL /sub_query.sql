use mydb;
CREATE TABLE employees (
id INT PRIMARY KEY,
name VARCHAR(60) NOT NULL,
department VARCHAR(50),
Salary int,
manager_ID INT
);

INSERT INTO employees VALUE(1, "A", "IT", 10, NULL);
INSERT INTO employees VALUE(2, "B", "IT", 10, NULL);
INSERT INTO employees VALUE(3, "c", "IT", 15, 1);
INSERT INTO employees VALUE(4, "D", "Sales", 12, 2);
INSERT INTO employees VALUE(5, "E", "Sales", 14, 4);
INSERT INTO employees VALUE(6, "F", "Admin", 11, NULL);
INSERT INTO employees VALUE(7, "F", "Office", 9, NULL);

SELECT * FROM employees ;
-- * WHERE
-- Subqueries are  used when you need an answer from one query used insider anotgher query
-- Finding earnings more than av by employees
SELECT name, salary FROM employees
WHERE salary > (SELECT AVG (salary) FROM employees);
-- Finding below average 
SELECT name, salary FROM employees
WHERE salary< (SELECT AVG(salary) FROM employees);
-- Finding highest paid employee 
SELECT name, salary
 FROM employees
WHERE salary= (SELECT MAX(SALARY) FROM employees);


-- * WItH insert
-- Find departments that have salary >8000
SELECT name from employees
WHERE department IN ( SELECT department FROM employees WHERE salary>15);

-- NOT in

SELECT name FROM employees
WHERE id NOT IN (SELECT manager_id FROM employees Where manager_ID is NOT NULL);