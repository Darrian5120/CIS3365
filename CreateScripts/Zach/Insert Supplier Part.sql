''' SET IDENTITY_INSERT CoogTechSolutions.dbo.Supplier_Part OFF;
 INSERT INTO CoogTechSolutions.dbo.Supplier_Part (SUP_PART_NUMBER, SUP_PART_DATE, SUP_PART_PRICE)
VALUES (?,?,?) ''', 
row.SUP_PART_NUMNER, row.SUP_PART_DATE, row.SUP_Part_Price)
