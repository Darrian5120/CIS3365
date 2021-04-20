Customer.C_LNAME AS 'Last Name',
STATE.STATE_NAME AS 'STATE',
CUSTOMER_VEHICLE.V_ID AS 'VIN',
MAKE.MAKE_NAME AS 'Make',
MODEL.MODEL_NAME AS 'Model',
VEHICLE.V_YEAR AS 'Year',
VEHICLE.V_LICENSE_PLATE AS 'License Plate'

FROM Customer
JOIN CUSTOMER_STATE
ON Customer.CUSTOMER_ID = CUSTOMER_STATE.CUSTOMER_ID
JOIN STATE
ON CUSTOMER_STATE.STATE_ID = STATE.STATE_ID
JOIN CUSTOMER_VEHICLE
ON Customer.CUSTOMER_ID = CUSTOMER_VEHICLE.CUSTOMER_ID
JOIN VEHICLE
ON CUSTOMER_VEHICLE.V_ID = VEHICLE.V_ID
JOIN MAKE
ON VEHICLE.MAKE_ID = MAKE.MAKE_ID
JOIN MODEL
ON VEHICLE.MODEL_ID = MODEL.MODEL_ID

ORDER BY STATE.STATE_ID, Customer.CUSTOMER_ID


