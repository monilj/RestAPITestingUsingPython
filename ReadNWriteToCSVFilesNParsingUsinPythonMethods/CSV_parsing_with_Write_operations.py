import csv

with open(
        r'C:\Users\monil.joshi\Documents\monilj\pycharmprojects\RestAPITestingUsingPython\util\Loanapp.csv',
        'a')as csvW:
    writeToF = csv.writer(csvW)
    writeToF.writerow(['Bob', 'Rejected'])
