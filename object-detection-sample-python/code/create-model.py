import requests, os, json

url = "https://app.nanonets.com/api/v2/ObjectDetection/Model/"
api_key = 'oyNfoBJz_VLPU29E7mFOtTQhojj4SnDm'

payload = "{\"categories\" : [\"TieFighter\", \"MillenniumFalcon\"]}"
headers = {'Content-Type': "application/json",}

response = requests.request("POST", url, headers=headers, auth=requests.auth.HTTPBasicAuth(api_key, ''), data=payload)

# print(api_key)
# print(json.loads(response.text))

model_id = json.loads(response.text)["model_id"]

print("NEXT RUN: export NANONETS_MODEL_ID=" + model_id)
print("THEN RUN: python ./code/upload-training.py")