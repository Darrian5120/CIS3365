USE CoogTechSolutions

SELECT VEHICLE.V_VIN AS 'VIN', VEHICLE.V_YEAR AS 'Year', MAKE.MAKE_NAME AS 'Make', 
MODEL.MODEL_NAME AS 'Model', SERVICE.SERVICE_TYPE AS 'Service', SUPPLIER.SUPPLIER_NAME AS 'Supplier',
PART.PART_NAME AS 'Part' /*COUNT(PART.PART_NAME) AS '*/

FROM VEHICLE
JOIN VEHICLE_SERVICE
ON VEHICLE.V_ID = VEHICLE_SERVICE.V_ID
JOIN MAKE
ON VEHICLE.MAKE_ID = MAKE.MAKE_ID
JOIN MODEL
ON VEHICLE.MODEL_ID = MODEL.MODEL_ID
JOIN SERVICE
ON VEHICLE_SERVICE.SERVICE_ID = SERVICE.SERVICE_ID
JOIN SERVICE_LINE
ON SERVICE.SERVICE_ID = SERVICE_LINE.SERVICE_ID
JOIN SERVICE_LINE_PART
ON  SERVICE_LINE.SERVICE_ORDER_ID = SERVICE_LINE_PART.SERVICE_ORDER_ID AND SERVICE_LINE.SERVICE_ID = SERVICE_LINE_PART.SERVICE_ID
JOIN PART
ON SERVICE_LINE_PART.PART_ID = PART.PART_ID
JOIN SUPPLIER_PART
ON PART.PART_ID = SUPPLIER_PART.PART_ID
JOIN SUPPLIER
ON SUPPLIER_PART.SUPPLIER_ID = SUPPLIER.SUPPLIER_ID

GROUP BY VEHICLE.V_VIN, VEHICLE.V_YEAR, MAKE.MAKE_NAME, MODEL.MODEL_NAME, SERVICE.SERVICE_TYPE, SUPPLIER.SUPPLIER_NAME,PART.PART_NAME
ORDER BY SERVICE.SERVICE_TYPE, PART.PART_NAME;