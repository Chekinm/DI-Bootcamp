create table if not exists user_password (
	id serial primary key,
	username varchar(40) UNIQUE,
	password VARCHAR (200)
	);

