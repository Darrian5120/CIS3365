USE CoogTechSolutions
CREATE TABLE dbo.WELDER(
	EMP_ID int PRIMARY KEY,
	FOREIGN KEY (EMP_ID) REFERENCES EMPLOYEE(EMP_ID)
);
