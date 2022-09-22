# ML-Inference-Invoke
Back end tool chain to get inputs from front end and invoke ML inference 

## Prerequisites 
install functions core tool - https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Cwindows%2Ccsharp%2Cportal%2Cbash
install visual studio code - https://code.visualstudio.com/download#
install python - https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe

## Set up infrastructure

  unzip ARM-Template-HackathonRG.zip
  
  use az cli or azure portal to deploy the required resource
  
 Note: Above script creates the following services 
  - Storage account to store the jpg file uploaded from the frontend
  - Service Bus Queue to store the play load with metadata related to the uploaded files
  - Function to invole the ML infeence when the meta data related to the uploaded files is received on Service Bus queue


## Deploy function code 

  unzip AzFunctoniServiceBusTrigger.zip
  
  deploy the azure service bus trigger to invoke the ML inference when a payload from front end is receive on Service Bus queue
