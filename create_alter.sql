USE CoogTechSolutions
-------------------Darrian-------------------------------
CREATE TABLE dbo.Customer (
    CUSTOMER_ID INT IDENTITY(1,1) NOT NULL,
    C_LNAME varchar(25) NOT NULL,
    C_FNAME varchar(25) NOT NULL,
	C_BUSINESS_NAME varchar(50),
	ACTIVE_ID INT NOT NULL,
	BUSINESS_ID INT NOT NULL,
	CONSTRAINT CUSTOMER_ID_PK PRIMARY KEY (CUSTOMER_ID)
);
CREATE TABLE dbo.PAYMENT (
	PMT_ID int NOT NULL,
	PMT_TYPE VARCHAR(10) NOT NULL,
	CONSTRAINT PMT_ID_PK PRIMARY KEY (PMT_ID)
);
CREATE TABLE dbo.SERVICE_LINE (
    SERVICE_LINE_ID INT IDENTITY(1,1) NOT NULL,
	SERVICE_ORDER_ID INT NOT NULL,
	SERVICE_ID INT NOT NULL,
    QUANTITY INT,
	LINE_COST MONEY,
	ACTIVE_ID INT NOT NULL,
	CONSTRAINT SERVICE_LINE_ID_PK PRIMARY KEY (SERVICE_LINE_ID, SERVICE_ORDER_ID, SERVICE_ID)
);
CREATE TABLE dbo.INVOICE_PAYMENT (
	PMT_ID int NOT NULL,
    INVOICE_ID int NOT NULL,
	PMT_AMOUNT MONEY NOT NULL,
	ACTIVE_ID INT NOT NULL,
	CONSTRAINT PMT_NUMBER_PK1 PRIMARY KEY (PMT_ID, INVOICE_ID)
);
-----------------Anthony-------------------------------
--Employee Create Script--
CREATE TABLE dbo.EMPLOYEE (
	EMPLOYEE_ID int IDENTITY(1,1) NOT NULL,
	EMPLOYEE_LNAME varchar(30) not null,
	EMPLOYEE_FNAME varchar(30) not null,
	EMPLOYEE_ADDRESS varchar(50) not null,
	EMPLOYEE_HIRE_DATE DATETIME,
	EMPLOYEE_HOURS int,
	EMPLOYEE_PAY_RATE MONEY,
	EMPLOYEE_PHONE bigint not null,
	EMPLOYEE_BANK_INFO bigint,
	EMPLOYEE_TAX int,
	EMPLOYEE_JOB_FUNC varchar(30),
	ACTIVE_ID INT NOT NULL,
	CONSTRAINT EMPLOYEE_ID_PK PRIMARY KEY (EMPLOYEE_ID)
);
--Supplier Create Script--
CREATE TABLE dbo.SUPPLIER (
	SUPPLIER_ID int IDENTITY(1,1) not null,
	SUPPLIER_NAME varchar(50),
	ACTIVE_ID INT NOT NULL,
	CONSTRAINT SUPPLIER_ID_PK PRIMARY KEY (SUPPLIER_ID)
);

--Service Order Status Create--
CREATE TABLE dbo.SERVICE_ORDER_STATUS (
    ACTIVE_ID int NOT NULL,
    ACTIVE varchar(25),
	CONSTRAINT SO_ACTIVE_ID_PK1 PRIMARY KEY (ACTIVE_ID)
);

