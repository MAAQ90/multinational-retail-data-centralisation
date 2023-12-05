-- Query 1:	How many stores does the business have and in which countries?

SELECT		country_code, 	
		COUNT (country_code) AS total_no_stores
FROM		dim_store_details
GROUP BY	country_code
ORDER BY	total_no_stores DESC;

-- Query 2:	Which location currently have the most stores?

SELECT		locality,
		COUNT(*) AS total_no_stores
FROM		dim_store_details
GROUP BY	locality
ORDER BY	total_no_stores DESC
LIMIT		7;

-- Query 3:	Which months produced the largest amount of sales?

SELECT		SUM(orders_table.product_quantity * dim_products.product_price) AS total_sales,
		dim_date_times.month
FROM		dim_date_times
JOIN		orders_table ON dim_date_times.date_uuid = orders_table.date_uuid
JOIN		dim_products ON orders_table.product_code = dim_products.product_code
GROUP BY	dim_date_times.month
ORDER BY	total_sales DESC
LIMIT		3;

-- Query 4:	How many sales are coming from online?

SELECT		COUNT(*) as number_of_sales,
		SUM(product_quantity) AS product_quantity_count,
CASE		WHEN store_code LIKE 'WEB%' THEN 'Web'
		ELSE 'Offline'
		END AS location
FROM		orders_table
GROUP BY	location;

-- Query 5:	What percentage of sales comes through from each type of store?

SELECT		store_type,
		SUM(orders_table.product_quantity * dim_products.product_price) AS total_sales,
		SUM(product_quantity * product_price * 100)/(SUM(SUM(product_quantity * product_price))OVER()) AS percentage_total
FROM		orders_table
		JOIN dim_store_details 	ON orders_table.store_code = dim_store_details.store_code
		JOIN dim_products		ON orders_table.product_code = dim_products.product_code
GROUP BY	store_type
ORDER BY	total_sales DESC;

-- Query 6:	Which month in each year produced the highest cost of sales?

SELECT		SUM(product_quantity * product_price) AS total_sales,
		dim_date_times.year,
		dim_date_times.month
FROM		orders_table
		JOIN dim_date_times		ON orders_table.date_uuid = dim_date_times.date_uuid
		JOIN dim_products		ON orders_table.product_code = dim_products.product_code
GROUP BY	YEAR,
		MONTH
ORDER BY	total_sales DESC
LIMIT		10;

-- Query 7:	What is our staff headcount?

SELECT		SUM(staff_numbers) AS total_staff_numbers,
		country_code
FROM		dim_store_details
GROUP BY	country_code
ORDER BY	total_staff_numbers DESC;

-- Query 8: Which German store type is selling the most?

SELECT		SUM(product_quantity * product_price) AS total_sales,
		store_type,
		country_code
FROM		orders_table
		JOIN dim_store_details	ON orders_table.store_code = dim_store_details.store_code
		JOIN dim_products		ON orders_table.product_code = dim_products.product_code
WHERE		country_code = 'DE'
GROUP BY	store_type,
		country_code
ORDER BY	total_sales ASC;

-- Query 9: How quickly is the company making sales?

WITH		CTE1_datetime_extract AS
		(
		SELECT 		TO_TIMESTAMP(CONCAT(year, '-', month, '-', day, ' ', timestamp), 'YYYY-MM-DD H:M:S') as date_time,
							year
		FROM		dim_date_times
		ORDER BY	date_time DESC
		),
		CTE2_timediff AS
		(
		SELECT 		year,
				date_time,
				LEAD(date_time, 1) OVER (ORDER BY date_time DESC) as timediff
		FROM		CTE1_datetime_extract
		)
SELECT		year,
		AVG(date_time - timediff) AS actual_time_taken
FROM		CTE2_timediff
GROUP BY	year
ORDER BY	actual_time_taken DESC
LIMIT		5;







