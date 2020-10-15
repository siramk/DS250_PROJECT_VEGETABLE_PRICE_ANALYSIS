from bs4 import BeautifulSoup as bs
import pandas as pd
with open('onion_data.xls', 'r') as f:
    content = f.read()
    
soup = bs(content, 'html5lib')
data = []
table = soup.find('table')
for tr in table.findAll('tr'):
    row = []
    count = 0
    for td in tr.findAll('td'):
        if count != 0:
            row.append(td.span.text)
        count += 1  
    data.append(row)

print(len(data))
print(data[:5])
data_dict = []
for row in data:
    row_dict = {}
    row_dict['DISTRICT'] = row[0]
    row_dict['MARKET'] = row[1]
    row_dict['COMMODITY'] = row[2]
    row_dict['VARIETY'] = row[3]
    row_dict['GRADE'] = row[4]
    row_dict['MIN'] = row[5]
    row_dict['MAX'] = row[6]
    row_dict['MODAL'] = row[7]
    row_dict['DATE'] = row[8]
    data_dict.append(row_dict)

df = pd.DataFrame(data= data_dict)
df.to_csv("full_onion_data.csv")
    
