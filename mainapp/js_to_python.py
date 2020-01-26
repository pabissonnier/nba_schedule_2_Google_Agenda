"""import js2py

context = js2py.EvalJs({'python_sum': sum})
js_code = static/mainapp/js/googleapi.js
context.execute(js_code)
print(context.profile)"""

import re

js = open("static/mainapp/js/googleapi.js", "r").readlines()

matcher_rex = re.compile(r'^var\s+(?P<varname>\w+)\s+=\s+"(?P<varvalue>[\w\s]+)";?$')
for line in js:
    matches = matcher_rex.match(line)
    if matches:
        name, value = matches.groups()
        print (name, value)
