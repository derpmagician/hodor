#!/usr/bin/python3
"""level 0"""
import requests


currentvote = 0
passed = 0
failed = 0
url = "http://158.69.76.135/level0.php"

try:
    ID = int(input("Input ID number: "))
except ValueError:
    print("PLEASE: input an integer")
    exit(1)
try:
    votes = int(input("Input number of votes: "))
except ValueError:
    print("PLEASE: input an integer")
    exit(1)

mydata = {"id": ID, "holdthedoor": "Submit"}
response = requests.get(url)

for i in range(currentvote, votes):
    response = requests.post(url, mydata)
    if response.status_code == 200:
            passed += 1
            print("{} Passed".format(passed), end='\r')
    else:
            failed += 1
            print("{} Failed".format(failed), end='\r')

print()
print("Passed {}, Failed {}".format(passed, failed))