--Create Invoice--
CREATE TABLE dbo.INVOICE (
	INVOICE_ID int IDENTITY(1,1) not null,
	CUSTOMER_ID int not null,
	TOTAL_COST MONEY,
	INVOICE_DATE date not null,
	AMT_OWED MONEY,
	ACTIVE_ID INT NOT NULL,
	CONSTRAINT INVOICE_ID_PK PRIMARY KEY (INVOICE_ID)
);
------------------Mustafa-----------------------------------------------
--Service Line Status--
CREATE TABLE dbo.SERVICE_LINE_STATUS (
	ACTIVE_ID int not null,
	ACTIVE varchar(20),
	CONSTRAINT SL_ACTIVE_ID_PK1 PRIMARY KEY (ACTIVE_ID)
);
--customer contact--
CREATE TABLE dbo.CUSTOMER_CONTACT_INFO (
	CUSTOMER_ID INT not null,
	C_PHONE varchar(15)  not null,
	C_EMAIL varchar(30) not null,
	C_ADDRESS varchar(30) not null,
	C_ZIP INT not null,
	C_CITY varchar(30) not null,
	STATE_NAME varchar(10) not null,
	CONSTRAINT CUSTOMER_ID_PK1 PRIMARY KEY(CUSTOMER_ID)
);
--VEHICLE STATUS--
CREATE TABLE dbo.VEHICLE_STATUS (
	ACTIVE_ID int not null,
	ACTIVE varchar(20),
	CONSTRAINT V_ACTIVE_ID_PK1 PRIMARY KEY (ACTIVE_ID)
);
--PAYMENT REVENUE--
create table dbo.PAYMENT_REVENUE(
	REVENUE_ID int not null,
	PMT_ID int not null,
	INVOICE_ID int not null,
	REVENUE_VALUE MONEY not null,
	CONSTRAINT REVENUE_ID_PK1 PRIMARY KEY (REVENUE_ID, PMT_ID, INVOICE_ID)
);
------------Jahidul---------------------------------------------------
/*create table dbo.CUSTOMER_ORDER(
	SERVICE_ORDER_ID int not null,
	CUSTOMER_ID int not null,
	CONSTRAINT SERVICE_ORDER_ID_PK2 PRIMARY KEY (SERVICE_ORDER_ID, CUSTOMER_ID)
);*/
create table dbo.CUSTOMER_VEHICLE(
	V_VIN varchar(20) not null,
	CUSTOMER_ID int not null,
	CONSTRAINT V_VIN_PK2 PRIMARY KEY (V_VIN, CUSTOMER_ID)
);
create table dbo.VEHICLE_POLICY(
	V_VIN varchar(20) not null,
	POLICY_ID int not null,
	EXPIRATION_DATE date not null,
	CONSTRAINT V_VIN_PK4 PRIMARY KEY (V_VIN, POLICY_ID)
);
create table dbo.COMPANY_INSURANCE_POLICY(
	INSURANCE_ID int not null,
	POLICY_ID int not null,
	COVARAGE_COST money not null,
	CONSTRAINT INSURANCE_ID_PK1 PRIMARY KEY (INSURANCE_ID, POLICY_ID)
);
----------------------------Kyle--------------------------------------
CREATE TABLE dbo.VEHICLE_SERVICE(
	SERVICE_ID INT NOT NULL,
	V_VIN VARCHAR(20) NOT NULL,
	CONSTRAINT SERVICE_ID_PK2 PRIMARY KEY (SERVICE_ID, V_VIN)
);
CREATE TABLE dbo.CUSTOMER_STATUS (
	ACTIVE_ID INT NOT NULL,
	ACTIVE_NAME VARCHAR(20) NOT NULL,
	CONSTRAINT C_ACTIVE_ID_PK2 PRIMARY KEY (ACTIVE_ID)
);
CREATE TABLE dbo.SUPPLIER_STATUS(
	ACTIVE_ID INT NOT NULL,
	ACTIVE_NAME VARCHAR(15) NOT NULL,
	CONSTRAINT SUP_ACTIVE_ID_PK1 PRIMARY KEY (ACTIVE_ID)
);
CREATE TABLE dbo.VEHICLE(
	V_VIN VARCHAR(20) NOT NULL,
	V_MAKE VARCHAR(15) NOT NULL,
	V_MODEL VARCHAR(15) NOT NULL,
	V_YEAR INT NOT NULL,
	V_LICENSE_PLATE VARCHAR(15) NOT NULL,
	ACTIVE_ID INT NOT NULL,
	CONSTRAINT V_VIN_PK PRIMARY KEY (V_VIN)
);
--------------------------------Brandon--------------------------------
CREATE TABLE dbo.PART (
  PART_ID INT IDENTITY(1,1) NOT NULL,
  PART_NAME varchar(50),
  CONSTRAINT PART_ID_PK1 PRIMARY KEY (PART_ID)
 );
