
-- Part II:

-- Create a table named Book, with the columns : book_id SERIAL PRIMARY KEY, title NOT NULL, author NOT NULL

create table book (
book_id serial primary key,
title varchar (50) NOT NULL,
author  varchar (50) NOT NULL
);

-- Insert those books :
-- Alice In Wonderland, Lewis Carroll
-- Harry Potter, J.K Rowling
-- To kill a mockingbird, Harper Lee

INSERT INTO book (title, author)
VALUES 
( 'Alice In Wonderland', 'Lewis Carroll'),
( 'Harry Potter', 'J.K Rowling'),
( 'To kill a mockingbird', 'Harper Lee');



-- Create a table named Student, with the columns : student_id SERIAL PRIMARY KEY, name NOT NULL UNIQUE, age. Make sure that the age is never bigger than 15 (Find an SQL method);

create table student (
	student_id SERIAL PRIMARY KEY, 
	name varchar (20) NOT NULL UNIQUE,
	age int CHECK(age < 15)

);

INSERT INTO student (name, age)
VALUES
('John', 12),
('Lera', 11),
('Patrick', 10),
('Bob', 14);


-- Create a table named Library, with the columns :
-- book_fk_id ON DELETE CASCADE ON UPDATE CASCADE
-- student_id ON DELETE CASCADE ON UPDATE CASCADE
-- borrowed_date
-- This table, is a junction table for a Many to Many relationship with the Book and Student tables : A student can borrow many books, and a book can be borrowed by many children
-- book_fk_id is a Foreign Key representing the column book_id from the Book table
-- student_fk_id is a Foreign Key representing the column student_id from the Student table
-- The pair of Foreign Keys is the Primary Key of the Junction Table

create table library (
	book_fk_id int   NOT NULL,
	student_fk_id int  NOT NULL,
	primary key (book_fk_id, student_fk_id),
	CONSTRAINT book_fk FOREIGN KEY (book_fk_id) REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT student_fk FOREIGN KEY (student_fk_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
);

ALTER TABLE library
ADD date_taken date;


-- Add 4 records in the junction table, use subqueries.
-- the student named John, borrowed the book Alice In Wonderland on the 15/02/2022
-- the student named Bob, borrowed the book To kill a mockingbird on the 03/03/2021
-- the student named Lera, borrowed the book Alice In Wonderland on the 23/05/2021
-- the student named Bob, borrowed the book Harry Potter the on 12/08/2021


INSERT INTO library (student_fk_id, book_fk_id, date_taken)
VALUES 
((SELECT student_id FROM student WHERE name='John'),(SELECT book_id FROM book WHERE title='Alice In Wonderland'), now());

INSERT INTO library (student_fk_id, book_fk_id, date_taken)
VALUES 
((SELECT student_id FROM student WHERE name='Bob'),(SELECT book_id FROM book WHERE title='To kill a mockingbird'),'2021-03-03'),
((SELECT student_id FROM student WHERE name='Lera'),(SELECT book_id FROM book WHERE title='Alice In Wonderland'), '2021-05-23'),
((SELECT student_id FROM student WHERE name='Bob'),(SELECT book_id FROM book WHERE title='Harry Potter'), '2021-08-01');




-- Display the data
-- Select all the columns from the junction table

SELECT * FROM library

-- Select the name of the student and the title of the borrowed books

SELECT name, title, age FROM library 
JOIN student ON  student_fk_id=student_id
JOIN book ON book_fk_id=book_id)

-- Select the average age of the children, that borrowed the book Alice in Wonderland

SELECT AVG(age) FROM
	(SELECT name, title, age 
	 FROM library 
	 JOIN student ON  student_fk_id=student_id
	 JOIN book ON book_fk_id=book_id) as joined_table
WHERE title = 'Alice In Wonderland'


-- Delete a student from the Student table, what happened in the junction table ?
DELETE from student
WHERE name='Bob'

all records related to deleted student also removes, as we specify on delete cascade constraint
