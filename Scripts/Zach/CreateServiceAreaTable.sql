USE CoogTechSolutions
CREATE TABLE dbo.Service_Area(
	AREA_ID int not null,
	SERVICE_TYPE varchar(15) not null,
	V_VIN int not null,
	INVENTORY TEXT,

	PRIMARY KEY(AREA_ID),
	FOREIGN KEY(V_VIN) REFERENCES VEHICLE(V_VIN)
	/*Zach Kurtubi*/
);
