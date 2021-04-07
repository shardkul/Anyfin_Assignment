# Anyfin_Assignment

------------------------------------------------------------------------------------------------
Task 1
------------------------------------------------------------------------------------------------


------------------------------------------------------------------------------------------------
Task 2
------------------------------------------------------------------------------------------------



------------------------------------------------------------------------------------------------
Task 3
------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------
Instructions for task 4 & 5 to deploys dags:
------------------------------------------------------------------------------------------------
Please copy all the following contents of dags folder to <container_id>:/usr/local/airflow/dags

1. key folder - contains public key for encryption
2. sql folder - contains queries used in dags for task 4 and 5
3. task_4_5_dag.py file

------------------------------------------------------------------------------------------------
Task 4
------------------------------------------------------------------------------------------------



------------------------------------------------------------------------------------------------
Task 5
------------------------------------------------------------------------------------------------
I had an option of doing this task in two ways, i.e. using symmetric encryption or using asymmetric encryption.
Because asymmetric encrytion is more secure, I have used the same for email column as required in task 5. 
Unlike symmetric encrytion where encryption and decryption can be done using same key, asymmetric encryption encrypts and decrypts
the data using two separate yet mathematically-connected cryptographic keys. I achieved this using PGP_PUB_ENCRYPT 
and PGP_PUB_DECRYPT functions from pgcrytpo extension in postgres.

For assignment purpose I generated the key pair (public/private) on my end. Ideally it should be generated by the 
client/data owner and then use that public key to encrypt the data, so that it could be decrypted using the private key they already have.
This ways it would be more secure and one need not risk the security by sending the same over mail.


Steps to decrypt the encrypted email.

1. Open the decryption_query.sql.
2. Open the secret.key sent over another email.
2. Replace the <private_key> place holder in sql with secret.key file contents and execute.
