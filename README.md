# ML-Inference-Invoke
back end tool chain to get inputs from front end and invoke ML inference 

## Prerequsited
install functions core tool - https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Cwindows%2Ccsharp%2Cportal%2Cbash
install visual studio code - https://code.visualstudio.com/download#
install python - https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe

## Set up infrastructure for the following 
- Storage account to store the jpg file uploaded from the frontend
- Service Bus Queue to store the play load with metadata related to the uploaded files
-Function to invole the ML infeence when the meta data related to the uploaded files is received on Service Bus queue

unzip ARM-Template-HackathonRG
use az cli or azure portal to deploy the required resource
