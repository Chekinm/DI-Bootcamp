create table customers (
	id serial primary key,
	first_name varchar(12), 
	second_name varchar (12)
	); 

create table items (
	id serial primary key,
	item varchar(20), 
	price int
	); 

insert into customers (first_name, second_name) 
values
('Greg','Jones'),
('Sandra ','Jones'),
('Scott','Scott'),
('Trevor ','Green'),
('Melanie ','Johnson');

insert into items (item, price) 
values
('Small Desk',100),
('Large desk',300),
('Fan ',80);

select * from items

select * from items where price > 80

select * from items where price <= 300

select * from customers where second_name = 'Smith'

select * from customers where second_name = 'Jones'

select * from customers where second_name != 'Scott'



