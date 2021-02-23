“SET IDENTITY_INSERT CoogTechSolutions.dbo.COUNTRY OFF; 
INSERT INTO CoogTechSolutions.dbo.COUNTRY (C_COUNTRY, C_ID) 
VALUES (?,?)
“,row.C_COUNTRY,row.C_ID)
