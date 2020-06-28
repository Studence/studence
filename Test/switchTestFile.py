from Utitlty.CSVUtility import CSVUtility

csvutility = CSVUtility()
row = {"hello", "hi"}
csvObj = csvutility.createCSVFile("demo")
print(csvutility.writeFile(csvObj, row))
