CREATE DATABASE Libraries;

CREATE TABLE Library(
    lib_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    lib_name varchar(50) NOT NULL,
    lib_address varchar(50) NOT NULL,
    lib_birth int NOT NULL,
    lib_tel varchar(50) NOT NULL
);

CREATE TABLE Book(
    book_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    lib_id int NOT NULL,
    book_name varchar(100) NOT NULL,
    book_author varchar(100) NOT NULL,
    book_pages int NOT NULL,
    FOREIGN KEY (lib_id) REFERENCES Library(lib_id)
);

ALTER TABLE Book ADD book_qtd int;

CREATE TABLE User(
    user_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_name varchar(50) NOT NULL,
    user_tel varchar(50),
    user_address varchar(50) NOT NULL
)