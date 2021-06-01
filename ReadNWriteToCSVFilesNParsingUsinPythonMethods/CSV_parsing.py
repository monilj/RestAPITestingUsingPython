import csv

with open(
        r'C:\Users\monil.joshi\Documents\monilj\pycharmprojects\RestAPITestingUsingPython\util\Loanapp.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    # print(list(csvReader))
    names = []
    status = []
    for row in csvReader:
        names.append(row[0])
        status.append(row[1])
    print(names)
    print(status)
