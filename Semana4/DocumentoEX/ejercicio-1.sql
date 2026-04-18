-- SQL para crear la base de datos y tablas
-- Generated from CSV files

-- Create database
CREATE DATABASE IF NOT EXISTS empleados;
USE empleados;

-- Table: departamentos
DROP TABLE IF EXISTS departamentos;
CREATE TABLE departamentos (
    iddepartamentos INT PRIMARY KEY,
    departamento VARCHAR(45)
);

-- Table: puestos
DROP TABLE IF EXISTS puestos;
CREATE TABLE puestos (
    idpuestos INT PRIMARY KEY,
    puesto VARCHAR(45)
);

-- Table: lideres
DROP TABLE IF EXISTS lideres;
CREATE TABLE lideres (
    idlideres INT PRIMARY KEY,
    nombre VARCHAR(45)
);

-- Table: empleados
DROP TABLE IF EXISTS empleados;
CREATE TABLE empleados (
    idempleados INT PRIMARY KEY,
    nombre VARCHAR(45),
    fecha_ingreso DATE,
    sueldo DECIMAL(10,2),
    puestos_idpuestos INT NOT NULL,
    departamentos_iddepartamentos INT NOT NULL,
    lideres_idlideres INT,
    FOREIGN KEY (puestos_idpuestos) REFERENCES puestos(idpuestos),
    FOREIGN KEY (departamentos_iddepartamentos) REFERENCES departamentos(iddepartamentos),
    FOREIGN KEY (lideres_idlideres) REFERENCES lideres(idlideres)
);

-- Insert data: departamentos
INSERT INTO departamentos (iddepartamentos, departamento) VALUES
(1, 'Ventas'),
(2, 'TI'),
(3, 'Marketing');

-- Insert data: puestos
INSERT INTO puestos (idpuestos, puesto) VALUES
(1, 'Gerente'),
(2, 'Analista'),
(3, 'Desarrollador');

-- Insert data: lideres
INSERT INTO lideres (idlideres, nombre) VALUES
(1, 'Juan Pérez'),
(2, 'Ana Gómez');

-- Insert data: empleados
-- Nota: Los empleados con id_lider NULL son gerentes que no tienen líder
INSERT INTO empleados (idempleados, nombre, fecha_ingreso, sueldo, puestos_idpuestos, departamentos_iddepartamentos, lideres_idlideres) VALUES
(1, 'Juan Pérez', '2015-06-01', 75000.00, 1, 1, NULL),
(2, 'Ana Gómez', '2018-09-15', 50000.00, 2, 2, 1),
(3, 'Luis Martínez', '2020-01-10', 60000.00, 3, 2, 2),
(4, 'María Rodríguez', '2014-12-20', 80000.00, 1, 3, NULL),
(5, 'Carlos García', '2019-03-30', 52000.00, 2, 2, 1),
(6, 'Elena Fernández', '2021-07-22', 62000.00, 3, 2, 2),
(7, 'Pedro Sánchez', '2013-11-18', 77000.00, 1, 1, NULL),
(8, 'Marta Díaz', '2017-05-25', 53000.00, 2, 2, 1),
(9, 'José López', '2020-10-14', 63000.00, 3, 2, 2),
(10, 'Laura Torres', '2016-08-05', 79000.00, 1, 3, NULL);