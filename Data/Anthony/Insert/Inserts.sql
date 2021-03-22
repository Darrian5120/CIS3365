USE CoogTechSolutions
--Service Order Status--
Bulk INSERT SERVICE_ORDER_STATUS
	FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\Service_Order_Status.txt'
	WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
--Employee Insert--
Bulk INSERT EMPLOYEE
	FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\Employee.txt'
	WITH (
			FIRSTROW =2,
			FIELDTERMINATOR = '|',
			ROWTERMINATOR = '\n',
			MAXERRORS = 1
		);
--Invoice Invoice--
Bulk INSERT INVOICE
	FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\Invoice.txt'
	WITH (
			FIRSTROW =2,
			FIELDTERMINATOR = '|',
			ROWTERMINATOR = '\n',
			MAXERRORS = 1
		);
--Supplier--
Bulk INSERT SUPPLIER
	FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\Supplier.txt'
	WITH (
			FIRSTROW =2,
			FIELDTERMINATOR = '|',
			ROWTERMINATOR = '\n',
			MAXERRORS = 1
		);
