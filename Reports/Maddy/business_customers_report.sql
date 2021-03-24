USE CoogTechSolutions

DECLARE
@business BIT

SELECT @business = 1
SELECT 
Customer.CUSTOMER_ID AS 'Customer ID', 
Customer.C_LNAME AS 'Customer Last Name', 
Customer.C_FNAME AS 'Customer First Name', 
Customer.C_BUS_NAME AS 'Customer Business Name', 
Customer_Type.IS_BUSINESS AS 'Is Business',
Customer_Order.SERVICE_ORDER_ID AS 'Service Order ID',
Customer_Vehicle.V_VIN AS 'Vehicle Identification Number'

FROM CUSTOMER
JOIN CUSTOMER_TYPE ON Customer.CUSTOMER_ID = Customer_Type.CUSTOMER_ID
JOIN CUSTOMER_VEHICLE ON Customer.CUSTOMER_ID = Customer_Vehicle.CUSTOMER_ID
JOIN CUSTOMER_ORDER ON Customer.CUSTOMER_ID = Customer_Order.CUSTOMER_ID

WHERE Customer_Type.IS_BUSINESS = @business

ORDER BY Customer.CUSTOMER_ID;