CREATE TABLE dbo.EMPLOYEE_SERVICE_LINE_ASSIGNMENT (
  SERVICE_LINE_ID INT NOT NULL,
  SERVICE_ORDER_ID INT NOT NULL,
  SERVICE_ID INT NOT NULL,
  EMPLOYEE_ID INT NOT NULL,
  CONSTRAINT SERVICE_LINE_ID_PK2 PRIMARY KEY (SERVICE_LINE_ID, EMPLOYEE_ID)
);
CREATE TABLE dbo.SERVICE (
  SERVICE_ID INT not null,
  SERVICE_TYPE VARCHAR(75) not null,
  COST MONEY NOT NULL,
  ACTIVE_ID INT NOT NULL,
  CONSTRAINT SERVICE_ID_PK PRIMARY KEY (SERVICE_ID)
);
CREATE TABLE dbo.SERVICE_LINE_PART(
  SERVICE_LINE_ID INT NOT NULL,
  SERVICE_ORDER_ID INT NOT NULL,
  SERVICE_ID INT NOT NULL,
  PART_ID INT NOT NULL,
  CONSTRAINT SERVICE_LINE_ID_PK3 PRIMARY KEY (SERVICE_LINE_ID, PART_ID)
);
--------------------------------Maddy------------------------------------
CREATE TABLE dbo.COUNTRY (
	COUNTRY_ID int IDENTITY(1,1) not null,
	COUNTRY_NAME varchar(60) not null,
	CONSTRAINT COUNTRY_ID_PK PRIMARY KEY (COUNTRY_ID)
);
CREATE TABLE dbo.CUSTOMER_TYPE (
	BUSINESS_ID int NOT NULL, /*0-not business(individual) 1-business(business) */
	BUSINESS varchar(20) NOT NULL,
	CONSTRAINT BUSINESS_ID_PK3 PRIMARY KEY (BUSINESS_ID)
);
CREATE TABLE dbo.SERVICE_ORDER (
	SERVICE_ORDER_ID int IDENTITY(1,1) not null,
	CUSTOMER_ID INT NOT NULL,
	ORDER_DATE DATETIME NOT NULL,
	ACTIVE_ID INT NOT NULL,
	CONSTRAINT SERVICE_ORDER_ID_PK PRIMARY KEY (SERVICE_ORDER_ID)
);
------------------------------Giancarlos------------------------------------
CREATE TABLE dbo.VIOLATION (
    VIOLATION_ID int not null,
    VIOLATION_NAME VARCHAR(80),
	LAW_CODE VARCHAR(15),
    CONSTRAINT VIOLATION_ID_PK PRIMARY KEY (VIOLATION_ID)
);
CREATE TABLE dbo.CUSTOMER_STATE (
    CUSTOMER_ID INT NOT NULL,
	STATE_ID INT NOT NULL,
    CONSTRAINT CUSTOMER_ID_PK4 PRIMARY KEY (CUSTOMER_ID, STATE_ID)
);
CREATE TABLE dbo.INVOICE_STATUS(
	ACTIVE_ID int not null,
	ACTIVE_NAME varchar(15)
	CONSTRAINT I_ACTIVE_ID_PK2 PRIMARY KEY (ACTIVE_ID)
);
CREATE TABLE dbo.PAYMENT_STATUS(
	ACTIVE_ID int not null,
	ACTIVE_NAME varchar(15)
	CONSTRAINT P_ACTIVE_ID_PK PRIMARY KEY (ACTIVE_ID)
);
------------------------------Zach------------------------------------------
CREATE TABLE dbo.SUPPLIER_PART (
	PART_ID int IDENTITY(1,1) not null,
	SUPPLIER_ID INT not null,
	CONSTRAINT PART_ID_PK PRIMARY KEY (PART_ID, SUPPLIER_ID)
);
CREATE TABLE dbo.STATE(
	STATE_ID int not null,
	STATE_NAME varchar(30),
	CONSTRAINT STATE_ID_PK PRIMARY KEY (STATE_ID)
);
CREATE TABLE dbo.Employee_Status(
	ACTIVE_ID int not null,
	ACTIVE_NAME varchar(15)
	CONSTRAINT E_ACTIVE_ID_PK2 PRIMARY KEY (ACTIVE_ID)
);
CREATE TABLE dbo.STATE_VIOLATION(
	VIOLATION_ID int IDENTITY(1,1) not null,
	STATE_ID int not null
	CONSTRAINT VIOLATION_ID_PK1 PRIMARY KEY (VIOLATION_ID, STATE_ID)
);
-----------------------------Jerry-----------------------------------------
--ACCOUNT REVENUE Table--
CREATE TABLE dbo.ACCOUNT_REVENUE (
	REVENUE_ID int IDENTITY(1,1) not null,
	REVENUE_NAME varchar(30),
	CONSTRAINT REVENUE_ID_PK PRIMARY KEY (REVENUE_ID)
);
--Service Status Create--
CREATE TABLE dbo.SERVICE_STATUS (
    ACTIVE_ID int NOT NULL,
    ACTIVE_NAME varchar(30),
	CONSTRAINT SERV_ACTIVE_ID_PK1 PRIMARY KEY (ACTIVE_ID)
);
--INSURANCE COMPANY Table--
CREATE TABLE dbo.INSURANCE_COMPANY (
	INSURANCE_ID int IDENTITY(1,1) not null,
	INSURANCE_NAME varchar(40) not null,
	CONSTRAINT INSURANCE_ID_PK PRIMARY KEY (INSURANCE_ID)
);
--INSURANCE POLICY Table--
CREATE TABLE dbo.INSURANCE_POLICY (
	POLICY_ID int IDENTITY(1,1) not null,
	POLICY_NAME varchar(40),
	CONSTRAINT POLICY_ID_PK PRIMARY KEY (POLICY_ID)
);
---------------------------------------------------------------------------------------------------------------------------
--------------------------------------------- ALTER TABLE -----------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------
-------------------------Darrian-----------------------------------------------------
--Alter Customer--
ALTER TABLE Customer
add CONSTRAINT ACTIVE_ID_FK5 FOREIGN KEY (ACTIVE_ID) REFERENCES CUSTOMER_STATUS(ACTIVE_ID),
CONSTRAINT BUSINESS_ID_FK5 FOREIGN KEY (BUSINESS_ID) REFERENCES CUSTOMER_TYPE(BUSINESS_ID);
--Alter Service Line--
ALTER TABLE SERVICE_LINE
add CONSTRAINT SERVICE_ORDER_ID_FK1 FOREIGN KEY (SERVICE_ORDER_ID) REFERENCES SERVICE_ORDER(SERVICE_ORDER_ID), 
CONSTRAINT SERVICE_ID_FK2 FOREIGN KEY (SERVICE_ORDER_ID) REFERENCES SERVICE_ORDER(SERVICE_ORDER_ID),
CONSTRAINT ACTIVE_ID_FK FOREIGN KEY (ACTIVE_ID) REFERENCES SERVICE_LINE_STATUS(ACTIVE_ID);
--Alter Invoice Payment--
ALTER TABLE INVOICE_PAYMENT
add CONSTRAINT PMT_ID_FK FOREIGN KEY (PMT_ID) REFERENCES PAYMENT(PMT_ID),
CONSTRAINT INVOICE_ID_FK2 FOREIGN KEY (INVOICE_ID) REFERENCES INVOICE(INVOICE_ID),
CONSTRAINT ACTIVE_ID_FK8 FOREIGN KEY (ACTIVE_ID) REFERENCES PAYMENT_STATUS(ACTIVE_ID);
----------------------------Anthony-----------------------------------------------------
--Alter Supplier--
ALTER TABLE SUPPLIER
add CONSTRAINT ACTIVE_ID_FK6 FOREIGN KEY (ACTIVE_ID) REFERENCES SUPPLIER_STATUS(ACTIVE_ID);
--Alter Employee--
ALTER TABLE EMPLOYEE
add CONSTRAINT ACTIVE_ID_FK4 FOREIGN KEY (ACTIVE_ID) REFERENCES EMPLOYEE_STATUS(ACTIVE_ID);
--Alter Invoice--
ALTER TABLE INVOICE
add CONSTRAINT CUSTOMER_ID_FK1 FOREIGN KEY (CUSTOMER_ID) REFERENCES Customer(CUSTOMER_ID);

