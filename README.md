# Delete-AWS-Rest-API
Problem: API Gateway has the default quota of deleting REST API's which is set to 1 requests every 30 seconds per account. This can be very time consuming and annoying to sit in the console and manually delete each REST API.. The below script allows you to delete all rest APIs using a shell script which looks over all API Gateway REST API's using the get-rest-apis command and deletes each one.

How to run: On MacOs, copy and paste the below scipt in your terminal (.zsh) and run the command, substituting the AWS Region with the region of your choice. 

#shell script to delete all AWS REST API's within a region.

for rest_api_id in $(aws apigateway get-rest-apis --region eu-west-1 --query 'items[*].id' --output text); do aws apigateway delete-rest-api --region eu-west-1 --rest-api-id $rest_api_id ; done
