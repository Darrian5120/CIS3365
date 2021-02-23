USE CoogTechSolutions
CREATE TABLE dbo.SERVICE_STAUS (
	SERVICE_ID int not null,
	C_ID int not null,
	SERVICE_ISSUES text not null,
	FOREIGN KEY (SERVICE_ID) REFERENCES CURRENT_SERVICE(SERVICE_ID),
	FOREIGN KEY (C_ID) REFERENCES Customer(C_ID)
);