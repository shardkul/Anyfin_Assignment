-------------------------------------------------------------------------------
-- A. CAN YOU PROVIDE THE CUSTOMER_ID OF ALL CUSTOMERS WITH MAX DPD > 10 DAYS?

SELECT CUSTOMER_ID FROM CYCLES
GROUP BY CUSTOMER_ID
HAVING MAX(DPD) > 10
