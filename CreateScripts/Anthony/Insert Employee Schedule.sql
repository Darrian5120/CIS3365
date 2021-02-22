'''SET IDENTITY_INSERT CoogTechSolutions.dbo.Employee_Schedule OFF;
INSERT INTO CoogTechSolutions.dbo.Employee_Schedule (EMP_SCHD_WEEK, EMP_SCHD_EMP_IDS) VALUES (?, ?)
''', row.EMP_SCHD_WEEK, row.EMP_SCHD_EMP_IDS)