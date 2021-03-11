--Account Assets Insert--
Bulk INSERT ACCOUNT_ASSETS
FROM 'C:\Users\kyle\Documents\GitHub\CIS3365\CreateScripts\Darrian\ACCOUNT_ASSETS.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
--Account Liability Insert--
Bulk INSERT ACCOUNT_LIABILITY
FROM 'C:\Users\kyle\Documents\GitHub\CIS3365\CreateScripts\Darrian\ACCOUNT_LIABILITY.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
--Customer Status Insert--
Bulk INSERT CUSTOMER_STATUS
FROM 'C:\Users\kyle\Documents\GitHub\CIS3365\CreateScripts\Darrian\CUSTOMER_STATUS.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
--Supplier Status Insert--
Bulk INSERT SUPPLIER_STATUS
FROM 'C:\Users\kyle\Documents\GitHub\CIS3365\CreateScripts\Darrian\SUPPLIER_STATUS.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
--Vehicle Insert--
Bulk INSERT VEHICLE
FROM 'C:\Users\kyle\Documents\GitHub\CIS3365\CreateScripts\Darrian\VEHICLE.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);