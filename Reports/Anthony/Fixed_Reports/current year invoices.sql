USE ct

SELECT 
INVOICE.INVOICE_ID AS 'Invoice ID',
FORMAT (INVOICE.TOTAL_COST, 'C') AS 'Total Cost',
FORMAT (INVOICE.AMT_OWED, 'C') AS 'Amount Owned',
INVOICE.INVOICE_DATE AS 'Date',
PAYMENT.PMT_TYPE AS 'Payment Type',
Customer.C_FNAME AS 'Customer First Name',
Customer.C_LNAME AS 'Customer Last Name',
Customer.C_PHONE AS 'Customer Phone Number',
VEHICLE.V_VIN AS 'VIN Worked On'

FROM INVOICE
JOIN INVOICE_PAYMENT
ON INVOICE.INVOICE_ID = INVOICE_PAYMENT.INVOICE_ID
JOIN PAYMENT
ON INVOICE_PAYMENT.PMT_ID = PAYMENT.PMT_ID
JOIN SERVICE_ORDER
ON INVOICE.SERVICE_ORDER_ID = SERVICE_ORDER.SERVICE_ORDER_ID
JOIN Customer
ON SERVICE_ORDER.CUSTOMER_ID = Customer.CUSTOMER_ID
JOIN CUSTOMER_VEHICLE
ON Customer.CUSTOMER_ID = CUSTOMER_VEHICLE.CUSTOMER_ID
JOIN VEHICLE
ON CUSTOMER_VEHICLE.V_ID = VEHICLE.V_ID

WHERE YEAR(INVOICE.INVOICE_DATE) = YEAR(GETDATE()) AND INVOICE.INVOICE_DATE < GETDATE()

ORDER BY INVOICE.INVOICE_DATE;
