USE CoogTechSolutions
CREATE TABLE dbo.SERVICE_REQUEST (
	SERVICE_ID int not null,
	C_ID int not null,
	SERVICE_TYPE varchar(30) not null,
	REQUEST_DATE int not null,
	PRIMARY KEY (SERVICE_ID),
	FOREIGN KEY (C_ID) REFERENCES Customer(C_ID)
);
