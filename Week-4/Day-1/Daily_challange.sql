CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
)

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Matt','Damon','08/10/1970', 5);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('George','Clooney','06/05/1961', 2);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Matt','Damon','08/10/1970', 5);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Kate','Fox','01/02/1922', 12);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Megan','Jain','01/03/2001', 0);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES
('Julia','Rain','01/03/1998', 1),
('Mike','Farber','02/03/2001', 13),
('John','Don','04/03/2001', 17);


select count(first_name) as counts from actors;

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Stoya',NULL,'01/03/2001', 0);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Ken','Barby','1998/1/1', );

-- change column constraint to accept NULL value

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Ken','Barby','1998/1/1', NULL );

select * from actors
--  now added succesefully





