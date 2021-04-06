USE CoogTechSolutions
---------------------Darrian----------------------------------------------------------------------
--Customer Insert--
BULK INSERT Customer
	FROM 'C:\Users\JAHID\OneDrive\Documents\GitHub\CIS3365\Data\Customer.txt'
	WITH(
		FIRSTROW = 1,
		FIELDTERMINATOR = '|',
		ROWTERMINATOR = '\n',
		MAXERRORS = 1
	);
--PAYMENT Insert--
BULK INSERT PAYMENT
	FROM 'C:\Users\JAHID\OneDrive\Documents\GitHub\CIS3365\Data\PAYMENT.txt'
	WITH(
		FIRSTROW = 1,
		FIELDTERMINATOR = '|',
		ROWTERMINATOR = '\n',
		MAXERRORS = 1
	);
--Invoice Payment Insert--
BULK INSERT INVOICE_PAYMENT
	FROM 'C:\Users\JAHID\OneDrive\Documents\GitHub\CIS3365\Data\INVOICE_PAYMENT.txt'
	WITH(
		FIRSTROW = 2,
		FIELDTERMINATOR = '|',
		ROWTERMINATOR = '\n',
		MAXERRORS = 1
	);
--Service Line Insert--
BULK INSERT SERVICE_LINE
	FROM 'C:\Users\JAHID\OneDrive\Documents\GitHub\CIS3365\Data\SERVICE_LINE.txt'
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
Bulk INSERT CUSTOMER_CONTACT_INFO
	FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\customer_contact_info.txt'
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
Bulk INSERT CUSTOMER_ORDER
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\CUSTOMER_ORDER.txt'
      
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
Bulk INSERT VEHICLE_POLICY
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\VEHICLE_POLICY.txt'
	WITH(
		FIRSTROW = 2,
		FIELDTERMINATOR = '|',
		ROWTERMINATOR = '\n',
		MAXERRORS = 1
		);
Bulk INSERT COMPANY_INSURANCE_POLICY
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\COMPANY_INSURANCE_POLICY.txt'
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
Bulk INSERT CUSTOMER_STATUS
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\CUSTOMER_STATUS.txt'
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
Bulk INSERT CUSTOMER_TYPE
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\CUSTOMER_TYPE.txt'
WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);		
Bulk INSERT EMPLOYEE_LOOKUP
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\EMPLOYEE_LOOKUP.txt'
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
------------------------------Giancarlos------------------------------------
Bulk INSERT SUPPLIER_LOOKUP
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\SUPPLIER_LOOKUP.txt'
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
Bulk INSERT VEHICLE_LOOKUP
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\VEHICLE_LOOKUP.txt'
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
FROM 'C:\Users\darri\Documents\GitHub\CIS3365\Data\INSURANCE_COMPANY.txt'
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
