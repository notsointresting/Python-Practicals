create database demo;
use demo;
create user 'sahiil' @'localhost'IDENTIFIED BY '3000';
grant all on demo.*to 'sahiil'@'localhost';
create table student(NAME varchar(20), SURNAME varchar(20), AGE int, PRN varchar(12));