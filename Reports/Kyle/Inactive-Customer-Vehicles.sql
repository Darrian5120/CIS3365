SELECT
Customer.CUSTOMER_ID AS "Customer ID",
Customer.C_FNAME AS "First Name",
Customer.C_LNAME AS "Last Name",
CUSTOMER.ACTIVE_ID AS "Status",
CUSTOMER_VEHICLE.V_VIN AS "Vin",
VEHICLE.V_MAKE AS "Make",
VEHICLE.V_YEAR AS "Year",
VEHICLE.V_LISCENSE_PLATE AS "License Plate"

FROM Customer
JOIN CUSTOMER_VEHICLE
ON Customer.CUSTOMER_ID = CUSTOMER_VEHICLE.CUSTOMER_ID
JOIN VEHICLE
ON CUSTOMER_VEHICLE.V_VIN = VEHICLE.V_VIN

WHERE CUSTOMER.ACTIVE_ID = 2 OR CUSTOMER.ACTIVE_ID = 4

ORDER BY CUSTOMER.ACTIVE_ID, Customer.CUSTOMER_ID
