create database if not exists ma_database;

create table if not exists `ma_database`.`users` (
  id bigint not null AUTO_INCREMENT,
  first_name varchar(255) not null,
  last_name varchar(255) not null,
  email varchar(255) not null,
  age bigint not null,
  primary key (id)
)
