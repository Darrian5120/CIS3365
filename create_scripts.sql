--Customer Create Script--
USE CoogTechSolutions
-------------------Darrian-------------------------------
CREATE TABLE dbo.Customer (
    CUSTOMER_ID int IDENTITY(1,1) NOT NULL,
    C_LNAME varchar(15) NOT NULL,
    C_FNAME varchar(15),
    C_BUSINESS_NAME varchar(50),
	CONSTRAINT CUSTOMER_ID_PK PRIMARY KEY (CUSTOMER_ID)
);
CREATE TABLE dbo.PAYMENT (
    PMT_NUMBER int NOT NULL,
	PMT_ID int NOT NULL,
	PMT_TYPE VARCHAR(10) NOT NULL,
    AMT_PAID float,
	CONSTRAINT PMT_NUMBER_PK PRIMARY KEY (PMT_NUMBER)
);
CREATE TABLE dbo.SERVICE_LINE (
    SERVICE_LINE_ID INT NOT NULL,
	SERVICE_ORDER_ID INT NOT NULL,
	INVOICE_ID INT NOT NULL,
	/*SERVICE_ID INT NOT NULL,*/
    SERVICE_DATE DATETIME,
	LINE_COST FLOAT,
    SERVICE_QTY INT,
	CONSTRAINT SERVICE_ID_PK PRIMARY KEY (SERVICE_ID)
);
CREATE TABLE dbo.INVOICE_PAYMENT (
	PMT_NUMBER int NOT NULL,
    INVOICE_ID int NOT NULL,
	CONSTRAINT PMT_NUMBER_PK PRIMARY KEY (PMT_NUMBER)
);
-----------------Anthony-------------------------------
--Employee Create Script--
CREATE TABLE dbo.EMPLOYEE (
	EMP_ID int IDENTITY(1,1) NOT NULL,
	EMP_LNAME varchar(30) not null,
	EMP_FNAME varchar(30) not null,
	EMP_ADDRESS varchar(50) not null,
	EMP_HIRE_DATE DATE,
	EMP_HOURS float,
	EMP_PAY_RATE float,
	EMP_PHONE int not null,
	EMP_BANK_INFO int,
	EMP_TAX int,
	EMP_JOB_FUNC varchar(30),
	CONSTRAINT EMP_ID_PK PRIMARY KEY (EMP_ID)
);
--Supplier Create Script--
CREATE TABLE dbo.SUPPLIER (
	SUPPLIER_ID int not null,,
	SUPPLIER_NAME varchar(50),
	CONSTRAINT SUPPLIER_ID_PK PRIMARY KEY (SUPPLIER_ID)
);
  
--Service Status Create--
CREATE TABLE dbo.SERVICE_STATUS (
    SERVICE_ID int NOT NULL,
    ACTIVE_ID int NOT NULL,
    ACTIVE int,
	CONSTRAINT SERVICE_ID_PK PRIMARY KEY (SERVICE_ID)
);

--Create Invoice--
CREATE TABLE dbo.INVOICE (
	INVOICE_ID int not null,
	CUSTOMER_ID int not null,
	TOTAL_COST float,
	AMT_OWED float,
	INVOICE_DATE  datetime not null,
	CONSTRAINT INVOICE_ID_PK PRIMARY KEY (INVOICE_ID),
);

------------------Mustafa-----------------------------------------------
--Business info--
CREATE TABLE dbo.BUSINESS_INFO (
	BUS_ID int not null,
	BUS_ADDRESS  varchar(30) not null,
	BUS_CITY varchar(30) not null,
	BUS_STATE varchar(2) not null,
	BUS_ZIP int not null,
	BUS_PHONE int not null,
	BUS_FAX int not null,
	BUS_HOURS int not null,
	BUS_EMAIL varchar(30) not null,
	BUS_WEBSITE varchar(30) not null,
	/*BUS_IMAGES int*/
	PRIMARY KEY(BUS_ID)
);
--customer contact--
CREATE TABLE dbo.CUSTOMER_CONTACT_INFO (
	CUSTOMER_ID INT not null,
	C_PHONE INT  not null,
	C_EMAIL varchar(30) not null,
	C_ADDRESS varchar(90) not null,
	C_ZIP INT not null,
	C_CITY varchar(30) not null,
	C_STATE varchar(15) not null,
	CONSTRAINT CUSTOMER_ID_PK PRIMARY KEY(CUSTOMER_ID)
	/*FOREIGN KEY (C_ID) REFERENCES Customer(C_ID)*/
);
--service schedule--
CREATE TABLE dbo.SERVICE_SCHEDULE (
	SCHEDULE_ID int not null,
	SERVICE_TYPE varchar(30) not null,
	SERVICE_DATE datetime not null,
	CONSTRAINT SCHEDULE_ID_PK PRIMARY KEY (SCHEDULE_ID)
);
--VEHICLE_STATUS--
CREATE TABLE dbo.VEHICLE_STATUS (
	V_VIN int not null,
	ACTIVE_ID int not null,
	ACTIVE int null,
	CONSTRAINT V_VIN_PK PRIMARY KEY (V_VIN)
);

