USE CoogTechSolutions
--Customer Insert--
---------------------Darrian----------------------------------------------------------------------
BULK INSERT Customer
	FROM 'C:\Users\darri\Documents\GitHub\CIS3365\CreateScripts\Darrian\customer.txt'
	WITH(
		FIRSTROW = 2,
		FIELDTERMINATOR = '|',
		ROWTERMINATOR = '\n',
		MAXERRORS = 1
	);
--PAYMENT Insert--
BULK INSERT PAYMENT
	FROM 'C:\Users\darri\Documents\GitHub\CIS3365\CreateScripts\Darrian\payment.txt'
	WITH(
		FIRSTROW = 3,
		FIELDTERMINATOR = '|',
		ROWTERMINATOR = '\n',
		MAXERRORS = 1
	);
--Finished Order Insert--
BULK INSERT INVOICE_PAYMENT
	FROM 'C:\Users\darri\Documents\GitHub\CIS3365\CreateScripts\Darrian\invoice_payment.txt'
	WITH(
		FIRSTROW = 2,
		FIELDTERMINATOR = '|',
		ROWTERMINATOR = '\n',
		MAXERRORS = 1
	);
--Service Order Line Insert--
BULK INSERT SERVICE_LINE
	FROM 'C:\Users\darri\Documents\GitHub\CIS3365\CreateScripts\Darrian\service_line.txt'
	WITH(
		FIRSTROW = 2,
		FIELDTERMINATOR = '|',
		ROWTERMINATOR = '\n',
		MAXERRORS = 1
	);
------------------------------Anthony---------------------------------------------------------------------------
--Employee Schedule Insert--
Bulk INSERT Employee_Schedule
	FROM 'C:\Users\darri\Documents\GitHub\CIS3365\CreateScripts\Darrian\Data\Employee_Schedule.txt'
	WITH (
			FIRSTROW =2,
			FIELDTERMINATOR = '|',
			ROWTERMINATOR = '\n',
			MAXERRORS = 1
		);
--Employee Insert--
Bulk INSERT Employee
	FROM 'C:\Users\darri\Documents\GitHub\CIS3365\CreateScripts\Darrian\Data\Employee.txt'
	WITH (
			FIRSTROW =2,
			FIELDTERMINATOR = '|',
			ROWTERMINATOR = '\n',
			MAXERRORS = 1
		);
--Invoice Invoice--
Bulk INSERT Invoice
	FROM 'C:\Users\darri\Documents\GitHub\CIS3365\CreateScripts\Darrian\Data\Invoice.txt'
	WITH (
			FIRSTROW =2,
			FIELDTERMINATOR = '|',
			ROWTERMINATOR = '\n',
			MAXERRORS = 1
		);
--Supplier--
Bulk INSERT Supplier
	FROM 'C:\Users\darri\Documents\GitHub\CIS3365\CreateScripts\Darrian\Data\Supplier.txt'
	WITH (
			FIRSTROW =2,
			FIELDTERMINATOR = '|',
			ROWTERMINATOR = '\n',
			MAXERRORS = 1
		);
-----------------------------------Mustafa-------------------------------------------------------------------------------
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
Bulk INSERT VEHICLE_STATUS
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
	
----------------------------------------Jahidul--------------------------------------------------------------
--Customer Request Insert--
Bulk INSERT CUSTOMER_REQUEST
FROM 'C:\Users\JAHID\OneDrive\Documents\GitHub\CIS3365\Scripts\Jahidul\ji.txt'
	WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
--Customer Vehicle Insert--
Bulk INSERT CUSTOMER_VEHICLE
FROM 'C:\Users\JAHID\OneDrive\Documents\GitHub\CIS3365\Scripts\Jahidul\ji.txt'

	WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
--Vehicle Policy Insert--
Bulk INSERT VEHICLE_POLICY
FROM 'C:\Users\JAHID\OneDrive\Documents\GitHub\CIS3365\Scripts\Jahidul\ji.txt'

	WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
--Company Insurance Insert--
Bulk INSERT COMPANY_INSURANCE
FROM 'C:\Users\JAHID\OneDrive\Documents\GitHub\CIS3365\Scripts\Jahidul\ji.txt'

	WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);

------------------------------------Kyle-----------------------------------------
--Account Assets Insert--
Bulk INSERT VEHICLE_SERVICE
FROM 'C:\Users\kyle\Documents\GitHub\CIS3365\CreateScripts\Darrian\VEHICLE_SERVICE.txt'
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
--------------------------------Jerry------------------------------------------------
--Service Status--
Bulk INSERT Service_Status
	FROM 'C:\Users\darri\Documents\GitHub\CIS3365\CreateScripts\Darrian\Data\Service_Status.txt'
	WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
