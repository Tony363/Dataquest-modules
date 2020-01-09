
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import json

internal_cols = ['name', 'url', 'location', 'activities', 'industries', 'descriptions']

filename = "pRODUCTION_MFT Master List Final_v1"

df = pd.read_csv("{}.csv".format(filename), dtype='str', low_memory=False)

df.rename(columns={'Firm Name': 'name',
                   'Firm ID': 'firm_id',
                   #'# of Companies': 'count_company',
                   'Number_of_Companies': 'count_company',
                   'URL': 'url',
                   'Zip': 'zip',
                   'Rev Low': 'revenue_lo',
                   'Rev High': 'revenue_hi',
                   'EBITDA Low': 'ebitda_lo',
                   'EBITDA High': 'ebitda_hi',
                   'EV Low': 'ev_low',
                   'EV High': 'ev_high',
                   'EI Low': 'ei_low',
                   'EI High': 'ei_high',
                   'Ind 1': 'industries',
                   #'Portfolio Notes': 'industries'},
                   }, inplace=True)

df.fillna('', inplace=True) # remove NaN values
df = df.apply(lambda x: x.str.strip(), 1) # remove gaps

for col in ['firm_id', 'count_company', 'zip', 'revenue_lo', 'revenue_hi', 'ebitda_lo', 'ebitda_hi', 'ev_low', 'ev_high', 'ei_low', 'ei_high']: 
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)  

new_df = df.loc[:, :'industries']

def create_dict(x):
    return [dict(zip(internal_cols, list(x[i:i+6].astype(str)))) for i in xrange(0, len(x), 6) if any(list(x[i:i+6].astype(str)))]

new_df['portfolio_companies'] = df.loc[:, 'Portfolio Company 1 Name':].apply(lambda x: create_dict(x), 1)


def update_dict(x):
    for d in x['portfolio_companies']:
        d.update({'owner': x['name']})
    return x['portfolio_companies']

new_df['portfolio_companies'] = new_df[['name', 'portfolio_companies']].apply(lambda x: update_dict(x), 1) # add an owner

new_df = new_df.to_dict('records')
with open("{}.json".format(filename), "w") as f:
    f.write(json.dumps(new_df, indent=4, sort_keys=True, ensure_ascii=False))