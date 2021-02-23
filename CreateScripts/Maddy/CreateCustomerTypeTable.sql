USE CoogTechSolutions
CREATE TABLE dbo.CUSTOMER_TYPE (
	C_ID int not null,
	IS_BUSINESS BIT not null,
	PRIMARY KEY (C_ID),
	FOREIGN KEY (C_ID) REFERENCES Customer(C_ID)
);
