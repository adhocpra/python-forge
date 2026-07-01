USE mydb;
CREATE TABLE sales (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    department VARCHAR(50) NOT NULL,
    salary INT,
    email VARCHAR(100) UNIQUE
);

INSERT INTO sales (name, department, salary, email) VALUES ("Rita", "IT", 60000, "rita@gmail.com");
INSERT INTO sales (name, department, salary, email) VALUES ("Cam", "Production", 50000, "cam@gmail.com");
INSERT INTO sales (name, department, salary, email) VALUES ("Dan", "Developer", 80000, "dan@gmail.com");
INSERT INTO sales (name, department, salary, email) VALUES ("Even", "IT", 90000, "even@gmail.com");
INSERT INTO sales (name, department, salary, email) VALUES ("Fish", "Maintenance", 30000, "fish@gmail.com");

SELECT * FROM sales;
-- GROUP BY
SELECT department, COUNT(*) as total_employees
FROM sales
GROUP BY department;

SELECT department, sum(salary) as total_salary
FROM sales
GROUP BY department;

SELECT department, MAX(salary) as highest_salary
FROM sales
GROUP BY department;

SELECT department, AVG(salary) as Average_Salary
FROM sales
GROUP BY Department
ORDER BY AVerage_salary DESC;

SELECT department, AVG(salary) as Average_Salary
FROM sales
GROUP BY department

HAVING Average_salary> 40000;

INSERT INTO sales(name, department, salary, email) VALUES ("Wish", "IT", 30000, "dis@gmail.com");
SELECT department,COUNT(*) AS total
FROM sales
GROUP BY department
Having count(*)>1;

SELECT DISTINCT department FROM sales;

-- LIMIT (rows)
-- Show only three rows
SELECT * FROM sales LIMIT 3;
-- skip 2 rows and show next 3
SELECT * FROM sales LIMIT 3 OFFSET 2;

-- top 3 salaries
SELECT * FROM sales
ORDER BY salary DESC
LIMIT 3;

-- LIKE ( pattern search)

-- Name starting with R
SELECT * FROM sales where name LIKE 'R%';
select * from sales where name LIKE '%h';-- ending with h
-- Names containing 'a'

SELECT * FROM sales where name  LIKe '%a%' ;
select * from sales where name like '___'

