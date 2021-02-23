USE CoogTechSolutions
CREATE TABLE dbo.Supplier_Part (
	SUP_PART_ID int PRIMARY KEY not null,
	SUPPLIER_ID int not null,
	SUP_PART_DATE DATE not null, 
	SUP_PART_PRICE float not null,
	FOREIGN KEY (SUPPLIER_ID) REFERENCES SUPPLIER(SUPPLIER_ID)
	/*Zach Kurtubi*/
  
);
