USE CoogTechSolutions
CREATE TABLE dbo.Service (  
  SERVICE_ID INT not null,  
  SERVICE_TYPE VARCHAR(30) not null,    
  DATE_START DATETIME NOT NULL, 
  DATE_END DATETIME, 
  COST MONEY NOT NULL,  
  PRIMARY KEY (SERVICE_ID)
); 