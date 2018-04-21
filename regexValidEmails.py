# program to find valid email addresses

import re

emails = ["john@example.com", "pythonl985ist@python.org", "??%4ly@email.com",'abx@11.com']

pattern = re.compile("^[a-zA-Z0-9.?]+@\w+.\w+")

for line in emails:
    match = re.search(pattern,line)
    if(match):
        print(match.group(0))

