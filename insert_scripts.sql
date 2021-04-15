USE CoogTechSolutions

Bulk INSERT CUSTOMER_STATUS
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\CUSTOMER_STATUS.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
Bulk INSERT CUSTOMER_TYPE
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\CUSTOMER_TYPE.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);

---------------------Darrian----------------------------------------------------------------------
--Customer Insert--
BULK INSERT Customer
	FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\customer.txt'
	WITH(
		FIRSTROW = 2,
		FIELDTERMINATOR = '|',
		ROWTERMINATOR = '\n',
		MAXERRORS = 1
	);
--PAYMENT Insert--
BULK INSERT PAYMENT
	FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\payment.txt'
	WITH(
		FIRSTROW = 2,
		FIELDTERMINATOR = '|',
		ROWTERMINATOR = '\n',
		MAXERRORS = 1
	);
--Invoice Payment Insert--
BULK INSERT INVOICE_PAYMENT
	FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\invoice_payment.txt'
	WITH(
		FIRSTROW = 2,
		FIELDTERMINATOR = '|',
		ROWTERMINATOR = '\n',
		MAXERRORS = 1
	);
--Service Line Insert--
BULK INSERT SERVICE_LINE
	FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\service_line.txt'
	WITH(
		FIRSTROW = 2,
		FIELDTERMINATOR = '|',
		ROWTERMINATOR = '\n',
		MAXERRORS = 1
	);
------------------------------Anthony---------------------------------------------------------------------------
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
-----------------------------------Mustafa-------------------------------------------------------------------------------
--Service Line Status--
Bulk INSERT SERVICE_LINE_STATUS
	FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\service_line_status.txt'
	WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
--Vehicle service Insert--
Bulk INSERT VEHICLE_STATUS
	FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\vehicle_status.txt'
	WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
--Customer contact info Insert--
Bulk INSERT VEHICLE_CONDITION
	FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\vehicle_condition.txt'
	WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
Bulk INSERT PAYMENT_REVENUE
	FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\payment_revenue.txt'
	WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
----------------------------------------Jahidul--------------------------------------------------------------
Bulk INSERT MODEL
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\model.txt'  
	WITH(
		FIRSTROW = 2,
		FIELDTERMINATOR = '|',
		ROWTERMINATOR = '\n',
		MAXERRORS = 1
		);
Bulk INSERT MAKE
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\make.txt'      
	WITH(
		FIRSTROW = 2,
		FIELDTERMINATOR = '|',
		ROWTERMINATOR = '\n',
		MAXERRORS = 1
		);
Bulk INSERT CUSTOMER_VEHICLE
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\CUSTOMER_VEHICLE.txt'
	WITH(
		FIRSTROW = 2,
		FIELDTERMINATOR = '|',
		ROWTERMINATOR = '\n',
		MAXERRORS = 1
		);
Bulk INSERT POLICY
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\policy.txt'
	WITH(
		FIRSTROW = 2,
		FIELDTERMINATOR = '|',
		ROWTERMINATOR = '\n',
		MAXERRORS = 1
		);
--------------------------------Kyle------------------------------------------------
Bulk INSERT VEHICLE_SERVICE
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\VEHICLE_SERVICE.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
		
Bulk INSERT SUPPLIER_STATUS
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\SUPPLIER_STATUS.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
Bulk INSERT VEHICLE
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\VEHICLE.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);		
--------------------------------Brandon--------------------------------------------
Bulk INSERT PART
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\PART.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
Bulk INSERT EMPLOYEE_SERVICE_LINE_ASSIGNMENT
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\EMPLOYEE_SERVICE_LINE_ASSIGNMENT.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);		
Bulk INSERT Service
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\Service.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
Bulk INSERT SERVICE_LINE_PART
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\SERVICE_LINE_PART.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);	
--------------------------------Maddy------------------------------------
Bulk INSERT COUNTRY
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\COUNTRY.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);

Bulk INSERT SERVICE_ORDER
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\SERVICE_ORDER.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);	

Bulk INSERT ROLE
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\ROLE.txt'
WITH (
			FIRSTROW = 2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
------------------------------Giancarlos------------------------------------
Bulk INSERT INVOICE_STATUS
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\invoice_status.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
Bulk INSERT VIOLATION
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\VIOLATION.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);		
Bulk INSERT CUSTOMER_STATE
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\CUSTOMER_STATE.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
Bulk INSERT PAYMENT_STATUS
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\payment_status.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);	
------------------------------Zach------------------------------------------
Bulk INSERT SUPPLIER_PART
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\SUPPLIER_PART.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
Bulk INSERT STATE
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\STATE.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);		
Bulk INSERT Employee_Status
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\Employee_Status.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
Bulk INSERT STATE_VIOLATION
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\STATE_VIOLATION.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);	
------------------------------------Jerry-----------------------------------------
Bulk INSERT ACCOUNT_REVENUE
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\ACCOUNT_REVENUE.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
Bulk INSERT SERVICE_STATUS
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\SERVICE_STATUS.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
Bulk INSERT INSURANCE_COMPANY
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\insurance_company.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
Bulk INSERT INSURANCE_POLICY
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\INSURANCE_POLICY.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);
