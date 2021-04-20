USE CoogTechSolutions
-------------------Darrian-------------------------------
CREATE TABLE dbo.Customer (
    CUSTOMER_ID INT IDENTITY(1,1) NOT NULL,
    C_LNAME varchar(25) NOT NULL,
    C_FNAME varchar(25) NOT NULL,
	C_BUSINESS_NAME varchar(50),
	ACTIVE_ID INT NOT NULL,
	BUSINESS_ID INT NOT NULL,
	C_ADDRESS_LINE1 varchar(30) not null,
	C_ADDRESS_LINE2 varchar(30),
	C_CITY varchar(30) not null,
	STATE_NAME varchar(15) not null,
	C_ZIP varchar(6) not null,
	COUNTRY_NAME varchar(30) not null,
	C_PHONE varchar(15)  not null,
	C_EMAIL varchar(35),
	CONSTRAINT CUSTOMER_ID_PK PRIMARY KEY (CUSTOMER_ID)
);
CREATE TABLE dbo.PAYMENT (
	PMT_ID int NOT NULL,
	PMT_TYPE VARCHAR(10) NOT NULL,
	CONSTRAINT PMT_ID_PK PRIMARY KEY (PMT_ID)
);
CREATE TABLE dbo.SERVICE_LINE (
	SERVICE_ORDER_ID INT NOT NULL,
	SERVICE_ID INT NOT NULL,
    QUANTITY INT,
	LINE_COST MONEY,
	ACTIVE_ID INT NOT NULL,
	CONSTRAINT SERVICE_LINE_ID_PK PRIMARY KEY (SERVICE_ORDER_ID, SERVICE_ID)
);
CREATE TABLE dbo.INVOICE_PAYMENT (
	PMT_ID int NOT NULL,
    INVOICE_ID int NOT NULL,
	SERVICE_ORDER_ID INT NOT NULL,
	PMT_AMOUNT MONEY NOT NULL,
	ACTIVE_ID INT NOT NULL,
	CONSTRAINT IP_NUMBER_PK1 PRIMARY KEY (PMT_ID, INVOICE_ID, SERVICE_ORDER_ID)
);
-----------------Anthony-------------------------------
--Employee Create Script--
CREATE TABLE dbo.EMPLOYEE (
	EMPLOYEE_ID int IDENTITY(1,1) NOT NULL,
	EMPLOYEE_LNAME varchar(30) not null,
	EMPLOYEE_FNAME varchar(30) not null,
	ROLE_ID INT NOT NULL,
	ACTIVE_ID INT NOT NULL,
	E_ADDRESS_LINE1 varchar(30)  not null,
	E_ADDRESS_LINE2 varchar(30),
	E_CITY varchar(30) not null,
	E_STATE varchar(15) not null,
	E_ZIP varchar(6) not null,
	E_COUNTRY varchar(30) not null,
	E_PHONE varchar(15) not null,
	E_EMAIL varchar(35) not null,
	CONSTRAINT EMPLOYEE_ID_PK PRIMARY KEY (EMPLOYEE_ID)
);
--Supplier Create Script--
CREATE TABLE dbo.SUPPLIER (
	SUPPLIER_ID int IDENTITY(1,1) not null,
	SUPPLIER_NAME varchar(50) NOT NULL,
	ACTIVE_ID INT NOT NULL,
	S_ADDRESS_LINE1 varchar(30)  not null,
	S_ADDRESS_LINE2 varchar(30),
	S_CITY varchar(30) not null,
	S_STATE varchar(15) not null,
	S_ZIP varchar(6) not null,
	S_COUNTRY varchar(30) not null,
	S_PHONE varchar(15) not null,
	S_EMAIL varchar(35) not null,
	CONSTRAINT SUPPLIER_ID_PK PRIMARY KEY (SUPPLIER_ID)
);

--Service Order Status Create--
CREATE TABLE dbo.SERVICE_ORDER_STATUS (
    ACTIVE_ID int NOT NULL,
    ACTIVE_NAME varchar(25) not null,
	CONSTRAINT SO_ACTIVE_ID_PK1 PRIMARY KEY (ACTIVE_ID)
);

