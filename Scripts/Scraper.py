# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 09:53:00 2023

@author: jules
"""

import requests, pandas as pd
import numpy as np
import AlgorithmV2
from requests.structures import CaseInsensitiveDict

url = "https://api.geoapify.com/v1/routematrix?apiKey=7f593117b83546499e9872537faba272"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"  

GPS=[{"location":[11.331041511519276,46.46960527242423]},{"location":[11.330936111085462,46.47005696291675]},{"location":[11.3259701032973,46.47165266952819]},{"location":[11.330398392102571,46.46772152905843]}]

data = '{"mode":"drive","sources": [{"location":[11.331041511519276,46.46960527242423]},{"location":[11.330936111085462,46.47005696291675]},{"location":[11.3259701032973,46.47165266952819]},{"location":[11.330398392102571,46.46772152905843]}],"targets":[{"location":[11.331041511519276,46.46960527242423]},{"location":[11.330936111085462,46.47005696291675]},{"location":[11.3259701032973,46.47165266952819]},{"location":[11.330398392102571,46.46772152905843]}]}'

resp = requests.post(url, headers=headers, data=data)
#print(resp.json())

clean = resp.json().get('sources_to_targets')
# print(clean)

Mamma = []
for item in clean:
    for i in item:
        Mamma.append(i)
#print(Mamma)
               
df = pd. DataFrame(Mamma, columns=['distance','time', 'source_index', 'target_index'], index=range(len(GPS)*len(GPS)))
df.pop('time')
#print(df) 
pivoted = df.pivot(index='target_index', columns='source_index', values='distance')
pivoted.replace(0, np.nan, inplace=True)

#print(pivoted)
#print(df.pivot(columns="source_index"))
#print(pivoted['source_index'])
calc = AlgorithmV2.Itinerary.Default(pivoted)

