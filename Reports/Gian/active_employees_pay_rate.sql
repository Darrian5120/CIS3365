SELECT EMPLOYEE.EMPLOYEE_LNAME AS 'Last Name',
       EMPLOYEE.EMPLOYEE_FNAME AS 'First Name',
       ROLE.ROLE_NAME AS 'Job Role',
       ROLE.PAY_RATE AS 'Hourly Pay',
       Employee_Status.ACTIVE_NAME AS 'Status'

FROM EMPLOYEE

JOIN ROLE ON EMPLOYEE.ROLE_ID=ROLE.ROLE_ID
INNER JOIN Employee_Status ON EMPLOYEE.ACTIVE_ID=Employee_Status.ACTIVE_ID

WHERE Employee_Status.ACTIVE_ID = 1 OR Employee_Status.ACTIVE_ID = 2

ORDER BY [Job Role],[Hourly Pay];
