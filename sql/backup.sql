CREATE TABLE	dim_store_details_backup AS
SELECT * FROM dim_store_details;

INSERT INTO dim_store_details_backup
SELECT * FROM dim_store_details;