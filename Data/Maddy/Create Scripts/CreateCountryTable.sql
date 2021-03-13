USE CoogTechSolutions
CREATE TABLE dbo.COUNTRY (
	C_COUNTRY varchar(20) not null,
	C_ID int not null,
	PRIMARY KEY (C_COUNTRY),
	FOREIGN KEY (C_ID) REFERENCES Customer(C_ID)
);