------------Jahidul---------------------------------------------------
create table dbo.CUSTOMER_REQUEST(
	SERVICE_ID int not null,
	CUSTOMER_ID int not null,
	CONSTRAINT SERVICE_ID_PK PRIMARY KEY (SERVICE_ID)
);

create table dbo.CUSTOMER_VEHICLE(
	V_VIN int not null,
	CUSTOMER_ID int not null,
	CONSTRAINT V_VIN_PK PRIMARY KEY (V_VIN)
);

create table dbo.VEHICLE_POLICY(
	POLICY_ID int not null,
	V_VIN int not null,
	CONSTRAINT POLICY_ID_PK PRIMARY KEY (POLICY_ID)	
);

create table dbo.COMPANY_INSURANCE_POLICY(
	POLICY_ID int not null,
	INSURANCE_ID int not null,
	CONSTRAINT POLICY_ID_PK PRIMARY KEY (POLICY_ID)
);
------------Jerry-----------------------------------------------------
--Service Status Create--
CREATE TABLE dbo.SERVICE_STATUS (
    SERVICE_ID int NOT NULL,
    ACTIVE_ID int NOT NULL,
    ACTIVE int,
	CONSTRAINT SERVICE_ID_PK PRIMARY KEY (SERVICE_ID)
);
--ACCOUNT REVENUE Table--
CREATE TABLE dbo.ACCOUNT_REVENUE (
	TOTAL_REV int not null,
	CONSTRAINT TOTAL_REV_PK PRIMARY KEY (TOTAL_REV)
);
--INSURANCE COMPANY Table--
CREATE TABLE dbo.INSURANCE_COMPANY (
	INSURANCE_ID int not null,
	COMPANY_NAME varchar(30) not null,
	CONSTRAINT INSURANCE_ID_PK PRIMARY KEY (INSURANCE_ID)
);
--INSURANCE POLICY Table--
CREATE TABLE dbo.INSURANCE_POLICY (
	POLICY_ID int not null,
	INSURANCE_ID int not null,
	CUSTOMER_ID INT not null,
	V_VIN INT not null,
	COVERAGE_COST int,
	CONSTRAINT POLICY_ID_PK PRIMARY KEY (POLICY_ID)
);
----------------------------Kyle--------------------------------------
CREATE TABLE VEHICLE_SERVICE( 
	SERVICE_ID INT NOT NULL, 
	V_VIN NOT NULL,
	CONSTRAINT SERVICE_ID_PK PRIMARY KEY (SERVICE_ID)
);
CREATE TABLE dbo.CUSTOMER_STATUS ( 
	CUSTOMER_ID INT NOT NULL, 
	C_ACTIVE INT NOT NULL, 
	ACTIVE VARCHAR(15) NOT NULL
	CONSTRAINT CUSTOMER_ID_PK PRIMARY KEY (CUSTOMER_ID)

);
CREATE TABLE dbo.SUPPLIER_STATUS( 
	SUPPLIER_ID INT NOT NULL, 
	ACTIVE_ID INT NOT NULL, 
	ACTIVE VARCHAR(15) NOT NULL,
	CONSTRAINT SUPPLIER_ID_PK PRIMARY KEY (SUPPLIER_ID)
);
CREATE TABLE dbo.VEHICLE(
	V_VIN INT NOT NULL,
	V_MAKE VARCHAR, 
	V_LISCENSE_PLATE VARCHAR NOT NULL, 
	V_MODEL VARCHAR, 
	V_YEAR INT, 
	CONSTRAINT V_VIN_PK PRIMARY KEY (V_VIN)
); 
--------------------------------Brandon--------------------------------
CREATE TABLE dbo.PART ( 
  SUP_PART_ID INT NOT NULL,
  SUPPLIER_PART_NAME INT,
  CONSTRAINT SUP_PART_ID_PK PRIMARY KEY (SUP_PART_ID)
 );
CREATE TABLE dbo.EMPLOYEE_SERVICE_LINE_ASSIGNMENT ( 
  SERVICE_LINE_ID INT NOT NULL, 
  EMPLOYEE_ID INT NOT NULL, 
  CONSTRAINT SERVICE_LINE_ID_PK PRIMARY KEY (SERVICE_LINE_ID)
);
CREATE TABLE dbo.Service (  
  SERVICE_ID INT not null,  
  SERVICE_TYPE VARCHAR(30) not null,    
  DATE_START DATETIME NOT NULL, 
  DATE_END DATETIME, 
  COST INT NOT NULL,  
  CONSTRAINT SERVICE_ID_PK PRIMARY KEY (SERVICE_ID)
);
CREATE TABLE dbo.SERVICE_LINE_PART(
  SERVICE_LINE_ID INT NOT NULL,
  EMPLOYEE_ID INT NOT NULL, 
  CONSTRAINT SERVICE_LINE_ID_PK PRIMARY KEY (SERVICE_LINE_ID)
);     
