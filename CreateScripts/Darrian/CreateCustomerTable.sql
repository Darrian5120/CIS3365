USE CoogTechSolutions
CREATE TABLE dbo.Customer (
    C_ID int IDENTITY(1,1) PRIMARY KEY,
    C_LNAME varchar(15) NOT NULL,
    C_FNAME varchar(15),
    SERVICE_ID int,
    ORDER_ID int,
    C_BUSINESS_NAME varchar(50)
);
