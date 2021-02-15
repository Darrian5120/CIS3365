CREATE TABLE INVOICE (
	INVOICE_ID int not null,
	CUSTOMER_ID int not null,
	ITEM_ID int not null,
	AMT_PAID float,
	AMT_OWED float,
	ITEM_QUANTITY int,
	ITEM_COST float,
	DATE  datetime not null,
	PRIMARY KEY (INVOICE_ID)
);
