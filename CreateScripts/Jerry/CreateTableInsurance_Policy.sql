CREATE TABLE INSURANCE_POLICY (
	POLICY_ID int(9) not null,
	INSURANCE_ID int(9) not null,
	V_VIN varchar(17) not null,
	COVERAGE_COST int(9),
	PRIMARY KEY (INSURANCE_ID)
);