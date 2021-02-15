CREATE TABLE Employee_Status(

	EMP_ID int,
	EMP_ACTIVE BIT,

	PRIMARY KEY(EMP_ID),
  FOREIGN KEY (EMP_ID) REFERENCES Employee(EMP_ID)
  
/*Zach Kurtubi*/

)
