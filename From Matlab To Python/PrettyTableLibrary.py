from prettytable import PrettyTable

myTable = PrettyTable(["STT", "Name"])

myTable.add_row(["1", "Phuoc"])

myTable.add_row(["2", "Ngan"])

myTable.add_row(["3", "Hoang"])

myTable.add_row(["4", "Duy"])

print(myTable)
