import json

with open("C:\\Users\\monil.joshi\\Documents\\monilj\\pycharmprojects\\RestAPITestingUsingPython\\JsonFiles\\courses.json") as f:
    data = json.load(f)
    print(data['courses'])
    print(data['courses'][1])
    print(data['courses'][1]['title'])
    print("============ Print Website ============")
    print(data['dashboard'])
    print(data['dashboard']['website'])

