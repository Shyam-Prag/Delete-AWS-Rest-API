#```

import json
import boto3 
import time

def main():
    client = boto3.client('apigateway')
    response = client.get_rest_apis()
    api_ids = []
    list_of_deleted_rest_apis = []
    list_of_items = response['items']
    
    for api_id in list_of_items:
        a_single_api_id = api_id['id']
        api_ids.append(a_single_api_id)

    print(api_ids)    

    for delete_api in api_ids:
        print(delete_api)
        if delete_api in ('xxxxxxxx', 'xxxxxxxx', 'xxxxxxxx','xxxxxxxx','xxxxxxxx'): #enter a list of API ID's which you DO NOT want to delete
            print(f'doing nothing.. not deleting {delete_api}')
        
        else:    
            print('sleeping 35 seconds')    #sleeping 35 seconds due to 30 second TPS limit.
            time.sleep(35)
            client.delete_rest_api(restApiId = delete_api)
            list_of_deleted_rest_apis.append(delete_api)
            print(f'deleted api -> {delete_api}')
            
    return list_of_deleted_rest_apis

main()
#```
