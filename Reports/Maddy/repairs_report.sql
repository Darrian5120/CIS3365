USE CoogTechSolutions

DECLARE 
@serviceRepairs varchar(7)
@trailerRepairs varchar(15)

SELECT 
Service.SERVICE_ID AS 'Service ID', 
Service.SERVICE_NAME AS 'Service Name'
SELECT @serviceRepairs = 'REPAIRS'
SELECT @trailerRepairs = 'TRAILER REPAIRS'

FROM SERVICE
JOIN EMPLOYEE_LOOKUP ON Service.SERVICE_NAME = EMPLOYEE_LOOKUP.EMPLOYEE_CURR_SERVICE

WHERE Service.SERVICE_NAME like @serviceRepairs
AND Service.SERVICE_NAME like @trailerRepairs
