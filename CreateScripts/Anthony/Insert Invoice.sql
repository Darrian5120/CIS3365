'''SET IDENTITY_INSERT CoogTechSolutions.dbo.Invoice OFF;
INSERT INTO CoogTechSolutions.dbo.Invoice (CUSTOMER_ID, ITEM_ID, AMT_PAID, AMT_OWED, ITEM_QUANTITY, ITEM_COST, DATE) VALUES (?, ?, ?, ?, ?, ?, ?)
''', row.CUSTOMER_ID, row.ITEM_ID, row.AMT_PAID, row.AMT_OWED, row.ITEM_QUANTITY, row.ITEM_COST, row.DATE)