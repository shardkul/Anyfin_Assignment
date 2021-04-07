-------------------------------------------------------------------------------
-- B. CAN YOU PROVIDE THE APPLICATION_IDS FOR THE FIRST APPLICATION OF EACH CUSTOMER

with QRY1 as (
select *,
rank() over (partition by customer_id order by created_at,id) as rnk
from applications
where customer_id is not null
)

select distinct ID from QRY1 where rnk = 1
