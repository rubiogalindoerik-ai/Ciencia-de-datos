CREATE DATABASE exccomp2;

USE exccomp2;

CREATE TABLE excercise1 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    department VARCHAR(30) NOT NULL,
    salary INT
);

INSERT INTO excercise1 (name, department, salary)
VALUES 
    ('Juan', 'IT', 50000),
    ('Maria', 'HR', 45000),
    ('Carlos', 'IT', 55000),
    ('Ana', 'Finanzas', 48000),
    ('Pedro', 'Marketing', 42000);

SELECT * FROM excercise1;

SELECT name, salary FROM excercise1 WHERE department='IT';

SELECT MAX(salary) FROM excercise1;

SELECT  department, COUNT(*) AS count_of_values FROM excercise1 GROUP BY department;

UPDATE excercise1 SET salary = 50000 WHERE name=Maria;

CREATE TABLE department (
    idDepartment INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL
);

INSERT INTO department (name)
VALUES 
    ('IT'),
    ('HR'),
    ('Finanzas');

CREATE TABLE employe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    idDepartment int NOT NULL,
    CONSTRAINT fk_department
    	FOREIGN KEY (idDepartment)
    	REFERENCES department(idDepartment)
);

INSERT INTO employe (name, idDepartment)
VALUES 
    ('Juan', 1),
    ('Maria', 2),
    ('Carlos', 1);

SELECT employe.name AS Employes, department.name AS Departments FROM employe
INNER JOIN department ON employe.idDepartment = department.idDepartment;

SELECT e.name AS Employes, d.name AS Departments FROM employe e
LEFT JOIN department d ON e.idDepartment = d.idDepartment;

SELECT d.name AS Department, COUNT(e.id) AS Total_Employes FROM department d
LEFT JOIN employe e ON d.idDepartment = e.idDepartment GROUP BY d.idDepartment, d.name;
