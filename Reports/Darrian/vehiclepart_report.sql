USE CoogTechSolutions

SELECT VEHICLE_SERVICE.V_VIN AS "VIN", VEHICLE.YEAR, VEHICLE.MAKE, VEHICLE.MODEL, SUPPLIER.SUPPLIER_NAME, SUPPLIER_PART.PART_NAME
FROM VEHICLE
JOIN VEHICLE_SERVICE
ON VEHICLE.V_VIN = VEHICLE_SERVICE.V_VIN
JOIN SERVICE
ON VEHICLE_SERVICE.SERVICE_ID = SERVICE.SERVICE_ID
JOIN SERVICE_ORDER
ON SERVICE.SERVICE_ID = SERVICE_ORDER.SERVICE_ID
JOIN SERVICE_LINE
ON SERVICE_ORDER.SERVICE_ORDER_ID = SERVICE_LINE.SERVICE_ORDER_ID
JOIN SERVICE_LINE_PART
ON  SERVICE_LINE_PART.PART_ID = PART.PART_ID
JOIN PART
ON SUPPLIER_PART.PART_ID = PART.PART_ID
JOIN SUPPLIER
ON SUPPLIER_PART.SUPPLIER_ID = SUPPLIER.SUPPLIER_ID
ORDER BY VEHICLE.V_VIN;