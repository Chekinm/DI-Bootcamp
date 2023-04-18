/* 1. Use UPDATE to change the language of some films. Make sure that you use valid languages.*/

UPDATE film
SET language_id = 3
WHERE film_id=1;

/* 2 Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table? */

cutomer has one foreign key - address_id with reference to address
we cannot create cutomer with addres_id not defined in addres table
Key (address_id)=(12345) is not present in table "address".

insert into customer (first_name, last_name,address_id, store_id)
values ('mike','john',12345, 1)

/*get back Key (address_id)=(12345) is not present in table "address".*/



/* 3. We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking? */

I think it is an easy step. As we thisis a child table, not parent.

DROP TABLE customer_review;

/* 4. Find out how many rentals are still outstanding (ie. have not been returned to the store yet).*/

select count(rental_id) from rental
where return_date is NULL;


/* 5 Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet) */

SELECT title, rental_rate
FROM film
WHERE film_id in (
	SELECT i.film_id
	FROM inventory AS i
	INNER JOIN rental AS r
	on i.inventory_id= r.inventory_id
	where r.return_date is NULL
	)
ORDER BY rental_rate DESC LIMIT 30;



/* 6.1. Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.*/

SELECT f.film_id, f.title
FROM  film  as f
JOIN film_actor as fa ON
f.film_id = fa.film_id
WHERE 
description ILIKE '%sumo wrestler%' AND 
actor_id = (select actor_id from actor where first_name='Penelope' and last_name='Monroe');



/* 6.2 The 2nd film : A short documentary (less than 1 hour long), rated “R”.*/
SELECT film_id,  title
FROM film
WHERE fulltext @@ plainto_tsquery('documentary') AND length < 60 AND rating = 'R';


 /*The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.*/


select f.title from film as f
inner join inventory as i on f.film_id = i.film_id
where
inventory_id in 
		(select r.inventory_id from rental as r
		inner join payment as pay on r.customer_id= pay.customer_id
		where 
			amount > 4.00 and 
			r.customer_id = (select customer_id from customer where first_name='Matthew' and last_name = 'Mahan') and
			return_date >= '2005-07-29' and return_date <= '2005-07-30');



/* The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.*/


SELECT f.title, f.film_id, f.replacement_cost 
FROM film as f
INNER JOIN inventory AS i 
ON f.film_id = i.film_id
WHERE
fulltext @@ plainto_tsquery('boat') 
AND inventory_id in (SELECT r.inventory_id 
					 FROM rental AS r
					 INNER JOIN payment as pay 
					 ON r.customer_id = pay.customer_id
					 WHERE amount > 4.00 and 
						   r.customer_id = (SELECT customer_id 
											FROM customer
											WHERE first_name='Matthew' 
											AND   last_name = 'Mahan'
											) 
					)
ORDER BY f.replacement_cost DESC LIMIT 1;