CREATE TABLE CUSTOMER_STATUS ( 

C_ID INT(9) NOT NULL, 

C_ACTIVE BOOL NOT NULL, 

PRIMARY KEY (C_ID), 

FOREIGN KEY (C_ID) REFERENCES Customer(C_ID) 
  
); 
