USE CoogTechSolutions
CREATE TABLE dbo.INSURANCE_COMPANY (
	INSURANCE_ID int not null,
	C_ID int not null,
	COMPANY_NAME varchar(30) not null,
	PRIMARY KEY (INSURANCE_ID),
	FOREIGN KEY (C_ID) REFERENCES Customer(C_ID)
);
