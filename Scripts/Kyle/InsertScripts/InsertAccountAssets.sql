“SET IDENTITY_INSERT CoogTechSolutions.dbo.ACCOUNT_ASSETS OFF;
INSERT INTO CoogTechSolutions.dbo.ACCOUNT_ASSETS (ASSET_NAME, ASSET_VALUE)
VALUES (?,?)
”,row.ASSET_NAME, row.ASSET_VALUE