--Create Invoice--
CREATE TABLE dbo.INVOICE (
	INVOICE_ID int IDENTITY(1,1) not null,
	SERVICE_ORDER_ID INT NOT NULL,
	TOTAL_COST MONEY,
	INVOICE_DATE date not null,
	AMT_OWED MONEY,
	ACTIVE_ID INT NOT NULL,
	CONSTRAINT INVOICE_ID_PK PRIMARY KEY (INVOICE_ID, SERVICE_ORDER_ID)
);
------------------Mustafa-----------------------------------------------
--Service Line Status--
CREATE TABLE dbo.SERVICE_LINE_STATUS (
	ACTIVE_ID int not null,
	ACTIVE_NAME varchar(20),
	CONSTRAINT SL_ACTIVE_ID_PK1 PRIMARY KEY (ACTIVE_ID)
);
--VEHICLE STATUS--
CREATE TABLE dbo.VEHICLE_STATUS (
	ACTIVE_ID int not null,
	ACTIVE_NAME varchar(20) not null,
	CONSTRAINT V_ACTIVE_ID_PK1 PRIMARY KEY (ACTIVE_ID)
);
--PAYMENT REVENUE--
create table dbo.PAYMENT_REVENUE(
	REVENUE_ID int not null,
	PMT_ID int not null,
	INVOICE_ID int not null,
	SERVICE_ORDER_ID int not null,
	REVENUE_VALUE MONEY not null,
	CONSTRAINT REVENUE_ID_PK1 PRIMARY KEY (REVENUE_ID, PMT_ID, INVOICE_ID, SERVICE_ORDER_ID)
);
CREATE TABLE dbo.VEHICLE_CONDITION (
	CONDITION_ID INT not null,
	CONDITION varchar(30) not null,
	CONSTRAINT CONDITION_ID_PK PRIMARY KEY(CONDITION_ID)
);
------------Jahidul---------------------------------------------------

