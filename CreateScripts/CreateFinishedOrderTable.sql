CREATE TABLE FINSHED_ORDER (
    ORDER_ID int NOT NULL PRIMARY KEY,
    DATE_START DATETIME NOT NULL,
    DATE_END DATETIME NOT NULL,
    Quality text,
    /*SERVICE_ID int FOREIGN KEY REFERENCES Service(SERVICE_ID)*/
);