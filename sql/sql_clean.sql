-- M3_T1:

ALTER TABLE orders_table
	ALTER COLUMN date_uuid			TYPE UUID USING date_uuid::UUID,
	ALTER COLUMN user_uuid			TYPE UUID USING user_uuid::UUID,
	ALTER COLUMN card_number		TYPE BIGINT USING card_number::BIGINT,
	ALTER COLUMN store_code			TYPE VARCHAR(20),
	ALTER COLUMN product_code		TYPE VARCHAR(20),
	ALTER COLUMN product_quantity 	TYPE SMALLINT;
	
-- M3_T2:

ALTER TABLE dim_users_table
	ALTER COLUMN first_name			TYPE VARCHAR(255),
	ALTER COLUMN last_name			TYPE VARCHAR(255),
	ALTER COLUMN date_of_birth		TYPE DATE,
	ALTER COLUMN country_code		TYPE VARCHAR(10),
	ALTER COLUMN user_uuid			TYPE UUID USING user_uuid::UUID,
	ALTER COLUMN join_date 			TYPE DATE;
	
-- M3_T3:

DELETE FROM dim_store_details
WHERE		store_code IN ('NRQKZWJ9OZ', 'QIUU9SVP51', 'Y8J0Z2W8O9', 'ISEE8A57FE', 'T0R2CQBDUS', 'TUOKF5HAAQ', '9D4LK7X4LZ');

DELETE FROM dim_store_details
WHERE		store_code = 'NULL';

UPDATE 		dim_store_details
SET 		opening_date = TO_DATE(opening_date, 'Month YYYY DD')::DATE
WHERE 		opening_date ~ '^[[:alpha:]]+ \d{4} \d{2}$';

UPDATE 		dim_store_details
SET 		opening_date = TO_DATE(opening_date, 'YYYY Month DD')::DATE
WHERE 		opening_date ~ '^\d{4} [[:alpha:]]+ \d{2}$';

ALTER TABLE dim_store_details
	ALTER COLUMN longitude			TYPE FLOAT,
	ALTER COLUMN locality			TYPE VARCHAR(255),
	ALTER COLUMN store_code			TYPE VARCHAR(20),
	ALTER COLUMN staff_numbers		TYPE SMALLINT,
	ALTER COLUMN opening_date		TYPE DATE USING opening_date::DATE,
	ALTER COLUMN store_type			TYPE VARCHAR(255),
	ALTER COLUMN latitude			TYPE FLOAT,
	ALTER COLUMN country_code		TYPE VARCHAR(10),
	ALTER COLUMN continent			TYPE VARCHAR(255);

-- M3_T4:

--DELETE FROM	dim_products
--WHERE			date_added ISNULL;

DELETE FROM	dim_products
WHERE		product_name IN ('LB3D71C025', 'VLPCU81M30', '9SX4G65YUX');

UPDATE		dim_products
SET			date_added = REPLACE(date_added, 'September 2017 06', '2017-09-06');

UPDATE		dim_products
SET			date_added = REPLACE(date_added, '2018 October 22', '2018-10-22');

UPDATE		dim_products
SET			product_price = REPLACE(product_price, '£', '');

ALTER TABLE	dim_products
ADD COLUMN	weight_class VARCHAR(20);

UPDATE	dim_products
SET		weight_class =
	CASE
		WHEN weight < 2 					THEN 'Light'
		WHEN weight >= 2 AND weight < 40 	THEN 'Mid_Sized'
		WHEN weight >= 40 AND weight < 140 	THEN 'Heavy'
		ELSE 'Truck_Required'
	END;
	
-- M3_T5:

ALTER TABLE	dim_products
	RENAME	removed to still_available;

UPDATE		dim_products
SET			still_available = REPLACE(still_available, 'Still_avaliable', 'True');

UPDATE		dim_products
SET			still_available = REPLACE(still_available, 'Removed', 'False');

ALTER TABLE dim_products
	ALTER COLUMN product_price		TYPE FLOAT USING product_price::double precision,
	ALTER COLUMN weight				TYPE FLOAT,
	ALTER COLUMN "EAN"				TYPE VARCHAR(20),
	ALTER COLUMN product_code		TYPE VARCHAR(20),
	ALTER COLUMN date_added			TYPE DATE USING date_added::DATE,
	ALTER COLUMN uuid				TYPE UUID USING uuid::UUID,
	ALTER COLUMN "still_available" 	TYPE BOOL USING still_available::BOOL,
	ALTER COLUMN weight_class		TYPE VARCHAR(20);
	
-- M3_T6:

--SELECT MAX(LENGTH(CAST("time_period" AS VARCHAR))) AS max_length
--FROM dim_date_times;

DELETE FROM dim_date_times
WHERE		"timestamp" ISNULL;

ALTER TABLE dim_date_times
	ALTER COLUMN "month"			TYPE VARCHAR(10),
	ALTER COLUMN "year"				TYPE VARCHAR(10),
	ALTER COLUMN "day"				TYPE VARCHAR(10),
	ALTER COLUMN time_period		TYPE VARCHAR(10),
	ALTER COLUMN date_uuid			TYPE UUID USING date_uuid::UUID;

-- M3_T7:

--SELECT MAX(LENGTH(CAST("card_details" AS VARCHAR))) AS max_length
--FROM dim_card_details;

UPDATE 	dim_card_details
SET 	date_payment_confirmed = TO_DATE(date_payment_confirmed, 'Month YYYY DD')::DATE
WHERE 	date_payment_confirmed ~ '^[[:alpha:]]+ \d{4} \d{2}$';

ALTER TABLE dim_card_details
	ALTER COLUMN card_number			TYPE BIGINT USING card_number::BIGINT,
	ALTER COLUMN expiry_date			TYPE DATE USING expiry_date::DATE,
	ALTER COLUMN date_payment_confirmed	TYPE DATE USING date_payment_confirmed::date;
