USE CoogTechSolutions

SELECT SUPPLIER.SUPPLIER_NAME, PART.PART_NAME, EMPLOYEE.EMPLOYEE_ID, EMPLOYEE.EMP_LNAME, EMPLOYEE.EMP_FNAME
FROM EMPLOYEE
JOIN EMPLOYEE_SERVICE_LINE_ASSIGNMENT
ON EMPLOYEE.EMPLOYEE_ID = EMPLOYEE_SERVICE_LINE_ASSIGNMENT.EMPLOYEE_ID
JOIN SERVICE_LINE
ON EMPLOYEE_SERVICE_LINE_ASSIGNMENT.SERVICE_LINE_ID = SERVICE_LINE.SERVICE_LINE_ID
JOIN SERVICE_LINE_PART
ON SERVICE_LINE.SERVICE_LINE_ID = SERVICE_LINE_PART.SERVICE_LINE_ID
JOIN PART
ON SERVICE_LINE_PART.PART_ID = PART.PART_ID
JOIN SUPPLIER_PART
ON PART.PART_ID = SUPPLIER_PART.PART_ID
JOIN SUPPLIER
ON SUPPLIER_PART.SUPPLIER_ID = SUPPLIER.SUPPLIER_ID
ORDER BY PART.PART_NAME;