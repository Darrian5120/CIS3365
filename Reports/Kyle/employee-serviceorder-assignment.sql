SELECT
EMPLOYEE.EMPLOYEE_ID AS 'Employee ID',
EMPLOYEE.EMPLOYEE_LNAME AS 'Last Name',
EMPLOYEE.EMPLOYEE_FNAME AS 'First Name',
ROLE.ROLE_NAME AS 'Role',
SERVICE.SERVICE_TYPE AS 'Service',
SERVICE_ORDER.SERVICE_ORDER_ID AS 'Order ID',
SERVICE_ORDER.ORDER_DATE AS 'Order Date'

FROM EMPLOYEE
JOIN ROLE
ON EMPLOYEE.ROLE_ID = ROLE.ROLE_ID
JOIN EMPLOYEE_SERVICE_LINE_ASSIGNMENT
ON EMPLOYEE.EMPLOYEE_ID = EMPLOYEE_SERVICE_LINE_ASSIGNMENT.EMPLOYEE_ID
JOIN SERVICE_LINE
ON EMPLOYEE_SERVICE_LINE_ASSIGNMENT.SERVICE_ORDER_ID = SERVICE_LINE.SERVICE_ORDER_ID
JOIN SERVICE
ON SERVICE_LINE.SERVICE_ID = SERVICE.SERVICE_ID
JOIN SERVICE_ORDER
ON SERVICE_LINE.SERVICE_ORDER_ID = SERVICE_ORDER.SERVICE_ORDER_ID

WHERE EMPLOYEE.ACTIVE_ID = 1 OR EMPLOYEE.ACTIVE_ID = 3

ORDER BY EMPLOYEE.EMPLOYEE_ID