----EMPLOYEE_CONTACT_INFO-----
/*CREATE TABLE dbo.EMPLOYEE_CONTACT_INFO (
	EMPLOYEE_ID INT not null,
	CONTACT_ID INT not null,
	CONSTRAINT EMPLOYEE_ID_PK1 PRIMARY KEY(EMPLOYEE_ID, CONTACT_ID)
);
CREATE TABLE dbo.SUPPLIER_CONTACT_INFO (
	SUPPLIER_ID INT not null,
	CONTACT_ID INT not null,
	S_ADDRESS_LINE1 varchar(30)  not null,
	S_ADDRESS_LINE2 varchar(30),
	S_CITY varchar(30) not null,
	S_STATE varchar(15) not null,
	S_ZIP INT not null,
	S_COUNTRY varchar(30) not null,
	S_PHONE varchar(15) not null,
	S_EMAIL varchar(35) not null,
	CONSTRAINT SUPPLIER_ID_PK1 PRIMARY KEY(SUPPLIER_ID, CONTACT_ID)
);*/
create table dbo.CUSTOMER_VEHICLE(
	V_ID int not null,
	CUSTOMER_ID int not null,
	CONSTRAINT V_ID_PK2 PRIMARY KEY (V_ID, CUSTOMER_ID)
);
create table dbo.MAKE(
	MAKE_ID int IDENTITY(1,1) not null,
	MAKE_NAME varchar(30) not null,
	CONSTRAINT MAKE_PK PRIMARY KEY (MAKE_ID)
);
create table dbo.MODEL(
	MODEL_ID int IDENTITY(1,1) not null,
	MAKE_ID INT NOT NULL,
	MODEL_NAME varchar(30) NOT NULL,
	CONSTRAINT MODEL_PK PRIMARY KEY (MODEL_ID)
);
create table dbo.POLICY(
	CUSTOMER_ID INT NOT NULL,
	V_ID INT NOT NULL,
	INSURANCE_ID int not null,
	POLICY_ID int not null,
	EXPIRATION_DATE DATE,
	CONSTRAINT CPOLICY_ID_PK1 PRIMARY KEY (CUSTOMER_ID, V_ID, INSURANCE_ID, POLICY_ID)
);
----------------------------Kyle--------------------------------------
CREATE TABLE dbo.VEHICLE_SERVICE(
	SERVICE_ID INT NOT NULL,
	V_ID INT NOT NULL,
	CONSTRAINT SERVICE_ID_PK2 PRIMARY KEY (SERVICE_ID, V_ID)
);
CREATE TABLE dbo.CUSTOMER_STATUS (
	ACTIVE_ID INT NOT NULL,
	ACTIVE_NAME VARCHAR(20) NOT NULL,
	CONSTRAINT C_ACTIVE_ID_PK PRIMARY KEY (ACTIVE_ID)
);
CREATE TABLE dbo.SUPPLIER_STATUS(
	ACTIVE_ID INT NOT NULL,
	ACTIVE_NAME VARCHAR(25) NOT NULL,
	CONSTRAINT SUP_ACTIVE_ID_PK1 PRIMARY KEY (ACTIVE_ID)
);
CREATE TABLE dbo.VEHICLE(
	V_ID INT IDENTITY(1,1) NOT NULL,
	V_VIN VARCHAR(20) NOT NULL,
	MAKE_ID INT NOT NULL,
	MODEL_ID INT NOT NULL,
	V_YEAR INT NOT NULL,
	V_LICENSE_PLATE VARCHAR(15) NOT NULL,
	V_COLOR VARCHAR(15),
	ACTIVE_ID INT NOT NULL,
	CONDITION_ID INT NOT NULL,
	CONSTRAINT V_ID_PK PRIMARY KEY (V_ID)
);
--------------------------------Brandon--------------------------------
CREATE TABLE dbo.PART (
  PART_ID INT IDENTITY(1,1) NOT NULL,
  PART_NAME varchar(50) NOT NULL,
  CONSTRAINT PART_ID_PK1 PRIMARY KEY (PART_ID)
 );
