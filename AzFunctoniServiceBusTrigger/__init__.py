import logging

import azure.functions as func
import requests
import json

inference_endpoint = 'https://mybgfn.azurewebsites.net/api/HttpTrigger1?code=IaYZreYjwUsW3lcd4sFGhXdxGAlXYPtpiiKKIL7lGX4jDcoNB/aNkQ=='
#inference_endpoint = 'https://reqbin.com/echo/post/json'

# Inference_endpoint
#inference_endpoint = 'https://edpmle.pdakstrn2.eastus2.az.cloud.geico.net:443/api/v1/service/automl-image-test2/score'

# Request headers.
headers = {
    'content-type': 'application/json',
    'api_key': 'bYvVJqiGOmGKbRmeu4u79xzeSWh4cOdr',
}

def main(msg: func.ServiceBusMessage):
    logging.info('Python ServiceBus queue trigger processed message: %s',
                 msg.get_body().decode('utf-8'))

    #inference_payload = dict(msg.get_body().decode('utf-8'))

    #response = requests.post(inference_endpoint, json=json.loads(inference_payload))
    #response = requests.post(inference_endpoint, json = dict(msg.get_body().decode('utf-8')))
    #response.raise_for_status()
    #logging.info(json.loads(inference_payload))
    logging.info(str(json.loads(msg.get_body().decode('utf-8'))))
    response = requests.post(inference_endpoint, headers=headers, json=json.loads(msg.get_body().decode('utf-8')))
    response.raise_for_status()

