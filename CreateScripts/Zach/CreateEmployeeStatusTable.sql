USE CoogTechSolutions
CREATE TABLE dbo.Employee_Status(
	EMP_ID int not null,
	EMP_ACTIVE BIT,
	PRIMARY KEY(EMP_ID),
	FOREIGN KEY (EMP_ID) REFERENCES Employee(EMP_ID)
  
/*Zach Kurtubi*/

)
