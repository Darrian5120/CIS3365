“SET IDENTITY_INSERT CoogTechSolutions.dbo.CUSTOMER_TYPE OFF; 
INSERT INTO CoogTechSolutions.dbo.CUSTOMER_TYPE (IS_BUSINESS, IS_INDIVIDUAL) 
VALUES (?,?) 
“,row.IS_BUSINESS,row.IS_INDIVIDUAL)