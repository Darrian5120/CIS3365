--Long Term Customers --
USE ct

SELECT 
Customer.CUSTOMER_ID AS "ID",
Customer.C_FNAME AS "First Name",
Customer.C_LNAME AS "Last Name",
CUSTOMER_STATUS.ACTIVE AS "Customer Type",
CUSTOMER_VEHICLE.V_VIN AS "VIN #",
VEHICLE.V_MAKE AS "Make",
VEHICLE.V_MODEL AS "Model",
SERVICE_ORDER.ORDER_DATE AS "First Time Customer Date"

FROM Customer 
JOIN CUSTOMER_STATUS
ON Customer.CUSTOMER_ID = CUSTOMER_STATUS.CUSTOMER_ID
JOIN CUSTOMER_VEHICLE
ON Customer.CUSTOMER_ID = CUSTOMER_VEHICLE.CUSTOMER_ID
JOIN VEHICLE
ON CUSTOMER_VEHICLE.V_VIN = VEHICLE.V_VIN
JOIN CUSTOMER_ORDER
ON Customer.CUSTOMER_ID = CUSTOMER_ORDER.CUSTOMER_ID
JOIN SERVICE_ORDER
ON CUSTOMER_ORDER.SERVICE_ORDER_ID = SERVICE_ORDER.SERVICE_ORDER_ID

WHERE (CUSTOMER_STATUS.C_ACTIVE= 1 OR CUSTOMER_STATUS.C_ACTIVE= 3) AND SERVICE_ORDER.ORDER_DATE < DATEADD(YEAR, -1, GETDATE());
