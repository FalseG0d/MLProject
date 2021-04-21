import requests, os, sys

model_id = 'fcc82e2d-1a47-457d-b0d5-41e35dc7026d'
api_key = 'oyNfoBJz_VLPU29E7mFOtTQhojj4SnDm'

image_path = sys.argv[1]

url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/' + model_id + '/LabelFile/'

data = {'file': open(image_path, 'rb'),    'modelId': ('', model_id)}

response = requests.post(url, auth=requests.auth.HTTPBasicAuth(api_key, ''), files=data)

print(response.text)