---------------------------Mustafa------------------------------------------------------
--CUSTOMER CONTACT INFO ALTER
ALTER TABLE CUSTOMER_CONTACT_INFO
add CONSTRAINT CUSTOMER_ID_FK2 FOREIGN KEY (CUSTOMER_ID) REFERENCES Customer(CUSTOMER_ID);
/*CONSTRAINT STATE_ID_FK FOREIGN KEY (STATE_ID) REFERENCES STATE(STATE_ID);*/
ALTER TABLE PAYMENT_REVENUE
add CONSTRAINT REVENUE_ID_FK FOREIGN KEY (REVENUE_ID) REFERENCES ACCOUNT_REVENUE(REVENUE_ID),
CONSTRAINT PMT_ID_FK6 FOREIGN KEY (PMT_ID, INVOICE_ID) REFERENCES INVOICE_PAYMENT(PMT_ID, INVOICE_ID);

-------------------------jahidul----------------------------------------------------------------
--Alter Customer Order--
/*ALTER TABLE CUSTOMER_ORDER
add CONSTRAINT SERVICE_ORDER_ID_FK2 FOREIGN KEY (SERVICE_ORDER_ID) REFERENCES SERVICE_ORDER(SERVICE_ORDER_ID),
CONSTRAINT CUSTOMER_ID_FK4 FOREIGN KEY (CUSTOMER_ID) REFERENCES Customer(CUSTOMER_ID);*/
--Alter Customer Vehicle--
ALTER TABLE CUSTOMER_VEHICLE
add CONSTRAINT V_VIN_FK2 FOREIGN KEY (V_VIN) REFERENCES VEHICLE(V_VIN),
CONSTRAINT CUSTOMER_ID_FK5 FOREIGN KEY (CUSTOMER_ID) REFERENCES Customer(CUSTOMER_ID);
--Alter Vehicle Policy--
ALTER TABLE VEHICLE_POLICY
add CONSTRAINT POLICY_ID_FK1 FOREIGN KEY (POLICY_ID) REFERENCES INSURANCE_POLICY(POLICY_ID),
CONSTRAINT V_VIN_FK3 FOREIGN KEY (V_VIN) REFERENCES VEHICLE(V_VIN);
--Alter Company Insurance policy--
ALTER TABLE COMPANY_INSURANCE_POLICY
add CONSTRAINT POLICY_ID_FK2 FOREIGN KEY (POLICY_ID) REFERENCES INSURANCE_POLICY(POLICY_ID),
CONSTRAINT INSURANCE_ID_FK FOREIGN KEY (INSURANCE_ID) REFERENCES INSURANCE_COMPANY(INSURANCE_ID);

