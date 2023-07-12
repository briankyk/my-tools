import sys
import csv
import json

filePath = sys.argv 
csvFilePath = filePath[1]
jsonFilePath = filePath[2]

def csv_to_json(csvfilePath, jsonFilePath):
    jsonArray=[]

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            jsonArray.append(row)
    print(csvReader)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


if __name__ == '__main__':
    csv_to_json(csvFilePath, jsonFilePath)
