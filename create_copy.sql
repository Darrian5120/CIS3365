USE CoogTechSolutions
-------------------Darrian-------------------------------
CREATE TABLE dbo.Customer (
    CUSTOMER_ID int IDENTITY(1,1) NOT NULL,
    C_LNAME varchar(25) NOT NULL,
    C_FNAME varchar(25),
    C_BUSINESS_NAME varchar(50),
	CONSTRAINT CUSTOMER_ID_PK PRIMARY KEY (CUSTOMER_ID)
);
CREATE TABLE dbo.PAYMENT (
    PMT_NUMBER int NOT NULL,
	PMT_ID int NOT NULL,
	PMT_TYPE VARCHAR(10) NOT NULL,
    AMT_PAID decimal,
	CONSTRAINT PMT_NUMBER_PK PRIMARY KEY (PMT_NUMBER)
);
CREATE TABLE dbo.SERVICE_LINE (
    SERVICE_LINE_ID INT IDENTITY(1,1) NOT NULL,
	SERVICE_ID INT NOT NULL,
	SERVICE_ORDER_ID INT NOT NULL,
    LINE_DATE DATE,
	LINE_COST FLOAT,
	CONSTRAINT SERVICE_LINE_ID_PK PRIMARY KEY (SERVICE_LINE_ID)
);
CREATE TABLE dbo.INVOICE_PAYMENT (
	PMT_NUMBER int NOT NULL,
    INVOICE_ID int NOT NULL,
	CONSTRAINT PMT_NUMBER_PK1 PRIMARY KEY (PMT_NUMBER)
);
-----------------Anthony-------------------------------
--Employee Create Script--
CREATE TABLE dbo.EMPLOYEE (
	EMPLOYEE_ID int IDENTITY(1,1) NOT NULL,
	EMPLOYEE_LNAME varchar(30) not null,
	EMPLOYEE_FNAME varchar(30) not null,
	EMPLOYEE_ADDRESS varchar(50) not null,
	EMPLOYEE_HIRE_DATE DATE,
	EMPLOYEE_HOURS float,
	EMPLOYEE_PAY_RATE float,
	EMPLOYEE_PHONE int not null,
	EMPLOYEE_BANK_INFO int,
	EMPLOYEE_TAX int,
	EMPLOYEE_JOB_FUNC varchar(30),
	CONSTRAINT EMPLOYEE_ID_PK PRIMARY KEY (EMPLOYEE_ID)
);
--Supplier Create Script--
CREATE TABLE dbo.SUPPLIER (
	SUPPLIER_ID int IDENTITY(1,1) not null,
	SUPPLIER_NAME varchar(50),
	CONSTRAINT SUPPLIER_ID_PK PRIMARY KEY (SUPPLIER_ID)
);
  
--Service Status Create--
CREATE TABLE dbo.SERVICE_ORDER_STATUS (
    SERVICE_ORDER_ID int NOT NULL,
    ACTIVE_ID int NOT NULL,
    ACTIVE varchar(15),
	CONSTRAINT SERVICE_ORDER_ID_PK1 PRIMARY KEY (SERVICE_ORDER_ID)
);

--Create Invoice--
CREATE TABLE dbo.INVOICE (
	INVOICE_ID int IDENTITY(1,1) not null,
	CUSTOMER_ID int not null,
	TOTAL_COST float,
	AMT_OWED float,
	INVOICE_DATE date not null,
	CONSTRAINT INVOICE_ID_PK PRIMARY KEY (INVOICE_ID),
);

