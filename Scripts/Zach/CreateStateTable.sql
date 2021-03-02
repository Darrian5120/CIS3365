USE CoogTechSolutions
CREATE TABLE dbo.State(
	C_STATE varchar(15) not null,
	C_ID int not null,
	LAW_CODE varchar(15) not null,  
	PRIMARY KEY(C_STATE, LAW_CODE),
	FOREIGN KEY (C_ID, C_STATE) REFERENCES CUSTOMER_CONTACT_INFO(C_ID, C_STATE)
 
	/*Zach Kurtubi*/
);
