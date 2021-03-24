USE CoogTechSolutions
CREATE TABLE dbo.BUSINESS_INFO (
	BUS_ID int not null,
	BUS_ADDRESS  varchar(30) not null,
	BUS_CITY varchar(30) not null,
	BUS_STATE varchar(2) not null,
	BUS_ZIP int not null,
	BUS_PHONE int not null,
	BUS_FAX int not null,
	BUS_HOURS int not null,
	BUS_EMAIL varchar(30) not null,
	BUS_WEBSITE varchar(30) not null,
	/*BUS_IMAGES int*/
	PRIMARY KEY(BUS_ID),
);
