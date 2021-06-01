import csv

with open(
        r'C:\Users\monil.joshi\Documents\monilj\pycharmprojects\RestAPITestingUsingPython\util\Loanapp.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    names = []
    status = []
    for row in csvReader:
        names.append(row[0])
        status.append(row[1])
print(names)
print(status)

index = names.index('Sim')
print(status[index])

with open(
        r'C:\Users\monil.joshi\Documents\monilj\pycharmprojects\RestAPITestingUsingPython\util\Loanapp.csv',
        'a') as csvW:
    writeToF = csv.writer(csvW)
    newo = ["Gon", "Rejected"]
    writeToF.writerow(newo)