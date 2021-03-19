/*USE CoogTechSolutions*/
-------------------------Darrian-----------------------------------------------------
--Alter Service Line--
ALTER TABLE SERVICE_LINE
add CONSTRAINT SERVICE_ORDER_ID1_FK1 FOREIGN KEY (SERVICE_ORDER_ID) REFERENCES SERVICE_ORDER(SERVICE_ORDER_ID), --FIXME--
CONSTRAINT SERVICE_ID_FK2 FOREIGN KEY (SERVICE_ID) REFERENCES SERVICE_ORDER(SERVICE_ID), --FIXME--
CONSTRAINT ORDER_ID_FK1 FOREIGN KEY (ORDER_ID) REFERENCES CUSTOMER_ORDER(ORDER_ID);
/*CONSTRAINT SERVICE_ID_FK1 FOREIGN KEY (SERVICE_ID) REFERENCES SERVICE(SERVICE_ID);*/
--Alter Invoice Payment--
ALTER TABLE INVOICE_PAYMENT
add CONSTRAINT PMT_NUMBER_FK FOREIGN KEY (PMT_NUMBER) REFERENCES PAYMENT(PMT_NUMBER),
/* PMT_NUMBER_PK FOREIGN KEY (PMT_NUMBER) REFERENCES PAYMENT(PMT_NUMBER),*/
CONSTRAINT INVOICE_ID_FK2 FOREIGN KEY (INVOICE_ID) REFERENCES INVOICE(INVOICE_ID);

----------------------------Anthony-----------------------------------------------------
--Alter Invoice--
ALTER TABLE INVOICE
add CONSTRAINT CUSTOMER_ID_FK1 FOREIGN KEY (CUSTOMER_ID) REFERENCES Customer(CUSTOMER_ID);
ALTER TABLE SERVICE_ORDER_STATUS
add CONSTRAINT SERVICE_ORDER_ID_FK4 FOREIGN KEY (SERVICE_ORDER_ID) REFERENCES SERVICE_ORDER(SERVICE_ORDER_ID);

---------------------------Mustafa------------------------------------------------------
--CUSTOMER CONTACT INFO ALTER
ALTER TABLE CUSTOMER_CONTACT_INFO
add CONSTRAINT CUSTOMER_ID_FK2 FOREIGN KEY (CUSTOMER_ID) REFERENCES Customer(CUSTOMER_ID);
/*CONSTRAINT STATE_ID_FK FOREIGN KEY (STATE_ID) REFERENCES STATE(STATE_ID);*/
----CURRENT SERVICE ALTER 
ALTER TABLE SERVICE_LINE_STATUS
add CONSTRAINT SERVICE_LINE_ID_FK1 FOREIGN KEY (SERVICE_LINE_ID) REFERENCES SERVICE_LINE(SERVICE_LINE_ID);
ALTER TABLE VEHICLE_STATUS
add CONSTRAINT V_VIN_FK6 FOREIGN KEY (V_VIN) REFERENCES VEHICLE(V_VIN);

-------------------------jahidul----------------------------------------------------------------
--Alter Customer Order--
/*ALTER TABLE CUSTOMER_ORDER
add CONSTRAINT SERVICE_ORDER_ID_FK2 FOREIGN KEY (SERVICE_ORDER_ID) REFERENCES SERVICE_ORDER(SERVICE_ORDER_ID),
CONSTRAINT CUSTOMER_ID_FK4 FOREIGN KEY (CUSTOMER_ID) REFERENCES Customer(CUSTOMER_ID);*/
--Alter Customer Vehicle--
ALTER TABLE CUSTOMER_VEHICLE
add CONSTRAINT V_VIN_FK2 FOREIGN KEY (V_VIN) REFERENCES VEHICLE(V_VIN),
CONSTRAINT CUSTOMER_ID_FK5 FOREIGN KEY (CUSTOMER_ID) REFERENCES Customer(CUSTOMER_ID);
--Alter Vehicle Policy--
ALTER TABLE VEHICLE_POLICY
add CONSTRAINT POLICY_ID_FK1 FOREIGN KEY (POLICY_ID) REFERENCES INSURANCE_POLICY(POLICY_ID),
CONSTRAINT V_VIN_FK3 FOREIGN KEY (V_VIN) REFERENCES VEHICLE(V_VIN);
--Alter Company Insurance policy--
ALTER TABLE COMPANY_INSURANCE_POLICY
add CONSTRAINT POLICY_ID_FK2 FOREIGN KEY (POLICY_ID) REFERENCES INSURANCE_POLICY(POLICY_ID),
CONSTRAINT INSURANCE_ID_FK FOREIGN KEY (INSURANCE_ID) REFERENCES INSURANCE_COMPANY(INSURANCE_ID);

