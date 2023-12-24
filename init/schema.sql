create database if not exists postgreesql;

create table if not exists
  users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    age BIGINT NOT NULL
  );
