import json

with open(
        "C:\\Users\\monil.joshi\\Documents\\monilj\\pycharmprojects\\RestAPITestingUsingPython\\JsonFiles\\courses.json") as f:
    dict_json1 = json.load(f)

with open(
        "C:\\Users\\monil.joshi\\Documents\\monilj\\pycharmprojects\\RestAPITestingUsingPython\\JsonFiles\\coursesNew.json") as fi:
    dict_json2 = json.load(fi)
    print(dict_json1 == dict_json2)
