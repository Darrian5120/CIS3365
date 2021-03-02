--Employee Schedule Insert--
Bulk INSERT Employee_Schedule
	FROM 'C:\Users\anthony\Documents\GitHub\CIS3365\CreateScripts\Darrian\Employee_Schedule.txt'
	WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
--Employee Insert--
Bulk INSERT Employee
	FROM 'C:\Users\anthony\Documents\GitHub\CIS3365\CreateScripts\Darrian\Employee.txt'
	WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
--Invoice Invoice--
Bulk INSERT Invoice
	FROM 'C:\Users\anthony\Documents\GitHub\CIS3365\CreateScripts\Darrian\Invoice.txt'
	WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
--Supplier--
Bulk INSERT Supplier
	FROM 'C:\Users\anthony\Documents\GitHub\CIS3365\CreateScripts\Darrian\Supplier.txt'
	WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);