import os, requests
from tqdm import tqdm

pathToAnnotations = './annotations/json'
pathToImages = './images'
model_id = 'fcc82e2d-1a47-457d-b0d5-41e35dc7026d'
api_key = 'oyNfoBJz_VLPU29E7mFOtTQhojj4SnDm'

for root, dirs, files in os.walk(pathToAnnotations, topdown=False):
    for name in tqdm(files):
        annotation = open(os.path.join(root, name), "r")
        filePath = os.path.join(root, name)
        imageName, ext = name.split(".")
        imagePath = os.path.join(pathToImages, imageName + '.jpg')
        jsonData = annotation.read()
        url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/' + model_id + '/UploadFile/'
        data = {'file' :open(imagePath, 'rb'),  'data' :('', '[{"filename":"' + imageName+".jpg" + '", "object": '+ jsonData+'}]'),   'modelId' :('', model_id)}       
        response = requests.post(url, auth=requests.auth.HTTPBasicAuth(api_key, ''), files=data)
        if response.status_code > 250 or response.status_code<200:
            print(response.text), response.status_code

print("\n\n\nNEXT RUN: python ./code/train-model.py")