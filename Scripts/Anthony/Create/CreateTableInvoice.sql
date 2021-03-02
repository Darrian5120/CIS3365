USE CoogTechSolutions
CREATE TABLE dbo.INVOICE (
	INVOICE_ID int not null,
	CUSTOMER_ID int not null,
	TOTAL_COST float,
	AMT_OWED float,
	INVOICE_DATE  datetime not null,
	PRIMARY KEY (INVOICE_ID),
	FOREIGN KEY (C_ID) REFERENCES Payment(C_ID)
);
