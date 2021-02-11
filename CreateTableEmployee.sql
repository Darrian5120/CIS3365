CREATE TABLE EMPLOYEE (
	EMP_ID int not null,
	EMP_LNAME varchar(30) not null,
	EMP_FNAME varchar(30) not null,
	EMP_ADDRESS varchar(50) not null,
	EMP_HIRE_DATE varchar(8),
	EMP_HOURS varchar(4),
	EMP_PAY_RATE int,
	EMP_PHONE int not null,
	EMP_BANK_INFO int,
	EMP_TAX int,
	EMP_JOB_FUNC varchar(30),
	PRIMARY KEY (EMP_ID)
);
