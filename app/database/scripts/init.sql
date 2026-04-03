CREATE SCHEMA IF NOT EXISTS restaurant_app;



CREATE TABLE IF NOT EXISTS restaurant_app.companies (
id 					SERIAL 		PRIMARY KEY,
company_name 		VARCHAR(40) UNIQUE 			                NOT NULL,
franchise_name 		VARCHAR(40) UNIQUE 			                NOT NULL
);


CREATE TABLE IF NOT EXISTS restaurant_app.restaurants (
id 					SERIAL 		PRIMARY KEY,
company_id 			INT 		REFERENCES restaurant_app.companies(id),
terminals_amount 	SMALLINT 	DEFAULT 1 		                NOT NULL	CHECK (terminals_amount > 0),
restaurant_size 	SMALLINT 					                NOT NULL 	CHECK (restaurant_size > 0),
address 			VARCHAR(100) 				                NOT NULL 	CHECK (CHAR_LENGTH(address) BETWEEN 4 AND 100)
);


CREATE TABLE IF NOT EXISTS restaurant_app.restaurant_menu (
id 					SERIAL 		PRIMARY KEY,
restaurant_id 		INT 		REFERENCES restaurant_app.restaurants(id),
item 				VARCHAR(50)                         		NOT NULL	CHECK (CHAR_LENGTH(item) BETWEEN 2 AND 50),
price 				INT 						                NOT NULL	CHECK (price > 0),
discount 			INT		    DEFAULT 0	                    NOT NULL    CHECK (discount BETWEEN 0 AND 100),
is_temporary 		BOOL 		DEFAULT FALSE	                NOT NULL,
UNIQUE(restaurant_id, item)
);


CREATE TABLE IF NOT EXISTS restaurant_app.orders (
id 					SERIAL 		PRIMARY KEY,
restaurant_id  		INT 		REFERENCES restaurant_app.restaurants(id),
order_id 	  		INT 		unique 			                NOT NULL 	CHECK (order_id > 0),
terminal_number 	VARCHAR(1) 					                NOT NULL,
items               VARCHAR(50)[]                               NOT NULL,
to_go 				BOOL 		DEFAULT FALSE 	                NOT NULL
);
