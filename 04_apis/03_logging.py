# 03 - logging
# made with `cp 02_errors.py 03_logging.py`
# to rename, `mv 03_loggings.py`

import httpx
import json
import logging # another built-in python package

logging.basicConfig(filename='events.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# options for levels are
#     DEBUG — most verbose
#     INFO
#     WARNING
#     ERROR
#     CRITICAL
# when we make a log, we decide what kind of level it is

# can log to Datadog, which you can get a connection string for
# can also log to Kafka

USER = "schacon"
URL = "https://api.github.com/users/{user}/events/public"

try:
    response = httpx.get(URL.format(user=USER))
    response.raise_for_status()
    data = response.json()
    
    for item in data:
        print(item['repo']['name'], '—', item['type'])

    logging.info(f'fetched {len(data)} events for {USER}')

except httpx.HTTPError as e:
    logging.error(f'error fetching events for {USER}: {e}')
