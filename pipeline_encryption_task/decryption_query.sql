select 
CUSTOMER_ID,
PGP_PUB_DECRYPT(ENCRYPTED_EMAIL,DEARMOR('<private_key>')) as DECRYPTED_EMAIL
from CUSTOMER_EMAIL