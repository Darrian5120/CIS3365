Bulk INSERT Employee
	FROM ''
	WITH (
			FIRSTROW =2,
				FIELDTERMINATOR = '|',
				ROWTERMINATOR = '\n',
				MAXERRORS = 1
		);