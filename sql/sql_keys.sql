-- Set primary keys:

ALTER TABLE 	dim_card_details
ADD PRIMARY KEY	(card_number);

ALTER TABLE		dim_date_times
ADD PRIMARY KEY	(date_uuid);

ALTER TABLE		dim_products
ADD PRIMARY KEY	(product_code);

ALTER TABLE		dim_store_details
ADD PRIMARY KEY	(store_code);

ALTER TABLE		dim_users_table
ADD PRIMARY KEY (user_uuid);

-- Set foreign keys:

ALTER TABLE 	orders_table
ADD CONSTRAINT	fk_card_details
FOREIGN KEY 	(card_number)
REFERENCES		dim_card_details(card_number);

ALTER TABLE 	orders_table
ADD CONSTRAINT	fk_date_times
FOREIGN KEY 	(date_uuid)
REFERENCES		dim_date_times(date_uuid);

ALTER TABLE 	orders_table
ADD CONSTRAINT	fk_products
FOREIGN KEY 	(product_code)
REFERENCES		dim_products(product_code);

ALTER TABLE 	orders_table
ADD CONSTRAINT	fk_store_details
FOREIGN KEY 	(store_code)
REFERENCES		dim_store_details(store_code);

ALTER TABLE 	orders_table
ADD CONSTRAINT	fk_users_table
FOREIGN KEY 	(user_uuid)
REFERENCES		dim_users_table(user_uuid);