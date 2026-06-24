use db_name;
CREATE TABLE employees(
ID int PRIMARY KEY,
name VARCHAR(50)
);

CREATE TABLE departments(
ID int,
dept_name VARCHAR(50)
);

INSERT INTO employees VALUES (1,'Pravat');
INSERT INTO employees VALUES (2,'Sarah');
INSERT INTO employees VALUES (3,'Moin');

INSERT INTO departments VALUE(1, 'Finance');
INSERT INTO departments VALUES (2,'IT');

SELECT * FROM employees;
SELECT * FROM departments;
-- LEFT join  
SELECT employees.name, departments.dept_name -- want name and employee columns from 2 table
FROM employees -- main table is employee
LEFT JOIN departments ON employees.ID= departments.ID;
-- in this join MOIN has null dept and appears

-- INNER JOIN
SELECT employees.name, departments.dept_name
FROM employees
INNER JOIN departments ON employees.ID= departments.ID;

INSERT INTO departments VALUES (99, 'HR');
-- RIGHT JOIN
SELECT employees.name, departments.dept_name
FROM employees
RIGHT JOIN departments ON employees.ID= departments.ID;

-- FULL JOIN
SELECT employees.name, departments.dept_name
FROM employees
LEFT JOIN departments ON employees.ID = departments.ID 
UNION
SELECT employees.name, departments.dept_name
FROM employees
RIGHT JOIN departments ON employees.ID= departments.ID;


