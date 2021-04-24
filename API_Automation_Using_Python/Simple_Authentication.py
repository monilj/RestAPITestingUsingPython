import requests

password = 'mmmmmm'

ses = requests.session()
ses.auth = auth = ('monilj', password)

url = "https://api.github.com/user"
# git_response = requests.get(url, auth=('monilj', password))
git_response = ses.get(url)
# print(git_response.status_code)

url_2 = "https://api.github.com/user/get/user/repo"
# git_response3 = requests.get(url_2, auth=('monilj', password))
git_response3 = ses.get(url_2)
# for SSL
# git_response = requests.get(url, verify=False, auth=('monilj', 'password'))
