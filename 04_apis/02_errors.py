# 02 - error /exception handling with try, except, finally
# made with `cp 01_plain.py 02_errors.py`

import httpx
import json

USER = "schaconxyz"
URL = "https://api.github.com/users/{user}/events/public"

try:
    response = httpx.get(URL.format(user=USER))
    response.raise_for_status() # immediately moves to the except if this is triggered
    data = response.json()
    
    for item in data:
        print(item['repo']['name'], '—', item['type'])

# httpx is newer than requests and has its own set of features
# requests does have something similar to HTTPError tho
except httpx.HTTPError as e:
    print(e)

# "word does the most shitty fucking thing called smart quotes" lol