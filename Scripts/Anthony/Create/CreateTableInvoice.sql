USE CoogTechSolutions
CREATE TABLE dbo.INVOICE (
	INVOICE_ID int not null,
	C_ID int not null,
	AMT_PAID float,
	AMT_OWED float,
	INVOICE_DATE  datetime not null,
	PRIMARY KEY (INVOICE_ID),
	FOREIGN KEY (C_ID) REFERENCES Payment(C_ID)
);
