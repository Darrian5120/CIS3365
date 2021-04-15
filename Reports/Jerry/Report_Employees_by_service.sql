SELECT
EMPLOYEE.EMP_FNAME AS 'First Name',
EMPLOYEE.EMP_LNAME AS 'Last Name',
SERVICE.SERVICE_ID AS 'Service ID',
SERVICE.SERVICE_TYPE AS 'Service'

FROM EMPLOYEE
JOIN EMPLOYEE_SERVICE_LINE_ASSIGNMENT
ON EMPLOYEE.EMPLOYEE_ID = EMPLOYEE_SERVICE_LINE_ASSIGNMENT.EMPLOYEE_ID
JOIN SERVICE_LINE
ON EMPLOYEE_SERVICE_LINE_ASSIGNMENT.SERVICE_LINE_ID = SERVICE_LINE.SERVICE_LINE_ID
JOIN SERVICE
ON SERVICE_LINE.SERVICE_ID = SERVICE.SERVICE_ID
JOIN SERVICE_STATUS
ON SERVICE.SERVICE_ID = SERVICE_STATUS.SERVICE_ID

WHERE SERVICE.ACTIVE_ID = 2

ORDER BY SERVICE.SERVICE_ID
