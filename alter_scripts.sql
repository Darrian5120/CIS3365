USE CoogTechSolutions
-------------------------Darrian-----------------------------------------------------
--Alter Payment--
ALTER TABLE PAYMENT
add CONSTRAINT CUSTOMER_ID_FK FOREIGN KEY (CUSTOMER_ID) REFERENCES Customer(CUSTOMER_ID);
--Alter Service Order Line--
ALTER TABLE SERVICE_ORDER_LINE
add CONSTRAINT ORDER_ID_FK FOREIGN KEY (ORDER_ID) REFERENCES FINSIHED_ORDER(ORDER_ID);
--Alter Finsihed Order--
ALTER TABLE FINSIHED_ORDER
add CONSTRAINT ORDER_ID_FK FOREIGN KEY (ORDER_ID) REFERENCES SERVICE_REQUEST(ORDER_ID);
---------------------------------------------------------------------------------------