CREATE TABLE dbo.EMPLOYEE_SERVICE_LINE_ASSIGNMENT (
  SERVICE_ORDER_ID INT NOT NULL,
  SERVICE_ID INT NOT NULL,
  EMPLOYEE_ID INT NOT NULL,
  CONSTRAINT SERVICE_LINE_ID_PK2 PRIMARY KEY (SERVICE_ORDER_ID, SERVICE_ID, EMPLOYEE_ID)
);
CREATE TABLE dbo.SERVICE (
  SERVICE_ID INT not null,
  SERVICE_TYPE VARCHAR(75) not null,
  COST MONEY NOT NULL,
  ACTIVE_ID INT NOT NULL,
  CONSTRAINT SERVICE_ID_PK PRIMARY KEY (SERVICE_ID)
);
CREATE TABLE dbo.SERVICE_LINE_PART(
  SERVICE_ORDER_ID INT NOT NULL,
  SERVICE_ID INT NOT NULL,
  PART_ID INT NOT NULL,
  CONSTRAINT SERVICE_LINE_ID_PK3 PRIMARY KEY (SERVICE_ORDER_ID, SERVICE_ID, PART_ID)
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
CREATE TABLE dbo.ROLE (
	ROLE_ID int IDENTITY(1,1) NOT NULL,
	ROLE_NAME VARCHAR(30) NOT NULL,
	PAY_RATE MONEY,
	CONSTRAINT ROLE_ID_PK PRIMARY KEY (ROLE_ID)
);
------------------------------Giancarlos------------------------------------
CREATE TABLE dbo.VIOLATION (
    VIOLATION_ID int IDENTITY(1,1) not null,
    VIOLATION_NAME VARCHAR(255) not null,
	LAW_CODE VARCHAR(15),
	V_ID int not null,
	VIOLATION_DATE DATE,
    CONSTRAINT VIOLATION_ID_PK PRIMARY KEY (VIOLATION_ID)
);
CREATE TABLE dbo.CUSTOMER_STATE (
    CUSTOMER_ID INT NOT NULL,
	STATE_ID INT NOT NULL,
    CONSTRAINT CUSTOMER_ID_PK4 PRIMARY KEY (CUSTOMER_ID, STATE_ID)
);
CREATE TABLE dbo.INVOICE_STATUS(
	ACTIVE_ID int not null,
	ACTIVE_NAME varchar(15) not null,
	CONSTRAINT I_ACTIVE_ID_PK2 PRIMARY KEY (ACTIVE_ID)
);
CREATE TABLE dbo.PAYMENT_STATUS(
	ACTIVE_ID int not null,
	ACTIVE_NAME varchar(15) not null,
	CONSTRAINT P_ACTIVE_ID_PK PRIMARY KEY (ACTIVE_ID)
);
------------------------------Zach------------------------------------------
CREATE TABLE dbo.SUPPLIER_PART (
	PART_ID int not null,
	SUPPLIER_ID INT not null,
	PART_COST MONEY,
	QUANTITY INT not null,
	CONSTRAINT PART_ID_PK PRIMARY KEY (PART_ID, SUPPLIER_ID)
);
CREATE TABLE dbo.STATE(
	STATE_ID int IDENTITY(1,1) not null,
	COUNTRY_ID int not null,
	STATE_ABBREVIATION varchar(2) not null,
	STATE_NAME varchar(30),
	CONSTRAINT STATE_ID_PK PRIMARY KEY (STATE_ID)
);
CREATE TABLE dbo.Employee_Status(
	ACTIVE_ID int not null,
	ACTIVE_NAME varchar(20) not null,
	CONSTRAINT E_ACTIVE_ID_PK2 PRIMARY KEY (ACTIVE_ID)
);
CREATE TABLE dbo.STATE_VIOLATION(
	VIOLATION_ID int not null,
	STATE_ID int not null,
	CONSTRAINT VIOLATION_ID_PK1 PRIMARY KEY (VIOLATION_ID, STATE_ID)
);
-----------------------------Jerry-----------------------------------------
--ACCOUNT REVENUE Table--
CREATE TABLE dbo.ACCOUNT_REVENUE (
	REVENUE_ID int IDENTITY(1,1) not null,
	REVENUE_NAME varchar(30) not null,
	CONSTRAINT REVENUE_ID_PK PRIMARY KEY (REVENUE_ID)
);
--Service Status Create--
CREATE TABLE dbo.SERVICE_STATUS (
    ACTIVE_ID int NOT NULL,
    ACTIVE_NAME varchar(30) not null,
	CONSTRAINT SERV_ACTIVE_ID_PK1 PRIMARY KEY (ACTIVE_ID)
);
--INSURANCE COMPANY Table--
CREATE TABLE dbo.INSURANCE_COMPANY (
	INSURANCE_ID int IDENTITY(1,1) not null,
	INSURANCE_NAME varchar(50) not null,
	I_ADDRESS_LINE1 varchar(50),
	I_ADDRESS_LINE2 varchar(50),
	I_CITY varchar(50),
	I_STATE varchar(50),
	I_ZIP varchar(6),
	I_COUNTRY varchar(50),
	I_PHONE varchar(15),
	I_EMAIL varchar(40),
	CONSTRAINT INSURANCE_ID_PK PRIMARY KEY (INSURANCE_ID)
);
--INSURANCE POLICY Table--
CREATE TABLE dbo.INSURANCE_POLICY (
	POLICY_ID int IDENTITY(1,1) not null,
	POLICY_NAME varchar(50) not null,
	CONSTRAINT POLICY_ID_PK PRIMARY KEY (POLICY_ID)
);
---------------------------------------------------------------------------------------------------------------------------
--------------------------------------------- ALTER TABLE -----------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------
-------------------------Darrian-----------------------------------------------------
--Alter Customer--
ALTER TABLE Customer
add CONSTRAINT ACTIVE_ID_FK5 FOREIGN KEY (ACTIVE_ID) REFERENCES CUSTOMER_STATUS,
CONSTRAINT BUSINESS_ID_FK FOREIGN KEY (BUSINESS_ID) REFERENCES CUSTOMER_TYPE(BUSINESS_ID);
--Alter Service Line--
ALTER TABLE SERVICE_LINE
add CONSTRAINT SERVICE_ORDER_ID_FK1 FOREIGN KEY (SERVICE_ORDER_ID) REFERENCES SERVICE_ORDER(SERVICE_ORDER_ID), 
CONSTRAINT SERVICE_ID_FK FOREIGN KEY (SERVICE_ID) REFERENCES SERVICE(SERVICE_ID),
CONSTRAINT ACTIVE_ID_FK FOREIGN KEY (ACTIVE_ID) REFERENCES SERVICE_LINE_STATUS(ACTIVE_ID);
--Alter Invoice Payment--
ALTER TABLE INVOICE_PAYMENT
add CONSTRAINT PMT_ID_FK FOREIGN KEY (PMT_ID) REFERENCES PAYMENT(PMT_ID),
CONSTRAINT INVOICE_ID_FK FOREIGN KEY (INVOICE_ID, SERVICE_ORDER_ID) REFERENCES INVOICE,
CONSTRAINT ACTIVE_ID_FK8 FOREIGN KEY (ACTIVE_ID) REFERENCES PAYMENT_STATUS(ACTIVE_ID);
----------------------------Anthony-----------------------------------------------------
--Alter Supplier--
ALTER TABLE SUPPLIER
add CONSTRAINT ACTIVE_ID_FK6 FOREIGN KEY (ACTIVE_ID) REFERENCES SUPPLIER_STATUS(ACTIVE_ID);
--Alter Employee--
ALTER TABLE EMPLOYEE
add CONSTRAINT ACTIVE_ID_FK4 FOREIGN KEY (ACTIVE_ID) REFERENCES EMPLOYEE_STATUS(ACTIVE_ID),
CONSTRAINT ROLE_ID_FK FOREIGN KEY (ROLE_ID) REFERENCES ROLE(ROLE_ID);
--Alter Invoice--
ALTER TABLE INVOICE
add CONSTRAINT SO_ID_FK FOREIGN KEY (SERVICE_ORDER_ID) REFERENCES SERVICE_ORDER,
CONSTRAINT ACTIVE_ID_FK7 FOREIGN KEY (ACTIVE_ID) REFERENCES INVOICE_STATUS(ACTIVE_ID);

---------------------------Mustafa------------------------------------------------------
--CUSTOMER CONTACT INFO ALTER
/*ALTER TABLE CUSTOMER_CONTACT_INFO
add CONSTRAINT CUSTOMER_ID_FK2 FOREIGN KEY (CUSTOMER_ID) REFERENCES Customer(CUSTOMER_ID);
CONSTRAINT STATE_ID_FK FOREIGN KEY (STATE_ID) REFERENCES STATE(STATE_ID);*/
ALTER TABLE PAYMENT_REVENUE
add CONSTRAINT REVENUE_ID_FK FOREIGN KEY (REVENUE_ID) REFERENCES ACCOUNT_REVENUE(REVENUE_ID),
CONSTRAINT PR_ID_FK6 FOREIGN KEY (PMT_ID, INVOICE_ID, SERVICE_ORDER_ID) REFERENCES INVOICE_PAYMENT;

-------------------------jahidul----------------------------------------------------------------
--Alter Customer Vehicle--
ALTER TABLE CUSTOMER_VEHICLE
add CONSTRAINT V_ID_FK2 FOREIGN KEY (V_ID) REFERENCES VEHICLE(V_ID),
CONSTRAINT CUSTOMER_ID_FK5 FOREIGN KEY (CUSTOMER_ID) REFERENCES Customer(CUSTOMER_ID);
--Alter Company Insurance policy--
ALTER TABLE POLICY
add CONSTRAINT POLICY_ID_FK2 FOREIGN KEY (POLICY_ID) REFERENCES INSURANCE_POLICY(POLICY_ID),
CONSTRAINT INSURANCE_ID_FK FOREIGN KEY (INSURANCE_ID) REFERENCES INSURANCE_COMPANY(INSURANCE_ID),
CONSTRAINT V_ID_FK FOREIGN KEY (V_ID) REFERENCES VEHICLE(V_ID),
CONSTRAINT CUSTOMER_ID_FK FOREIGN KEY (CUSTOMER_ID) REFERENCES Customer(CUSTOMER_ID);
--Model
ALTER TABLE MODEL
add CONSTRAINT MAKE_ID_FK FOREIGN KEY (MAKE_ID) REFERENCES MAKE;

---------------------------Jerry---------------------------------------------------------------
---------------------------Kyle---------------------------------------------------------------
--Alter Vehicle Service--
ALTER TABLE VEHICLE
add CONSTRAINT ACTIVE_ID_FK1 FOREIGN KEY (ACTIVE_ID) REFERENCES VEHICLE_STATUS(ACTIVE_ID),
CONSTRAINT CONDITION_ID_FK FOREIGN KEY (CONDITION_ID) REFERENCES VEHICLE_CONDITION,
CONSTRAINT MAKE_ID_FK1 FOREIGN KEY (MAKE_ID) REFERENCES MAKE,
CONSTRAINT MODEL_ID_FK1 FOREIGN KEY (MODEL_ID) REFERENCES MODEL;
ALTER TABLE VEHICLE_SERVICE
add CONSTRAINT SERVICE_ID_FK5 FOREIGN KEY (SERVICE_ID) REFERENCES SERVICE,
CONSTRAINT V_ID_FK4 FOREIGN KEY (V_ID) REFERENCES VEHICLE;
--------------------------------Brandon--------------------------------
--Alter Employee Service Line Assignment--
ALTER TABLE SERVICE
add CONSTRAINT ACTIVE_ID_FK3 FOREIGN KEY (ACTIVE_ID) REFERENCES SERVICE_STATUS(ACTIVE_ID);

ALTER TABLE EMPLOYEE_SERVICE_LINE_ASSIGNMENT
add CONSTRAINT SERVICE_LINE_ID_FK FOREIGN KEY (SERVICE_ORDER_ID, SERVICE_ID) REFERENCES SERVICE_LINE,
CONSTRAINT EMPLOYEE_ID_FK3 FOREIGN KEY (EMPLOYEE_ID) REFERENCES EMPLOYEE(EMPLOYEE_ID);

ALTER TABLE SERVICE_LINE_PART
add CONSTRAINT SERVICE_LINE_ID_FK1 FOREIGN KEY (SERVICE_ORDER_ID, SERVICE_ID) REFERENCES SERVICE_LINE,
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
CONSTRAINT CUSTOMER_ID_FK7 FOREIGN KEY (CUSTOMER_ID) REFERENCES Customer(CUSTOMER_ID);
ALTER TABLE VIOLATION
add CONSTRAINT V_ID_FK1 FOREIGN KEY (V_ID) REFERENCES VEHICLE(V_ID);
---------------------------Zach---------------------------------------------------------
--STATE--
ALTER TABLE STATE
add CONSTRAINT COUNTRY_ID_FK FOREIGN KEY (COUNTRY_ID) REFERENCES COUNTRY;
--Alter Supplier Part--
ALTER TABLE SUPPLIER_PART
add CONSTRAINT PART_ID_FK2 FOREIGN KEY (PART_ID) REFERENCES PART(PART_ID),
CONSTRAINT SUPPLIER_ID_FK4 FOREIGN KEY (SUPPLIER_ID) REFERENCES SUPPLIER(SUPPLIER_ID);
--Alter State Violation--
ALTER TABLE STATE_VIOLATION
add CONSTRAINT VIOLATION_ID_FK FOREIGN KEY (VIOLATION_ID) REFERENCES VIOLATION(VIOLATION_ID),
CONSTRAINT STATE_ID_FK2 FOREIGN KEY (STATE_ID) REFERENCES STATE(STATE_ID);

