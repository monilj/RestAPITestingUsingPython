import requests

url= 'https://petstore.swagger.io/v2/pet/uploadFile/pet/9843217/uploadImage'
files = {'file': open('report.xls', 'rb')}

requests.post(url,files=files)

