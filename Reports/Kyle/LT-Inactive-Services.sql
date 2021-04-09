SELECT
SERVICE.SERVICE_ID AS "Service ID",
SERVICE.SERVICE_TYPE AS "Service Type",
SERVICE.DATE_START AS "Start Date",
SERVICE.DATE_END AS "End Date",
SERVICE.COST AS "Cost",
SERVICE.ACTIVE_ID AS "Status"

FROM SERVICE
JOIN SERVICE_STATUS
ON SERVICE.SERVICE_ID = SERVICE_STATUS.SERVICE_ID

WHERE SERVICE_STATUS.ACTIVE_ID = 1 AND SERVICE.DATE_END < DATEADD(YEAR, -1, GETDATE())

ORDER BY SERVICE.SERVICE_ID
