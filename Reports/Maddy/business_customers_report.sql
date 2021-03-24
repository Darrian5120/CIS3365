USE CoogTechSolutions

DECLARE
@business BIT

SELECT Customer.CUSTOMER_ID, Customer.C_LNAME, Customer.C_FNAME, Customer.C_BUS_NAME, Customer_Type.IS_BUSINESS
SELECT @business = 1

FROM CUSTOMER
JOIN CUSTOMER_TYPE ON Customer.CUSTOMER_ID = Customer_Type.CUSTOMER_ID

WHERE Customer_Type.IS_BUSINESS = @business
