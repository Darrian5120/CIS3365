'''SET IDENTITY_INSERT CoogTechSolutions.dbo.EMPLOYEE OFF;
INSERT INTO CoogTechSolutions.dbo.EMPLOYEE (EMP_LNAME, EMP_FNAME, EMP_ADDRESS, EMP_HIRE_DATE, EMP_HOURS, EMP_PAY_RATE, EMP_PHONE, EMP_BANK_INFO, EMP_TAX, EMP_JOB_FUNC) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', row.EMP_LNAME, row.EMP_FNAME, row.EMP_ADDRESS, row.EMP_HIRE_DATE, row.EMP_HOURS, row.EMP_PAY_RATE, row.EMP_PHONE, row.EMP_BANK_INFO, row.EMP_TAX, row.EMP_JOB_FUNC)