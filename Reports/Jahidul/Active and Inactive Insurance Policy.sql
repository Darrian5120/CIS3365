SELECT CV.Customer_id AS "Customer id", V.V_VIN AS 'Vehicle VIN',
IP.Policy_name as 'Policy name',
Case when VP.EXPIRATION_DATE<GETDATE() then 'Inactive' else 'Active' end As 'Policy Status',
VP.EXPIRATION_DATE As 'Expire in this day'
FROM Vehicle V
JOIN Vehicle_STATUS VS
ON V.ACTIVE_ID = VS.ACTIVE_ID
JOIN CUSTOMER_Vehicle CV
ON CV.V_ID = V.V_ID
JOIN Policy VP
ON V.V_ID = VP.V_ID
JOIN INSURANCE_POLICY IP
ON VP.POLICY_ID= IP.POLICY_ID
WHERE VS.ACTIVE_ID in (1,2)
ORDER BY 4;
