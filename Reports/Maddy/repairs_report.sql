USE CoogTechSolutions

DECLARE 
@serviceRepairs varchar(7)
@trailerRepairs varchar(15)

SELECT Service.SERVICE_ID, Service.SERVICE_NAME
SELECT @serviceRepairs = 'Repairs'

WHERE Service.SERVICE_NAME like @serviceRepairs
AND Service.SERVICE_NAME like @trailerRepairs
