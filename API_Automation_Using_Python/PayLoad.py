from util.configurations import getQuery


def addBookPayLoad():
    body = {
        "name": "Learn Appium Automation with Java",
        "isbn": "bwd",
        "aisle": "327",
        "author": "John foe"
    }
    return body


def buildPayLoadFromDb(query):
    addBody = {}
    tp = getQuery(query)
    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody
