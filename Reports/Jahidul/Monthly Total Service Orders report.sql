SELECT
count(SERVICE_ORDER.SERVICE_ORDER_ID) AS 'Total Orders',
FORMAT(SERVICE_ORDER.ORDER_DATE,'MM/yyyy') As 'Month and Year',
Sum(INVOICE.TOTAL_COST) AS 'Cost',
INVOICE_STATUS.ACTIVE_NAME AS 'Invoice Status',
SERVICE_ORDER_STATUS.ACTIVE_NAME As 'Progress Status'
From SERVICE_ORDER
Join INVOICE
On SERVICE_ORDER.SERVICE_ORDER_ID = INVOICE.SERVICE_ORDER_ID
Join SERVICE_ORDER_STATUS
On SERVICE_ORDER.ACTIVE_ID = SERVICE_ORDER_STATUS.ACTIVE_ID
Join INVOICE_STATUS
On INVOICE_STATUS.ACTIVE_ID = INVOICE.ACTIVE_ID
Where INVOICE_STATUS.ACTIVE_NAME='Fully paid'
group by INVOICE_STATUS.ACTIVE_NAME, FORMAT(SERVICE_ORDER.ORDER_DATE,'MM/yyyy'),SERVICE_ORDER_STATUS.ACTIVE_NAME
order by 2
