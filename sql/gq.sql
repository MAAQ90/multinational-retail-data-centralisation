/*
UPDATE dim_store_details
SET opening_date = TO_DATE(opening_date, 'Month YYYY DD')::DATE
WHERE opening_date ~ '^[[:alpha:]]+ \d{4} \d{2}$';

UPDATE dim_store_details
SET opening_date = TO_DATE(opening_date, 'YYYY Month DD')::DATE
WHERE opening_date ~ '^\d{4} [[:alpha:]]+ \d{2}$';
*/

DELETE FROM dim_store_details
WHERE		store_code IN ('NRQKZWJ9OZ', 'QIUU9SVP51', 'Y8J0Z2W8O9', 'ISEE8A57FE', 'T0R2CQBDUS', 'TUOKF5HAAQ', '9D4LK7X4LZ');

DELETE FROM dim_store_details
WHERE		store_code = 'NULL';

SELECT		*
FROM		dim_store_details;

--FROM		orders_table
--ORDER BY	store_code ASC;
--WHERE		store_code IN ('NRQKZWJ9OZ', 'QIUU9SVP51', 'Y8J0Z2W8O9', 'ISEE8A57FE', 'T0R2CQBDUS', 'TUOKF5HAAQ', '9D4LK7X4LZ');





/*
UPDATE		dim_store_details
SET			opening_date = TO_DATE(date_added, 'Month YYYY DD')::DATE;

"October 2012 08"
"2020 February 01"
"May 2003 27"
"2016 November 25"
"October 2006 04"
"2001 May 04"
"1994 November 24"
"February 2009 28"
"March 2015 02"

STORE CODE CHECK: "NRQKZWJ9OZ" "QIUU9SVP51" "Y8J0Z2W8O9" "ISEE8A57FE" "T0R2CQBDUS" "TUOKF5HAAQ" "9D4LK7X4LZ"
*/

