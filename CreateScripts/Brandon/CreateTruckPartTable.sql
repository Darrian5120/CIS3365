USE CoogTechSolutions
CREATE TABLE dbo.TRUCK_PART ( 
  TRCK_PRT_ID INT NOT NULL,
  TRCK_PRT_FURNITURE INT NOT NULL, 
  TRCK_PRT_FRAME INT NOT NULL, 
  TRCK_PRT_GATE INT NOT NULL, 
  TRCK_PRT_BED INT NOT NULL, 
  TRCK_PRT_WETLINE INT NOT NULL, 
  TRCK_PRT_TARP INT NOT NULL, 
  TRCK_PRT_FLAT_BED INT NOT NULL, 
  TRCK_PRT_FUEL_PUMP INT NOT NULL, 
  TRCK_PRT_BENDING_MATERIAL INT NOT NULL, 
  TRCK_PRT_AXEL INT NOT NULL, 
  TRCK_PRT_WOOD INT NOT NULL,
  PRIMARY KEY (TRCK_PRT_ID)
); 
