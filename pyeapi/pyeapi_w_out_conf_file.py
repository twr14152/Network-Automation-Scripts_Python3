#Got a question asked of me if there was a way to configure pyeapi without the config file.

import pyeapi
conn = pyeapi.connect(host="127.0.0.1", transport="https", username="arista", password = "arista", port="8443")
conn.execute(['show version'])

### It works...
