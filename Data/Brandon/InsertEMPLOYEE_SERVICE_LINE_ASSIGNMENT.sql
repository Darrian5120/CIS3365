Bulk INSERT EMPLOYEE_SERVICE_LINE_ASSIGNMENT
	FROM ''
	WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);