USE CoogTechSolutions

DECLARE
@business BIT

SELECT 
Customer.CUSTOMER_ID AS 'Customer ID', 
Customer.C_LNAME AS 'Customer Last Name', 
Customer.C_FNAME AS 'Customer First Name', 
Customer.C_BUS_NAME AS 'Customer Business Name', 
Customer_Type.IS_BUSINESS AS 'Is Business'
SELECT @business = 1

FROM CUSTOMER
JOIN CUSTOMER_TYPE ON Customer.CUSTOMER_ID = Customer_Type.CUSTOMER_ID

WHERE Customer_Type.IS_BUSINESS = @business
