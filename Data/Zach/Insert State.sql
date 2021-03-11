''' SET IDENTITY_INSERT CoogTechSolutions.dbo.State OFF;
 INSERT INTO CoogTechSolutions.dbo.State (C_STATE, LAW_CODE)
VALUES (?,?) ''', 
row.C_State, row.LAW_CODE)
