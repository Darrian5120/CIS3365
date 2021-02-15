CREATE TABLE CUSTOMER_CONTACT_INFO (
C_ID INT not null,
C_PHONE INT  not null,
C_EMAIL varchar(30) not null,
C_ADDRESS varchar(90) not null,
C_ZIP INT not null,
C_CITY varchar(30) not null,
C_STATE varchar(2) not null, 
PRIMARY KEY (C_ID)

/*FOREIGN KEY (C_ID) REFERENCES Customer(C_ID)*/
);