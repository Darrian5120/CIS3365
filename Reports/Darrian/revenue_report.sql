USE CoogTechSolutions

SELECT Customer.CUSTOMER_ID AS "Customer ID", Customer.C_LNAME AS "Last Name", Customer.C_FNAME AS "First Name",
ACCOUNT_REVENUE.REVENUE_NAME AS "Revenue Name", ACCOUNT_REVENUE.REVENUE_VALUE AS "Revenue Value"

FROM CUSTOMER
JOIN INVOICE
ON Customer.CUSTOMER_ID = INVOICE.CUSTOMER_ID
JOIN INVOICE_PAYMENT
ON  INVOICE.INVOICE_ID = INVOICE_PAYMENT.INVOICE_ID
JOIN PAYMENT
ON INVOICE_PAYMENT.PMT_NUMBER = PAYMENT.PMT_NUMBER
JOIN PAYMENT_REVENUE
ON PAYMENT.PMT_NUMBER = PAYMENT_REVENUE.PMT_NUMBER
JOIN ACCOUNT_REVENUE
ON PAYMENT_REVENUE.REVENUE_ID = ACCOUNT_REVENUE.REVENUE_ID

ORDER BY INVOICE.INVOICE_DATE;