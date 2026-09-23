# 01 - The happy path. No error handling at all.
# Break it: misspell USER, or turn off Wi-Fi, and read the traceback.

import httpx # need to install it with pip or smth like that
import json # always in python but still need to import
# if you name a file the same thing as a package, then python imports that file, not the package

USER = "schacon"
URL = "https://api.github.com/users/{user}/events/public"

response = httpx.get(URL.format(user=USER))

data = response.json()
# print(json.dumps(data, indent=2))

for item in data:
    print(item['repo']['name'], '—', item['type']) # this isn't really logging, it's just showing it to you the developer

# turn off your wifi, and then run that script again . . barf
# that's a technical term btw, barf