------------------Mustafa-----------------------------------------------
--Service Line Status--
CREATE TABLE dbo.SERVICE_LINE_STATUS (
	SERVICE_LINE_ID int not null,
	ACTIVE_ID int not null,
	ACTIVE varchar(20),
	CONSTRAINT SERVICE_LINE_ID_PK1 PRIMARY KEY (SERVICE_LINE_ID)
);
--customer contact--
CREATE TABLE dbo.CUSTOMER_CONTACT_INFO (
	CUSTOMER_ID INT not null,
	C_PHONE INT  not null,
	C_EMAIL varchar(30) not null,
	C_ADDRESS varchar(30) not null,
	C_ZIP INT not null,
	C_CITY varchar(30) not null,
	STATE_NAME varchar(10) not null,
	CONSTRAINT CUSTOMER_ID_PK1 PRIMARY KEY(CUSTOMER_ID)
);
--VEHICLE_STATUS--
CREATE TABLE dbo.VEHICLE_STATUS (
	V_VIN varchar(15) not null,
	ACTIVE_ID int not null,
	ACTIVE varchar(20),
	CONSTRAINT V_VIN_PK1 PRIMARY KEY (V_VIN)
);
------------Jahidul---------------------------------------------------
create table dbo.CUSTOMER_ORDER(
	SERVICE_ORDER_ID int not null,
	CUSTOMER_ID int not null,
	CONSTRAINT SERVICE_ORDER_ID_PK2 PRIMARY KEY (SERVICE_ORDER_ID)
);
create table dbo.CUSTOMER_VEHICLE(
	V_VIN varchar(20) not null,
	CUSTOMER_ID int not null,
	CONSTRAINT V_VIN_PK2 PRIMARY KEY (V_VIN)
);
create table dbo.VEHICLE_POLICY(
	POLICY_ID int not null,
	V_VIN varchar(20) not null,
	CONSTRAINT POLICY_ID_PK2 PRIMARY KEY (POLICY_ID)	
);
create table dbo.COMPANY_INSURANCE_POLICY(
	POLICY_ID int not null,
	INSURANCE_ID int not null,
	CONSTRAINT POLICY_ID_PK1 PRIMARY KEY (POLICY_ID)
);
------------Jerry-----------------------------------------------------
--Service Status Create--
CREATE TABLE dbo.SERVICE_STATUS (
    SERVICE_ID int NOT NULL,
    ACTIVE_ID int NOT NULL,
    ACTIVE int,
	CONSTRAINT SERVICE_ID_PK1 PRIMARY KEY (SERVICE_ID)
);
--ACCOUNT REVENUE Table--
CREATE TABLE dbo.ACCOUNT_REVENUE (
	REVENUE_ID int IDENTITY(1,1) not null,
	REVENUE_NAME varchar(15),
	REVENUE_VALUE float,
	CONSTRAINT REVENUE_ID_PK PRIMARY KEY (REVENUE_ID)
);
--INSURANCE COMPANY Table--
CREATE TABLE dbo.INSURANCE_COMPANY (
	INSURANCE_ID int IDENTITY(1,1) not null,
	INSURANCE_NAME varchar(30) not null,
	CONSTRAINT INSURANCE_ID_PK PRIMARY KEY (INSURANCE_ID)
);
--INSURANCE POLICY Table--
CREATE TABLE dbo.INSURANCE_POLICY (
	POLICY_ID int IDENTITY(1,1) not null,
	POLICY_NAME varchar(30),
	COVERAGE_COST float,
	CONSTRAINT POLICY_ID_PK PRIMARY KEY (POLICY_ID)
);
----------------------------Kyle--------------------------------------
CREATE TABLE dbo.VEHICLE_SERVICE( 
	SERVICE_ID INT NOT NULL, 
	V_VIN VARCHAR(20) NOT NULL,
	CONSTRAINT SERVICE_ID_PK2 PRIMARY KEY (SERVICE_ID)
);
CREATE TABLE dbo.CUSTOMER_STATUS ( 
	CUSTOMER_ID INT NOT NULL, 
	C_ACTIVE INT NOT NULL, 
	ACTIVE VARCHAR(15) NOT NULL
	CONSTRAINT CUSTOMER_ID_PK2 PRIMARY KEY (CUSTOMER_ID)

);
CREATE TABLE dbo.SUPPLIER_STATUS( 
	SUPPLIER_ID INT NOT NULL, 
	ACTIVE_ID INT NOT NULL, 
	ACTIVE VARCHAR(15) NOT NULL,
	CONSTRAINT SUPPLIER_ID_PK1 PRIMARY KEY (SUPPLIER_ID)
);
CREATE TABLE dbo.VEHICLE(
	V_VIN VARCHAR(20) NOT NULL,
	V_MAKE VARCHAR(15), 
	V_LISCENSE_PLATE VARCHAR(15) NOT NULL, 
	V_MODEL VARCHAR(15), 
	V_YEAR INT, 
	CONSTRAINT V_VIN_PK PRIMARY KEY (V_VIN)
); 
--------------------------------Brandon--------------------------------
CREATE TABLE dbo.PART ( 
  PART_ID INT IDENTITY(1,1) NOT NULL,
  PART_NAME INT,
  CONSTRAINT PART_ID_PK1 PRIMARY KEY (PART_ID)
 );
