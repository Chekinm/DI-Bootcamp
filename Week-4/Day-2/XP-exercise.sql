SELECT * from customer

SELECT (first_name, last_name) as full_name from customer

SELECT DISTINCT create_date from customer

SELECT * from customer ORDER BY first_name DESC

SELECT film_id, title, description, release_year, rental_rate 
FROM film
ORDER BY rental_rate ASC

SELECT address, phone 
FROM address 
WHERE district = 'Texas'

SELECT *
FROM film
WHERE film_id = 15 or film_id = 150 

SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title='Groundhog day' or  title='Nemo Campus'

SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title ilike 'Gr%'

SELECT film_id, title, rental_rate
FROM film
ORDER BY rental_rate ASC
LIMIT 10

SELECT film_id, title, rental_rate
FROM film
ORDER BY rental_rate ASC
OFFSET 10 ROWS
FETCH NEXT 10 ROWS ONLY

SELECT c.customer_id, first_name, last_name, amount, payment_date
FROM customer as c 
INNER JOIN payment as p
ON  p.customer_id  = c.customer_id 
ORDER BY c.customer_id ASC


SELECT f.film_id
FROM film as f
LEFT OUTER JOIN inventory as i
ON  (f.film_id = i.film_id) 
WHERE i.film_id is NULL

/*another solution for 13*/

SELECT f.film_id
FROM film as f
EXCEPT
SELECT i.film_id
FROM inventory as i
ORDER BY film_id

select city,  country 
FROM city AS s
INNER JOIN  country AS c
ON c.country_id=s.country_id

SELECT c.customer_id, first_name, last_name, amount, payment_date, staff_id
FROM customer as c 
INNER JOIN payment as p
ON  p.customer_id  = c.customer_id 
ORDER BY p.staff_id ASC























