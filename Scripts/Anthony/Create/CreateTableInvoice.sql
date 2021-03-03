USE CoogTechSolutions
CREATE TABLE dbo.INVOICE (
	INVOICE_ID int not null,
	CUSTOMER_ID int not null,
	TOTAL_COST float,
	AMT_OWED float,
	INVOICE_DATE  datetime not null,
	CONSTRAINT INVOICE_ID_PK PRIMARY KEY (INVOICE_ID),
);
