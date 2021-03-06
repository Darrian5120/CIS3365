DECLARE
@minimumCost float(8)

SELECT @minimumCost = 1
SELECT
Invoice.SERVICE_ORDER_ID AS 'Service Order ID',
Invoice.INVOICE_DATE AS 'Invoice Date',
FORMAT(Invoice.TOTAL_COST, 'C2') AS 'Total Cost'

FROM INVOICE_PAYMENT
JOIN INVOICE ON INVOICE_PAYMENT.SERVICE_ORDER_ID = INVOICE.SERVICE_ORDER_ID AND INVOICE_PAYMENT.INVOICE_ID = INVOICE.INVOICE_ID
JOIN PAYMENT_STATUS ON INVOICE_PAYMENT.ACTIVE_ID = PAYMENT_STATUS.ACTIVE_ID
JOIN PAYMENT_REVENUE ON INVOICE_PAYMENT.SERVICE_ORDER_ID = PAYMENT_REVENUE.SERVICE_ORDER_ID
JOIN PAYMENT ON INVOICE_PAYMENT.PMT_ID = PAYMENT.PMT_ID


WHERE INVOICE.TOTAL_COST >= @minimumCost

GROUP BY Invoice.SERVICE_ORDER_ID,INVOICE.TOTAL_COST,INVOICE.INVOICE_DATE
ORDER BY INVOICE.TOTAL_COST;
