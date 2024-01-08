# Delete-AWS-Rest-API
Problem: API Gateway has the default quota of deleting REST API's which is set to 1 requests every 30 seconds per account. This can be very time consuming and annoying to sit in the console and manually delete each REST API.. The below python script allows you to delete all rest APIs using using the get_rest_apis boto3 API call and the delete_rest_apis API call to delete all REST API's within the account. 

