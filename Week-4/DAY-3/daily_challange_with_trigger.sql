create table product_orders (
id serial primary key,
buyer_name varchar (20),
total int
	
)

create table items (
	id serial primary key,
	item_name varchar(20),
	item_price int,
	order_id int 
)

/* Create one to many connetcion. Now we can set order_id to item and it will belong to aome order from product oreders */
ALTER TABLE items 
    ADD FOREIGN KEY (order_id) REFERENCES product_orders (id);


/* create some itmes*/
INSERT INTO items (item_name, item_price)
VALUES 
('one', 10),
('two', 20),
('three', 30),
('four', 40),
('fife', 50),
('six', 60);

/* create two orders */
insert into product_orders (buyer_name)
values ('mike');

insert into product_orders (buyer_name)
values ('bob');



/* create function which will do calcualtions */
create or replace function total(porduct_id int)
returns int as $$
	declare
		total_sum int;
	begin 
		total_sum := (select sum(item_price) from items where order_id = porduct_id );
		return total_sum;
	end;
$$ language plpgsql IMMUTABLE; 


/* now we need this function execute each time when status of the items (orders_id) is updated
we create triger and tirger function which will call our clculation finction
a little bit tricky but it is working and I don't know how to optimaize it */

CREATE OR REPLACE FUNCTION update_total()
  RETURNS trigger AS
$$
BEGIN

update product_orders as product_orders 
set total = total(id) ;
return New;
END;
$$
LANGUAGE 'plpgsql';
CREATE or replace TRIGGER update_total
  AFTER UPDATE
  ON items

  EXECUTE PROCEDURE update_total();




/* Now we can set sold some item to BOd and some to Mike */

update items
set order_id = 1 
where id = 1 or id = 3 or id = 5;

update items
set order_id = 2 
where id = 2 or id = 4 or id = 6;





/* now get all things to mike*/
update items
set order_id = 1 
where id = 2 or id = 4 or id = 6;

select * from product_orders;

/*cool!*/






