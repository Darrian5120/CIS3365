CREATE TABLE PAYMENT (
    C_ID int NOT NULL PRIMARY KEY,
    AMT_PAID float NOT NULL,
    FOREIGN KEY (C_ID) REFERENCES CUSTOMER(C_ID)
);