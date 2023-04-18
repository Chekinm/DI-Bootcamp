/* ex1 1 Get a list of all film languages. */

SELECT name
FROM language as l
INNER JOIN film as f ON
l.language_id = f.language_id
group by name

/* 2  Get a list of all films joined with their languages – select the following details : film title, description, and language name. Try your query with different joins:
Get all films, even if they don’t have languages.
Get all languages, even if there are no films in those languages.*/

SELECT title, description, name 
FROM film as f 
INNER JOIN language as l ON
l.language_id = f.language_id;

SELECT title, description, name 
FROM film as f 
LEFT JOIN language as l ON
l.language_id = f.language_id
ORDER BY l.name DESC;


SELECT title, description, name 
FROM film as f 
RIGHT JOIN language as l ON
l.language_id = f.language_id
ORDER BY l.name DESC;

/* 3 Create a new table called new_film with the following columns : id, name. Add some new films to the table. */

create table new_Film (
id serial primary key,
name varchar (50)
	)
INSERT INTO new_Film (name)
VALUES ('Kill Bill 1'),
 ('Kill Bill 2');


/*Create a new table called customer_review, which will contain film reviews that customers will make.
Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
It should have the following columns:
review_id – a primary key, non null, auto-increment.
film_id – references the new_film table. The film that is being reviewed.
language_id – references the language table. What language the review is in.
title – the title of the review.
score – the rating of the review (1-10).
review_text – the text of the review. No limit on the length.
last_update – when the review was last updated.*/

CREATE TABLE customer_review (
review_id serial primary key,
film_id int,
language_id int,
title varchar(50),
score int CHECK( score > 0 AND score < 11),
review_text text,
last_update timestamp,
CONSTRAINT film_id_cnstr
      FOREIGN KEY(film_id)
      REFERENCES film(film_id)
	  ON DELETE CASCADE
	)

INSERT INTO customer_review (
	film_id,
	language_id,
	title,
	score,
	review_text,
	last_update)
VALUES(
1,
2,
'my review 1',
10,
'film suck',
now())


INSERT INTO customer_review (
	film_id,
	language_id,
	title,
	score,
	review_text,
	last_update)
VALUES(
999,
3,
'my review 2',
1,
'film rocks',
now());

SELECT f.title, cr.title , cr.review_text
FROM film as f
INNER JOIN customer_review as cr on 
f.film_id = cr.film_id;

INSERT INTO film (title, language_id)
values ('sdfsdfsdf', 2);

INSERT INTO customer_review (
	film_id,
	language_id,
	title,
	score,
	review_text,
	last_update)
VALUES(
1002,
3,
'my review 2',
1,
'film realy suck better to delete',
now());

SELECT f.title, cr.title , cr.review_text
FROM film as f
INNER JOIN customer_review as cr on 
f.film_id = cr.film_id
WHERE f.film_id > 1000;

DELETE FROM
WHERE film_id = 1002;

SELECT * from customer_review;




