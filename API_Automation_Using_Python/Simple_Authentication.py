import requests

url = "https://api.github.com/user"
git_response = requests.get(url, auth=('monilj', 'password'))
print(git_response.status_code)

# for SSL
git_response = requests.get(url, verify=False, auth=('monilj', 'password'))
