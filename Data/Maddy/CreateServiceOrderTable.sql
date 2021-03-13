USE CoogTechSolutions
CREATE TABLE dbo.SERVICE_ORDER (
	SERVICE_ORDER_ID int not null,
	SERVICE_TYPE varchar(30) not null,
	DATE_START datetime NOT NULL,
	DATE_END datetime NOT NULL,
	COST float(8) NOT NULL,
	PRIMARY KEY (SERVICE_ORDER_ID),
);
