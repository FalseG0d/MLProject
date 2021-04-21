import requests, os

model_id = 'fcc82e2d-1a47-457d-b0d5-41e35dc7026d'
api_key = 'oyNfoBJz_VLPU29E7mFOtTQhojj4SnDm'

url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/' + model_id + '/Train/'

querystring = {'modelId': model_id}

response = requests.request('POST', url, auth=requests.auth.HTTPBasicAuth(api_key, ''), params=querystring)

print(response.text)

print("\n\nNEXT RUN: python ./code/model-state.py")