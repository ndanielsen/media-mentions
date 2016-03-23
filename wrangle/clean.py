"""
Cleaning functions for data with pandas dataframes

By
Nathan Danielsen
"""

import pandas as pd
import calendar

data_file = './data/extracted_stories.json'
month = {name:str(v) for v, name in enumerate(calendar.month_name)}
month.update({' 10':'November'})

def month_map(x):
    if x in month.keys():
        x = month[x]
    return x
        
def dater(x):
    try:
        month, day, year = x[0], x[1], x[2]
        if len(month) == 1:
            month = '0' + month
        if len(day) == 1:
            day = '0' + day
        if len(year) == 2:
            year = '20' + year
        return '-'.join(elem for elem in [month, day, year])
    except:
        return 'na'

df = pd.read_json(data_file)
df = df.dropna(thresh=5)
# df = df[(df.headline != '') ]
# df['doc_year'] = df.docx.str.extract('^data/(\d{4})/(\w+)')[0]
# df['doc_month'] = df.docx.str.extract('^data/(\d{4})/(\w+)')[1]
df['datetime'] = df.date.str.split('/').apply(dater)



# df['doc_month'] = df.doc_month.apply(month_map)
# df = df.reset_index()
# df['year_month'] = df.doc_year + '-' + df.doc_month


if __name__ == '__main__':
    df.to_json('./data/cleaned_stories.json')
    print('done')



