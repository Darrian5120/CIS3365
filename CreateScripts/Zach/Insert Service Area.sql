''' SET IDENTITY_INSERT CoogTechSolutions.dbo.Service_Area_Part OFF;
 INSERT INTO CoogTechSolutions.dbo.Service_Area (AREA_ID, SERVICE_TYPE, V_ID, INVENTORY)
VALUES (?,?,?,?) ''', 
row.AREA_ID, row.SERVICE_Type, row.V_ID, row.INVENTORY)
