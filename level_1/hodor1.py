#!/usr/bin/python3
"""level 1"""
import requests


currentvote = 0
passed = 0
failed = 0
url = "http://158.69.76.135/level1.php"

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

response = requests.get(url)
"""
print(response.cookies)
"""
key = response.cookies["HoldTheDoor"]
mydata = {'id': ID, "holdthedoor": "Submit", "key": key}
cookie = {"HoldTheDoor": key}
"""
txt = response.text.split()
txtid = txt.index(str(ID))
"""
for i in range(currentvote, votes):
    response = requests.post(url, mydata, cookies=cookie)
    if response.status_code == 200:
            passed += 1
            print("{} Passed".format(passed), end='\r')
    else:
            failed += 1
            print("{} Failed".format(failed), end='\r')

print()
print("Passed {}, Failed {}".format(passed, failed))
