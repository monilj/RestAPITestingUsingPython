import requests

cookie = {'visit-month': 'Febuary'}
# requests.get("https://rahulshettyacademy.com/", cookies=cookie)


se = requests.session()
se.cookies.update(cookie)
res= se.get("https://httpbin.org/cookies")
# res= requests.get("https://httpbin.org/cookies",cookies=cookie)
res = se.get("https://httpbin.org/cookies", cookies={'visit-year': '2020'})

print(res.text)