CREATE TABLE CUSTOMER (
    C_ID int NOT NULL PRIMARY KEY,
    C_LNAME varchar(15) NOT NULL,
    C_FNAME varchar(15) NOT NULL,
    SERVICE_ID int,
    ORDER_ID int,
    C_BUSINESS_NAME varchar(50)
);
