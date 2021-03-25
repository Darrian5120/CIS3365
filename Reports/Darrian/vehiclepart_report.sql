USE CoogTechSolutions

SELECT VEHICLE_SERVICE.V_VIN AS "VIN", VEHICLE.V_YEAR AS "Year", VEHICLE.V_MAKE AS "Make", 
VEHICLE.V_MODEL AS "Model", SUPPLIER.SUPPLIER_NAME AS "Supplier", PART.PART_NAME AS "Part"

FROM VEHICLE
JOIN VEHICLE_SERVICE
ON VEHICLE.V_VIN = VEHICLE_SERVICE.V_VIN
JOIN SERVICE
ON VEHICLE_SERVICE.SERVICE_ID = SERVICE.SERVICE_ID
JOIN SERVICE_LINE
ON SERVICE.SERVICE_ID = SERVICE_LINE.SERVICE_ID
JOIN SERVICE_LINE_PART
ON  SERVICE_LINE.SERVICE_LINE_ID = SERVICE_LINE_PART.SERVICE_LINE_ID
JOIN PART
ON SERVICE_LINE_PART.PART_ID = PART.PART_ID
JOIN SUPPLIER_PART
ON PART.PART_ID = SUPPLIER_PART.PART_ID
JOIN SUPPLIER
ON SUPPLIER_PART.SUPPLIER_ID = SUPPLIER.SUPPLIER_ID

ORDER BY VEHICLE.V_VIN;