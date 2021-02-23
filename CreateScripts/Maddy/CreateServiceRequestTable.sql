USE CoogTechSolutions
CREATE TABLE SERVICE_REQUEST (
	SERVICE_ID int not null,
	SERVICE_TYPE varchar(30) not null,
	REQUEST_DATE int not null,
	PRIMARY KEY (SERVICE_ID)
);
