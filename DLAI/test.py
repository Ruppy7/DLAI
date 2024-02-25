import requests

url = 'http://127.0.0.1:8000/api/upload/'

file_path = './Samples/sample1.pdf'

with open(file_path, 'rb') as file:
    files = {'file': file}
    response = requests.post(url, files=files)

# Print the response
print(response.status_code)
print(response.json()) 