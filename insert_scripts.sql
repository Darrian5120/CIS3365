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
		FIRSTROW = 2,
		FIELDTERMINATOR = '|',
		ROWTERMINATOR = '\n',
		MAXERRORS = 1
	);
--Finished Order Insert--
BULK INSERT FINISHED_ORDER
	FROM 'C:\Users\darri\Documents\GitHub\CIS3365\CreateScripts\Darrian\finished_order.txt'
	WITH(
		FIRSTROW = 2,
		FIELDTERMINATOR = '|',
		ROWTERMINATOR = '\n',
		MAXERRORS = 1
	);
--Service Order Line Insert--
BULK INSERT SERVICE_ORDER_LINE
	FROM 'C:\Users\darri\Documents\GitHub\CIS3365\CreateScripts\Darrian\service_order_line.txt'
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
------------------------------------------------------------------------------------------------------
