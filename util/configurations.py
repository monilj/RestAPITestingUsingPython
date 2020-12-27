import configparser


def getConfig():
    config =configparser.ConfigParser()
    config.read('util/properties.ini')
    return config