CREATE TABLE dbo.EMPLOYEE_SERVICE_LINE_ASSIGNMENT ( 
  SERVICE_LINE_ID INT NOT NULL, 
  EMPLOYEE_ID INT NOT NULL, 
  CONSTRAINT SERVICE_LINE_ID_PK2 PRIMARY KEY (SERVICE_LINE_ID)
);
CREATE TABLE dbo.SERVICE (  
  SERVICE_ID INT not null,  
  SERVICE_TYPE VARCHAR(30) not null,    
  DATE_START DATETIME NOT NULL, 
  DATE_END DATETIME, 
  COST INT NOT NULL,  
  CONSTRAINT SERVICE_ID_PK PRIMARY KEY (SERVICE_ID)
);
CREATE TABLE dbo.SERVICE_LINE_PART(
  SERVICE_LINE_ID INT NOT NULL,
  PART_ID INT NOT NULL, 
  CONSTRAINT SERVICE_LINE_ID_PK3 PRIMARY KEY (SERVICE_LINE_ID)
);     
--------------------------------Maddy------------------------------------
CREATE TABLE dbo.COUNTRY (
	COUNTRY_ID int IDENTITY(1,1) not null,
	COUNTRY_NAME varchar(20) not null,
	CONSTRAINT COUNTRY_ID_PK PRIMARY KEY (COUNTRY_ID)
);
CREATE TABLE dbo.CUSTOMER_TYPE (
	CUSTOMER_ID int not null,
	IS_BUSINESS BIT not null,
	CONSTRAINT CUSTOMER_ID_PK3 PRIMARY KEY (CUSTOMER_ID)
);
CREATE TABLE dbo.EMPLOYEE_LOOKUP (
	EMPLOYEE_ID int not null,
	EMPLOYEE_CURR_SERVICE varchar(15) not null,
	CONSTRAINT EMPLOYEE_ID_PK1 PRIMARY KEY (EMPLOYEE_ID)
);
CREATE TABLE dbo.SERVICE_ORDER (
	SERVICE_ORDER_ID int IDENTITY(1,1) not null,
	ORDER_DATE date,
	TOTAL_COST float(8),
	CONSTRAINT SERVICE_ORDER_ID_PK PRIMARY KEY (SERVICE_ORDER_ID)
);
------------------------------Giancarlos------------------------------------
CREATE TABLE dbo.SUPPLIER_LOOKUP (
    SUPPLIER_ID INT NOT NULL,
    PART_ID INT NOT NULL,
    CONSTRAINT SUPPLIER_ID_PK2 PRIMARY KEY (SUPPLIER_ID)
);
CREATE TABLE dbo.VIOLATION (
    VIOLATION_ID int not null,
    VIOLATION_NAME VARCHAR(80),
	LAW_CODE VARCHAR(15),
    CONSTRAINT VIOLATION_ID_PK PRIMARY KEY (VIOLATION_ID)
);
CREATE TABLE dbo.CUSTOMER_STATE (
    STATE_ID INT NOT NULL,
    CUSTOMER_ID INT NOT NULL,
    CONSTRAINT STATE_ID_PK1 PRIMARY KEY (STATE_ID)
);
CREATE TABLE dbo.VEHICLE_LOOKUP (
    V_VIN VARCHAR(20) NOT NULL,
    V_SERVICE VARCHAR(255) NOT NULL,
    V_CONDITION VARCHAR(255) NOT NULL,
	CONSTRAINT V_VIN_PK3 PRIMARY KEY (V_VIN)
);
------------------------------Zach------------------------------------------
CREATE TABLE dbo.SUPPLIER_PART (
	PART_ID int IDENTITY(1,1) not null,
	SUPPLIER_ID INT not null,
	CONSTRAINT PART_ID_PK PRIMARY KEY (PART_ID)
);
CREATE TABLE dbo.STATE(
	STATE_ID int not null,
	STATE_NAME varchar(30),
	CONSTRAINT STATE_ID_PK PRIMARY KEY (STATE_ID)
);
CREATE TABLE dbo.Employee_Status(
	EMPLOYEE_ID int IDENTITY(1,1) not null,
	ACTIVE_ID int not null,
	ACTIVE varchar(15)
	CONSTRAINT EMPLOYEE_ID_PK2 PRIMARY KEY (EMPLOYEE_ID)
);
CREATE TABLE dbo.STATE_VIOLATION(
	VIOLATION_ID int IDENTITY(1,1) not null,
	STATE_ID int not null
	CONSTRAINT VIOLATION_ID_PK1 PRIMARY KEY (VIOLATION_ID)
);
