CREATE TABLE Customer (
    C_ID int not null,
    C_LNAME varchar(15) not null,
    C_FNAME varchar(15) not null,
    SERVICE_ID int,
    C_ORDER_NUM int,
    C_BUSINESS_NAME varchar(50),
    PRIMARY KEY (C_ID)
);