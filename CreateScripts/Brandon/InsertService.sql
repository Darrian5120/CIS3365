“SET IDENTITY_INSERT CoogTechSolutions.[dbo].[Service] OFF;  
INSERT INTO CoogTechSolutions.[dbo].[Service] ([SERVICE_ID],[SERVICE_TYPE],[V_ID][DATE_IN],[DATE_OUT],[SERVICE_RATE],[MATERIALS_REQUIRED]) 
VALUES (?,?,?,?) 
“,row.[SERVICE_ID],row.[SERVICE_TYPE],row.[V_ID],row.[DATE_IN],row.[DATE_OUT],row.[SERVICE_RATE],row.[MATERIALS_REQUIRED]) 
