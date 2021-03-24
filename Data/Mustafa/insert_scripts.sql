--Business info Insert--
Bulk INSERT BUSINESS_INFO
	FROM 'C:\Users\Mustafi\Documents\GitHub\CIS3365\CreateScripts\Mustafa\ma.txt'
	WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
--Current service Insert--
Bulk INSERT CURRENT_SERVICE
	FROM 'C:\Users\Mustafi\Documents\GitHub\CIS3365\CreateScripts\Mustafa\ma.txt'

	WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
--Customer contact info Insert--
Bulk INSERT CUSTOMER_CONTACT_INFO
	FROM 'C:\Users\Mustafi\Documents\GitHub\CIS3365\CreateScripts\Mustafa\ma.txt'
	WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
--Service Schedule Insert--
Bulk INSERT SERVICE_SCHEDULE
	FROM 'C:\Users\Mustafi\Documents\GitHub\CIS3365\CreateScripts\Mustafa\ma.txt'
	WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
