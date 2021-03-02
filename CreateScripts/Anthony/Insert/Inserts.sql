--Employee Schedule Insert--
Bulk INSERT Employee_Schedule
	FROM 'C:\Users\anthony\Documents\GitHub\CIS3365\CreateScripts\Anthony\Data\Employee_Schedule.txt'
	WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
--Employee Insert--
Bulk INSERT Employee
	FROM 'C:\Users\anthony\Documents\GitHub\CIS3365\CreateScripts\Anthony\Data\Employee.txt'
	WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
--Invoice Invoice--
Bulk INSERT Invoice
	FROM 'C:\Users\anthony\Documents\GitHub\CIS3365\CreateScripts\Anthony\Data\Invoice.txt'
	WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
--Supplier--
Bulk INSERT Supplier
	FROM 'C:\Users\anthony\Documents\GitHub\CIS3365\CreateScripts\Anthony\Data\Supplier.txt'
	WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);