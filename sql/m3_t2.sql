-- M3_T2:

/*
UPDATE	dim_users_table
SET		country_code = REPLACE(country_code, 'GGB', 'GB')
WHERE	country_code LIKE '%GGB%'
*/

ALTER TABLE dim_users_table
	ALTER COLUMN first_name		TYPE VARCHAR(255),
	ALTER COLUMN last_name		TYPE VARCHAR(255),
	ALTER COLUMN date_of_birth	TYPE DATE,
	ALTER COLUMN country_code	TYPE VARCHAR(2),
	ALTER COLUMN user_uuid		TYPE UUID USING user_uuid::UUID,
	ALTER COLUMN join_date 		TYPE DATE;