---------------------------Jerry---------------------------------------------------------------
ALTER TABLE SERVICE_STATUS
add CONSTRAINT SERVICE_ID_FK4 FOREIGN KEY (SERVICE_ID) REFERENCES SERVICE(SERVICE_ID);
---------------------------Kyle---------------------------------------------------------------
--Alter Customer Status--
ALTER TABLE CUSTOMER_STATUS
add CONSTRAINT CUSTOMER_ID_FK6 FOREIGN KEY (CUSTOMER_ID) REFERENCES Customer(CUSTOMER_ID);
--Alter Supplier Status--
ALTER TABLE SUPPLIER_STATUS
add CONSTRAINT SUPPLIER_ID_FK1 FOREIGN KEY (SUPPLIER_ID) REFERENCES SUPPLIER(SUPPLIER_ID);
--Alter Vehicle Service--
ALTER TABLE VEHICLE_SERVICE
add CONSTRAINT SERVICE_ID_FK2 FOREIGN KEY (SERVICE_ID) REFERENCES SERVICE(SERVICE_ID),
CONSTRAINT V_VIN_FK4 FOREIGN KEY (V_VIN) REFERENCES VEHICLE(V_VIN);
--------------------------------Brandon--------------------------------
--Alter Employee Service Line Assignment--
ALTER TABLE EMPLOYEE_SERVICE_LINE_ASSIGNMENT
add CONSTRAINT SERVICE_LINE_ID_FK FOREIGN KEY (SERVICE_LINE_ID) REFERENCES SERVICE_LINE(SERVICE_LINE_ID),
CONSTRAINT EMPLOYEE_ID_FK3 FOREIGN KEY (EMPLOYEE_ID) REFERENCES EMPLOYEE(EMPLOYEE_ID);
ALTER TABLE SERVICE_LINE_PART
add CONSTRAINT SERVICE_LINE_ID_FK2 FOREIGN KEY (SERVICE_LINE_ID) REFERENCES SERVICE_LINE(SERVICE_LINE_ID),
CONSTRAINT PART_ID_FK3 FOREIGN KEY (PART_ID) REFERENCES PART(PART_ID);
-----------------------------Maddy----------------------------------------------------------------
--Alter Employee Lookup--
/*ALTER TABLE SERVICE_ORDER
add CONSTRAINT SERVICE_ID1_FK FOREIGN KEY (SERVICE_ID1) REFERENCES SERVICE(SERVICE_ID);*/
ALTER TABLE EMPLOYEE_LOOKUP
add CONSTRAINT EMPLOYEE_ID_FK1 FOREIGN KEY (EMPLOYEE_ID) REFERENCES EMPLOYEE(EMPLOYEE_ID);
ALTER TABLE CUSTOMER_TYPE
add CONSTRAINT CUSTOMER_ID_FK3 FOREIGN KEY (CUSTOMER_ID) REFERENCES Customer(CUSTOMER_ID);
------------------------------Gian---------------------------------------------------
--ALter Vehicle Lookup--
ALTER TABLE VEHICLE_LOOKUP
add CONSTRAINT V_VIN_FK5 FOREIGN KEY (V_VIN) REFERENCES VEHICLE(V_VIN);
--ALter Supplier Lookup--
ALTER TABLE SUPPLIER_LOOKUP
add CONSTRAINT SUPPLIER_ID_FK3 FOREIGN KEY (SUPPLIER_ID) REFERENCES SUPPLIER(SUPPLIER_ID),
CONSTRAINT PART_ID_FK1 FOREIGN KEY (PART_ID) REFERENCES PART(PART_ID);
--Alter Customer State--
ALTER TABLE CUSTOMER_STATE
add CONSTRAINT STATE_ID_FK1 FOREIGN KEY (STATE_ID) REFERENCES STATE(STATE_ID),
CONSTRAINT CUSTOMER_ID_FK7 FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMER_CONTACT_INFO(CUSTOMER_ID);
---------------------------Zach---------------------------------------------------------
--Alter Supplier Part--
ALTER TABLE SUPPLIER_PART
add CONSTRAINT PART_ID_FK2 FOREIGN KEY (PART_ID) REFERENCES PART(PART_ID),
CONSTRAINT SUPPLIER_ID_FK4 FOREIGN KEY (SUPPLIER_ID) REFERENCES SUPPLIER(SUPPLIER_ID);
--Alter Employee Status--
ALTER TABLE EMPLOYEE_STATUS
add CONSTRAINT EMPLOYEE_ID_FK2 FOREIGN KEY (EMPLOYEE_ID) REFERENCES EMPLOYEE(EMPLOYEE_ID);
--Alter State Violation--
ALTER TABLE STATE_VIOLATION
add CONSTRAINT VIOLATION_ID_FK FOREIGN KEY (VIOLATION_ID) REFERENCES VIOLATION(VIOLATION_ID),
CONSTRAINT STATE_ID_FK2 FOREIGN KEY (STATE_ID) REFERENCES STATE(STATE_ID);