---------------------------Jerry---------------------------------------------------------------
---------------------------Kyle---------------------------------------------------------------
--Alter Vehicle Service--
ALTER TABLE VEHICLE
add CONSTRAINT ACTIVE_ID_FK1 FOREIGN KEY (ACTIVE_ID) REFERENCES VEHICLE_STATUS(ACTIVE_ID);
ALTER TABLE VEHICLE_SERVICE
add CONSTRAINT SERVICE_ID_FK3 FOREIGN KEY (SERVICE_ID) REFERENCES SERVICE(SERVICE_ID),
CONSTRAINT V_VIN_FK4 FOREIGN KEY (V_VIN) REFERENCES VEHICLE(V_VIN);
--------------------------------Brandon--------------------------------
--Alter Employee Service Line Assignment--
ALTER TABLE SERVICE
add CONSTRAINT ACTIVE_ID_FK3 FOREIGN KEY (ACTIVE_ID) REFERENCES SERVICE_STATUS(ACTIVE_ID);
ALTER TABLE EMPLOYEE_SERVICE_LINE_ASSIGNMENT
add CONSTRAINT SERVICE_LINE_ID_FK FOREIGN KEY (SERVICE_LINE_ID, SERVICE_ORDER_ID, SERVICE_ID) REFERENCES SERVICE_LINE(SERVICE_LINE_ID, SERVICE_ORDER_ID, SERVICE_ID),
CONSTRAINT EMPLOYEE_ID_FK3 FOREIGN KEY (EMPLOYEE_ID) REFERENCES EMPLOYEE(EMPLOYEE_ID);
ALTER TABLE SERVICE_LINE_PART
add CONSTRAINT SERVICE_LINE_ID_FK2 FOREIGN KEY (SERVICE_LINE_ID, SERVICE_ORDER_ID, SERVICE_ID) REFERENCES SERVICE_LINE(SERVICE_LINE_ID, SERVICE_ORDER_ID, SERVICE_ID),
CONSTRAINT PART_ID_FK3 FOREIGN KEY (PART_ID) REFERENCES PART(PART_ID);
-----------------------------Maddy----------------------------------------------------------------
--Alter Service Order--
ALTER TABLE SERVICE_ORDER
add CONSTRAINT ACTIVE_ID_FK2 FOREIGN KEY (ACTIVE_ID) REFERENCES SERVICE_ORDER_STATUS(ACTIVE_ID),
CONSTRAINT CUSTOMER_ID_FK6 FOREIGN KEY (CUSTOMER_ID) REFERENCES Customer(CUSTOMER_ID);
------------------------------Gian-------------------------------------------------------------------
--Alter Customer State--
ALTER TABLE CUSTOMER_STATE
add CONSTRAINT STATE_ID_FK1 FOREIGN KEY (STATE_ID) REFERENCES STATE(STATE_ID),
CONSTRAINT CUSTOMER_ID_FK7 FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMER_CONTACT_INFO(CUSTOMER_ID);
---------------------------Zach---------------------------------------------------------
--Alter Supplier Part--
ALTER TABLE SUPPLIER_PART
add CONSTRAINT PART_ID_FK2 FOREIGN KEY (PART_ID) REFERENCES PART(PART_ID),
CONSTRAINT SUPPLIER_ID_FK4 FOREIGN KEY (SUPPLIER_ID) REFERENCES SUPPLIER(SUPPLIER_ID);
--Alter State Violation--
ALTER TABLE STATE_VIOLATION
add CONSTRAINT VIOLATION_ID_FK FOREIGN KEY (VIOLATION_ID) REFERENCES VIOLATION(VIOLATION_ID),
CONSTRAINT STATE_ID_FK2 FOREIGN KEY (STATE_ID) REFERENCES STATE(STATE_ID);

