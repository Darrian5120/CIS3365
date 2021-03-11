USE CoogTechSolutions
CREATE TABLE dbo.SERVICE_SCHEDULE (
	SCHEDULE_ID int not null,
	SERVICE_TYPE varchar(30) not null,
	SERVICE_DATE datetime not null
	PRIMARY KEY (SCHEDULE_ID),
);
