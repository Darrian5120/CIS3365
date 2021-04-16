DECLARE
@business BIT

SELECT @business = 1
SELECT 
Customer.CUSTOMER_ID AS 'Customer ID', 
Customer.C_LNAME AS 'Customer Last Name', 
Customer.C_FNAME AS 'Customer First Name', 
Customer.C_BUSINESS_NAME AS 'Customer Business Name', 
Customer_Type.BUSINESS AS 'Business Customer',
Service_Order.SERVICE_ORDER_ID AS 'Service Order ID',
Customer_Status.ACTIVE_NAME as 'Active/Inactive Status'

FROM CUSTOMER
JOIN CUSTOMER_TYPE ON Customer.BUSINESS_ID = Customer_Type.BUSINESS_ID
JOIN CUSTOMER_VEHICLE ON Customer.CUSTOMER_ID = Customer_Vehicle.CUSTOMER_ID
JOIN SERVICE_ORDER ON Customer.CUSTOMER_ID = Service_Order.CUSTOMER_ID
JOIN CUSTOMER_STATUS ON Customer.ACTIVE_ID = CUSTOMER_STATUS.ACTIVE_ID

WHERE Customer_Type.BUSINESS_ID = @business

ORDER BY Customer.CUSTOMER_ID;