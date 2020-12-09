import json

courses = '{"name":"Rahul", "languages": [ "Java","Python"]}'
dict_course = json.loads(courses)
print(type(dict_course))

print(dict_course)

print(dict_course['name'])

print(dict_course['languages'])

list_languages = dict_course['languages']
print(list_languages[0])
print(list_languages[1])
