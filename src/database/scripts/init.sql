CREATE SCHEMA IF NOT EXISTS restaurant_app;


CREATE TABLE IF NOT EXISTS restaurant_app.users (
    id 		SERIAL 		PRIMARY KEY,
    name 	VARCHAR(30) NOT NULL 	CHECK (CHARACTER_LENGTH(name) BETWEEN 2 AND 30),
    surname VARCHAR(30) 			CHECK (CHARACTER_LENGTH(surname) BETWEEN 2 AND 30),
    
    phone 	VARCHAR(20) 			CHECK (
        CHARACTER_LENGTH(phone) BETWEEN 10 AND 20
    ),
    
    email 	VARCHAR(50) NOT NULL 	CHECK (
        email ~  '^[^@]+@[^@]+\.[^@]+$' AND
        CHARACTER_LENGTH(email) BETWEEN 5 AND 50
    ),
    
    address VARCHAR(100),
    payment VARCHAR(100)
);


CREATE TABLE IF NOT EXISTS restaurant_app.companies (
id 					SERIAL 		PRIMARY KEY,
company_name 		VARCHAR(40) UNIQUE 			                NOT NULL,
franchise_name 		VARCHAR(40) UNIQUE 			                NOT NULL
);


CREATE TABLE IF NOT EXISTS restaurant_app.restaurants (
id 					SERIAL 			PRIMARY KEY,
company_id 			INT 										REFERENCES restaurant_app.companies(id),
restaurant_size 	SMALLINT 						NOT NULL 	CHECK (restaurant_size > 0),
address 			VARCHAR(100)            		NOT NULL 	CHECK (CHAR_LENGTH(address) BETWEEN 4 AND 100)
);


CREATE TABLE IF NOT EXISTS restaurant_app.restaurant_menu (
id 					SERIAL 		PRIMARY KEY,
restaurant_id 		INT 		REFERENCES restaurant_app.restaurants(id),
name 				VARCHAR(50)                         		NOT NULL	CHECK (CHAR_LENGTH(name) BETWEEN 2 AND 50),
price 				INT 						                NOT NULL	CHECK (price > 0),
discount 			INT		    DEFAULT 0	                    NOT NULL    CHECK (discount BETWEEN 0 AND 100),
is_temporary 		BOOL 		DEFAULT FALSE	                NOT NULL,
UNIQUE(restaurant_id, name)
);


CREATE TABLE IF NOT EXISTS restaurant_app.orders (
id					SERIAL 		PRIMARY KEY,
restaurant_menu_id 	INT 		REFERENCES restaurant_app.restaurant_menu(id),
user_id				INT 		REFERENCES restaurant_app.users(id),
to_go 				BOOL		DEFAULT FALSE
);


CREATE TABLE IF NOT EXISTS restaurant_app.order_items (
id					SERIAL		PRIMARY KEY,
order_id			INT			REFERENCES restaurant_app.orders(id),
item				INT			REFERENCES restaurant_app.restaurant_menu(id),
amount				SMALLINT									NOT NULL	CHECK(amount > 0)
);


