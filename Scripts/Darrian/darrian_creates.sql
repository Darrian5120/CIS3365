USE CoogTechSolutions
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
	
--Alter Payment--
ALTER TABLE PAYMENT
add CONSTRAINT C_ID_FK FOREIGN KEY (C_ID) REFERENCES Customer(C_ID);
--Alter Service Order Line--
ALTER TABLE SERVICE_ORDER_LINE
add CONSTRAINT ORDER_ID_FK FOREIGN KEY (ORDER_ID) REFERENCES FINSIHED_ORDER(ORDER_ID);
--Alter Finsihed Order--
ALTER TABLE FINSIHED_ORDER
add CONSTRAINT ORDER_ID_FK FOREIGN KEY (ORDER_ID) REFERENCES SERVICE_REQUEST(ORDER_ID);