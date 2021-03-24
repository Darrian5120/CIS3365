USE CoogTechSolutions

DECLARE
@minimumCost float(8)

SELECT @minimumCost = 1
SELECT
Service_Line.SERVICE_LINE_ID AS 'Service Line ID',
Service_Line.LINE_COST as 'Cost'

FROM SERVICE_LINE
LEFT JOIN SERVICE ON SERVICE_LINE.SERVICE_ID = SERVICE.SERVICE_ID AND SERVICE_LINE.LINE_COST = SERVICE.COST
LEFT JOIN INVOICE ON SERVICE_LINE.LINE_COST = INVOICE.TOTAL_COST
JOIN SERVICE_LINE_PART ON SERVICE_LINE.SERVICE_LINE_ID = SERVICE_LINE_PART.SERVICE_LINE_ID
JOIN SERVICE_LINE_STATUS ON SERVICE_LINE.SERVICE_LINE_ID = SERVICE_LINE_STATUS.SERVICE_LINE_ID

WHERE SERVICE_LINE.LINE_COST >= @minimumCost

ORDER BY SERVICE_LINE.LINE_COST;
