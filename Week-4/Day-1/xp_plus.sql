CREATE TABLE students (
	ID SERIAL PRIMARY KEY,
	first_name VARCHAR(12), 
	last_name VARCHAR (12),
	birth_date DATE
); 

INSERT INTO students (first_name, last_name, birth_date)
VALUES ('Marc','Benichou','1998-11-02'),
('Yoan','Cohen','2010-12-03'),
('Lea','Benichou','1987-07-27'),
('Amelia','Dux','1996-04-07'),
('David','Grez','2003-06-14'),
('Omer','Simpson','1980-10-03');
INSERT INTO students (first_name, last_name, birth_date)
VALUES ('Mikhail','Chekin','1976-06-25');

select ID from students where last_name = 'Chekin'

select * from  students

select * from  students where last_name = 'Benichou' and  first_name = 'Marc'

select * from  students where last_name = 'Benichou' or first_name = 'Marc'

select * from  students where first_name LIKE '%a%'

select * from  students where first_name ILIKE 'a%'

select * from  students where first_name LIKE '%a'

select * from  students where first_name LIKE '%a_'

select * from  students where ID = 1 or ID = 3 

select * from  students  where birth_date  >= '2000-01-01'
