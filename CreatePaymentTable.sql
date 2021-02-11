CREATE TABLE Payment (
    C_ID int not null,
    AMT_PAID float null,
    PRIMARY KEY (C_ID),
    FOREIGN KEY (C_ID) REFERENCES Customer(C_ID)
);