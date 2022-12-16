import os
import io
import boto3
import json
import numpy as np
import csv
import urllib.request
from PIL import Image
 

runtime= boto3.client('runtime.sagemaker')
client = boto3.client('sagemaker')
 
def lambda_handler(event, context):

    print(event)
    print(type(event))
    event = str(event)
    event = event.replace("\'", "\"")

    print("first string")
    print(event)
    print(type(event))
    
    payload = json.loads(event)
    payload = str(payload)
    payload = payload.replace("\'", "\"")
    print("COnverted")
    print("payload after loads")
    print(payload)
    print(type(payload))
    

   
    response = runtime.invoke_endpoint(EndpointName="pytorchinference1", 
                                       ContentType='application/json', 
                                       Body=payload)
    result = response['Body'].read()
    result = json.loads(result)
    print('predicted:', result[0]['prediction'])
    
    output = "Image predicted: "+result[0]['prediction']
    return output