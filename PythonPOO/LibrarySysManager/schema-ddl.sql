CREATE DATABASE Libraries;

CREATE TABLE Library(
    lib_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    lib_name varchar(50) NOT NULL,
    lib_address varchar(50) NOT NULL,
    lib_birth int NOT NULL,
    lib_tel varchar(50) NOT NULL
);