#!/usr/bin/env python

import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.seattle.gov", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.seattle.gov,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
# results = client.get("ppi5-g2bj", limit=2000)
results = client.get("ppi5-g2bj", limit=20)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
print(results_df.columns)