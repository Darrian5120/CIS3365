--Customer Create Script--
USE CoogTechSolutions
-------------------Darrian-------------------------------
CREATE TABLE dbo.Customer (
    C_ID int IDENTITY(1,1) NOT NULL,
    C_LNAME varchar(15) NOT NULL,
    C_FNAME varchar(15),
    ORDER_ID int,
    C_BUSINESS_NAME varchar(50),
	CONSTRAINT C_ID_PK PRIMARY KEY (C_ID)
);
CREATE TABLE dbo.PAYMENT (
    C_ID int NOT NULL,
    AMT_PAID float NOT NULL,
	CONSTRAINT C_ID_PK PRIMARY KEY (C_ID)
);
CREATE TABLE dbo.SERVICE_ORDER_LINE (
    ORDER_ID INT NOT NULL,
    SERVICE_DATE DATETIME,
    ITEM_QTY INT NOT NULL,
    ITEM_COST FLOAT NOT NULL,
    LABOR_HOURS FLOAT,
	CONSTRAINT ORDER_PK PRIMARY KEY (ORDER_ID)
);
CREATE TABLE dbo.FINISHED_ORDER (
	ORDER_ID int NOT NULL,
    DATE_START DATETIME,
    DATE_END DATETIME NOT NULL,
    Quality text,
	CONSTRAINT ORDER_ID_PK PRIMARY KEY (ORDER_ID)
);
-------------------------------------------------------
--Business Create Script--
CREATE TABLE dbo.BUSINESS (
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
	CONSTRAINT BUS_ID_PK PRIMARY KEY(BUS_ID)
);
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
--Supplier Create Script
CREATE TABLE dbo.SUPPLIER (
	SUPPLIER_ID int not null,
	SUPPLIER_PHONE int not null,
	SUPPLIER_ADDRESS varchar(50),
	CONSTRAINT SUPPLIER_ID_PK PRIMARY KEY (SUPPLIER_ID)
);
--Create Employee Schedule--
CREATE TABLE dbo.EMPLOYEE_SCHEDULE (
	SCHEDULE_ID int not null,
	EMP_SCHD_WEEK DATE not null,
	EMP_SCHD_EMP_IDS int not null,
	CONSTRAINT SCHEDULE_ID_PK PRIMARY KEY (SCHEDULE_ID)
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
