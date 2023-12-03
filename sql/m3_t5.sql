--ALTER TABLE dim_products
--	RENAME removed	TO still_available


ALTER TABLE dim_products
	ALTER COLUMN product_price		TYPE FLOAT USING product_price::double precision,
	ALTER COLUMN weight				TYPE FLOAT,
	ALTER COLUMN "EAN"				TYPE VARCHAR(17),
	ALTER COLUMN product_code		TYPE VARCHAR(11),
	ALTER COLUMN date_added			TYPE DATE,
	ALTER COLUMN uuid				TYPE UUID USING uuid::UUID,
	ALTER COLUMN "still_available" 	TYPE BOOL USING still_available::BOOL,
	ALTER COLUMN weight_class		TYPE VARCHAR(14);