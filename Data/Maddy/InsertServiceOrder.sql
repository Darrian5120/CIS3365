“SET IDENTITY_INSERT CoogTechSolutions.dbo.SERVICE_ORDER OFF; 
INSERT INTO CoogTechSolutions.dbo.SERVICE_ORDER (SERVICE_TYPE, DATE_START, DATE_END, COST) 
VALUES (?,?,?,?)
“,row.SERVICE_TYPE,row.DATE_START,row.DATE_END, row.COST)
