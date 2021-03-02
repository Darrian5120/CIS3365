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