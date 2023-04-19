create table customer (
customer_id serial primary key,
first_name varchar (20),
last_name  varchar (20) NOT NULL
	
);

create table customer_profile (
	customer_id int primary key, 
	isLoggedIn bool DEFAULT false,
	CONSTRAINT customer_to_profile FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE
);

INSERT INTO customer (first_name, last_name)
VALUES 
	('John', 'Doe'),
	('Jerome', 'Lalu'),
	('Lea', 'Rive');

INSERT INTO customer_profile (customer_id, isLoggedIn)
VALUES 
	((SELECT(customer_id) FROM customer WHERE first_name='John'), TRUE), 
	((SELECT(customer_id) FROM customer WHERE first_name='Jerome'), FALSE)
;

/* The first_name of the LoggedIn customers*/
SELECT first_name FROM customer as cs
LEFT JOIN customer_profile as cp
ON cs.customer_id = cp.customer_id
WHERE isLoggedIn

/*All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.
 The number of customers that are not LoggedIn */

SELECT first_name, isLoggedIn FROM customer as cs
LEFT JOIN customer_profile as cp
ON cs.customer_id = cp.customer_id

