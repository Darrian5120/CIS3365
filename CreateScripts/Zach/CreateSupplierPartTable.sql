CREATE TABLE Supplier_Part (

SUP_PART_NUMBER varchar(15) PRIMARY KEY not null,
SUP_PART_DATE DATE not null, /*NEEDS TO BE REVIEWED*/
SUP_PART_PRICE float not null,

  
PRIMARY KEY (SUP_PART_ID),
FOREIGN KEY (SUP_PART_ID) REFERENCES (Supplier_Lookup)
/*Zach Kurtubi*/
  
);
