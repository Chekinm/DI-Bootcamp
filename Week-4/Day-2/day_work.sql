-- CREATE TABLE producers(
--  producer_id SERIAL PRIMARY KEY,
--  first_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (50) NOT NULL,
--  birthdate DATE NOT NULL,
--  number_oscars SMALLINT NOT NULL
-- );

-- INSERT INTO producers (first_name, last_name, birthdate, number_oscars)
-- VALUES('Lisa','Vachovski','08/10/1970', 15);

-- INSERT INTO producers (first_name, last_name, birthdate, number_oscars)
-- VALUES('Tinto','Brass','06/05/1955', 100);

-- create table apartment (
-- id serial primary key,
-- location varchar(50),
-- actor_id int references actors(actor_id)
-- ); 

-- insert into apartment (location, actor_id) 
-- values 
-- ('Beverly hills', 1); 

-- insert into apartment (location, actor_id) 
-- values 
-- ('Los Angeles', 2); 

-- insert into apartment (location, actor_id) 
-- values 
-- ('New York', 3); 

-- select *
-- from actors, producers
--   inner join apartment
--     on actors.actor_id = apartment.actor_id;

-- alter table actors 
-- ADD  location_id int  references apartment(id);

-- update actors
-- set location_id = 1  where actor_id = 1 or actor_id = 2 or actor_id = 3;

-- update actors
-- set location_id = 3  where actor_id = 7 or actor_id = 8 or actor_id = 9;

select *
from actors
  inner join apartment
    on actors.location_id = apartment.id
	where apartment.id = 3;