import requests

cookie = {'visit-month': 'Febuary'}
rep = requests.get("https://rahulshettyacademy.com/",allow_redirects= False, cookies=cookie, timeout=4)
print(rep.history)
print(rep.status_code)

se = requests.session()
se.cookies.update(cookie)
# res = se.get("https://httpbin.org/cookies")
# res= requests.get("https://httpbin.org/cookies",cookies=cookie)
# response = se.get("https://httpbin.org/cookies", cookies={'visit-year': '2020'})
# print(response.history)
# print(res.text)
