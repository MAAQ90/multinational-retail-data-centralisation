--SELECT MAX(LENGTH(CAST("card_details" AS VARCHAR))) AS max_length
--FROM dim_card_details;

ALTER TABLE dim_card_details
	ALTER COLUMN card_number			TYPE VARCHAR(19),
	ALTER COLUMN expiry_date			TYPE DATE USING expiry_date::DATE,
	ALTER COLUMN date_payment_confirmed	TYPE DATE;